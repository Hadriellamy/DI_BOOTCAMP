#Exercise 3: String Module
"""
Instructions

Generate random String of length 5
Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
Hint: use the string module

"""

import random
import string

# Génère une chaîne de 5 lettres aléatoires (majuscules + minuscules)
random_string = ''.join(random.choices(string.ascii_letters, k=5))

print(random_string)
