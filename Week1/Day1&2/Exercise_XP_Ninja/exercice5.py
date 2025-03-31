#Exercise 5: Longest word without a specific character

"""Instructions
Keep asking the user to input the longest sentence they can without the character “A”.
Each time a user successfully sets a new longest sentence, print a congratulations message."""

record = ""  

while True:
    sentence = input("Entrez la phrase la plus longue que vous pouvez sans utiliser le caractère 'A': ")

    if "A" in sentence:
        print("Votre phrase contient le caractère 'A'. Essayez encore.")
        continue

    if len(sentence) > len(record):
        record = sentence
        print("Félicitations! Vous avez établi un nouveau record!")
    else:
        print("Cette phrase n'est pas plus longue que le record actuel. Essayez encore!")
