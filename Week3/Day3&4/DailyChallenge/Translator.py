#Instructions :
"""
Consider this list

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 
Look at this result :
{"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
You have to recreate the result using a translator module. Take a look at the googletrans module
##############################################################################################################

Explication de l'énoncé :
L'objectif de cet exercice est d'utiliser un module de traduction pour convertir une liste de mots en français dans leur traduction en anglais. Le module suggéré dans l'énoncé est googletrans, qui est une bibliothèque Python permettant d'utiliser l'API Google Translate.

Étapes à suivre :
Liste donnée : La liste de mots en français french_words est donnée, et nous devons créer un dictionnaire où chaque mot en français est la clé, et sa traduction en anglais est la valeur.
Utilisation de googletrans :
Installer et importer le module googletrans.
Utiliser ce module pour traduire chaque mot de la liste en anglais.
Créer un dictionnaire : Pour chaque mot de la liste french_words, traduire le mot en anglais et ajouter une entrée dans un dictionnaire où la clé est le mot en français et la valeur est sa traduction en anglais.

"""


from googletrans import Translator


french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# Création d'un objet Translator
translator = Translator()

# Création du dictionnaire pour stocker les traductions
translations = {}

# Traduction des mots français en anglais
for word in french_words:
    translated_word = translator.translate(word, src='fr', dest='en')
    translations[word] = translated_word.text

# Affichage du dictionnaire des traductions
print(translations)


