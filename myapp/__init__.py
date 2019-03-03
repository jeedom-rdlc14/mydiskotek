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

from flask import Flask, request

from flask_mail import Mail, Message
from flask_script import Manager, Command, Shell
from flask_login import LoginManager
from flask_pymongo import PyMongo
import os, config
import logging
from logging import Formatter, FileHandler
from logging.handlers import RotatingFileHandler
import traceback
from time import strftime

# create application instance
app = Flask(__name__)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')
#app.config.from_object('config')

# initializes extensions
mongo = PyMongo(app)

mail = Mail(app)
lm = LoginManager(app)
lm.init_app(app)
lm.login_view = 'login'

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
'''
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
'''
from . import routes

# logging
# mydiskotek

logger = logging.getLogger('whatever')
handler = logging.StreamHandler()
file_handler = RotatingFileHandler('/var/log/supervisor/mydiskotek.log', maxBytes=10000, backupCount=3)
#file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s ' '[in %(pathname)s:%(lineno)d]'))
#handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s ' '[in %(pathname)s:%(lineno)d]'))
logger.addHandler(file_handler)
logger.addHandler(handler)
logger.setLevel(logging.INFO)