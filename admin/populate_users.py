#!/usr/bin/python

from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from myapp import mongo


# Connexion to database
MONGO_HOST = "192.168.1.24"
MONGO_PORT = 27017
MONGO_DB = "mymusicDev"
MONGO_USER = "mydiskotekUser"
MONGO_PASS = "DISK_Ranv14860"

# Connexion to database
MONGO_HOST = "192.168.1.24"
MONGO_PORT = 27017
MONGO_DB = "mymusicDev"
MONGO_USER = "mydiskotekUser"
MONGO_PASS = "DISK_Ranv14860"


# Ask for data to store
user = input("Nom utilisateur : ")
courriel = input("Courriel : ")
password = input("Mot de passe : ")
pass_hash = generate_password_hash(password, method='pbkdf2:sha256')
# Insert the user in the DB
try:
    users.insert({"_id": user, "courriel":courriel, "password": pass_hash})print("Utilisateur créé.")

    except DuplicateKeyError:
        print("Utilisateur déjà présent en Base.")

if __name__ == '__main__':
    main()