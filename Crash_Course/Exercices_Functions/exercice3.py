#Exercise 3 : Check If Number Is Even Or Odd

"""""
Instructions

Write a function check_even_odd that takes one number and prints “Even” if the number is even, and “Odd” if the number is odd.

Example:

check_even_odd(4)  # Output: "Even"
check_even_odd(7)  # Output: "Odd""

"""""

def check_even_odd(number):
    if number%2 == 0 :
        print("Even")
    else :
        print("Odd")    

#test 
check_even_odd(4)