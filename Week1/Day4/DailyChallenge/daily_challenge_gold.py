#Instructions
"""
Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
Display a little cake as seen below:
       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~

The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

Bonus : If they were born on a leap year, display two cakes !

"""

from datetime import datetime

# Demander la date de naissance à l'utilisateur, au format DD/MM/YYYY
birthdate_str = input("Entrez votre date de naissance (DD/MM/YYYY) : ")
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")

# Calculer l'âge de l'utilisateur en années
today = datetime.today()
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

# Le nombre de bougies = le dernier chiffre de l'âge
# Par exemple, pour 53 ans, 53 % 10 donne 3 bougies.
nb_candles = age % 10

# Vérifier si l'année de naissance est bissextile
year = birthdate.year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap = True
else:
    leap = False

# Construire la représentation du gâteau :
# On insère un nombre de "i" égal à nb_candles dans la première ligne.
candles = "i" * nb_candles
cake_lines = [
    "       ___" + candles + "___",
    "      |:H:a:p:p:y:|",
    "    __|___________|__",
    "   |^^^^^^^^^^^^^^^^^|",
    "   |:B:i:r:t:h:d:a:y:|",
    "   |                 |",
    "   ~~~~~~~~~~~~~~~~~~~"
]

# Afficher le gâteau.
# Si l'utilisateur est né une année bissextile, afficher deux gâteaux.
if leap:
    print("\n".join(cake_lines))
    print()  # Ligne vide pour séparer les deux gâteaux
    print("\n".join(cake_lines))
else:
    print("\n".join(cake_lines))
