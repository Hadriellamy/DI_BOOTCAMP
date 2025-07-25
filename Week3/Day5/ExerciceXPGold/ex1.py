
#Exercise 1 : Restaurant Menu Manager
"""
Instructions

Description: Create a restaurant menu management system for a manager. The program should allow the manager to view the menu, add an item and delete an item.

The menu should be saved to a local file – the program should load the file when it begins and add the updated details to the file before exiting.

The program should be written in two files – one which will deal with the UI (user interface), eg. showing the user menu and getting user input, etc.
The second file will handle all other functionality such as adding/removing items from the menu, along with loading and saving the data to a JSON file.
Separating the files is important – the file which deals with the UI functionality should not have any details about the menu file itself (encapsulation).

The following code is the basic menu for a restaurant. You can make any changes you want.

{
    "items": [
        {
            "name": "Vegetable soup",
            "price": 30
        },
        {
            "name": "Hamburger",
            "price": 44.9
        },
        {
            "name": "Milkshake",
            "price": 22.5
        },
        {
            "name": "Artichoke",
            "price": 18
        },
        {
            "name": "Beef stew",
            "price": 52.5
        }
    ]
}


Create a JSON file called restaurant_menu.json. Paste the menu provided above in the restaurant_menu.json file.

Create a file called menu_manager.py. The file should contain a class called MenuManager, with the following functions:

__init__() - The function should read the menu from the restaurant_menu.json file and store it in a variable called menu.

add_item(name, price) – this method should add an item to the menu, although do not save the changes to the file yet.

remove_item(name) – if the item is in the menu, this function should remove it from the menu (and again do not save the changes to the file yet) and return True. If the item was not in the menu, return False. (Hint: use Python’s del operator).

save_to_file() - When the manager is finished updating the menu this function should be called and it should save all the updates and write them into the the restaurant_menu.json file (ie. the file which holds the menu).

Create a file called menu_editor.py , which will have the following functions:
load_manager()- this function should create a new MenuManager instance.

show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to choose an item. Call the appropriate function that matches the user’s input.

add_item_to_menu() - this will ask the user to input the item’s name and price. It will not interact with the menu itself, but simply call the appropriate function from the MenuManager object.
If the item was added successfully print a message which states: item was added successfully.

remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. The function should not interact with the menu itself, but simply call the appropriate function from the MenuManager object.
If the item was deleted successfully – print a message to let the user know this was completed.
If not – print a message which states that there was an error.

show_restaurant_menu() - print the restaurant’s menu.

When the user chooses to exit the program, first write the menu to the file and then print a message that states that the menu was saved, finally exit the program.

After exiting the program the changes should be reflected in the menu (see Part 1.1) and in the JSON file.

Here’s an example of the menu shown to the user:

##############################################################################################################################################################


L'exercice consiste à créer un système de gestion de menu pour un restaurant. Ce système permet à un responsable de consulter le menu, d'ajouter ou de supprimer des éléments du menu, et de sauvegarder les modifications dans un fichier JSON.

Voici une explication détaillée du fonctionnement de l'exercice et de sa structure :


But de l'exercice :

Créer un programme qui gère un menu de restaurant, permettant de :

Afficher le menu.
Ajouter un élément au menu.
Supprimer un élément du menu.
Sauvegarder les modifications dans un fichier JSON.
Le programme est divisé en deux fichiers :
menu_manager.py : Gère les données du menu (ajouter, supprimer, sauvegarder les éléments).
menu_editor.py : Gère l'interface utilisateur (affichage du menu et interactions avec l'utilisateur).
Détails des fichiers :
1. restaurant_menu.json

Il s'agit du fichier où le menu est enregistré en format JSON. Il doit contenir des éléments avec un nom et un prix. Par exemple :

{
    "items": [
        {"name": "Vegetable soup", "price": 30},
        {"name": "Hamburger", "price": 44.9},
        {"name": "Milkshake", "price": 22.5},
        {"name": "Artichoke", "price": 18},
        {"name": "Beef stew", "price": 52.5}
    ]
}
2. menu_manager.py

Ce fichier contient une classe MenuManager qui gère le menu. Les méthodes de cette classe permettent d'ajouter, de supprimer et de sauvegarder des éléments dans le fichier JSON. Les principales fonctions de cette classe sont :

__init__() : Charge le menu depuis le fichier JSON au démarrage et le stocke dans une variable menu.
add_item(name, price) : Ajoute un élément au menu (sans sauvegarder immédiatement dans le fichier).
remove_item(name) : Supprime un élément du menu en fonction de son nom (sans sauvegarder immédiatement dans le fichier).
save_to_file() : Sauvegarde toutes les modifications dans le fichier JSON.
3. menu_editor.py

Ce fichier gère l'interface utilisateur (UI). Les fonctions incluent :

load_manager() : Crée une instance de MenuManager.
show_user_menu() : Affiche le menu de l'utilisateur, avec les options pour ajouter ou supprimer des éléments.
add_item_to_menu() : Demande à l'utilisateur d'entrer un nom et un prix pour un nouvel élément à ajouter au menu.
remove_item_from_menu() : Demande à l'utilisateur de spécifier un élément à supprimer.
show_restaurant_menu() : Affiche le menu du restaurant (la liste des éléments avec leurs prix).
Lorsque l'utilisateur choisit de quitter le programme, le menu est sauvegardé dans le fichier JSON et un message de confirmation est affiché.

"""


#fichier menu_manager.py & menu_editor.py
