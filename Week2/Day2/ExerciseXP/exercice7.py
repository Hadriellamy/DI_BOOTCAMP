#Exercise 7 : Temperature Advice
"""
Instructions

Create a function called get_random_temp().
This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
Test your function to make sure it generates expected results.

Create a function called main().
Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
between 16 and 23
between 24 and 32
between 32 and 40

Change the get_random_temp() function:
Add a parameter to the function, named ‘season’.
Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
Now that we’ve changed get_random_temp(), let’s change the main() function:
Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
Use the season as an argument when calling get_random_temp().

Bonus: Give the temperature as a floating-point number instead of an integer.
Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

"""

import random

def get_random_temp(season="spring", as_float=False):
    if season.lower() == "winter":
        lower, upper = -10, 16
    elif season.lower() == "summer":
        lower, upper = 24, 40
    elif season.lower() in ["autumn", "fall"]:
        lower, upper = 0, 23
    elif season.lower() == "spring":
        lower, upper = 0, 30
    else:
        lower, upper = -10, 40  

    if as_float:
        temp = random.uniform(lower, upper)
        return round(temp, 1)
    else:
        return random.randint(lower, upper)

def main():
    season = input("Enter the season (winter, spring, summer, autumn): ")
    
    # Option bonus : demander le mois et déduire la saison
    # month = int(input("Enter the month number (1-12): "))
    # if month in [12, 1, 2]:
    #     season = "winter"
    # elif month in [3, 4, 5]:
    #     season = "spring"
    # elif month in [6, 7, 8]:
    #     season = "summer"
    # elif month in [9, 10, 11]:
    #     season = "autumn"
    
    # Obtenir la température avec un nombre à virgule
    temp = get_random_temp(season, as_float=True)
    
    print(f"The temperature right now is {temp} degrees Celsius.")
    
    
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 <= temp < 23:
        print("It's a bit cool; a light jacket might be a good idea.")
    elif 23 <= temp < 32:
        print("The weather is warm and nice!")
    elif 32 <= temp <= 40:
        print("It's hot outside! Stay hydrated.")
    else:
        print("Enjoy the weather!")

if __name__ == "__main__":
    main()


