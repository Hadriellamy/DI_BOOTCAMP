#Exercise 1 : Temperature
"""
Instructions

Write a base class called Temperature.
Implement the following subclasses: Celsius, Kelvin, Fahrenheit.
Each of the subclasses should have a method which can convert the temperture to another type.
You must consider different designs and pick the best one according to the SOLID Principle.

"""
"""
🎯 Objectif :
Créer une classe de base Temperature, et implémenter les sous-classes suivantes :

Celsius
Kelvin
Fahrenheit
Chaque sous-classe doit avoir des méthodes pour convertir la température dans les autres unités.

💡 Application des principes SOLID :

S - Single Responsibility Principle (Responsabilité unique)
Chaque classe a un rôle bien défini :
Temperature : interface générale.
Celsius, Kelvin, Fahrenheit : gèrent uniquement leur logique de conversion.
O - Open/Closed Principle (Ouvert/fermé)
Le code est ouvert à l'extension (on peut ajouter d'autres unités), mais fermé à la modification (pas besoin de toucher les classes existantes).
L - Liskov Substitution Principle
Les sous-classes peuvent remplacer la classe de base sans casser le code. On peut traiter toutes les températures comme des Temperature.
I - Interface Segregation Principle
On ne force pas les classes à implémenter des méthodes inutiles. Ici, toutes ont besoin des mêmes méthodes de conversion.
D - Dependency Inversion Principle
Le code principal n’est pas dépendant des classes concrètes. On travaille avec l’abstraction Temperature.

"""

from abc import ABC, abstractmethod

# Classe abstraite de base
class Temperature(ABC):
    @abstractmethod
    def to_celsius(self):
        pass

    @abstractmethod
    def to_kelvin(self):
        pass

    @abstractmethod
    def to_fahrenheit(self):
        pass

# Celsius
class Celsius(Temperature):
    def __init__(self, valeur):
        self.valeur = valeur

    def to_celsius(self):
        return self.valeur

    def to_kelvin(self):
        return self.valeur + 273.15

    def to_fahrenheit(self):
        return (self.valeur * 9/5) + 32

# Kelvin
class Kelvin(Temperature):
    def __init__(self, valeur):
        self.valeur = valeur

    def to_celsius(self):
        return self.valeur - 273.15

    def to_kelvin(self):
        return self.valeur

    def to_fahrenheit(self):
        return (self.valeur - 273.15) * 9/5 + 32

# Fahrenheit
class Fahrenheit(Temperature):
    def __init__(self, valeur):
        self.valeur = valeur

    def to_celsius(self):
        return (self.valeur - 32) * 5/9

    def to_kelvin(self):
        return (self.valeur - 32) * 5/9 + 273.15

    def to_fahrenheit(self):
        return self.valeur


#Test

t_celsius = Celsius(25)
print(f"25°C en Kelvin : {t_celsius.to_kelvin()} K")
print(f"25°C en Fahrenheit : {t_celsius.to_fahrenheit()} °F")

t_kelvin = Kelvin(300)
print(f"300 K en Celsius : {t_kelvin.to_celsius()} °C")
print(f"300 K en Fahrenheit : {t_kelvin.to_fahrenheit()} °F")

t_fahrenheit = Fahrenheit(77)
print(f"77°F en Celsius : {t_fahrenheit.to_celsius()} °C")
print(f"77°F en Kelvin : {t_fahrenheit.to_kelvin()} K")
