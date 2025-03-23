 #Exercise 2 : Cinemax #2
"""
Instructions

A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Given the following object:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

How much does each family member have to pay ?

Print out the family’s total cost for the movies.
Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

"""

# Dictionnaire de la famille fourni
family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}

total_cost = 0

for person, age in family.items():
    # Calculer le tarif selon l'âge
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15

    print(f"{person.title()} (âge {age}) doit payer : ${cost}")
    total_cost += cost

print(f"\nLe coût total pour la famille est : ${total_cost}")

