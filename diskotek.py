#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
runner.py

The runner.py is the entry point of the project. The file starts by creating an instance of Manager() object. It then defines make_shell_context() function. The objects returned by make_shell_context() function will be available inside the shell without explicit import statements. At last, the run() method on the Manager instance is called to start the server.

Created on  9|04
           -----
           20|18

@author: rdlc_Dev(alain)
@version:1.180409 

"""
import os
from myapp import app
from flask import Flask, request
from flask_script import Manager, Shell
import logging
from logging.handlers import RotatingFileHandler
import traceback
from time import strftime

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

# these names will be available inside the shell without explicit import
def make_shell_context():
    return dict(app=app)

manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    # maxBytes to small number, in order to demonstrate the generation of multiple log files (backupCount).
    handler = RotatingFileHandler('log/mydiskotek.log', maxBytes=10000, backupCount=3)
    # getLogger(__name__):   decorators loggers to file + werkzeug loggers to stdout
    #logger = logging.getLogger(__name__)
    # getLogger('werkzeug'): decorators loggers to file + nothing to stdout
    logger = logging.getLogger('werkzeug')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    #manager.run()
    app.run(host='192.168.1.86', port=8080)