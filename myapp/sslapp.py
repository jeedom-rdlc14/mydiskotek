#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
myapp/sslapp.py

Created on 02|11
           -----
           20|18

@author: rdlc_Dev(alain)
@version:1.0 

"""
'''

 gestion https  

'''
#generation certificat et key
'''
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout udara.com.key -out udara.com.crt
Below is the Flask code snippet to start your Flask API in HTTPS
'''

from flask import Flask
from OpenSSL import SSL
 
import os
 
context = SSL.Context(SSL.SSLv23_METHOD)
cer = os.path.join(os.path.dirname(__file__), 'resources/udara.com.crt')
key = os.path.join(os.path.dirname(__file__), 'resources/udara.com.key')
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World!'
 
if __name__ == '__main__':
    context = (cer, key)
    app.run( host='0.0.0.0', port=8000, debug = True, ssl_context=context)
#When you run above code, it will show below output. Note that it is running HTTPS

# Running on https://0.0.0.0:5000/ (Press CTRL+C to quit)
# Restarting with stat