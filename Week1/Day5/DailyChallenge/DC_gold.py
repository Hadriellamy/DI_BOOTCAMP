#Instructions
"""
In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

For example, with a left shift of 3 –> D would be replaced by A,
–> E would become B, and so on.

The method is named after Julius Caesar, who used it in his private correspondence.

Create a python program that encrypts and decrypts messages with ceasar cypher.
The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.

Check out this tutorial

Hint:

for letter in text:
    cypher_text += chr(ord(letter) + 3)

 
 
"""

def caesar_encrypt(message, shift):
    encrypted = ""
    for char in message:
        # On vérifie si le caractère est une lettre alphabétique
        if char.isalpha():
            # Pour les majuscules
            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            # Pour les minuscules
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # On laisse inchangés les caractères non alphabétiques (espaces, ponctuation, etc.)
            encrypted += char
    return encrypted

def caesar_decrypt(message, shift):
    # Déchiffrer revient à chiffrer avec un décalage négatif
    return caesar_encrypt(message, -shift)

# Demander à l'utilisateur s'il veut chiffrer ou déchiffrer
choix = input("Voulez-vous (C)hiffrer ou (D)échiffrer un message ? (C/D) : ").strip().lower()

# Demander le message et le décalage
message = input("Entrez votre message : ")
shift = int(input("Entrez le décalage : "))

# Exécuter l'opération choisie
if choix == "c":
    resultat = caesar_encrypt(message, shift)
    print("Message chiffré :", resultat)
elif choix == "d":
    resultat = caesar_decrypt(message, shift)
    print("Message déchiffré :", resultat)
else:
    print("Choix invalide. Veuillez entrer 'C' pour chiffrer ou 'D' pour déchiffrer.")


