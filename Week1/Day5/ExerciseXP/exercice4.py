#Exercise 4 : Disney Characters
"""
Instructions

Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
Analyse these results :

#1/

>>> print(disney_users_A)
{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/

>>> print(disney_users_B)
{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

#3/ 

>>> print(disney_users_C)
{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
Only recreate the 1st result for:
The characters, which names contain the letter “i”.
The characters, which names start with the letter “m” or “p”.

"""

# Liste initiale
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

# 1/ Créer disney_users_A : clés = noms, valeurs = indices (sans hardcoder les nombres)
disney_users_A = {}
for index, user in enumerate(users):
    disney_users_A[user] = index

print("disney_users_A:")
print(disney_users_A)
# Résultat attendu :
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# 2/ Créer disney_users_B : clés = indices, valeurs = noms
disney_users_B = {}
for index, user in enumerate(users):
    disney_users_B[index] = user

print("\ndisney_users_B:")
print(disney_users_B)
# Résultat attendu :
# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# 3/ Créer disney_users_C : même que A mais trié alphabétiquement par le nom.
# On peut faire cela facilement avec sorted() et une compréhension de dictionnaire.
sorted_users = sorted(users)
disney_users_C = {user: index for index, user in enumerate(sorted_users)}

print("\ndisney_users_C:")
print(disney_users_C)
# Résultat attendu (l'ordre des clés peut varier en fonction de l'affichage, mais les indices doivent être attribués à l'ordre alphabétique) :
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# ===========================================================
# Filtrage du 1er résultat (disney_users_A) selon deux critères :
# ===========================================================

# a) Seulement les personnages dont le nom contient la lettre "i"
disney_users_A_with_i = {}
for user, index in disney_users_A.items():
    if "i" in user.lower():  # recherche en minuscule pour ne pas rater "Mickey" ou "Minnie"
        disney_users_A_with_i[user] = index

print("\ndisney_users_A (noms contenant 'i'):")
print(disney_users_A_with_i)
# Résultat attendu :
# Par exemple, {"Mickey": 0, "Minnie": 1, "Ariel": 3}
# (Donald et Pluto n'ont pas de "i")

# b) Seulement les personnages dont le nom commence par "m" ou "p"
disney_users_A_mp = {}
for user, index in disney_users_A.items():
    if user.lower().startswith("m") or user.lower().startswith("p"):
        disney_users_A_mp[user] = index

print("\ndisney_users_A (noms commençant par 'm' ou 'p'):")
print(disney_users_A_mp)
# Résultat attendu :
# {"Mickey": 0, "Minnie": 1, "Pluto": 4}

