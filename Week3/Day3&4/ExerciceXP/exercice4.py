#Exercise 4 : Current Date
"""
Instructions

Create a function that displays the current date.
Hint : Use the datetime module.

"""

from datetime import date

def show_current_date():
    current_date = date.today()
    print("Current date:", current_date)

show_current_date()
