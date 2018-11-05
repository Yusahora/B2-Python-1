#!/usr/bin/env python36

# TITLE         : 1c-moy.py
# DESCRIPTION   : Addition de base
# DATE          : 16/10/18
# NAME          : Blanchet Noémie

import re
import operator

#Regex pour vérifier qu'il n'y a pas de nombre à l'intérieur
nameRegex = r'^[^0-9]+$'

#Vérifier qu'il n'y a pas de lettre
nbRegex = r'^\d+$'

#dictionnaire de noms et de notes
dic = {}

print('Entrez un prénom puis une note. Quand vous avez terminé appuyez sur "q"')

#boucle infinie
while True:
    name = input("Entrez un prénom ou 'q'\n")

    #"q" pour sortir de la boucle
    if name == 'q':
        break

    if re.match(nameRegex, name):
        note = input('Entrez une note\n')
        if re.match(nbRegex, note):
            dic[name] = int(note)
        else:
            print("Ce n'est pas un nombre..")

    else:
        print('Pas besoin de nombre dans un prénom..')


moyenne = sum(dic.values()) / float(len(dic))
print('Moyennne :' + str(moyenne))

#Trier le dictionnaire par ses valeurs
dicoTrie = sorted(dic.items(), key=operator.itemgetter(1), reverse = True)

#affiche le dictionnaire en gardant uniquement les 5 premières entrées
print(dicoTrie[:5])
