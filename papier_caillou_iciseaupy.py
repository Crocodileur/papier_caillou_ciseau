from numbers import Number
import time
import os
import random

os.system('cls')
print('Bienvenue dans le PIERRE, FEUILLE, CISEAU')

nb_manche = input('Saissisez le nombre de manche(s) : ')
nb_manche= int(nb_manche)
time.sleep(1)

for manche in range(nb_manche):
    os.system('cls')
    print('Début de la manche',manche+1,'.\n')
    reponse = ('Saissisez pierre, feuille ou ciseau (p,f,c)')

    while True:
        reponse = input("Entre votre réponse : (P, F, C) : ")
        list_rep = ['P','F','C','CISEAU','PIERRE','FEUILLE','p','f','c','pierre','feuille','ciseau']

        if(reponse not in list_rep):
            pass
        else:
            break

    list_pfc = ["PIERRE","FEUILLE","CISEAU"]
    choix_pc = random.choice(list_pfc)
        
    print('\nOrdinateur : ', choix_pc,'\n')
    
    if (reponse=='P' or reponse =='P' or reponse=='PIERRE' or reponse=='pierre'):
        print('Joueur : PIERRE')
        if choix_pc=="PIERRE":
            print('égalité')
        if choix_pc=="FEUILLE":
            print('perdu')
        if choix_pc=="CISEAU":
            print('gagné')
    
    
    elif (reponse=='C' or reponse =='C' or reponse=='CISEAU' or reponse=='CISEAU'):
        print('Joueur : CISEAU\n')
        if choix_pc=="PIERRE":
            print('perdu')
        if choix_pc=="FEUILLE":
            print('gagné')
        if choix_pc=="CISEAU":
            print('égalité')
    
    
    elif (reponse=='F' or reponse =='F' or reponse=='FEUILLE' or reponse=='feuille'):
        print('Joueur : FEUILLE\n')
        if choix_pc=="PIERRE":
            print('gagné')
        if choix_pc=="FEUILLE":
            print('égalité')
        if choix_pc=="CISEAU":
            print('perdu')

    print('\n\nFin de la manche, appuyez pour continuer...')
    input()
