#Challenge 2
"""
Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
Sort the list in alphabetical order.
Return “Nothing” if you can’t afford anything from the store.
Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

Examples

The key is the product, the value is the price

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

➞ ["Bread", "Fertilizer", "Water"]

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

➞ ["Apple", "Bananas", "Fan", "Honey", "Spoon"]

# In fact the prices of Apple + Honey + Fan + Bananas + Pan is more that $100, so you cannot by the Pan, 
# instead you can by the Spoon that is $2

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

➞ "Nothing"

"""

def parse_money(money_str):
    """Convertit une chaîne de type '$1,000' en entier (ici 1000)."""
    return int(money_str.replace("$", "").replace(",", ""))

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}
wallet = "$300"

# Pour tester d'autres exemples, décommente l'un des blocs suivants :

# Exemple 2 :
# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }
# wallet = "$100"

# Exemple 3 :
# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }
# wallet = "$1"

wallet_amount = parse_money(wallet)

items_list = []
for item, price_str in items_purchase.items():
    price = parse_money(price_str)
    items_list.append((item, price))

items_sorted = sorted(items_list, key=lambda x: x[1])

affordable_items = []
total_cost = 0

for item, price in items_sorted:
    if total_cost + price <= wallet_amount:
        affordable_items.append(item)
        total_cost += price
    else:
        break

affordable_items = sorted(affordable_items)

if affordable_items:
    print(affordable_items)
else:
    print("Nothing")
