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

# Connexion to database
MONGO_HOST = "192.168.1.24"
MONGO_PORT = 27017
MONGO_DB = "mymusicDev"
MONGO_USER = "mydiskotekUser"
MONGO_PASS = "DISK_Ranv14860"

connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB]
    
# Ask for data to store
user = input("Entrer votre nom d'utilisateur : ")
courriel = input("Entrer votre courriel : ")
password = input("Entrer votre mot de passe : ")
pass_hash = generate_password_hash(password, method='pbkdf2:sha256')

# Insert the user in the DB
try:
    db.users.insert({"_id": user, "email": courriel, "password": pass_hash})
    print("Utilisateur créé.")

except DuplicateKeyError:
    print ("Utilisateur déjà présent dans la base de donnéesq.")

