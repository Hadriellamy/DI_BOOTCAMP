#Exercise 9: Cinemax
"""
Instructions

A movie theater charges different ticket prices depending on a person’s age.
if a person is under the age of 3, the ticket is free.
if they are between 3 and 12, the ticket is $10.
if they are over the age of 12, the ticket is $15.

Ask a family the age of each person who wants a ticket.

Store the total cost of all the family’s tickets and print it out.

A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
At the end, print the final list.

"""

#2

family_size = int(input("How many people are in your family? "))

total_price = 0

for i in range(family_size):
    age = int(input(f"What's the age of person #{i+1}? "))

    if age < 3:
        total_price += 0
        print("The ticket is free for this person.")
    elif age >= 3 and age <= 12:
        total_price += 10
        print("The ticket costs 10 dollars for this person.")
    else:
        total_price += 15
        print("The ticket costs 15 dollars for this person.")

#3
print("The total cost for the family's tickets is:", total_price, "dollars.")



#4
teenagers = ["Hadriel", "Jeremy", "Mosko", "Aaron", "Yossef", "Raphael"]

for name in teenagers[:]:  
    age = int(input(f"What is your age {name}? : "))

    if 16 <= age <= 21:
        print(f"Ok {name}, you can watch the movie")
    else:
        print(f"Sorry {name}, you can't watch the movie")
        teenagers.remove(name)  

print("List of people allowed to watch the movie:", teenagers)














