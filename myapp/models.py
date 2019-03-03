
# -*- coding: utf-8 -*-

"""
models.py

Created on 10|04
           -----
           20|18 

@author: rdlc_Dev(alain)
@version:1.180410 

"""
from werkzeug.security import check_password_hash

class User():

    def __init__(self, username):
        self.username = username
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)

 
    