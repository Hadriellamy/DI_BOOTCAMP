#Challenge 2
"""
Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
Examples

user's word : "ppoeemm" ➞ "poem"

user's word : "wiiiinnnnd" ➞ "wind"

user's word : "ttiiitllleeee" ➞ "title"

user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
Notes
Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

"""

word = input("Enter a word: ")

result = ""
prev_char = ""

for char in word:
    if char != prev_char:
        result += char
    prev_char = char


print(result)


#Explications 

"""
Lecture du mot :
On demande à l'utilisateur d'entrer un mot (par exemple, "ppoeemm").
Initialisation :
On initialise result comme chaîne vide et prev_char pour stocker le caractère précédent lors de la boucle.
Parcours du mot :
Pour chaque caractère, si le caractère est différent du caractère précédent, on l'ajoute à result. Sinon, on passe au caractère suivant.
Affichage :
Le programme affiche le mot avec les doublons consécutifs supprimés (par exemple, "ppoeemm" devient "poem").

"""

