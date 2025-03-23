#Exercise 7: Min, Max, Sum
"""
Instructions

Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.

"""

number = list(range(1,1000001))

print("The minimum is :", min(number))
print("The maximum is :", max(number))

total = print("Sum of numbers from 1 to 1,000,000 is:", sum(number))