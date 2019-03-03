#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
utils.py
Created on 22|04
           -----
           20|18

@author: rdlc_DEV-alain
"""

from myapp import mongo, app
import datetime

def albumDict(disks):
    listAlbums = []
    
    for album in disks:
        artists = album["artists"]
        artist = artists[0]
        artistName = artist["name"]
    
        formats = album["formats"]
        typeformat = formats[0]
        formatName = typeformat["name"]
        formatQty = typeformat["qty"]
        support = "{formats} ({qty})".format(formats=formatName, qty=formatQty)

        #stockage = album["storage"]
        #stock = stockage[0]
        storageNom = album["storage"].get('nom')
        storagePosition = album["storage"].get('position')
        
        albumItem = {
            "thumb":album["thumb"],
            "id":int(album["id"]),
            "artistName":artistName,
            "title":album["title"],
            "formatName":support,
            "year":int(album["year"]),
            "storage":storageNom,
            "position":storagePosition
        }
        listAlbums.append(albumItem)
    
    return listAlbums


def addItems(listAlbums, nbadd):
    
    albumItem = {
        "thumb":"Vide",
        "id":"",
        "artistName":"",
        "title":"",
        "formatName":"",
        "year":""
    }
    
    i = 1
    while i <= nbadd:
        listAlbums.append(albumItem)
        i = i + 1
    
    return listAlbums


def infosDisk(disk):
    paramsList = []
    tracksList = []
    extraTracksList = []
    extraArtistsList = []
    creditsList = []
    videosList = []
    listInfosDisk = []
    
    for album in disk:
        release = int(album["id"])
        
        artists = album["artists"]
        artist = artists[0]
        artistName = artist["name"]
        artistId = artist["id"]
        
        formats = album["formats"]
        typeformat = formats[0]
        formatName = typeformat["name"]
        formatQty = typeformat["qty"]
    
        stockage = album["storage"]
        storageNom = stockage["nom"]
        storagePosition = int(stockage["position"])

        labels = album["labels"]
        label = labels[0]
        labelName = label["name"]
        labelCatalog = label["catno"]
        
        pisteslist = album["tracklist"]
        i = 0
        while i < len(pisteslist):
            piste = pisteslist[i]
            position = piste["position"]
            duration = piste["duration"]
            title = piste["title"]
            if 'extraartists' in piste:
                extraList = piste["extraartists"]
                j = 0
                while j < len(extraList):
                    extraartist = extraList[j]
                    name = extraartist["name"]
                    tracks = extraartist["tracks"]
                    role = extraartist["role"]
                    artistId = extraartist["id"]
                    
                    extraPiste = {
                        "name":name,
                        "role":role,
                        "tracks":tracks,
                        "id":artistId
                    }
                    extraTracksList.append(extraPiste)
                    j += 1
        
            pisteItem = {
                "position":position,
                "title":title,
                "duration":duration,
                "extrapiste":extraTracksList
            }
            tracksList.append(pisteItem)
            i += 1
        
        if 'videos' in album:
            videosList = album["videos"]
        '''
        i = 0
        while i < len(listVideos):
            video = listVideos[i]
            duration = video['duration']
            description = video['description']
            lien = video['uri']
            title = video['title']
                                    
            videoItem = {
                'duration':duration,
                'description':description,
                'lien':uri,
                'title':title
            }
            videosList.append(videoItem)
            i += 1
        '''    
                
        extrasList = album["extraartists"]
        i = 0
        while i < len(extrasList):
            extra = extrasList[i]
            name = extra["name"]
            role = extra["role"]
            tracks = extra["tracks"]
            extra_id = extra["id"]
        
            extraItem = {
                "role":role,
                "name":name,
                "tracks":tracks,
                "id":extra_id
            }
            extraArtistsList.append(extraItem)
            i += 1
        
        if "notes" in album:
            notes =album["notes"]
        else:
            notes =""
        
        albumItem = {        
            "thumb":album["thumb"],
            "id":release,
            "artistName":artistName,
            "artistId":artistId,
            "title":album["title"],
            "formatName":formatName,
            "formatQty":formatQty,
            "released":int(album["year"]),
            "labelName":labelName,
            "labelCatalog":labelCatalog,
            "country":album["country"],
            "genres":album["genres"],
            #"styles":album["styles"],
            "notes":notes,
            "videos":videosList,
            "credits":creditsList,
            "year":int(album["year"]),
            "storage":storageNom,
            "position":storagePosition
        }
        paramsList.append(albumItem)
    
    listInfosDisk.append(paramsList)
    listInfosDisk.append(tracksList)
    listInfosDisk.append(extraArtistsList)
    listInfosDisk.append(creditsList)
    listInfosDisk.append(videosList)
    
    return listInfosDisk


def templateParams(listAlbums, page_num, page_size, urlTag):
    paramsTemplate = {}
    #page_size = 60
    nb2add = 0
    lengthpage = 0
    
    listlength = len(listAlbums)
    if listlength % page_size == 0 and listAlbums:
        total = listlength // page_size
    else:
        total = listlength // page_size + 1
    
    final_list = listAlbums[(page_num - 1) * page_size: page_num * page_size]
    
    cursor = mongo.db.matrice.find({"total":len(final_list)})
    for doc in cursor:
        nb2add = doc["ajout"]
        lengthpage = doc["nbligne"]
    
    if len(final_list) == 60:
        lengthpage = 10
    else:
        final_list = addItems(final_list, nb2add)
        
    paramsTemplate = {
        "list":final_list,
        "listlong":listlength,
        "page_num":page_num,
        "total":total,
        "earlier":page_num + 1,
        "later":page_num - 1,
        "urlTag":urlTag,
        "pagelength":lengthpage
    }
    
    return paramsTemplate


def genereficTxt(support, categorie, disks):
    
    today = datetime.datetime.now()
    filename = support + '_' + today.strftime('%Y-%m-%d') + '.txt'
    
    fic = open(filename, "w")
    entete = 'Liste des ' + support + ' de ' + categorie
    fic.write(entete)
    fic.write('\n artiste  --  Titre  --  Année  --   release  --  Rangement --  Place')

    for album in disks:
        artist = album['artists']
        artiste = artist[0].get('name')
        titre = album['title']
        annee = str(album['year'])
        refAlbum = str(album['id'])
        rangement = ''
        place = ''
        ligne = '\n' + artiste + ' -- ' + titre + ' -- ' + annee + ' -- ' + refAlbum + ' -- ' + rangement + ' - ' + place
        fic.write(ligne)
        #fic.write('\n'.join("%.0f" % ligitem for item in rs))
    
    fic.close()

    return fic
    