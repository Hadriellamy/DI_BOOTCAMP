
from menu_item import MenuItem
from menu_manager import MenuManager

item = MenuItem('Burger', 35)
item.save()

item2 = MenuManager.get_by_name('Burger')
print(f"Récupéré : {item2.item_name} - {item2.item_price}")

item.delete()

item.update('Veggie Burger', 37)  # Cela ne fonctionnera pas car l'item a été supprimé.

item3 = MenuItem('Beef Stew', 45)
item3.save()

item4 = MenuManager.get_by_name('Beef Stew')
print(f"Récupéré : {item4.item_name} - {item4.item_price}")

items = MenuManager.all_items()
print("Tous les articles :")
for item in items:
    print(f"- {item.item_name} : {item.item_price}")