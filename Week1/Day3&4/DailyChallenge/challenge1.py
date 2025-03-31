#Challenge 1
"""
Ask the user for a number and a length.
Create a program that prints a list of multiples of the number until the list length reaches length.
Examples

number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

"""

number = int(input("Entrez un nombre: "))
length = int(input("Entrez la longueur de la liste: "))

multiples = []
for i in range(1, length + 1):
    multiples.append(number * i)

print(multiples)





#Explications 

"""
On demande à l'utilisateur d'entrer le nombre de base et la longueur désirée pour la liste.
On initialise une liste vide multiples.
On parcourt les nombres de 1 à length et, pour chaque itération, on calcule le multiple en multipliant le nombre de base par l'indice courant.
Enfin, on affiche la liste des multiples.
Exemple :

Si l'utilisateur entre 7 pour le nombre et 5 pour la longueur, le programme affiche [7, 14, 21, 28, 35].
 
"""
