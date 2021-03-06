#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
populate storage
Mise en base mongodb

Created on 24|06
           -----
           20|18

@author: Rdlc_Dev(Alain)

"""


from pymongo import MongoClient

# Connexion to database
MONGO_HOST = "192.168.1.24"
MONGO_PORT = 27017
MONGO_DB = "mymusicDev"
MONGO_USER = "mydiskotekUser"
MONGO_PASS = "DISK_Ranv14860"

connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB]
#db.authenticate(MONGO_USER, MONGO_PASS)

# Stockage des albums 
# Jazz Vinyl
#disks = db.releases.find({"formats.name": "Vinyl", "genres": "Jazz","storage.nom": ""},{"artists.name": 1, "_id": 0,"title": 1,"year":1, "id": 1}).limit(4).sort("artists.name", 1)
#disks = db.releases.find({"formats.name": "Vinyl", "artists.name": "Elton John", "storage.nom": ""},{"artists.name": 1, "_id": 0,"title": 1,"year":1, "id": 1}).sort("year", 1)
disks = db.releases.find({"formats.name": "CD", "artists.name": "Cassandra Wilson", "storage.nom": ""},{"artists.name": 1, "_id": 0,"title": 1,"year":1, "id": 1}).sort("year", 1)
place = 11
for document in disks:
    release = document['id']
    empl = 'MSGT1C1'
            
    try:
        criteria = release
        db.releases.update_one({'id': criteria},{'$set':{'storage.nom': empl, 'storage.position': place}})
          
        try:
            db.storage.insert_one({'nom': empl, 'position':place, 'release':release})
        
        except Exception as excep:
            print(excep)

    except Exception as excep:
        print(excep)
        
    print('\n\t== Emplacement : {empl} position {pos}.'.format(empl=empl, pos=place))
    place = place + 1

    