#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
config.py

Configurations

Created on  9|04
           -----
           20|18

@author: rdlc_Dev(alain)
@version:1.180409 

"""

import os,jinja2

APP_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

VERSION = 'v1.1.12'
BUILD = '20181223'

ARTISTS_COLLECTION = 'artists2'
RELEASES_COLLECTION = 'releases'
USERS_COLLECTION = 'users'

DEBUG = True

class BaseConfig:
    
    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'A SECRET KEY'
    SECRET_KEY = "175K8P8j6h65p32ltvkcw9WmL18BHBKO"
    
    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = "1I4LINdWx35bz7Tl773nQu50Ne4bY90n"
 
    # TEMPLATES FOLDER
    TEMPLATE_FOLDER = "templates"

    # ASSETS FOLDER
    ASSETS_FOLDER = "static"
    
    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    CSRF_ENABLED     = True
 
    ##### Flask-Mail configurations #####
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'alain.bisson@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    # JINJA LOADER
    JINJA_ENVIRONMENT = jinja2.ChoiceLoader([
        jinja2.FileSystemLoader([x[0] for x in os.walk('templates')]),
    ])
    
    WTF_CSRF_ENABLED = True
    
class DevelopementConfig(BaseConfig):
    DEBUG = True
    MONGO_DBNAME = 'mymusicDev'
    MONGO_URI = 'mongodb://192.168.1.24:27017/mymusicDev'
    
class TestingConfig(BaseConfig):
    DEBUG = True
    MONGO_DBNAME = 'mymusicTests'
    MONGO_URI = 'mongodb://192.168.1.24:27017/mymusicTests'
    
class ProductionConfig(BaseConfig):
    DEBUG = False
    MONGO_DBNAME = 'mymusicDB'
    MONGO_URI = 'mongodb://mydiskotekUser:DISK_Ranv14860@192.168.1.24:27017/mymusicDB'
    