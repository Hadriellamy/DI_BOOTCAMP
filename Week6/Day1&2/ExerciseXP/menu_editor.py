
from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\nMenu principal :")
        print("V - Afficher un article")
        print("A - Ajouter un article")
        print("D - Supprimer un article")
        print("U - Mettre à jour un article")
        print("S - Afficher le menu complet")
        print("Q - Quitter")

        choice = input("Votre choix : ").upper()

        if choice == 'V':
            view_item()
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'Q':
            show_restaurant_menu()
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


def add_item_to_menu():
    name = input("Nom de l'article : ")
    while True:
        try:
            price = int(input("Prix de l'article : "))
            break
        except ValueError:
            print("Prix invalide. Veuillez entrer un nombre.")

    item = MenuItem(name, price)
    item.save()
    print(f"L'article '{name}' a été ajouté avec succès.")


def remove_item_from_menu():
    name = input("Nom de l'article à supprimer : ")
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
        print(f"L'article '{name}' a été supprimé avec succès.")
    else:
        print(f"L'article '{name}' n'a pas été trouvé.")


def update_item_from_menu():
    name = input("Nom de l'article à mettre à jour : ")
    item = MenuManager.get_by_name(name)
    if item:
        while True:
            try:
                new_price = int(input("Nouveau prix : "))
                break
            except ValueError:
                print("Prix invalide. Veuillez entrer un nombre.")
        new_name = input("Nouveau nom (laisser vide pour garder le même) : ")
        if not new_name:
            new_name = name
        item.update(new_name, new_price)
        print(f"L'article '{name}' a été mis à jour avec succès.")
    else:
        print(f"L'article '{name}' n'a pas été trouvé.")


def view_item():
    name = input("Nom de l'article à afficher : ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Nom : {item.item_name}, Prix : {item.item_price}")
    else:
        print(f"L'article '{name}' n'a pas été trouvé.")



def show_restaurant_menu():
    items = MenuManager.all_items()
    if items:
        print("\nMenu du restaurant :")
        for item in items:
            print(f"- {item.item_name} : {item.item_price}")
    else:
        print("Le menu est vide.")

if __name__ == "__main__":
    show_user_menu()