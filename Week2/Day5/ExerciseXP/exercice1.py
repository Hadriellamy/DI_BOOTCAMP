#Exercise 1: Cats
"""
Instructions

Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
Instantiate three Cat objects using the code provided above.
Outside of the class, create a function that finds the oldest cat and returns the cat.
Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

"""
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

cat1 = Cat("Houmous", 3)
cat2 = Cat("Pilou", 5)
cat3 = Cat("Tomy", 4)

cats = [cat1, cat2, cat3]

def find_oldest_cat(cats):
    oldest = max(cats, key=lambda cat: cat.age)
    return oldest


oldest_cat = find_oldest_cat(cats)

print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

