#!/usr/bin/env python36

# TITLE         : 1d-mol.py
# DESCRIPTION   : PLus ou moins
# DATE          : 05/11/18
# NAME          : Blanchet Noémie

import random
import re
import signal

print('--- BIENVENU DANS LE JEU DU PLUS OU MOINS ---\n')


coups = 0
rand = random.randint(0,100) #générer le nombre aléatoire
user = -1
re = re.compile('^[0-9]+') #regex pour vérifier si c'est un int

#Fonction pour dire aurevoir + le résultat
def bisousbisous():
    return print('C\'était bien',str(rand),'\nA bientôt dude')
    exit()

#Fonction pour quitter le programme
def quitter(sig, frame):
    print('\nC\'est propre moyen c\'que tu fais')
    exit()

signal.signal(signal.SIGINT, quitter)

#Tant que l'utilisateur à pas trouvé on continu
while user != str(rand):
    print('Entrez un nombre entre 0 et 100 :')
    user = input()
    if user == 'q':
        bisousbisous()
    elif re.match(user):
        if int(user) > rand:
             print('C\'est trop grand')
        elif int(user) < rand:
            print('C\'est trop petit')
    else:
        print("tips : Pour trouver un nombre il faut entrer des nombres :)")

bisousbisous()
