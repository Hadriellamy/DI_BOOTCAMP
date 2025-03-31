#Exercise 8: Who Ordered A Pizza ?
"""
Instructions

Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
As they enter each topping, print a message saying you’ll add that topping to their pizza.
Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

"""

# Initialize empty list to hold pizza toppings
pizza_toppings = []
total_price = 0
# Loop to ask user for pizza toppings
while True:
    # Ask user for pizza topping
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    # Check if user wants to quit
    if topping.lower() == 'quit':
        break
    # Add topping to list and print message
    pizza_toppings.append(topping)
    print(f"Adding {topping} to your pizza!")
    # Calculate total price
    total_price += 10 + 2.5
    # Print all pizza toppings and total price
    print("\nYour pizza toppings are:")
    for topping in pizza_toppings:
        print(f"- {topping}")
        print(f"Total price: ${total_price:.2f}")
        break
    # Print final message
    print("Enjoy your pizza!")  # Removed the break statement here
    print("Thanks for ordering!")  # Removed the break statement here