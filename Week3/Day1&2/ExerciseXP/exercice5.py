#Exercise 5 : TheIncredibles Family
"""
Instructions

Create a class called TheIncredibles. This class should inherit from the Family class:
This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)


Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.


Add a method called incredible_presentation which :

Print a sentence like “*Here is our powerful family **”
Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)


Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.

    [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ]


Call the incredible_presentation method.


Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.


Call the incredible_presentation method again.

"""

from exercice4 import Family  

class UnderageMemberError(Exception):
    def __init__(self, name):
        super().__init__(f"{name} is not over 18 years old and cannot use their power.")

class TheIncredibles(Family):
    def __init__(self, last_name, members=None):
        super().__init__(last_name, members)

    def use_power(self, name):
        for member in self.members:
            if member.get('name') == name:
                if member.get('age', 0) >= 18:
                    print(f"{name}'s power is: {member.get('power')}")
                else:
                    raise UnderageMemberError(name)
                return
        print(f"No member named {name} found in the family.")

    def incredible_presentation(self):
        print("\n✨ Here is our powerful family ✨")
        super().family_presentation()


# --- Test the class ---
if __name__ == "__main__":
    incredible_members = [
        {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
        {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
    ]

    incredible_family = TheIncredibles("Incredibles", incredible_members)

    # First presentation
    incredible_family.incredible_presentation()

    # Use powers
    try:
        incredible_family.use_power("Michael")
        incredible_family.use_power("Sarah")
    except UnderageMemberError as e:
        print(e)

    # Add Baby Jack
    incredible_family.born(
        name="Baby Jack",
        age=2,
        gender="Male",
        is_child=True,
        power="Unknown Power",
        incredible_name="JackJack"
    )

    # Second presentation
    incredible_family.incredible_presentation()

    # Try to use Baby Jack's power
    try:
        incredible_family.use_power("Baby Jack")
    except UnderageMemberError as e:
        print(e)
