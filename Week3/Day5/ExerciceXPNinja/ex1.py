#Exercise 1 : Restaurant Menu Manager - Regular Expressions
"""
Instructions

Goal: The Manager wants to have a special Valentine’s night, but there are some rules.



Create a new list of special Valentine’s day items inside the json file. For now the list should be empty.

Ask to the manager for a new Valentine item to add, if the item is correct (ie. follows the rules below), then add it to the list inside the json file.
Each word in the item name should begin with an uppercase letter and because it’s Valentines Day, the first word needs to begin with a capital “V”.

If the name contains connection words, they should begin in lowercase.
Example: Vegetable Soup of Valentines-day

The name of the meal needs to contain at least two “e”, and no numbers.

The price needs to match the following pattern: XX,14, where X are numbers.

Create an algorithm that displays a heart made of stars (*), when the menu is showed.

###################################################################################################################################

🎯 Objectifs de l'exercice :

Créer un fichier JSON avec une liste d'articles pour la Saint-Valentin.
Permettre à un manager d'ajouter un nouvel élément au menu.
Valider l'élément ajouté (en respectant les règles de nommage et de prix).
Afficher un cœur en forme d'étoiles (★) à la fin du programme, pour ajouter une touche festive.

📝 Règles pour ajouter un nouvel élément :

Nom de l'élément :
Chaque mot commence par une majuscule, mais le premier mot commence par "V" pour valider "Valentine's".
Les mots de connexion (par exemple "of", "and", "the", "on") commencent par une minuscule.
Le nom doit contenir au moins deux lettres "e" et pas de chiffres.
Prix :
Le prix doit suivre le format XX,14 (où X représente un chiffre).
Affichage du menu :
Lors de l'affichage du menu, un cœur fait de étoiles (★) sera affiché.

"""

import json
import re

# Initialisation du fichier JSON avec une liste vide d'articles
menu_data = {
    "valentine_items": []
}

# Sauvegarder le fichier JSON initial
def save_menu_to_file():
    with open("valentine_menu.json", "w") as file:
        json.dump(menu_data, file, indent=4)

# Charger les données du fichier JSON
def load_menu_from_file():
    try:
        with open("valentine_menu.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return menu_data  # Fichier inexistant, retourne les données par défaut

# Vérification que le nom de l'élément suit les règles
def validate_item_name(name):
    # Vérification que le nom commence par "V" et respecte la capitalisation
    pattern = r"^V([A-Z][a-z]*\s)?([a-z]+[\s]?)?[a-zA-Z]+$"
    if re.match(pattern, name):
        if name.count("e") >= 2:  # Vérifier qu'il y a au moins 2 lettres "e"
            return True
    return False

# Vérification que le prix suit le format XX,14
def validate_price(price):
    price_pattern = r"^\d{2},14$"
    return bool(re.match(price_pattern, price))

# Ajouter un élément au menu s'il est valide
def add_item_to_menu(name, price):
    if validate_item_name(name) and validate_price(price):
        item = {"name": name, "price": price}
        menu_data["valentine_items"].append(item)
        save_menu_to_file()
        print(f"Item '{name}' added to the menu with price {price}.")
    else:
        print("Invalid item name or price. Please follow the rules.")

# Affichage d'un cœur en étoiles
def print_heart():
    heart = [
        "  **     **  ",
        "****   ****",
        "***********",
        "***********",
        " ********* ",
        "   *****   ",
        "    ***    ",
        "     *     "
    ]
    for line in heart:
        print(line)

# Affichage du menu avec un cœur
def show_menu():
    print_heart()  # Affiche le cœur en étoiles
    print("Valentine's Day Menu:\n")
    if len(menu_data["valentine_items"]) > 0:
        for item in menu_data["valentine_items"]:
            print(f"{item['name']} - {item['price']}")
    else:
        print("No items in the menu yet.")
    print_heart()  # Affiche à nouveau le cœur en étoiles

# Fonction principale du programme
def main():
    load_menu_from_file()  # Charger les articles du menu à partir du fichier

    print("Welcome to the Valentine’s Day Menu Manager!")
    
    while True:
        print("\nEnter a new Valentine item (or type 'exit' to quit):")
        name = input("Item name: ")
        if name.lower() == 'exit':
            break
        
        price = input("Item price (XX,14): ")
        
        add_item_to_menu(name, price)
        
        print("\nCurrent Menu:")
        show_menu()

# Lancer le programme principal
if __name__ == "__main__":
    main()


