#Exercise 2: Tuple
"""
Instructions

Given a tuple which value is integers, is it possible to add more integers to the tuple?

"""

#Solution

"""
No, it's not possible to directly add integers to a tuple because tuples are immutable in Python. However, you can indirectly add elements by converting the tuple into a list, adding elements to the list, and then converting it back to a tuple.

Example : 

my_tuple = (1, 2, 3)

# Convert tuple to a list
temp_list = list(my_tuple)

# Add integers to the list
temp_list.extend([4, 5])

# Convert back to a tuple
my_tuple = tuple(temp_list)

print(my_tuple)  # Output: (1, 2, 3, 4, 5)



In summary, you cannot directly modify a tuple, but you can achieve a similar effect by using a temporary list.

"""