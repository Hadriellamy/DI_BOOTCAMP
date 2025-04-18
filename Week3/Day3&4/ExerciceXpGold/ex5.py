#Exercise 5: Python Password Generator
"""
Instructions

Create a Python program that will generate a good password for you.

Program flow:

Ask the user to type in the number of characters that the password should have (password length) – between 6 and 30 characters.
Validate the input. Make sure the user is inputing a number between 6 to 30. Create a loop which will continue to ask the user for an input until they enter a valid one.

Generate a password with the required length.

Print the password with a user-friendly message which reminds the user to keep the password in a safe place!

Rules for the validity of the password

Each password should contain:
At least 1 digit (0-9)
At least 1 lower-case character (a-z)
At least 1 upper-case character (A-Z)
At least 1 special character (eg. !, @, #, $, %, ^, _, …)
Once there is at least 1 of each, the rest of the password should be composed of more characters from the options presented above.

Create a test function first!

Do the following steps 100 times, with different password lengths:
Generate a password.
Test the password to ensure that:
it fulfills all the requirements above (eg. it has at least one digit, etc.)
it has the specified length.

###########################################################################################################################################################################################################################################
L'exercice "Python Password Generator" demande de créer un programme qui génère un mot de passe sécurisé selon certaines règles, et qui permet également de tester ce générateur de mot de passe avec différentes longueurs de mot de passe.

Voici les étapes détaillées de ce que tu dois faire :

1. Demander à l'utilisateur la longueur du mot de passe
Le programme doit d'abord demander à l'utilisateur combien de caractères il souhaite pour son mot de passe.
La longueur doit être comprise entre 6 et 30 caractères (inclus).
Si l'utilisateur entre une valeur en dehors de cette plage, le programme doit lui demander de réessayer, jusqu'à ce qu'une valeur valide soit saisie.
2. Générer un mot de passe valide
Le mot de passe doit respecter les conditions suivantes :

Contenir au moins un chiffre (0-9)
Contenir au moins une lettre minuscule (a-z)
Contenir au moins une lettre majuscule (A-Z)
Contenir au moins un caractère spécial (par exemple : !, @, #, $, etc.)
Une fois ces conditions respectées, le programme peut compléter le mot de passe en ajoutant des caractères aléatoires (lettres, chiffres ou symboles) jusqu'à ce que la longueur spécifiée par l'utilisateur soit atteinte.

3. Afficher le mot de passe généré
Une fois le mot de passe généré, il doit être affiché à l'utilisateur avec un message indiquant de le garder en lieu sûr, car ce mot de passe est probablement complexe et difficile à retenir.

4. Tester le générateur de mot de passe
Pour s'assurer que le générateur fonctionne correctement, tu dois créer une fonction de test qui :

Génère des mots de passe avec des longueurs différentes (entre 6 et 30).
Vérifie si chaque mot de passe généré respecte toutes les règles de validité :
Longueur correcte
Contient au moins un chiffre, une lettre minuscule, une majuscule et un caractère spécial.
Cette fonction de test doit être exécutée 100 fois avec des longueurs de mot de passe différentes et vérifier la validité à chaque fois.

5. Interface utilisateur
L'utilisateur doit pouvoir interagir avec le programme via une invite de commande où il choisira la longueur de son mot de passe.
Ensuite, le programme générera le mot de passe et le lui affichera, avec un rappel de garder le mot de passe dans un endroit sûr.
Résumé des tâches à faire :
Demander à l'utilisateur une longueur de mot de passe valide (entre 6 et 30).
Générer un mot de passe qui respecte les critères de sécurité (un chiffre, une majuscule, une minuscule, un caractère spécial).
Afficher le mot de passe généré.
Tester le générateur de mot de passe en le faisant fonctionner pour différentes longueurs et en vérifiant qu'il respecte toutes les règles.
Assurer la convivialité en affichant des messages utilisateur clairs et en demandant des entrées valides si nécessaire.

"""

import random
import string

def generate_password(length):
    if length < 6 or length > 30:
        raise ValueError("Password length must be between 6 and 30 characters.")

    # Catégories obligatoires
    digits = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    specials = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Un caractère de chaque catégorie
    password = [
        random.choice(digits),
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(specials)
    ]

    # Mélange des caractères restants
    all_chars = digits + lowercase + uppercase + specials
    remaining = length - 4
    password += random.choices(all_chars, k=remaining)

    random.shuffle(password)

    return ''.join(password)

def is_password_valid(password):
    has_digit = any(c.isdigit() for c in password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for c in password)
    return all([has_digit, has_lower, has_upper, has_special])

def get_user_length():
    while True:
        try:
            length = int(input(" Combien de caractères doit contenir votre mot de passe (6 à 30) ? "))
            if 6 <= length <= 30:
                return length
            else:
                print(" Merci d’entrer un nombre entre 6 et 30.")
        except ValueError:
            print(" Veuillez entrer un **nombre valide**.")

def test_password_generator():
    print("Test automatique de génération de mot de passe...")
    for _ in range(100):
        length = random.randint(6, 30)
        pwd = generate_password(length)
        assert len(pwd) == length, f"Erreur de longueur : {len(pwd)} au lieu de {length}"
        assert is_password_valid(pwd), f"Mot de passe invalide : {pwd}"
    print("Tous les tests ont réussi !")

# Lancer les tests
test_password_generator()

# Génération manuelle
length = get_user_length()
password = generate_password(length)
print(f"\n Votre mot de passe sécurisé est : {password}")
print(" Gardez-le dans un endroit sûr !")

