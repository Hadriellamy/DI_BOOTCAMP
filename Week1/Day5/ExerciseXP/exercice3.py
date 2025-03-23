#Exercise 3: Zara
"""
Instructions

Here is some information about a brand.
name: Zara 
creation_date: 1975 
creator_name: Amancio Ortega Gaona 
type_of_clothes: men, women, children, home 
international_competitors: Gap, H&M, Benetton 
number_stores: 7000 
major_color: 
    France: blue, 
    Spain: red, 
    US: pink, green


2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
3. Change the number of stores to 2.
4. Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are.
5. Add a key called country_creation with a value of Spain.
6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
7. Delete the information about the date of creation.
8. Print the last international competitor.
9. Print the major clothes colors in the US.
10. Print the amount of key value pairs (ie. length of the dictionary).
11. Print the keys of the dictionary.
12. Create another dictionary called more_on_zara with the following details:

creation_date: 1975 
number_stores: 10 000


13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
14. Print the value of the key number_stores. What just happened ?

"""

# 1. Création du dictionnaire brand avec les informations fournies
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"]
    }
}

# 2. La variable brand a été créée avec :
#    - Les valeurs "type_of_clothes" et "international_competitors" en listes.
#    - "major_color" est un dictionnaire.

# 3. Changer le nombre de magasins en 2.
brand["number_stores"] = 2

# 4. Utiliser le key "type_of_clothes" pour imprimer une phrase expliquant qui sont les clients de Zara.
clients = ", ".join(brand["type_of_clothes"])
print(f"Zara's clients include: {clients}.")

# 5. Ajouter une clé "country_creation" avec pour valeur "Spain".
brand["country_creation"] = "Spain"

# 6. Vérifier si le key "international_competitors" existe dans le dictionnaire.
#    S'il existe, ajouter le magasin "Desigual".
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# 7. Supprimer l'information sur la date de création.
del brand["creation_date"]

# 8. Imprimer le dernier concurrent international.
print("Last international competitor:", brand["international_competitors"][-1])

# 9. Imprimer les principales couleurs de vêtements aux USA.
print("Major clothes colors in the US:", brand["major_color"]["US"])

# 10. Imprimer le nombre de paires clé/valeur du dictionnaire.
print("Number of key/value pairs in brand:", len(brand))

# 11. Imprimer les clés du dictionnaire.
print("Keys of the brand dictionary:", list(brand.keys()))

# 12. Créer un autre dictionnaire appelé more_on_zara avec les détails suivants :
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# 13. Ajouter les informations du dictionnaire more_on_zara au dictionnaire brand.
#     La méthode update() permet de mettre à jour ou ajouter les clés et valeurs.
brand.update(more_on_zara)

# 14. Imprimer la valeur de la clé "number_stores". Que s'est-il passé ?
print("Updated number of stores:", brand["number_stores"])
# La valeur affichée est 10000, ce qui montre que la mise à jour a remplacé l'ancienne valeur (2) par celle du dictionnaire more_on_zara.


