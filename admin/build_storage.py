#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
construction collection storage
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

print('\n\t== Collection storage: {nb} documents en base.'.format(nb=db.storage.count()))
result = db.storage.delete_many({})
print('Efffacés : ',result.deleted_count)

#disks = db.releases.find({"formats.name": "Vinyl", "genres": "Jazz"},{"artists.name": 1, "_id": 0,"title": 1,"year":1, "id": 1}).limit(45).sort("artists.name", 1)
disks = db.releases.find({"formats.name": "Vinyl", "artists.name": "Van Morrison"},{"artists.name": 1, "_id": 0,"title": 1,"year":1, "id": 1}).sort("year", 1)
print('\n\t== Collection releases: {nb} documents en base.'.format(nb=db.releases.count()))

for document in disks:
    release = document['id']
    
    try:
        criteria = release
        db.releases.update_one({'id': release},{'$set':{'storage':{'nom':'','position':0}}})
                
    except Exception as excep:
        print(excep)
'''
for empl in ['MSGEB1','MSGEB2','MSGEB3','MSGEB4']:
    libelle = 'Meuble Salon Gauche Etagère Bas'
    for place in range(1, 46):
        db.storage.insert_one({'nom':empl, 'description': libelle, 'stockage':{'position':place, 'release':0}})
print('\n\t== Collection storage : MSGEB1-4 (Meuble Salon Gauche Etagère Bas 1 --> 4 créé')

for empl in ['MSGEH1','MSGEH2','MSGEH3','MSGEH4']:
    libelle = 'Meuble Salon Gauche Etagère Haut'
    for place in range(1, 46):
        db.storage.insert_one({'nom':empl, 'description': libelle, 'stockage':{'position':place, 'release':0}})
print('\n\t== Collection storage : MSGEH1-4 (Meuble Salon Gauche Etagère Haut 1 --> 4 créé')

for empl in ['MSGT1R1','MSGT1R2','MSGT1R3','MSGT1R4','MSGT1R5']:
    libelle = 'Meuble Salon Gauche Tiroir 1'
    for place in range(1, 50):
        db.storage.insert_one({'nom':empl, 'description': libelle, 'stockage':{'position':place, 'release':0}})

print('\n\t== Collection storage : MSGT1R1-5 (Meuble Salon Gauche Tiroir 1 Rang 1 --> 5 créé')

for empl in ['MSGT2R1','MSGT2R2','MSGT2R3','MSGT2R4','MSGT2R5']:
    libelle = 'Meuble Salon Gauche Tiroir 2'
    for place in range(1, 50):
        db.storage.insert_one({'nom':empl, 'description': libelle, 'stockage':{'position':place, 'release':0}})

print('\n\t== Collection storage : MSGT2R1-5 (Meuble Salon Gauche Tiroir 2 Rang 1 --> 5 créé')

for empl in ['MSGT3R1','MSGT3R2','MSGT3R3','MSGT3R4','MSGT3R5']:
    libelle = 'Meuble Salon Gauche Tiroir 3'
    for place in range(1, 50):
        db.storage.insert_one({'nom':empl, 'description': libelle, 'stockage':{'position':place, 'release':0}})

print('\n\t== Collection storage : MSGT3R1-5 (Meuble Salon Gauche Tiroir 3 Rang 1 --> 5 créé')

for empl in ['MSDTB1','MSDTB2','MSDTB3']:
    libelle = 'Meuble Salon Droite Tiroir Bas'
    for place in range(1, 50):
        db.storage.insert_one({'nom':empl, 'description': libelle, 'stockage':{'position':place, 'release':0}})

print('\n\t== Collection storage : MSDTB1 (Meuble Salon Droite Tiroir Bas 1 --> 3 créé')

for empl in ['AET1B1','AET1B2','AET1B3']:
    libelle = 'Armoire Entrée Tablette 1 Bas'
    for place in range(1, 50):
        db.storage.insert_one({'nom':empl, 'description': libelle, 'stockage':{'position':place, 'release':0}})

print('\n\t== Collection storage : AETB1-3 (Armoire Entrée Tablette 1 Bas 1 --> 3 créé')

for empl in ['AET2B1','AET2B2','AET2B3']:
    libelle = 'Armoire Entrée Tablette 2 Bas'
    for place in range(1, 50):
        db.storage.insert_one({'nom':empl, 'description': libelle, 'stockage':{'position':place, 'release':0}})

print('\n\t== Collection storage : AETB1-3 (Armoire Entrée Tablette 2 Bas 1 --> 3 créé')

 ''' 