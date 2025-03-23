#Exercise 2 : List Of Integers
"""
Instructions

Given a list of 10 integers to analyze. For example:

    [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
    [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
    [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
    [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
Store the list of numbers in a variable.
Print the following information:
a. The list of numbers – printed in a single line
b. The list of numbers – sorted in descending order (largest to smallest)
c. The sum of all the numbers
A list containing the first and the last numbers.
A list of all the numbers greater than 50.
A list of all the numbers smaller than 10.
A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
The numbers without any duplicates – also print how many numbers are in the new list.
The average of all the numbers.
The largest number.
10.The smallest number.
11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
12.Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
13.Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
14.Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
15.Bonus: Will the code work when the number of random numbers is not equal to 10?

"""

import random
import math

# ==============================================================
# Partie de base avec une liste pré-définie de 10 entiers
# ==============================================================

# Exemple de liste (vous pouvez choisir l'un des exemples donnés)
numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

# a. Afficher la liste de nombres sur une seule ligne
print("a. Original list:")
print(numbers)

# b. Afficher la liste triée en ordre décroissant (du plus grand au plus petit)
sorted_desc = sorted(numbers, reverse=True)
print("\nb. Sorted in descending order:")
print(sorted_desc)

# c. Afficher la somme de tous les nombres
total_sum = sum(numbers)
print("\nc. Sum of all numbers:")
print(total_sum)

# d. Une liste contenant le premier et le dernier nombre
first_and_last = [numbers[0], numbers[-1]]
print("\nd. First and last numbers:")
print(first_and_last)

# e. Une liste de tous les nombres supérieurs à 50
greater_than_50 = [x for x in numbers if x > 50]
print("\ne. Numbers greater than 50:")
print(greater_than_50)

# f. Une liste de tous les nombres inférieurs à 10
smaller_than_10 = [x for x in numbers if x < 10]
print("\nf. Numbers smaller than 10:")
print(smaller_than_10)

# g. Une liste de tous les nombres élevés au carré
squared_numbers = [x ** 2 for x in numbers]
# Affichage sous forme d'une chaîne avec espaces (ex: "9 2209 9801 ...")
print("\ng. Numbers squared:")
print(" ".join(str(num) for num in squared_numbers))

# h. Les nombres sans doublons, et le nombre d'éléments uniques
unique_numbers = list(set(numbers))
print("\nh. Unique numbers:")
print(unique_numbers)
print("Count of unique numbers:", len(unique_numbers))

# i. La moyenne de tous les nombres
average = total_sum / len(numbers)
print("\ni. Average of numbers:")
print(average)

# j. Le plus grand nombre
largest = max(numbers)
print("\nj. Largest number:")
print(largest)

# k. Le plus petit nombre
smallest = min(numbers)
print("\nk. Smallest number:")
print(smallest)

# ==============================================================
# Bonus 1: Calcul manuel (sans utiliser les fonctions intégrées)
# ==============================================================

manual_sum = 0
manual_count = 0
manual_max = numbers[0]
manual_min = numbers[0]

for num in numbers:
    manual_sum += num
    manual_count += 1
    if num > manual_max:
        manual_max = num
    if num < manual_min:
        manual_min = num

manual_average = manual_sum / manual_count

print("\nBonus 1: Manual calculations (without built-in functions):")
print("Manual sum:", manual_sum)
print("Manual average:", manual_average)
print("Manual largest:", manual_max)
print("Manual smallest:", manual_min)

# ==============================================================
# Bonus 2: Demander à l'utilisateur 10 nombres entre -100 et 100
# ==============================================================

user_numbers = []
print("\nBonus 2: Enter 10 numbers between -100 and 100:")
for i in range(10):
    while True:
        try:
            n = int(input(f"Enter number {i+1}: "))
            if -100 <= n <= 100:
                user_numbers.append(n)
                break
            else:
                print("Number not in range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
print("User provided numbers:")
print(user_numbers)

# ==============================================================
# Bonus 3: Générer 10 entiers aléatoires entre -100 et 100
# ==============================================================

random_numbers_10 = [random.randint(-100, 100) for _ in range(10)]
print("\nBonus 3: 10 random numbers between -100 and 100:")
print(random_numbers_10)

# ==============================================================
# Bonus 4: Générer un nombre aléatoire d'entiers (au moins 50)
# ==============================================================

# Génère un entier aléatoire entre 50 et 100 pour le nombre d'éléments
n_numbers = random.randint(50, 100)
random_numbers_dynamic = [random.randint(-100, 100) for _ in range(n_numbers)]
print(f"\nBonus 4: {n_numbers} random numbers between -100 and 100:")
print(random_numbers_dynamic)

# ==============================================================
# Bonus 5: Comportement lorsque le nombre de nombres aléatoires n'est pas égal à 10
# ==============================================================

print("\nBonus 5:")
print("The code works regardless of the number of random numbers generated.")

