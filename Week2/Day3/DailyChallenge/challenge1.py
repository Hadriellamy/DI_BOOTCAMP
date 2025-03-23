#Challenge 1 : Sorting


"""
Instructions

Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Use List Comprehension
Example:

Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world

"""

input_string = input("Enter comma separated words: ")

words = [word.strip() for word in input_string.split(',')]

sorted_words = sorted(words)

print(','.join(sorted_words))
