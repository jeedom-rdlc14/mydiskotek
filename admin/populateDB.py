#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
populateDB.py
Created on 02|06
           -----
           20|18

@author: Rdlc_Dev(Alain)
"""

from flask import Flask
from werkzeug.security import generate_password_hash
import pymongo
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask_pymongo import PyMongo
import os, config


def main():
    # Connect to the DB
    client = MongoClient('mongodb://192.168.1.24:27017')

    # Get the sampleDB database
    db = client.mymusicDev
    
    # Ask for data to store
    user = input("Entrer votre nom d'utilisateur : ")
    password = input("Entrer votre mot de passe : ")
    pass_hash = generate_password_hash(password, method='pbkdf2:sha256')

    # Insert the user in the DB
    try:
        db.users.insert({"_id": user, "password": pass_hash})
        print("Utilisateur créé.")
    except DuplicateKeyError:
        print ("Utilisateur déjà présent dans la base de donnéesq.")


if __name__ == '__main__':
    main()