#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
myapp/__init__.py

Created on  9|04
           -----
           20|18

@author: rdlc_Dev(alain)
@version:1.18 

"""
from myapp import app
from flask import Flask, request
from flask_script import Command, Option, Manager, Shell
import logging
from logging.handlers import RotatingFileHandler
import traceback
from time import strftime

class GunicornApp(Command):

    def get_options(self):
        from gunicorn.config import make_settings

        settings = make_settings()
        options = (
            Option(*klass.cli, dest=klass.name, default=klass.default)
            for setting, klass in settings.items() if klass.cli
        )
        return options

    def __call__(self, app=None, *args, **kwargs):

        from gunicorn.app.base import Application
        class FlaskApplication(Application):
            def init(self, parser, opts, args):
                return kwargs

            def load(self):
                return app

        FlaskApplication().run()

    
@app.after_request
def after_request(response):
    """ Logging after every request. """
    # This avoids the duplication of registry in the log,
    # since that 500 is already logged via @app.errorhandler.
    if response.status_code != 500:
        ts = strftime('[%Y-%b-%d %H:%M]')
        logger.error('%s %s %s %s %s %s',
                      ts,
                      request.remote_addr,
                      request.method,
                      request.scheme,
                      request.full_path,
                      response.status)
    return response

@app.errorhandler(Exception)
def exceptions(e):
    """ Logging after every Exception. """
    ts = strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                  ts,
                  request.remote_addr,
                  request.method,
                  request.scheme,
                  request.full_path,
                  tb)
    return "Internal Server Error", 500

manager = Manager(app)
manager.add_command("gunicorn", GunicornApp())


if __name__ == '__main__':
    # maxBytes to small number, in order to demonstrate the generation of multiple log files (backupCount).
    handler = RotatingFileHandler('log/mydiskotek.log', maxBytes=10000, backupCount=3)
    # getLogger(__name__):   decorators loggers to file + werkzeug loggers to stdout
    logger = logging.getLogger(__name__)
    # getLogger('werkzeug'): decorators loggers to file + nothing to stdout
    #logger = logging.getLogger('werkzeug')

    handler2 = RotatingFileHandler('log/gunicorn.log', maxBytes=10000, backupCount=3)
    gunicorn_logger = logging.getLogger('gunicorn.error')
    logger.setLevel(logging.DEBUG)
    gunicorn_logger.setLevel(gunicorn_logger.levels)
    logger.addHandler(handler)
    logger.addHandler(handler2)

    manager.run()
    



