#Exercise 2 : Dungeons & Dragons
"""
Instructions

For a game of Dungeons & Dragons, each player starts by generating a character they can play with. This character has, among other things, six attributes/stats:
Strength
Dexterity
Constitution
Intelligence
Wisdom
Charisma

These six abilities have scores that are determined randomly. You do this by rolling four 6-sided dice and record the sum of the largest three dice. You do this six times, once for each ability.
For example, the six throws of four dice may look like:
5, 3, 1, 6: You discard the 1 and sum 5 + 3 + 6 = 14, which you assign to strength.
3, 2, 5, 3: You discard the 2 and sum 3 + 5 + 3 = 11, which you assign to dexterity.
1, 1, 1, 1: You discard the 1 and sum 1 + 1 + 1 = 3, which you assign to constitution.
2, 1, 6, 6: You discard the 1 and sum 2 + 6 + 6 = 14, which you assign to intelligence.
3, 5, 3, 4: You discard the 3 and sum 5 + 3 + 4 = 12, which you assign to wisdom.
6, 6, 6, 6: You discard the 6 and sum 6 + 6 + 6 = 18, which you assign to charisma.

Create a class called Character and a class called Game for this exercise.

The point of this exercise is to generate characters for players looking to start a game quickly.
Start by asking the user how many players are playing.
Each user then creates his/her character, let them establish what the characters name and age are.
Output the characters created into the following formats:
txt: a nicely formatted text file for the players to use
json: a json file of all the characters and attributes


Hint: the Character class should be in charge of creating characters, the Game class should be in charge of how many times the Character gets instantiated and of exporting the data in json or txt
###############################################################################################################################################################################################################

L'objectif de cet exercice est de créer un générateur de personnages pour un jeu de Dungeons & Dragons, en générant six attributs pour chaque personnage et en enregistrant les informations sous forme de fichiers texte et JSON.

Étapes à suivre :
Créer la classe Character :
Cette classe doit être responsable de la génération des six attributs : Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma.
Chaque attribut est généré en lançant quatre dés à six faces et en gardant la somme des trois plus grands résultats.
Demander un nom et un âge pour chaque personnage.
Créer la classe Game :
Cette classe gère plusieurs joueurs (personnages).
Elle pose des questions à l'utilisateur pour déterminer combien de joueurs vont participer.
Pour chaque joueur, elle génère un personnage, et ensuite, elle exporte les données dans un fichier texte et un fichier JSON.

Détails :
Lancer les dés pour chaque caractéristique : Utiliser la fonction random.randint() pour générer un nombre aléatoire entre 1 et 6 pour chaque dé, puis garder les trois plus grands résultats.
Génération du fichier txt : Le fichier doit être lisible et bien formaté, avec les noms des personnages, leurs âges et leurs six attributs.
Génération du fichier json : Le fichier JSON doit contenir une structure où chaque personnage est représenté par un dictionnaire avec son nom, son âge, et ses attributs.

"""


import random
import json

# Classe Character : gère la création d'un personnage
class Character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.attributes = self.generate_attributes()

    def generate_attributes(self):
        attributes = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
        generated_attributes = {}
        
        for attribute in attributes:
            dice_rolls = [random.randint(1, 6) for _ in range(4)]
            dice_rolls.sort(reverse=True)
            generated_attributes[attribute] = sum(dice_rolls[:3])  # Garder les 3 plus grands résultats
            
        return generated_attributes

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "attributes": self.attributes
        }

    def to_txt(self):
        result = f"Name: {self.name}\nAge: {self.age}\n"
        result += "\nAttributes:\n"
        for attribute, score in self.attributes.items():
            result += f"{attribute}: {score}\n"
        return result

# Classe Game : gère la création de plusieurs personnages et l'export des données
class Game:
    def __init__(self):
        self.players = []

    def create_characters(self, num_players):
        for _ in range(num_players):
            name = input("Enter the character's name: ")
            age = int(input(f"Enter {name}'s age: "))
            player = Character(name, age)
            self.players.append(player)

    def save_to_txt(self):
        with open("characters.txt", "w") as f:
            for player in self.players:
                f.write(player.to_txt())
                f.write("\n" + "="*20 + "\n")

    def save_to_json(self):
        with open("characters.json", "w") as f:
            json_data = [player.to_dict() for player in self.players]
            json.dump(json_data, f, indent=4)

# Fonction principale : gère le processus du jeu
def main():
    game = Game()
    
    num_players = int(input("How many players are playing? "))
    game.create_characters(num_players)
    
    # Sauvegarde des données dans les fichiers
    game.save_to_txt()
    game.save_to_json()
    
    print("Character data has been saved in 'characters.txt' and 'characters.json'.")

if __name__ == "__main__":
    main()
