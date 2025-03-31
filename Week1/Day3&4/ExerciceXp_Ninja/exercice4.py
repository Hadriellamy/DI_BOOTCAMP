#Exercise 4 : Frequency Of The Words
"""
Instructions

Write a program that prints the frequency of the words from the input.

Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Then, the output should be:

    2:2
    3.:1
    3?:1
    New:1
    Python:5
    Read:1
    and:1
    between:1
    choosing:1
    or:2
    to:1

"""

# Demande de saisie à l'utilisateur
text = input("Enter text: ")

# Séparation du texte en mots (en se basant sur les espaces)
words = text.split()

# Calcul de la fréquence de chaque mot
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Affichage des fréquences triées par ordre alphabétique des mots (sensible à la casse)
for word in sorted(frequency.keys()):
    print(f"{word}:{frequency[word]}")


#Explications 
"""
Saisie et séparation :
On demande à l'utilisateur d'entrer un texte, puis on le découpe en mots avec split().
Par exemple, pour l'entrée
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
on obtient la liste :
['New', 'to', 'Python', 'or', 'choosing', 'between', 'Python', '2', 'and', 'Python', '3?', 'Read', 'Python', '2', 'or', 'Python', '3.']
Calcul de la fréquence :
On parcourt chaque mot et on incrémente son compteur dans un dictionnaire frequency.
Affichage trié :
Enfin, on affiche chaque mot suivi de sa fréquence, le tout trié par ordre alphabétique (la casse est prise en compte, donc les mots commençant par un chiffre ou une majuscule seront affichés en premier).

"""
