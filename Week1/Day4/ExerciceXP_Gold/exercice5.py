#Exercise 5: The Alphabet
"""
Instructions

Create a string of all the letters in the alphabet
Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"

for char in alphabet:
    if char in vowels:
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")

