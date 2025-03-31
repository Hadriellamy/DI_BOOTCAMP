#Exercise 9 : Random Number
"""
Instructions

Ask the user to input a number from 1 to 9 (including).
Get a random number between 1 and 9. Hint: random module.
If the user guesses the correct number print a message that says Winner.
If the user guesses the wrong number print a message that says better luck next time.
Bonus: use a loop that allows the user to keep guessing until they want to quit.
Bonus 2: on exiting the loop tally up and display total games won and lost.

"""
import random

play = random.randint(1, 9)
number = int(input("Enter a number between 1 and 9 (include) : "))
if number == play :
   print("You guess the correct number ! You win")
else :
   print("Sorry, you loose. Next time maybe ...")


# Another method with Bonus 

import random

games_won = 0
games_lost = 0

while True:
    # Génère un nombre aléatoire entre 1 et 9 inclus
    play = random.randint(1, 9)

    # Demande à l'utilisateur de deviner ou quitter
    user_input = input("Guess a number between 1 and 9 (or type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        break  # Sortir de la boucle si l'utilisateur écrit 'quit'

    number = int(user_input)

    if number == play:
        print("You guessed the correct number! You win!")
        games_won += 1  # Compte les victoires
    else:
        print(f"Sorry, you lose. The number was {play}.")
        games_lost += 1  # Compte les défaites

# Afficher les résultats après avoir quitté la boucle
print(f"\nGames won: {games_won}")
print(f"Games lost: {games_lost}")
print("Thanks for playing!")

