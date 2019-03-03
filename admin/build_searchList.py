from pymongo import MongoClient
from os import path, chdir, getcwd, listdir
import os
import json

# Connexion to database
MONGO_HOST = "192.168.1.24"
MONGO_PORT = 27017
MONGO_DB = "mymusicDev"
MONGO_USER = "mydiskotekUser"
MONGO_PASS = "DISK_Ranv14860"

connection = MongoClient(MONGO_HOST, MONGO_PORT)
db = connection[MONGO_DB]
#db.authenticate(MONGO_USER, MONGO_PASS)

APP_DIR = os.path.abspath(os.path.dirname(__file__))

#Liste des tracks
print("Liste des tracks")
listTracks = db.releases.distinct("tracklist.title")

tracks = []
chdir('/Users/alain/projects/mydiskotek/myapp/static/data/json/')
with open('listTracks.json', 'w') as file:
    for track in listTracks:
        dictTrack = {
            'track':track
        }
        tracks.append(dictTrack)
        #print(json.dumps(dictTrack, indent=4))

    json.dump(tracks, file, indent=4)

#Liste des albums
print("Liste des albums")
listAlbums = db.releases.distinct("title")

albums = []
chdir('/Users/alain/projects/mydiskotek/myapp/static/data/json/')
with open('listAlbums.json', 'w') as file:
    for title in listAlbums:
        dictAlbum = {
            'title':title
        }
        albums.append(dictAlbum)
        #print(json.dumps(dictAlbum, indent=4))
        
    json.dump(albums, file, indent=4)

# Liste des artists
print("Liste des artistes")
listArtists = db.releases.distinct("artists.name")

artists = []
chdir('/Users/alain/projects/mydiskotek/myapp/static/data/json/')
with open('listArtists.json', 'w') as file:
    for artistName in listArtists:
        dictArtist = {
            'name':artistName
        }
        artists.append(dictArtist)
        #print(json.dumps(dictArtist, indent=4))
        
    json.dump(artists, file, indent=4)
