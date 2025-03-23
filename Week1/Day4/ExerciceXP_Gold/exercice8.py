#Exercise 8 : List And Tuple
"""
Instructions

Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.

Suppose the following input is supplied to the program: 34,67,55,33,12,98

Then, the output should be:

['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

"""

numbers = input("Enter numbers separated by commas: ")

numbers_list = numbers.split(",")

numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)
