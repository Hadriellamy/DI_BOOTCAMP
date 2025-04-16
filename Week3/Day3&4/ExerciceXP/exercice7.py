#Exercise 7 : Faker Module
"""
Instructions

Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
Create an empty list called users. Tip: It should be a list of dictionaries.
Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

"""

from faker import Faker

# Initialiser Faker
fake = Faker()

# Liste des utilisateurs
users = []

def add_user():
    # Générer un utilisateur avec des données fictives
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    # Ajouter l'utilisateur à la liste
    users.append(user)

# Ajouter quelques utilisateurs
for _ in range(5):  # Ajouter 5 utilisateurs
    add_user()

# Afficher la liste des utilisateurs
for user in users:
    print(user)
