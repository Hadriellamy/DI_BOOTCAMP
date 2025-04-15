#Exercise 4 : Family
"""
Instructions

Create a class called Family and implement the following attributes:

members: list of dictionaries
last_name : (string)

Implement the following methods:

born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
family_presentation: a method that prints the family’s last name and all the members’ details.

Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

    [
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ]

"""

class Family:
    def __init__(self, last_name, members=None):
        self.last_name = last_name
        self.members = members if members else []

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of {kwargs.get('name')}!")

    def is_18(self, name):
        for member in self.members:
            if member.get("name") == name:
                return member.get("age", 0) >= 18
        print(f"No member named {name} found in the family.")
        return False

    def family_presentation(self):
        print(f"Family Last Name: {self.last_name}")
        print("Family Members:")
        for member in self.members:
            print(f"  - {member}")

# Testing the class
if __name__ == "__main__":
    members_data = [
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
    ]

    my_family = Family("Johnson", members_data)

    my_family.family_presentation()
    print("Is Michael over 18?", my_family.is_18("Michael"))
    print("Is Sarah over 18?", my_family.is_18("Sarah"))

    # Add a new child
    my_family.born(name="Emily", age=0, gender="Female", is_child=True)

    my_family.family_presentation()
