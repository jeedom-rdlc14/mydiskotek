#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Récupération des compteurs
Mise en base mongodb

Created on Mon Oct  9 08:53:43 2017

@author: rdlc_Dev (alain)
@version:1.171201

"""

import time
from myapp import mongo

def compteurs_sup_cat():
    countList = []
    compteurs ={}
    # Total
    count_total = mongo.db.releases.count()
    compteurs["total"] = count_total
    
    # par support
    listSupport = ["Vinyl","CD","DVD","APPLE"]
    for support in listSupport:
        counterSupport = mongo.db.releases.count({"formats.name": support})
        compteurs[support] = counterSupport
    
    # par categorie
    listCategorie = ["Rock", "Jazz", "Pop", "Blues", "Reggae", "Latin", "Hip Hop", "Electronic", "Funk / Soul", "Folk, World, & Country"]
    for categorie in listCategorie:
        counterCategorie = mongo.db.releases.count({"genres": categorie})
        if categorie == 'Folk, World, & Country':
            categorie = 'Folk World Country'
        elif categorie == 'Funk / Soul':
            categorie = 'Funk Soul'
            
        compteurs[categorie] = counterCategorie
        
    countList.append(compteurs)
    return countList

def fctSortDict(value):
    return value['release']

def compteurs_artist():
    countArtists = []
    compteurs ={}
    listArtists = []
    total_artists = len(listArtists)
    
    compteurs["total_artists"] = total_artists
    for artist in listArtists:
        releaseByArtist = mongo.db.releases.count({"artists.name": artist})
        artistItem ={
            "artistName":artist,
            "release":releaseByArtist
        }
        countArtists.append(artistItem)
        #countArtistsReleases = sorted(countArtists.items(), key=fctSortDict, reverse=True)
     
    return sorted(countArtists, key=fctSortDict, reverse=True)


# main
countList = compteurs_sup_cat()
countArtists = compteurs_artist()
      