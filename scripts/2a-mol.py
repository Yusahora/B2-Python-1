#!/usr/bin/env python36

# TITLE         : 2a-mol.py
# DESCRIPTION   : PLus ou moins avec fichiers
# DATE          : 05/11/18
# NAME          : Blanchet Noémie

import signal
import random
import re


re = re.compile('^[0-9]+') #regex pour vérifirier si c'est un int
rand = random.randint(0, 100)
jeMeCasse = False

#Fonction pour dire aurevoir
def bisousbisous():
    return print('A bientôt dude, des bisous')
    exit()

#Fonction pour écrire dans un fichier
def editFichier(x):
  test = open("plusoumoins.txt", "w")
  test.write(x)
  test.close()

#on créé la fonction pour lire dans le fichier
def lectureFichier():
  test = open("plusoumoins.txt", "r")
  x = test.read()
  test.close()
  return x

#Fonction pour quitter le programme
def quitter(sig, frame):
    print('\nC\'est propre moyen c\'que tu fais')
    exit()

signal.signal(signal.SIGINT, quitter)

editFichier("--- Bienvenue dans le jeu du plus ou moins---\nEntrez un nombre entre 0 et 100 :")

#Tant qu'on ne trouve pas le bon nombre on continu
while jeMeCasse is False :
    user = lectureFichier()

    if re.match(user):
        user = int(user)
        if user > rand :
            editFichier('C\'est trop grand')
        elif user < rand :
            editFichier('C\'est trop petit')
        else :
            editFichier('Bien ouèj, on rigole on rigole mais on vois pas le fond du bol')
            jeMeCasse = True
            bisousbisous()
