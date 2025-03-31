#Exercise 6: Words And Letters
"""
Instructions

Ask a user for 7 words, store them in a list named words.
Ask the user for a single character, store it in a variable called letter.
Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

"""

words = []

for i in range(7):
    word = input(f"Enter word #{i + 1}: ")
    words.append(word)

print(words)

letter = input("Enter a single charactere : ")


for word in words:

  if letter in word:
    print(word.index(letter))
  else:
    print(f"'{letter}' is not found in '{word}'.")
