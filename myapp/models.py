
# -*- coding: utf-8 -*-

"""
models.py

flask

Created on 10|04
           -----
           20|18 

@author: rdlc_Dev(alain)
@version:1.180410 

"""

# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
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


   
class ListCollection():
    
    def __init__(self, artists, title, year, release, rangement, place):
        self.artists = artists
        self.title = title
        self.year = year
        self.release = release
        self.rangement = rangement
        self.place = place
    