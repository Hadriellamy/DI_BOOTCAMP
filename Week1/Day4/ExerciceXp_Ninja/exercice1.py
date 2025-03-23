#Exercise 1: Formula
"""
Instructions

Write a program that calculates and prints a value according to this given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50.
H is 30.
Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
For example, if the user inputs: 100,150,180
The output should be:

18,22,24

"""

import math

C = 50
H = 30
D = int(input("Enter a number for calcul : "))
Q = math.sqrt((2 * C * D)/H)
print(Q)


#Another method 

import math

C = 50
H = 30

# Demande des nombres séparés par des virgules
input_str = input("Entre des nombres séparés par des virgules : ")  # ex : "100,150,180"
D_values = input_str.split(",")  # découpe la chaîne en une liste

results = []

for d in D_values:
    D = float(d)  # convertit chaque valeur en nombre
    Q = math.sqrt((2 * C * D) / H)
    results.append(str(round(Q)))

print(",".join(results))  # affiche les résultats séparés par des virgules


