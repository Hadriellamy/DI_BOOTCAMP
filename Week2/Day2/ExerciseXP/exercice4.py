#Exercise 4 : Random
"""
Instructions

Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

"""

import random

def compare_random(num):
   random_number = random.randint(1,101)
  
   if num == random_number:
      print("Success")
   else:
      print("Error")


compare_random(34)






