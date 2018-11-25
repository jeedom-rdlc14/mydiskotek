#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
construction matrice
Mise en base mongodb

Created on Mon Oct  9 08:53:43 2017

@author: rdlc_Dev (alain)
@version:1.171129

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

print('\n\t== Collection matrice : {nb} documents en base.'.format(nb=db.matrice.count()))
result = db.matrice.delete_many({})
print('Efffacés : ',result.deleted_count)


for index in range(0, 11):
    ajout = 6
    for ite in range(1,7):
        ajout = ajout - 1
        total =(index * 6) + ite
        data = {}
        data['total'] = total
        data['nbligne'] = index + 1
        data['ajout'] = ajout
    
        db.matrice.insert_one(data)


 