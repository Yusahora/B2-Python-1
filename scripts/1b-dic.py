#!/usr/bin/env python36

# TITLE         : 1b-dic.py
# DESCRIPTION   : liste de noms
# DATE          : 15/10/18
# NAME          : Blanchet Noémie

import re

#Regex pour vérifier qu'il n'y a pas de nombre à l'intérieur
nameRegex = r'^[^0-9]+$'

#la liste des noms
tab = []
print('Entrer un prénom par ligne svp. Quand vous avez terminé appuyez sur "q"')

#boucle infinie
while True:
    name = input('')

    #"q" pour sortir de la boucle
    if name == 'q':
        break

    if re.match(nameRegex, name):
        tab.append(name)
    else:
        print('Pas besoin de nombre dans un prénom..')


#trier la liste par ordre alphabétique
tab.sort()
print(tab)
