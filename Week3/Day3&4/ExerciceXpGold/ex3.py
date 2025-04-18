#Exercise 3 : Regular Expression #1
"""
Instructions

Hint: Use the RegEx (module)

Use the regular expression module to extract numbers from a string.

Example

return_numbers('k5k3q2g5z6x9bn') 
// Excepted output : 532569

######
🎯 Objectif

Créer une fonction return_numbers qui extrait tous les chiffres d’une chaîne de caractères, en les regroupant dans une seule chaîne.

🧠 Astuce

On utilise le module re (RegEx = expressions régulières) avec le motif \d pour trouver tous les chiffres.
######


"""

import re

def return_numbers(s):
    # Trouve tous les chiffres dans la chaîne
    digits = re.findall(r'\d', s)
    # Les concatène pour former une seule chaîne de chiffres
    return ''.join(digits)

#Test
print(return_numbers('k5k3q2g5z6x9bn'))  

