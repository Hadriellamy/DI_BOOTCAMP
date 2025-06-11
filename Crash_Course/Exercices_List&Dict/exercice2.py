#Exercice 2 Dictionary

"""
1. Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).

2. Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"], return a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.

3. Create a dictionary where the keys are vowels in the alphabet and the values are 0. Your dictionary should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).

4. Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter itself. You should return something like this:

{1: 'A',
 2: 'B',
 3: 'C',
 4: 'D',
 5: 'E',
 6: 'F',
 7: 'G',
 8: 'H',
 9: 'I',
 10: 'J',
 11: 'K',
 12: 'L',
 13: 'M',
 14: 'N',
 15: 'O',
 16: 'P',
 17: 'Q',
 18: 'R',
 19: 'S',
 20: 'T',
 21: 'U',
 22: 'V',
 23: 'W',
 24: 'X',
 25: 'Y',
"""


#1
lst = [("name", "Elie"), ("job", "Instructor")]
d = dict(lst)
print(d)

#2
abbreviations = ["CA", "NJ", "RI"]
states = ["California", "New Jersey", "Rhode Island"]

d = dict(zip(abbreviations, states))
print(d)

#3
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_dict = {vowel: 0 for vowel in vowels}
print(vowel_dict)  

#4
alphabet_dict = {i + 1: chr(65 + i) for i in range(26)}

for key, value in alphabet_dict.items():
    print(f"{key}: {value}")





