#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 18:41:04 2018

@author: alain
"""

from pymongo import MongoClient, DESCENDING
import datetime


def artistsList():
    jsonf = open('artistsList.jsn','w') 
    data = json.dumps([r for r in csv_reader])
    jsonf.write(data)


def fctSortDict(value):
    return value['release']


def compteurs_artist():
    #countArtists = []
    compteursArt ={}
    listArtists = disks.find().distinct("artists.name")
    total_artists = len(listArtists)
    
    compteursArt["total_artists"] = total_artists
    for artist in listArtists:
        releaseByArtist = disks.count({"artists.name": artist})
        vinylByArtist = disks.find({"artists.name": artist, "formats.name":"Vinyl"}).count()
        cdByArtist = disks.find({"artists.name": artist, "formats.name":"CD"}).count()
        dvdByArtist = disks.find({"artists.name": artist, "formats.name":"DVD"}).count()
        dematByArtist = disks.find({"artists.name": artist, "formats.name":""}).count()
        compteursArt ={
            "artistName":artist,
            "release":releaseByArtist,
            "vinyl":vinylByArtist,
            "cd":cdByArtist,
            "dvd":dvdByArtist,
            "demat":dematByArtist
        }
        
        #compteursArt.append(artistItem)
        #countArtistsReleases = sorted(countArtists.items(), key=fctSortDict, reverse=True)
        
        post = db.compteursArt
        compteursArt_id = post.insert_one(compteursArt).inserted_id
        #print('Compteur Support et Catégorie : ',compteursArt_id)
     

def compteurs_sup_cat():
   # countList = []
    compteurs ={}
            
    # Total
    count_total = disks.count()
    compteurs["total"] = count_total
    #countList.append(compteurs)
    
    # par support
    listSupport = ["Vinyl","CD","DVD","APPLE"]
    for support in listSupport:
        counterSupport = disks.count({"formats.name": support})
        compteurs[support] = counterSupport
            
    # par categorie
    listCategorie = ["Rock", "Jazz", "Pop", "Blues", "Reggae", "Latin", "Hip Hop", "Electronic", "Funk / Soul", "Folk, World, & Country"]
    for categorie in listCategorie:
        counterCategorie = disks.count({"genres": categorie})
        if categorie == 'Folk, World, & Country':
            categorie = 'Folk World Country'
        elif categorie == 'Funk / Soul':
            categorie = 'Funk Soul'
            
        compteurs[categorie] = counterCategorie
     
    # par support & categorie
    supportList = ["Vinyl","CD","DVD","APPLE"]
    categorieList = ["Rock", "Jazz", "Pop", "Blues", "Reggae", "Latin", "Hip Hop", "Electronic", "Funk / Soul", "Folk, World, & Country"]
    for support in supportList:
        for categorie in categorieList:
            libelle = support + '_' + categorie
            counterSupCateg = disks.count({"formats.name": support, "genres": categorie})
            print(libelle, counterSupCateg)
            if categorie == 'Folk, World, & Country':
                categorie = 'Folk World Country'
            elif categorie == 'Funk / Soul':
                categorie = 'Funk Soul'
            
            compteurs[libelle] = counterSupCateg
        
    
    #maintenant = datetime.datetime.now()
    updated = datetime.datetime.now().strftime('%d-%m-%Y')
    compteurs['updated'] = updated
    post = db.compteursGen
    compteursGen_id = post.insert_one(compteurs).inserted_id
    print('Compteurs Support et Catégorie : ',compteursGen_id)
            
   #countList.append(compteurs)
   # return countList

# main
    
# Connexion to database
MONGO_HOST = "192.168.1.24"
MONGO_PORT = 27017
MONGO_DB = "mymusicDev"
MONGO_USER = "mydiskotekUser"
MONGO_PASS = "DISK_Ranv14860"

connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB]
#db.authenticate(MONGO_USER, MONGO_PASS)

# Getting a Collection
disks = db['releases']

#compteurs artists(total, vinyl, cd , dvd, demat)
print('Mise à jour des compteurs')
start_time = datetime.datetime.now().time().strftime('%H:%M:%S')

result = db.compteursArt.delete_many({})
print('compteurs Art Efffacés : ',result.deleted_count)
compteurs_artist()
print('Compteurs artistes: OK')

result = db.compteursGen.delete_many({})
print('compteurs Gen Efffacés : ',result.deleted_count)
countList = compteurs_sup_cat()
print('Compteurs Support et Catégories OK')
cursor = db.compteursGen.find()
for compteur in cursor:
    print(compteur['total'])
    print(compteur['Vinyl'])
    print(compteur['CD'])
    print(compteur['DVD'])
    print(compteur['APPLE'])
    print(compteur['updated'])
    print(compteur['Vinyl_Jazz'])
    print(compteur['Vinyl_Rock'])
    print(compteur['Vinyl_Pop'])
    
end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
total_time=(datetime.datetime.strptime(end_time,'%H:%M:%S') - datetime.datetime.strptime(start_time,'%H:%M:%S'))
print('Temps de mise à jour des compteurs : ', total_time)