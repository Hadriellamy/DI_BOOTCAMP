#Exercise 3 : Some Geography
"""
Instructions

Write a function called describe_city() that accepts the name of a city and its country as parameters.
The function should print a simple sentence, such as "<city> is in <country>".
For example “Reykjavik is in Iceland”
Give the country parameter a default value.
Call your function.

"""

def describe_city(name_of_the_city, coutry):
    print(f"{name_of_the_city} is in {coutry}")

describe_city("Paris" ,"France")