#Exercise 2: Import
"""
Instructions

In a file named func.py create a function that sum 2 numbers, and prints the result
In a file named exercise_one.py import the function and call it to print the result
Hint: You can use the the following syntaxes:

import module_name 

OR 

from module_name import function_name 

OR 

from module_name import function_name as fn 

OR

import module_name as mn

"""

from func import sum_numbers

sum_numbers(3, 5)
