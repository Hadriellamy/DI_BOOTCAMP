#Exercise 5: For Loop
"""
Instructions

#1Use a for loop to print all numbers from 1 to 20, inclusive.
#2Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

"""
#1
for number in range(1,21):

 print(number) 

#2
my_list = list(range(1,21))
for i in range(len(my_list)):
 if i % 2 == 0:
  print(my_list[i])  # prints every element with an even index