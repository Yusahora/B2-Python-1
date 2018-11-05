#!/usr/bin/env python36

# TITLE         : 1a-add
# DESCRIPTION   : Addition de base
# DATE          : 15/10/18
# NAME          : Blanchet Noémie

import re

#Vérifier qu'il n'y a pas de lettre
nbRegex = r'^\d+$'

print('Entrer deux nombres :')

#nombres choisis par l'utilisateur
input1 = input('Nombre 1 :\n')
input2 = input('Nombre 2 :\n')

#fonction pour additionner deux nombres
def add(number1, number2):
    return int(number1) + int(number2)

#boucle vérification nombre ou pas nombre
if re.match(nbRegex, input1) and re.match(nbRegex, input2):
    #le résultat de la fonction
    total = add(input1, input2)

    #afficher le résultat
    print(total)
else:
    print("Je t'ai dit des nombres stp")
