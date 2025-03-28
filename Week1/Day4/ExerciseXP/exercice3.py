 #Exercise 3: List

"""
Instructions

Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

Remove “Banana” from the list.
Remove “Blueberries” from the list.
Add “Kiwi” to the end of the list.
Add “Apples” to the beginning of the list.
Count how many apples are in the basket.
Empty the basket.
Print(basket)

"""

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove “Banana” from the list.
basket.remove("Banana")
# Remove “Blueberries” from the list.
basket.remove("Blueberries")
# Add “Kiwi” to the end of the list.
basket.append("Kiwi")
# Add “Apples” to the beginning of the list.
basket.insert(0, "Apples")
# Count how many apples are in the basket.
apples_count = basket.count("Apples")
# Empty the basket.
basket.clear()
# Print(basket)
print(basket)  # Output: []

