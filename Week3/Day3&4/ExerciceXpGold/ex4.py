#Exercise 4 : Regular Expression #2
"""
Instructions

Hint: Use the RegEx (module)

Ask the user for their full name (example: “John Doe”), and check the validity of their answer:
The name should contain only letters.
The name should contain only one space.
The first letter of each name should be upper cased.
#############

✅ Objectif

Créer un programme qui :

Demande à l’utilisateur son nom complet (ex: "Hadriel Lahmi")
Vérifie que :
Il n’y a que des lettres et un seul espace
Chaque nom commence par une majuscule
Le format est correct : Prénom Nom


🧠 Rappel RegEx utile :

^[A-Z][a-z]+ [A-Z][a-z]+$


Explication :

^ et $ : début et fin de chaîne
[A-Z] : majuscule
[a-z]+ : suite de lettres minuscules
: un seul espace
Répété une deuxième fois pour le nom de famille

"""

import re

def check_full_name():
    name = input("Entrez votre nom complet  : ")
    
    pattern = r'^[A-Z][a-z]+ [A-Z][a-z]+$'

    if re.fullmatch(pattern, name):
        print("Nom valide !")
    else:
        print("Nom invalide. Assurez-vous d'utiliser le bon format : 'Prénom Nom' avec des majuscules au début.")

#Test
check_full_name()

