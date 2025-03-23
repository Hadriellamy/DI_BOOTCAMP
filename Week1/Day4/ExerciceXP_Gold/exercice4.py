#Exercise 4: Greatest Number
"""
Instructions

Ask the user for 3 numbers and print the greatest number.

Test Data
Input the 1st number: 25
Input the 2nd number: 78
Input the 3rd number: 87

The greatest number is: 87

"""

numbers1 = int(input("Enter the 1er number : "))
numbers2 = int(input("Enter the 2nd number : "))
numbers3 = int(input("Enter the 3eme number : "))

if numbers1 >= numbers2 and numbers1 >= numbers3:
    print("The greatest number is:", numbers1)

elif numbers2 >= numbers1 and numbers2 >= numbers3:
    print("The greatest number is:", numbers2)

else:
    print("The greatest number is:", numbers3)


# Another method

numbers1 = int(input("Enter the 1er number : "))
numbers2 = int(input("Enter the 2nd number : "))
numbers3 = int(input("Enter the 3eme number : "))

print("The greatest number is:", max(numbers1, numbers2, numbers3))

