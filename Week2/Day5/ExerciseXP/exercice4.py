#Exercise 4 : Afternoon At The Zoo
"""
Instructions

Create a class called Zoo.
In this class create a method __init__ that takes one parameter: zoo_name.
It instantiates two attributes: animals (an empty list) and name (name of the zoo).
Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
Create a method called get_animals that prints all the animals of the zoo.
Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
Example

{ 
    A: "Ape",
    B: ["Baboon", "Bear"],
    C: ['Cat', 'Cougar'],
    E: ['Eel', 'Emu']
}


Create a method called get_groups that prints the animal/animals inside each group.

Create an object called new_york_zoo and call all the methods.
Tip: The zookeeper is the one who will use this class.
Example
Which animal should we add to the zoo --> Giraffe
x.add_animal(Giraffe)

"""


class Zoo:
    def __init__(self,name):
        self.name = name
        self.animals = []

    def add_animal(self, new_animal):
      if new_animal not in self.animals:
        self.animals.append(new_animal)


    def get_animals(self):
      print("The animals in the zoo are :")
      for animal in self.animals:
       print(animal)



    def sell_animal(self,animal_sold):
       if animal_sold in self.animals :
        self.animals.remove(animal_sold)


    def sort_animals(self):
        # Trie la liste d'animaux par ordre alphabétique
        self.animals.sort()
        # Crée un dictionnaire pour grouper les animaux par première lettre
        groups = {}
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in groups:
                groups[first_letter] = []
            groups[first_letter].append(animal)
        return groups

    def get_groups(self):
        # Affiche les groupes d'animaux créés par sort_animals
        groups = self.sort_animals()
        print("Groupes d'animaux:")
        for letter, animals in groups.items():
            print(f"{letter}: {animals}")


# Création d'un objet Zoo appelé new_york_zoo
new_york_zoo = Zoo("New York Zoo")

# Exemple d'ajout d'animaux
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")

# Affichage des animaux dans le zoo
new_york_zoo.get_animals()

# Vente d'un animal (suppression)
new_york_zoo.sell_animal("Bear")
print("\nAprès avoir vendu 'Bear' :")
new_york_zoo.get_animals()

# Affichage des groupes d'animaux par première lettre
print("\nAffichage des groupes d'animaux :")
new_york_zoo.get_groups()


