#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
myapp/const.

Created on 25|10
           -----
           20|18

@author: rdlc_Dev(alain)
@version:1.0 

"""
'''

 Définition des constantes  

'''
       
#Salon étagère gauche
MSGE =   'Salon Etagère Gauche'
MSGEH = 'Etagère Haute'
MSGEH1 = 'Case 1'
RMSGEH1 = MSGE + ' Haute : ' + MSGEH1
MSGEH2 = 'Case 2'
RMSGEH2 = MSGE + ' Haute : ' + MSGEH2
MSGEH3 = 'Case 3'
RMSGEH3 = MSGE + ' Haute : ' + MSGEH3
MSGEH4 = 'Case 4'
RMSGEH4 = MSGE + ' Haute : ' + MSGEH4
MSGEB = 'Etagère Basse'
MSGEB1 = 'Case 1'
RMSGEB1 = MSGE + ' Basse : ' + MSGEB1
MSGEB2 = 'Case 2'
RMSGEB2 = MSGE + ' Basse : ' + MSGEB2
MSGEB3 = 'Case 3'
RMSGEB3 = MSGE + ' Basse : ' + MSGEB3
MSGEB4 = 'Case 4'
RMSGEB4 = MSGE + ' Basse : ' + MSGEB4
         
#Salon tiroir bas gauche
MSGTB = 'Salon Tiroir Gauche Bas'
MSGTB1 = 'Tiroir Bas Gauche case 1'
MSGTB2 = 'Tiroir Bas Gauche case 2'
MSGTB3 = 'Tiroir Bas Gauche case 3'
    
#Salon tiroir centre
MSGTM = 'Salon Tiroirs Centre'
MSGT1 = 'Tiroir Haut'
MSGT1C1 = 'Colonne 1'
RMSGT1C1 = MSGTM + ' ' + MSGT1 +' : ' + MSGT1C1
MSGT1C2 = 'Colonne 2'
RMSGT1C2 = MSGTM + ' ' + MSGT1 +' : ' + MSGT1C2
MSGT1C3 = 'Colonne 3'
RMSGT1C3 = MSGTM + ' ' + MSGT1 +' : ' + MSGT1C3
MSGT1C4 = 'Colonne 4'
RMSGT1C4 = MSGTM + ' ' + MSGT1 +' : ' + MSGT1C4
MSGT1C5 = 'Colonne 5'
RMSGT1C5 = MSGTM + ' ' + MSGT1 +' : ' + MSGT1C5
MSGT2 = 'Tiroir Milieu'
MSGT2C1 = 'Colonne 1'
RMSGT2C1 = MSGTM + ' ' + MSGT2 +' : ' + MSGT2C1
MSGT2C2 = 'Colonne 2'
RMSGT2C2 = MSGTM + ' ' + MSGT2 +' : ' + MSGT2C2
MSGT2C3 = 'Colonne 3'
RMSGT2C3 = MSGTM + ' ' + MSGT2 +' : ' + MSGT2C3
MSGT2C4 = 'Colonne 4'
RMSGT2C4 = MSGTM + ' ' + MSGT2 +' : ' + MSGT2C4
MSGT2C5 = 'Colonne 5' 
RMSGT2C5 = MSGTM + ' ' + MSGT2 +' : ' + MSGT2C5
MSGT3 = 'Tiroir Bas'
MSGT3C1 = 'Colonne 1'
RMSGT3C1 = MSGTM + ' ' + MSGT3 +' : ' + MSGT3C1
MSGT3C2 = 'Colonne 2'
RMSGT3C2 = MSGTM + ' ' + MSGT3 +' : ' + MSGT3C2
MSGT3C3 = 'Colonne 3'
RMSGT3C3 = MSGTM + ' ' + MSGT3 +' : ' + MSGT3C3
MSGT3C4 = 'Colonne 4'
RMSGT3C4 = MSGTM + ' ' + MSGT3 +' : ' + MSGT3C4
MSGT3C5 = 'Colonne 5'
RMSGT3C5 = MSGTM + ' ' + MSGT3 +' : ' + MSGT3C5

#Salon tiroir droite
MSDTB = 'Salon Tiroir Droite Bas'
MSDTC1 = ' Case 1'
RMSDTC1 = MSDTB + MSDTC1
MSDTC2 = ' Case 2'
RMSDTC2 = MSDTB + MSDTC2
MSDTC3 = ' Case 3'
RMSDTC3 = MSDTB + MSDTC3
MSDTC4 = ' Case 4'
RMSDTC4 = MSDTB + MSDTC4
MSDTC5 = ' Case 5'
RMSDTC5 = MSDTB + MSDTC5
        
#Entrée armoire
MEAE = 'Entrée Armoire'
MEAE1 = ' Etagère 1'
AEE11 = ' Case 1'
RAEE11 = MEAE + MEAE1 + AEE11
AEE12 = ' Case 2'
RAEE12 = MEAE + MEAE1 + AEE12
AEE13 = ' Case 3'
RAEE13 = MEAE + MEAE1 + AEE13
MEAE2 = ' Etagère 2'
AEE21 = ' Case 1'
RAEE21 = MEAE + MEAE2 + AEE21
AEE22 = ' Case 2'
RAEE22 = MEAE + MEAE2 + AEE22
AEE23 = ' Case 3'
RAEE23 = MEAE + MEAE2 + AEE23

listStorage = [{'name':'MSGEH1', 'libelle': RMSGEH1},{'name':'MSGEH2', 'libelle':RMSGEH2},{'name':'MSGEH3', 'libelle':RMSGEH3},{'name':'MSGEH4','libelle':RMSGEH4},
                {'name':'MSGEB1','libelle':RMSGEB1},{'name':'MSGEB2','libelle':RMSGEB2},{'name':'MSGEB3','libelle':RMSGEB3},{'name':'MSGEB4','libelle':RMSGEB4},
                {'name':'MSGT1C1','libelle':RMSGT1C1},{'name':'MSGT1C2','libelle':RMSGT1C2},{'name':'MSGT1C3','libelle':RMSGT1C3},{'name':'MSGT1C4','libelle':RMSGT1C4},{'name':'MSGT1C5','libelle':RMSGT1C5},
                {'name':'MSGT2C1','libelle':RMSGT2C1},{'name':'MSGT2C2','libelle':RMSGT2C2},{'name':'MSGT2C3','libelle':RMSGT2C3},{'name':'MSGT2C4','libelle':RMSGT2C4},{'name':'MSGT2C5','libelle':RMSGT2C5},
                {'name':'MSGT3C1','libelle':RMSGT3C1},{'name':'MSGT3C2','libelle':RMSGT3C2},{'name':'MSGT3C3','libelle':RMSGT3C3},{'name':'MSGT3C4','libelle':RMSGT3C4},{'name':'MSGT3C5','libelle':RMSGT3C5},
                {'name':'MSGTB1','libelle':MSGTB1},{'name':'MSGTB2','libelle':MSGTB2},{'name':'MSGTB3','libelle':MSGTB3},
                {'name':'MSDTC1','libelle':RMSDTC1},{'name':'MSDTC2','libelle':RMSDTC2},{'name':'MSDTC3','libelle':RMSDTC3},{'name':'MSDTC4','libelle':RMSDTC4},{'name':'MSDTC5','libelle':RMSDTC5},
                {'name':'AEE11','libelle':RAEE11},{'name':'AEE12','libelle':RAEE12},{'name':'AEE13','libelle':RAEE13},
                {'name':'AEE21','libelle':RAEE21},{'name':'AEE22','libelle':RAEE22},{'name':'AEE23','libelle':RAEE23}]

listIMgBarre = [{'name':'Rock', 'imgBarre':'/static/img/vinyl-tranche-vert.jpg'},
                {'name':'Blues', 'imgBarre':'/static/img/vinyl-tranche-orange.jpg'},
                {'name':'Pop', 'imgBarre':'/static/img/vinyl-tranche-jaune.jpg'},
                {'name':'Latin', 'imgBarre':'/static/img/vinyl-tranche-rouge.jpg'},
                {'name':'Hip Hop', 'imgBarre':'/static/img/vinyl-tranche-noir.jpg'},
                {'name':'Jazz', 'imgBarre':'/static/img/vinyl-tranche.jpg'}]

dictIMgBarre = {'Jazz':'/static/img/vinyl-tranche.png', 'Rock':'/static/img/vinyl-tranche-vert.jpg', 'Blues':'/static/img/vinyl-tranche-orange.jpg',
                'Pop':'/static/img/vinyl-tranche-rouge.jpg', 'Latin':'/static/img/vinyl-tranche-jaune.jpg', 'Hip Hop':'/static/img/vinyl-tranche-noir.jpg',
                'Electronic':'/static/img/vinyl-tranche-vert2.jpg'}

dictIMgHorizontal = {'Jazz':'/static/img/vinyl-h.png', 'Rock':'/static/img/vinyl-h-vert.jpg', 'Blues':'/static/img/vinyl-h-orange.jpg',
                'Pop':'/static/img/vinyl-h-rouge.jpg', 'Latin':'/static/img/vinyl-h-jaune.jpg', 'Hip Hop':'/static/img/vinyl-h-noir.jpg',
                'Electronic':'/static/img/vinyl-h-vert2.jpg'}
    