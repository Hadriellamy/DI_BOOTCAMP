#Exercise 1 : Favorite Numbers

"""
Instructions

Create a set called my_fav_numbers with all your favorites numbers.
Add two new numbers to the set.
Remove the last number.
Create a set called friend_fav_numbers with your friend’s favorites numbers.
Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

"""


my_fav_numbers = {1,5,7,11,14,16,17,22}
my_fav_numbers.add(18)
my_fav_numbers.add(26)
my_fav_numbers.remove(26)


friend_fav_numbers = {3,6,12}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)

