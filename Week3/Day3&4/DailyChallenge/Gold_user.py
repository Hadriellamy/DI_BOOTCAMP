#Instruction: Information From The User
"""
Harder Daily Challenge
Notice : solve this exercise using a lambda function.

Ask a user for the following inputs 5 times:
Name (string)
Age (int)
Score (int)
Build a list of tuples using these inputs, each tuple should contain a name, age and score.
Sort the list by the following priority Name > Age > Score.
If the following tuples are given as input to the script:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
Note : The lambda function will not print but sort

################################################################################################################################

Explication de l'énoncé :
L'objectif de cet exercice est de demander à l'utilisateur des informations (nom, âge, et score) cinq fois. Ces informations doivent être stockées sous forme de tuples dans une liste. Ensuite, vous devez trier cette liste en fonction de trois critères : le nom (alphabetiquement), puis l'âge (numériquement), et enfin le score (numériquement).

Voici les étapes principales :

Demander à l'utilisateur d'entrer trois informations cinq fois : un nom (chaîne de caractères), un âge (entier), et un score (entier).
Créer des tuples pour chaque entrée et ajouter chaque tuple à une liste.
Trier cette liste en utilisant un critère qui respecte la priorité suivante :
Premier tri : par le nom, dans l'ordre alphabétique.
Deuxième tri : en cas d'égalité sur le nom, trier par âge.
Troisième tri : en cas d'égalité sur le nom et l'âge, trier par score.
Utiliser une fonction lambda pour effectuer ce tri.


"""

# Liste pour stocker les tuples
user_data = []

# Demander les entrées 5 fois
for _ in range(5):
    # Demander les informations
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    score = int(input("Enter score: "))
    
    # Ajouter le tuple dans la liste
    user_data.append((name, str(age), str(score)))  # Convertir age et score en string pour respecter l'exemple donné

# Trier la liste avec une lambda function
user_data.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))  # On trie par nom, puis par age, puis par score

# Afficher la liste triée
print(user_data)