 #Exercise 4: Floats
"""
Instructions

Recap – What is a float? What is the difference between an integer and a float?
Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
Can you think of another way to generate a sequence of floats?

"""


#A float is a numeric type in Python that represents numbers with decimal points (e.g., 2.5, 3.14).
#An integer (int) is a numeric type that represents whole numbers without decimal points (e.g., 2, 10, -5).

mixed_list = []
num = 1.5

while num <= 5:
    mixed_list.append(num)
    num += 0.5

print(mixed_list)
# Output: [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]


#Alternative ways to generate a sequence of floats

mixed_list = [x * 0.5 for x in range(3, 11)]
print(mixed_list)
# Output: [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

