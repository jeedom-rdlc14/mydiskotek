#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
routes.py
Created on 12|04
           -----
           20|18

@author: Rdlc_Dev(Alain)
"""
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from myapp import mongo, app, lm
from pymongo import DESCENDING, ASCENDING
from config import APP_DIR, VERSION, BUILD, DB_NAME, ARTISTS_COLLECTION, RELEASES_COLLECTION
import glob
from myapp import const

import sys
from os import path, chdir, getcwd, listdir
from io import BytesIO
import requests
import json
import math
import datetime

from myapp.forms import LoginForm
from myapp.models import User
#from myapp.table2Pdf import PdfPrint

from myapp.utils import albumDict, templateParams, addItems, infosDisk

'''
 WebService Routes  
'''

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    #app.logger.debug('route /')
    compteursGen = mongo.db.compteursGen.find()
    compteursArt = mongo.db.compteursArt.find().sort("release", DESCENDING).limit(15)
    
    disks = mongo.db.releases.find().sort("dateAdded", -1).limit(12)
    lastAlbums = albumDict(disks)
        
    template_context = dict(compteurs=compteursGen, compteursArtists=compteursArt, lastAlbums=lastAlbums, version=VERSION, build=BUILD) 
    return render_template('index.html', **template_context)

@app.route('/list/', methods=['GET'])
@app.route('/list/<int:page_num>', methods=['GET'])
def list(page_num=1):
    count_total = mongo.db.releases.count({})
    page_size = 60
    
    disks = mongo.db.releases.find().sort("artists.name", 1)
    albumsList = albumDict(disks)
    paramsTemplate = templateParams(albumsList, page_num, page_size, '')
    
    template_context = dict(count=count_total, paramsPage=paramsTemplate, version=VERSION)
    return render_template('list.html', **template_context)

@app.route('/artists/', methods=['GET'])
@app.route('/artists', methods=['GET'])
@app.route('/artists/<int:page_num>', methods=['GET'])
def list_artists(page_num=1):
    page_size = 60
       
    listArtists = mongo.db.releases.distinct("artists.name")
    count_total = len(listArtists)
        
    compteursArt = mongo.db.compteursArt.find().sort("artistName", ASCENDING)
    compteursArtList = []
    
    for compteur in compteursArt:
        compteursArtList.append(compteur)
    
    paramsTemplate = templateParams(compteursArtList, page_num, page_size, '')
    
    template_context = dict(count=count_total, paramsPage=paramsTemplate,version=VERSION) 
    return render_template('artistslist.html', **template_context)
            
        
@app.route('/artist/<artist>', methods=['GET'])
def list_albums(artist):
    #app.logger.debug('Artiste : %s', artist)
    
    count = mongo.db.releases.find({"artists.name":artist}).count()
    #app.logger.debug('count : %s', count)
    artistInfos = []
    albumsList = []
    page_size = 60
    
    if artist != 'Various':
        #disks = mongo.db.releases.find({"artists.name": artist}, {"id": 1, "_id": 0, "artists.name": 1, "formats": 1, "thumb": 1, "title": 1, "year": 1}).sort("year", 1)
        disks = mongo.db.releases.find({"artists.name": artist}).sort("year", 1)  
        artistDict = mongo.db.artists.find({"name": artist}).limit(1)
        albumsList = albumDict(disks)                    
        paramsTemplate = templateParams(albumsList, 1, page_size, '')
    
        if artistDict:
            #app.logger.debug('ArtistDict OK')
            for artist in artistDict:
                urls = []
                membersInfos = []
                membersLen = 0
       
                if "realname" in artist.keys():
                    nomReel = artist["realname"]
                else:
                    nomReel = ''
            
                if "members" in artist.keys():
                    membersInfos = artist["members"]
                    membersLen = len(membersInfos)
                            
                if "urls" in artist.keys():
                    urlsInfos = artist["urls"]
                    for url in urlsInfos:
                        urls.append(url)
                #app.logger.debug('URLS : %s', urls)

                artistItem = {
                    "id":artist["id"],
                    "name":artist["name"],
                    "realname":nomReel,
                    "profile":artist["profile"],
                    "releases_url":artist["releases_url"],
                    "urls":urls,
                    "uri":artist["uri"],
                    "members":membersInfos,
                    "membersLength":membersLen
                }
                artistInfos.append(artistItem)
        else:
            urls = []
            members = []
            artistItem = {
                #"id":artistId,
                "name":artist,
                "realname":'',
                "profile":'',
                "releases_url":'',
                "urls":urls,
                "members":members
            }
            artistInfos.append(artistItem)
        
    #app.logger.debug('Artiste infos : %s', artistInfos)
    #app.logger.debug('Params : %s', paramsTemplate)
    #app.logger.debug('Albums : %s', albumsList)                  
    template_context = dict(count=count, artist=artist, artistInfos=artistInfos, paramsPage=paramsTemplate, list=albumsList, version=VERSION) 
    return render_template('artists_2.html', **template_context)
   
@app.route('/artist/<int:artistId>/releases', methods=['GET'])
def discographie(artistId):
    page_size = 50
    nbItems = 0
    releasesList = []
    myDisco = "false"
        
    try:
        url = "https://api.discogs.com/artists/" + str(artistId) + "/releases"
        response = requests.get(url)
        releasesDict = json.loads(response.text)
        
        #app.logger.debug('requete : %s', url)
        #app.logger.debug('disco : %s', releasesDict)
        
        #liste des releases    
        listAlbums = releasesDict['releases']
        
        for album in listAlbums:
            artist = album["artist"]
            
            releaseItem = {
                "id":album["id"],
                "myDisco":myDisco,
                "title":album["title"],
                "artist":artist,
                "year":album["year"],
                "resource_url":album["resource_url"],
                "type":album["type"],
                "role":album["role"],
                "thumb":album["thumb"]
            }   
            releasesList.append(releaseItem)
                    
        #cursor = mongo.db.releses.find({"artists.name":artist})
        #for doc in cursor:
        #    releaseId = doc["id"]
            
        #compteurs de pagination
        pagination = releasesDict['pagination']
        page_size = pagination["per_page"]
        nbItems = pagination["items"]
        #nbPage = pagination["pages"]
        #page_num = pagination["page"]
            
    except Exception as excep:
        print(excep)
    
    paramsTemplate = {}
    paramsTemplate = templateParams(releasesList, 1, page_size, '')

    template_context = dict(count=nbItems, paramsPage=paramsTemplate, version=VERSION) 
    return render_template('releases.html', **template_context)


@app.route('/members/<name>/<int:artistId>', methods=['GET'])
def membre(name, artistId):
    artistInfos = []
    albumsList = []
    page_size = 60
    
    count = mongo.db.releases.find({"artists.name":name}).count()
    if count != 0:
        disks = mongo.db.releases.find({"artists.name": name}, {"id": 1, "_id": 0, "artists.name": 1, "formats": 1, "thumb": 1, "title": 1, "year": 1}).sort("year", 1)
        albumsList = albumDict(disks)
        
    paramsTemplate = templateParams(albumsList, 1, page_size, '')
      
    try:
        url = "https://api.discogs.com/artists/" + str(artistId)
        response = requests.get(url)
        artistDict = json.loads(response.text)
        
        urls = []
        groupsInfos = []
        groupsLen = 0
       
        if "realname" in artistDict:
            nomReel = artistDict["realname"]
        else:
            nomReel = ''
            
        if "groups" in artistDict:
            groupsInfos = artistDict["groups"]
            groupsLen = len(groupsInfos)
                            
        if "urls" in artistDict:
            urlsInfos = artistDict["urls"]
            for url in urlsInfos:
                urls.append(url)
        
        #app.logger.debug('URLS : %s', urls)

        artistItem = {
            "id":artistDict["id"],
            "name":artistDict["name"],
            "realname":nomReel,
            "profile":artistDict["profile"],
            "releases_url":artistDict["releases_url"],
            "urls":urls,
            "uri":artistDict["uri"],
            "groups":groupsInfos,
            "groupsLength":groupsLen
        }
        artistInfos.append(artistItem)
                
    except Exception as excep:
        print(excep)

    #app.logger.debug('Artiste infos : %s', artistInfos)
    #app.logger.debug('Params : %s', paramsTemplate)
    #app.logger.debug('Albums : %s', albumsList) 
    template_context = dict(count=count, artistInfos=artistInfos, paramsPage=paramsTemplate, list=albumsList, version=VERSION) 
    return render_template('modal-artist.html', **template_context)
        

@app.route('/album/<float:release>', methods=['GET'])
@app.route('/album/<int:release>', methods=['GET'])
def album(release):
        
    disk = mongo.db.releases.find({"id":int(release)})
    listInfosDisk = infosDisk(disk)
    videosLength = len(listInfosDisk[4])
    stocksLength = len(const.listStorage)
    
    template_context = dict(params=listInfosDisk[0], tracksList = listInfosDisk[1], extraartists = listInfosDisk[2], credits = listInfosDisk[3], videos = listInfosDisk[4], videosLength=videosLength, rangement=const.listStorage, stocksLength=stocksLength,id=int(release), version=VERSION)    
    return render_template('album.html', **template_context)


@app.route('/title/<title>', methods=['GET'])
def albumByTitle(title):
    disk = mongo.db.releases.find({"title":title})
    listInfosDisk = infosDisk(disk)
    videosLength = len(listInfosDisk[4])
    stocksLength = len(const.listStorage)
        
    #template_context = dict(params=listInfosDisk[0], tracksList = listInfosDisk[1], extraartists = listInfosDisk[2], credits = listInfosDisk[3], videos = listInfosDisk[4], rangement=const.listStorage, videosLength=videosLength)
    template_context = dict(params=listInfosDisk[0], tracksList = listInfosDisk[1], extraartists = listInfosDisk[2], credits = listInfosDisk[3], videos = listInfosDisk[4], videosLength=videosLength, rangement=const.listStorage, stocksLength=stocksLength)    
    
    return render_template('album.html', **template_context)


@app.route('/track/<track>', methods=['GET'])
def albumByTrack(track):
    #page_size = 60
    disks = mongo.db.releases.find({"tracklist.title":track})
    count = mongo.db.releases.count({"tracklist.title":track})
    albumsList = albumDict(disks)                    
    #paramsTemplate = templateParams(albumsList, 1, page_size, '')
        
    template_context = dict(track=track, count=count, albumsList=albumsList, version=VERSION)
    return render_template('track-modal.html', **template_context)


    
@app.route('/<support>', methods=['GET'])
@app.route('/<support>/', methods=['GET'])
@app.route('/<support>/<int:page_num>', methods=['GET'])
def support(support, page_num=1):
    #app.logger.debug('/support')
    page_size = 60
    
    disks = mongo.db.releases.find({"formats.name":support}).sort("artists.name", 1)
    listAlbums = albumDict(disks)                
    paramsTemplate = templateParams(listAlbums, page_num, page_size, support)
    
    compteursGen = mongo.db.compteursGen.find()
          
    template_context = dict(countList=compteursGen, support=support, typeList= "Support", paramsPage=paramsTemplate, version=VERSION)    
    return render_template('support.html', **template_context )
    
@app.route('/categorie/<categorie>', methods=['GET'])
@app.route('/categorie/<categorie>/', methods=['GET'])
@app.route('/categorie/<categorie>/<int:page_num>', methods=['GET'])
def categorylist(categorie, page_num=1):
    #app.logger.debug('/categorie')
    
    page_size = 60
    urlTag = categorie
    affiche = categorie
    if categorie == 'Hiphop':
        urlTag = 'Hip Hop'
        affiche = urlTag
    elif categorie == 'Folk':
        urlTag = 'Folk, World, & Country'
        affiche = 'Folk World Country'
    elif categorie == 'Funk Soul':   
        urlTag = 'Funk / Soul'
        affiche = 'Funk Soul'
    #message = urlTag
    #app.logger.debug(message)
    disks = mongo.db.releases.find({"genres":urlTag}).sort("artists.name", 1)
        
    listAlbums = albumDict(disks)
    paramsTemplate = templateParams(listAlbums, page_num, page_size, 'categorie/'+categorie)
    
    compteursGen = mongo.db.compteursGen.find()
        
    template_context = dict(countList=compteursGen, support=affiche, typeList= "Catégorie", paramsPage=paramsTemplate, version=VERSION)    
    return render_template('support.html', **template_context )

@app.route('/list/<support>/<categorie>', methods=['GET'])
@app.route('/list/<support>/<categorie>/', methods=['GET'])
@app.route('/list/<support>/<categorie>/<int:page_num>', methods=['GET'])
def listImprim(support, categorie, page_num=1):
    page_size = 60
    logged = connected()
    if categorie == 'Funk Soul':   
        categorie = 'Funk / Soul'
        
    disks = mongo.db.releases.find({"formats.name": support, "genres": categorie}).sort("artists.name", 1)
    listAlbums = albumDict(disks)                
    
    paramsTemplate = templateParams(listAlbums, page_num, page_size, 'list/'+support+'/'+categorie)
    compteursGen = mongo.db.compteursGen.find()
    libelle = support + '_' + categorie
    template_context = dict(countList=compteursGen, support=libelle, typeList= "Support", paramsPage=paramsTemplate, version=VERSION)    
    return render_template('supp-categList.html', **template_context )

'''
@app.route('/imprim/<support>/<categorie>', methods=['GET'])
@app.route('/imprim/<support>/<categorie>/', methods=['GET'])
def printCollections(support, categorie):
    logged = connected()
    if categorie == 'Funk Soul':   
        categorie = 'Funk / Soul'
        
    if categorie == 'undefined':
        disks = mongo.db.releases.find({"formats.name": support},{"artists.name": 1, "_id": 0,"title": 1,"year":1, "id": 1, "storage.nom": 1, "storage.position": 1}).sort("artists.name", 1)
    else:
        disks = mongo.db.releases.find({"formats.name": support, "genres": categorie},{"artists.name": 1, "_id": 0,"title": 1,"year":1, "id": 1, "storage.nom": 1, "storage.position": 1}).sort("artists.name", 1)                      
    
    compteursGen = mongo.db.compteursGen.find()
    libelle = support + '_' + categorie + '_'
    ficOut=''

    try:
        today = datetime.datetime.now()
        filename = libelle + today.strftime('%Y-%m-%d') + '.pdf'
        buffer = BytesIO()
        report = PdfPrint(buffer, 'A4', 'paysage')
        pdf = report.report(disks, libelle, today)
            
        chdir(APP_DIR+'/myapp/static/data/pdf/')
        ficOut = open(filename, "wb")
        ficOut.write(pdf)
        ficOut.close
        
    except Exception as excep:
        print(excep)
    
    #print(APP_DIR)
    #pdfListFiles = listdir(APP_DIR+'/myapp/static/data/pdf/')
    pdfListFiles = glob.glob(path.basename(APP_DIR + '/myapp/static/data/pdf/*.pdf'))

    template_context = dict(list=disks, countList=compteursGen, support=libelle, pdfFiles=pdfListFiles, file2Load=filename, version=VERSION, logged=logged)
    return render_template('imprimList.html', **template_context )       
'''

@app.route('/stockage', methods=['GET'])
@app.route('/stockage/', methods=['GET'])
def storage():
    countList = []
    countRange = []
    compteursGen = mongo.db.compteursGen.find()
    
    for support in ['Vinyl','CD','DVD']:
        nonClasse = mongo.db.releases.find({"formats.name":support, "storage.nom": "", "storage.position":0}).count()
        compteur = {
            support:nonClasse
        }
        countRange.append(compteur)
        #app.logger.debug(nonClasse)       

    #listInfosDisk = []
    for empl in ['MSGEH1','MSGEH2','MSGEH3','MSGEH4','MSGEB1','MSGEB2','MSGEB3','MSGEB4','MSGT1C1','MSGT1C2','MSGT1C3','MSGT1C4','MSGT1C5', 'MSGT2C1','MSGT2C2','MSGT2C3','MSGT2C4','MSGT2C5', 'MSGT3C1','MSGT3C2','MSGT3C3','MSGT3C4','MSGT3C5','MSGTB1','MSGTB2','MSGTB3','MSDTC1','MSDTC2','MSDTC3','MSDTC4','MSDTC5','AEE11','AEE12','AEE13', 'AEE21','AEE22','AEE23']:
        #stocks = mongo.db.releases.find({"storage.nom": empl},{"thumb": 1, "artists.name": 1, "_id": 0, "title": 1, "year": 1, "id": 1, "storage.nom": 1, "storage.position": 1}).sort("storage.position", 1)
        nbStock = mongo.db.releases.find({"storage.nom": empl}).count()
        #app.logger.debug(nbStock)
        stockItem = {
            empl:nbStock
        }
        #app.logger.debug(stockitem)
        countList.append(stockItem)
    listConstRangement = [const.MSGE,const.MSGTB,const.MSGTM,const.MSDTB,const.MEAE]

    template_context = dict(compteurs=countList, compteursGen=compteursGen, compteursRange=countRange, rangement=listConstRangement,version=VERSION)
    return render_template('stockage.html', **template_context ) 

@app.route('/stockage/<rangement>', methods=['GET'])
def storageDetail(rangement):
    countList = []
    listRangement = []
    #listIMgBarre = ["/static/img/vinyl-tranche-vert.jpg","/static/img/vinyl-tranche-orange.jpg","/static/img/vinyl-tranche-jaune.jpg","/static/img/vinyl-tranche-violet.jpg","/static/img/vinyl-tranche-rouge.jpg","/static/img/vinyl-tranche-noir.jpg","/static/img/vinyl-tranche-vert.jpg","/static/img/vinyl-tranche-orange.jpg"]
    support = 'Vinyl'
    color = const.dictIMgBarre
    
    if rangement == 'MSGEH':
        constRangement = const.MSGE + " : " + const.MSGEH
        listRangement = ['MSGEH1','MSGEH2','MSGEH3','MSGEH4']
        listConstRangement = [const.MSGEH1,const.MSGEH2,const.MSGEH3,const.MSGEH4]
    
    elif rangement == 'MSGEB':
        constRangement = const.MSGE + " : " + const.MSGEB
        listRangement = ['MSGEB1','MSGEB2','MSGEB3','MSGEB4']
        listConstRangement = [const.MSGEB1,const.MSGEB2,const.MSGEB3,const.MSGEB4]
    
    elif rangement == 'MSGTB':
        constRangement = const.MSGTB
        listRangement = ['MSGTB1','MSGTB2','MSGTB3']
        listConstRangement = [const.MSGTB1,const.MSGTB2,const.MSGTB3]
        support = 'DVD'
    
    elif rangement == 'MSGT1':
        listRangement = ['MSGT1C1','MSGT1C2','MSGT1C3','MSGT1C4','MSGT1C5']
        constRangement = const.MSGTM + " : " + const.MSGT1
        listConstRangement = [const.MSGT1C1,const.MSGT1C2,const.MSGT1C3,const.MSGT1C4,const.MSGT1C5]
        color = const.dictIMgHorizontal
        support = 'CD'

    elif rangement == 'MSGT2':
        constRangement = const.MSGTM + " : " + const.MSGT2
        listRangement = ['MSGT2C1','MSGT2C2','MSGT2C3','MSGT2C4','MSGT2C5']
        listConstRangement = [const.MSGT2C1,const.MSGT2C2,const.MSGT2C3,const.MSGT2C4,const.MSGT2C5]
        color = const.dictIMgHorizontal
        support = 'CD'
    
    elif rangement == 'MSGT3':
        constRangement = const.MSGTM + " : " + const.MSGT3
        listRangement = ['MSGT3C1','MSGT3C2','MSGT3C3','MSGT3C4','MSGT3C5']
        listConstRangement = [const.MSGT3C1,const.MSGT3C2,const.MSGT3C3,const.MSGT3C4,const.MSGT3C5]
        color = const.dictIMgHorizontal
        support = 'CD'

    elif rangement == 'MSDTB':
        constRangement = const.MSDTB
        listRangement = ['MSDTC1','MSDTC2','MSDTC3','MSDTC4','MSDTC5']   
        listConstRangement = [const.MSDTC1,const.MSDTC2,const.MSDTC3,const.MSDTC4,const.MSDTC5]
        
    elif rangement == 'MEAE1':
        constRangement = const.MEAE + " : " + const.MEAE1
        listRangement = ['AEE11','AEE12','AEE13']
        listConstRangement = [const.AEE11,const.AEE12,const.AEE13]

    elif rangement == 'MEAE2':
        constRangement = const.MEAE +  " : " + const.MEAE2
        listRangement = ['AEE21','AEE22','AEE23']
        listConstRangement = [const.AEE21,const.AEE22,const.AEE23]
    
    else:
        listRangement = []

    listInfosDisk = []
    for empl in listRangement:
        stocks = mongo.db.releases.find({"storage.nom": empl},{"thumb": 1, "artists.name": 1, "_id": 0, "title": 1, "genres": 1 , "year": 1, "id": 1, "storage.nom": 1, "storage.position": 1}).sort("storage.position", 1)
        nbStock = mongo.db.releases.find({"storage.nom": empl}).count()
        listAlbums = []
        
        for album in stocks:
            artists = album["artists"]
            artist = artists[0]
            artistName = artist["name"]
    
            stocks = album["storage"]
            #stockage = stocks[0]
            storagePosition = stocks["position"]
        
            albumItem = {
                "thumb":album["thumb"],
                "id":album["id"],
                "release":int(album["id"]),
                "artistName":artistName,
                "title":album["title"],
                "year":int(album["year"]), 
                "genres":album["genres"],
                "storage":empl,
                "position":storagePosition
            }
            listAlbums.append(albumItem)

        countList.append(nbStock)
    
        listInfosDisk.append(listAlbums)

    template_context = dict(list=listInfosDisk, rangement=rangement, compteur=countList, constRangement=constRangement, empl=listRangement, const=listConstRangement, nbEmpl=len(listRangement), color=color, support=support, version=VERSION)
    return render_template('detail_stockage.html', **template_context )
    
@app.route('/about/', methods=['GET'])
def about():
    #app.logger.debug('route /about/')
    
    template_context = dict(version=VERSION, build=BUILD, bdd=DB_NAME)
    return render_template('about.html', **template_context)

######################
#                    #
#  gestion erreurs   #
#                    #
######################

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

###########
#         #
#  admin  #
#         #
###########

@app.route('/admin/login', methods=['GET', 'POST'])
@app.route('/admin/login/', methods=['GET', 'POST'])
def login():
    #app.logger.debug(current_user.__dict__)
    #app.logger.debug(current_user.is_authenticated())
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        #user = app.config['USERS_COLLECTION'].find_one({"_id": form.username.data})
        user = mongo.db.users.find_one({"_id": form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            flash('Bienvenue, vous êtes connecté!', category='success')
            return redirect(url_for('index'))

        flash("Echec de l'identification. Vérifiez vos nom d'utilisateur et mot de passe!", category='error')
    return render_template('admin/login-modal.html', title='login', form=form)

@app.route('/admin/settings', methods=['GET', 'POST'])
@login_required
def settings():
    return render_template('admin/settings.html')

@lm.user_loader
def load_user(username):
    #u = app.config['USERS_COLLECTION'].find_one({"_id": username})
    u = mongo.db.users.find_one({"_id": username})
    if not u:
        return None
    
    return User(u['_id'])

@app.route("/admin/logout")
def logout():
    logout_user()
    flash('Vous êtes déconnecté. A bientôt!', category='error')
    return redirect(url_for('index'))

@app.route('/admin/stockage/<rangement>/<support>', methods=['GET'])
@app.route('/admin/stockage/<rangement>/<support>/<int:page_num>', methods=['GET'])
def manageStorage(rangement, support, page_num=1):
    #releasesIn = mongo.db.releases.find({"storage.nom": rangement}).sort("storage.position", 1)
    stockageIn = mongo.db.storage.find({"nom": rangement}).sort("position", 1)
    nbIn = mongo.db.storage.count({"nom": rangement})
    
    listAlbums = []
    for document in stockageIn:
        disks = mongo.db.releases.find({"id": document["release"]})
        
        if document['release'] == 0:
            albumItem = {
                "thumb":"Vide",
                "id":"",
                "artistName":"",
                "title":"",
                "formatName":"",
                "year":"",
                "storage":document['nom'],
                "position":document['position']
            }
            listAlbums.append(albumItem)

        else:
            for album in disks:
                artists = album["artists"]
                artist = artists[0]
                artistName = artist["name"]
    
                formats = album["formats"]
                typeformat = formats[0]
                formatName = typeformat["name"]
                formatQty = typeformat["qty"]
                formatSupport = "{formats} ({qty})".format(formats=formatName, qty=formatQty)

                storageNom = album["storage"].get('nom')
                storagePosition = album["storage"].get('position')
        
                albumItem = {
                    "thumb":album["thumb"],
                    "id":int(album["id"]),
                    "artistName":artistName,
                    "title":album["title"],
                    "formatName":formatSupport,
                    "year":int(album["year"]),
                    "storage":storageNom,
                    "position":storagePosition
                }
                listAlbums.append(albumItem)

    paramsTemplateIn = templateParams(listAlbums, page_num, 60, 'admin/stockage/'+rangement+'/'+support)
    
    releasesOut = mongo.db.releases.find({"formats.name": support, "storage.nom": ""}).sort("artists.name", 1)
    listOut = albumDict(releasesOut)
    nbOut = mongo.db.releases.count({"formats.name": support, "storage.nom": ""})
    paramsTemplateOut = templateParams(listOut, page_num, 60, 'admin/stockage/'+rangement+'/'+support)

    template_context = dict(paramsIn=paramsTemplateIn, paramsOut=paramsTemplateOut, rangement=rangement, nbIn=nbIn, nbOut=nbOut, support=support, version=VERSION)
    return render_template('admin/manage_storage.html', **template_context )

@app.route('/admin/stockage/update/<rangement>/support/<int:place>/<int:id>', methods=['GET'])
@app.route('/admin/stockage/update/<rangement>/support/<int:place>/<float:id>', methods=['GET'])
@app.route('/admin/stockage/update/<rangement>/support/<int:place>/<int:id>/<int:page_num>', methods=['GET'])
@app.route('/admin/stockage/update/<rangement>/support/<int:place>/<float:id>/<int:page_num>', methods=['GET'])
@login_required
def updateStorage(rangement, support, place, id, page_num=1):
    
    try:
        criteria = id
        mongo.db.releases.update_one({'id':criteria},{'$set':{'storage.nom':'', 'storage.position':0}})
          
    #    try:
    #        db.storage.update_one({'nom':rangement, 'release':id},{"$set":{"storage" : { "nom" : rangement, "position" : place, "release": 0}}})
        
    #    except Exception as excep:
    #        print(excep)

    except Exception as excep:
            print(excep)
    
    releasesIn = mongo.db.releases.find({"storage.nom": rangement}).sort("storage.position", 1)
    nbIn = mongo.db.releases.count({"storage.nom": rangement})
    listIn = albumDict(releasesIn)                
    paramsTemplateIn = templateParams(listIn, page_num, 60, 'admin/stockage/'+rangement+'/'+support)
    
    releasesOut = mongo.db.releases.find({"formats.name": support, "storage.nom": ""}).sort("artists.name", 1)
    listOut = albumDict(releasesOut)
    nbOut = mongo.db.releases.count({"formats.name": support, "storage.nom": ""})
    paramsTemplateOut = templateParams(listOut, page_num, 60, 'admin/stockage/'+rangement+'/'+support)

    template_context = dict(paramsIn=paramsTemplateIn, paramsOut=paramsTemplateOut, rangement=rangement, nbIn=nbIn, nbOut=nbOut, support=support, version=VERSION)
    return render_template('admin/manage_storage.html', **template_context )
