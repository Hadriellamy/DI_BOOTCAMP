#Exercice 1 - ex1.py

import json

class MenuManager:
    def __init__(self):
        # Charge le menu depuis le fichier JSON
        try:
            with open("restaurant_menu.json", "r") as file:
                self.menu = json.load(file)["items"]
        except FileNotFoundError:
            self.menu = []

    def add_item(self, name, price):
        # Ajoute un élément au menu
        new_item = {"name": name, "price": price}
        self.menu.append(new_item)

    def remove_item(self, name):
        # Supprime un élément du menu par son nom
        for item in self.menu:
            if item["name"].lower() == name.lower():
                self.menu.remove(item)
                return True
        return False

    def save_to_file(self):
        # Sauvegarde le menu dans le fichier JSON
        with open("restaurant_menu.json", "w") as file:
            json.dump({"items": self.menu}, file, indent=4)
