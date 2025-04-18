 #Exercise 1 – Random Sentence Generator
"""
Instructions

Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

Hint : The generated sentences do not have to make sense.

Download this word list

Save it in your development directory.

Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
use the words list to get your random words.
the amount of words should be the value of the length parameter.

Take the random words and create a sentence (using a python method), the sentence should be lower case.

Create a function called main which will:

Print a message explaining what the program does.

Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
If the user inputs incorrect data, print an error message and end the program.
If the user inputs correct data, run your code.
######################################################################################################################################################################

🔍 Objectif de l’exercice

Créer un générateur de phrases aléatoires qui :

Lit une liste de mots à partir d’un fichier texte.
Demande à l’utilisateur combien de mots il veut dans la phrase (entre 2 et 20).
Génére une phrase avec ce nombre de mots choisis aléatoirement dans la liste.
Affiche cette phrase en minuscules.


🧠 Étapes détaillées de l’exercice

1. Télécharger et lire le fichier de mots
Tu dois avoir un fichier texte contenant beaucoup de mots (souvent fourni sous le nom words.txt). Chaque mot est sur une ligne.

Tu devras écrire une fonction get_words_from_file() qui :

Ouvre le fichier
Lit chaque ligne (donc chaque mot)
Les stocke dans une collection Python : une liste est idéale ici.
2. Générer une phrase aléatoire
Une fonction get_random_sentence(length) qui :

Prend en paramètre le nombre de mots à inclure dans la phrase.
Utilise le module random pour sélectionner length mots de manière aléatoire dans la liste de mots.
Rejoint ces mots dans une phrase, en les mettant en minuscules.
3. Fonction main() pour l’interaction avec l’utilisateur
Cette fonction va :

Expliquer ce que fait le programme.
Demander à l’utilisateur d’entrer un nombre entre 2 et 20.
Valider l’entrée (vérifier que c’est bien un entier entre 2 et 20).
Si c’est correct, appeler get_random_sentence() et afficher la phrase.
Sinon, afficher un message d’erreur et arrêter le programme.


"""

import random

def get_words_from_file():
    try:
        with open("words.txt", "r") as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print("Le fichier 'words.txt' est introuvable.")
        return []

def get_random_sentence(length):
    words = get_words_from_file()
    if not words:
        return "Erreur : liste de mots vide."
    
    # Choisir des mots aléatoires
    sentence_words = random.choices(words, k=length)
    
    # Créer la phrase
    sentence = ' '.join(sentence_words).lower()
    return sentence

def main():
    print("Bienvenue dans le générateur de phrase aléatoire.")
    print("Ce programme génère une phrase aléatoire avec un nombre de mots choisi.")
    
    try:
        length = int(input("Combien de mots voulez-vous dans votre phrase ? (entre 2 et 20) : "))
        if 2 <= length <= 20:
            sentence = get_random_sentence(length)
            print("Phrase générée :", sentence)
        else:
            print("Erreur : le nombre doit être entre 2 et 20.")
    except ValueError:
        print("Erreur : vous devez entrer un **nombre entier**.")

# Lancer le programme
main()
