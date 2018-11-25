
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''

 Définition des constantes  

'''
       
#Salon étagère gauche
MSGE =   'Salon Gauche Etagère  (Vinyl)'
MSGEH1 = 'Etagère gauche Haut Case 1'
MSGEH2 = 'Etagère gauche Haut Case 2'
MSGEH3 = 'Etagère gauche Haut Case 3'
MSGEH4 = 'Etagère gauche Haut Case 4'

MSGEB1 = 'Etagère gauche Bas Case 1'
MSGEB2 = 'Etagère gauche Bas Case 2'
MSGEB3 = 'Etagère gauche Bas Case 3'
MSGEB4 = 'Etagère gauche Bas Case 4'
         
#Salon tiroir bas gauche
MSGTB = 'Salon Gauche Tiroir Bas (DVD)'
MSGTB1 = 'Tiroir Bas Gauche case 1'
MSGTB2 = 'Tiroir Bas Gauche case 2'
MSGTB3 = 'Tiroir Bas Gauche case 3'
    
#Salon tiroir centre
MSGTM = 'Salon Gauche Tiroirs Milieu (CD / DVD)'
MSGT1C1 = 'Tiroir Bas Centre 1 Rangée 1'
MSGT1C2 = 'Tiroir Bas Centre 1 Rangée 2'
MSGT1C3 = 'Tiroir Bas Centre 1 Rangée 3'
MSGT1C4 = 'Tiroir Bas Centre 1 Rangée 4'
MSGT1C5 = 'Tiroir Bas Centre 1 Rangée 5'
MSGT2C1 = 'Tiroir Bas Centre 2 Rangée 1'
MSGT2C2 = 'Tiroir Bas Centre 2 Rangée 2'
MSGT2C3 = 'Tiroir Bas Centre 2 Rangée 3'
MSGT2C4 = 'Tiroir Bas Centre 2 Rangée 4'
MSGT2C5 = 'Tiroir Bas Centre 2 Rangée 5'
MSGT3C1 = 'Tiroir Bas Centre 3 Rangée 1'
MSGT3C2 = 'Tiroir Bas Centre 3 Rangée 2'
MSGT3C3 = 'Tiroir Bas Centre 3 Rangée 3'
MSGT3C4 = 'Tiroir Bas Centre 3 Rangée 4'
MSGT3C5 = 'Tiroir Bas Centre 3 Rangée 5'

#Salon tiroir droite
MSDTB = 'Salon Droite Tiroir Bas (Vinyl)'
MSDTC1 = 'Tiroir Bas Droite Case 1'
MSDTC2 = 'Tiroir Bas Droite Case 2'
MSDTC3 = 'Tiroir Bas Droite Case 3'
MSDTC4 = 'Tiroir Bas Droite Case 4'
MSDTC5 = 'Tiroir Bas Droite Case 5'
        
#Entrée armoire
MEAE = 'Entrée Armoire (Vinyl)'
AEE11 = 'Armoire Etagère 1 Case 1'
AEE12 = 'Armoire Etagère 1 Case 2'
AEE13 = 'Armoire Etagère 1 Case 3'
AEE21 = 'Armoire Etagère 2 Case 1'
AEE22 = 'Armoire Etagère 2 Case 2'
AEE23 = 'Armoire Etagère 2 Case 3'

listStorage = [{'name':'MSGEH1', 'libelle': MSGEH1},{'name':'MSGEH2', 'libelle':MSGEH2},{'name':'MSGEH3', 'libelle':MSGEH3},{'name':'MSGEH4','libelle':MSGEH4},{'name':'MSGEB1','libelle':MSGEB1},{'name':'MSGEB2','libelle':MSGEB2},{'name':'MSGEB3','libelle':MSGEB3},{'name':'MSGEB4','libelle':MSGEB4},
                {'name':'MSGT1C1','libelle':MSGT1C1},{'name':'MSGT1C2','libelle':MSGT1C2},{'name':'MSGT1C3','libelle':MSGT1C3},{'name':'MSGT1C4','libelle':MSGT1C4},{'name':'MSGT1C5','libelle':MSGT1C5},
                {'name':'MSGT2C1','libelle':MSGT2C1},{'name':'MSGT2C2','libelle':MSGT2C2},{'name':'MSGT2C3','libelle':MSGT2C3},{'name':'MSGT2C4','libelle':MSGT2C4},{'name':'MSGT2C5','libelle':MSGT2C5},
                {'name':'MSGT3C1','libelle':MSGT3C1},{'name':'MSGT3C2','libelle':MSGT3C2},{'name':'MSGT3C3','libelle':MSGT3C3},{'name':'MSGT3C4','libelle':MSGT3C4},{'name':'MSGT3C5','libelle':MSGT3C5},
                {'name':'MSGTB1','libelle':MSGTB1},{'name':'MSGTB2','libelle':MSGTB2},{'name':'MSGTB3','libelle':MSGTB3},
                {'name':'MSDTC1','libelle':MSDTC1},{'name':'MSDTC2','libelle':MSDTC2},{'name':'MSDTC3','libelle':MSDTC3},{'name':'MSDTC4','libelle':MSDTC4},{'name':'MSDTC5','libelle':MSDTC5},
                {'name':'AEE11','libelle':AEE11},{'name':'AEE12','libelle':AEE12},{'name':'AEE13','libelle':AEE13},
                {'name':'AEE21','libelle':AEE21},{'name':'AEE22','libelle':AEE22},{'name':'AEE23','libelle':AEE23}]

for index in range(0, len(listStorage)):
    if listStorage[index].get('name') == 'MSDTC4':
        print(listStorage[index].get('libelle'))
    else:
        print(index)


        