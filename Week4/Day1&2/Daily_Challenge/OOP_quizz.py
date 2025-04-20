#Instructions
"""
Part 1 : Quizz :

Answer the following questions

What is a class?
What is an instance?
What is encapsulation?
What is abstraction?
What is inheritance?
What is multiple inheritance?
What is polymorphism?
What is method resolution order or MRO?


Part 2: Create A Deck Of Cards Class.

The Deck of cards class should NOT inherit from a Card class.

The requirements are as follows:

The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
The Deck class :
should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

"""

#Part 1 

"""

Part 1: Answers to the Quiz Questions

- What is a class? 
A class is a blueprint or template for creating objects in object-oriented programming (OOP). It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.

- What is an instance? 
An instance is a specific object created from a class. It represents a single entity with its own set of attributes, as defined by the class. For example, if Dog is a class, then a specific dog like "Rex" is an instance of that class.

- What is encapsulation? 
Encapsulation is the concept of bundling the data (attributes) and methods (functions) that operate on the data into a single unit or class. It also refers to restricting direct access to some of an object's attributes and methods, to protect the integrity of the object. This is typically done using access modifiers (like private, public, or protected).

- What is abstraction?
Abstraction is the concept of hiding the complexity of an implementation and exposing only the essential features or functionalities to the user. It allows a programmer to focus on what an object does, rather than how it does it. In Python, abstraction is often implemented using abstract base classes (ABC) or interfaces.

- What is inheritance? 
Inheritance is a mechanism in object-oriented programming where a new class (child class or subclass) inherits the attributes and methods of an existing class (parent class or superclass). This allows for code reuse and can be used to implement a hierarchy of classes.

- What is multiple inheritance? 
Multiple inheritance occurs when a class can inherit from more than one class. This allows the child class to inherit features (attributes and methods) from multiple parent classes. Python supports multiple inheritance, but care should be taken to avoid conflicts between inherited methods (this can be managed using method resolution order).

- What is polymorphism?
Polymorphism is the ability of an object to take many forms. It allows one method or function to work with different types of objects. In Python, this is often implemented using method overriding or method overloading, where methods in a subclass have the same name but can behave differently depending on the type of object.

- What is method resolution order or MRO? 
The Method Resolution Order (MRO) is the order in which Python searches for a method in the class hierarchy when multiple classes are involved. It is particularly relevant in multiple inheritance. Python uses the C3 linearization algorithm to determine the MRO, which ensures a consistent and predictable order in which methods are resolved.


"""


#Part 2 Create A Deck Of Cards Class

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


#The Card class has two attributes: suit (Hearts, Diamonds, Clubs, Spades) and value (A, 2, 3, ..., K). The __repr__ method is defined for a user-friendly string representation of a card.

import random

class Deck:
    def __init__(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        """Shuffle the deck randomly"""
        random.shuffle(self.cards)

    def deal(self):
        """Deal one card from the deck"""
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return "No more cards to deal."


#Test 

# Create a deck of cards
deck = Deck()

# Shuffle the deck
deck.shuffle()

# Deal one card
card = deck.deal()
print(card)

# Check remaining cards
print(f"Remaining cards in deck: {len(deck.cards)}")
