#Exercise 2 : Dogs
"""
Instructions

Create a class called Dog with the following attributes name, age, weight.
Implement the following methods in the Dog class:
bark: returns a string which states: “<dog_name> is barking”.
run_speed: returns the dogs running speed (weight/age*10).
fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

Create 3 dogs and run them through your class.

"""

class Dog:
    def __init__(self, name, age, weight):
        self.name = name 
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"
    

    def run_speed(self):
        return (self.weight/self.age)*10



    def fight(self, other_dog):
        self_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if self_power > other_power:
            return f"{self.name} wins the fight against {other_dog.name}"
        elif self_power < other_power:
            return f"{other_dog.name} wins the fight against {self.name}"
        else:
            return f"It's a tie between {self.name} and {other_dog.name}!"

# Création de 3 chiens
dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Bella", 3, 15)
dog3 = Dog("Max", 4, 25)

# Tester les méthodes
print(dog1.bark())
print(f"{dog1.name}'s run speed: {dog1.run_speed()}")

print(dog2.bark())
print(f"{dog2.name}'s run speed: {dog2.run_speed()}")

print(dog3.bark())
print(f"{dog3.name}'s run speed: {dog3.run_speed()}")

# Combats entre les chiens
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))    

