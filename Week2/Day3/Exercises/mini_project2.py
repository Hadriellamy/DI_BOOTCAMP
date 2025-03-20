"""Instructions

The computer choose a random word and mark stars for each letter of each word.
Then the player will guess a letter.
If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
The player can’t guess the same letter twice.
"""

   
import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

def display_word(word, guessed_letters):

    displayed = ""
    for char in word:
        if char == " ":
            displayed += " "
        elif char.lower() in guessed_letters:
            displayed += char
        else:
            displayed += "*"
    return displayed



def display_hangman(mistakes):
    
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    print(stages[mistakes])



def hangman():
    word = random.choice(wordslist)
    word_lower = word.lower()  # pour faciliter la vérification
    guessed_letters = set()
    mistakes = 0
    max_mistakes = 6

    print("welcome to the Hangman game!")
    print("Guess the word:")
    
    
    while mistakes < max_mistakes:
        current_display = display_word(word, guessed_letters)
        print("\nCurrent word: ", current_display)
        display_hangman(mistakes)
        
        
        if "*" not in current_display:
            print("Congratulations, you guessed the word!")
            break
        
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed this letter. Try another one.")
            continue
        guessed_letters.add(guess)
        
        if guess in word_lower:
            print("Good game!")
        else:
            print("Wrong answer.")
            mistakes += 1
    
    # En cas de défaite
    if mistakes == max_mistakes:
        display_hangman(mistakes)
        print("Too bad! You were hanged.")
        print("The word was: ", word)

if __name__ == '__main__':
    hangman()
