"""
What You Will Create



Mini-Project: Rock, Paper, Scissors

Rock-paper-scissors is an old game that can be played between two people. You can read about it in wikipedia

We will create a game for the user to play Rock-paper-scissors against the computer.

The user will input his/her move (rock/paper/scissors),
and the computer will select either rock, paper or scissors at random.
We will then compare the user’s move with the computer’s move, and determine the results of the game:

The user won

The computer won (the user lost)
A draw (tie)
We will print the outcome of each game: the user’s choice, the computer’s choice, and the result.

The user will be able to play again and again. Once the user decides to exit the program, we will print a summary of the outcomes of all the games: how many times they won, lost or and tied the computer.

Here’s some example output:






Instructions

Create a new directory for the game. Inside it, create 2 files:
rock-paper-scissors.py – this will contain functions to show the main menu, handle user’s input, and show the game summary before exiting.
game.py – this will contain a Game class which will have functions to play a single game of rock-paper-scissors against the computer, determine the game’s result, and return the result.


Steps

Part I - Game.py

game.py – this file/module should contain a class called Game. It should have 4 methods:
get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.

get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).

get_game_result(self, user_item, computer_item) – Determine the result of the game.
Parameters:
user_item – the user’s chosen item (rock/paper/scissors)
computer_item – the computer’s chosen (random) item (rock/paper/scissors)
Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.

play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
Get the user’s item (rock/paper/scissors) and remember it

Get a random item for the computer (rock/paper/scissors) and remember it

Determine the results of the game by comparing the user’s item and the computer’s item
Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”

Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.


Part II - Rock-Paper-Scissors.py

rock-paper-scissors.py : create 3 functions
get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation), and return the choice. No looping should occur here.
The possibles choices are : Play a new game or Show scores or Quit

print_results(results) – this should print the results of the games played. It should have a single parameter named results; which will be a dictionary of the results of the games played. It should display these results in a user-friendly way, and thank the user for playing.


Note: results should be in this form: {win: 2,loss: 4,draw: 3}. Bear in mind that this dictionary will need to be created and populated in some other part of our code, and passed in to the print_results function at the right time.

main() - the main function. It should take care of 3 things:
Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)

When the user chooses to play a game:
Create a new Game object (see below), and call its play() function, receiving the result of the game that is returned.
Remember the results of every game that is played.

When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.

"""


from game import Game

def get_user_menu_choice():
    print("\n--- Rock Paper Scissors ---")
    print("1. Play a new game")
    print("2. Show scores")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ").strip()
    if choice in ["1", "2", "3"]:
        return choice
    else:
        print("Invalid choice. Please enter 1, 2 or 3.")
        return get_user_menu_choice()

def print_results(results):
    print("\nGame Results:")
    print(f"Wins: {results.get('win', 0)}")
    print(f"Losses: {results.get('loss', 0)}")
    print(f"Draws: {results.get('draw', 0)}")
    print("\nThanks for playing!")

def main():
    results = {"win": 0, "loss": 0, "draw": 0}
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == "1":
            game = Game()
            result = game.play()
            results[result] += 1
        
        elif choice == "2":
            print_results(results)
        
        elif choice == "3":
            print_results(results)
            break

if __name__ == "__main__":
    main()
