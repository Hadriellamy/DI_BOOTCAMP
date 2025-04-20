#suite ex1.py


from menu_manager import MenuManager

def load_manager():
    # Crée et retourne une instance de MenuManager
    return MenuManager()

def show_user_menu():
    # Affiche le menu utilisateur
    print("\nMenu:")
    print("1. Afficher le menu du restaurant")
    print("2. Ajouter un élément au menu")
    print("3. Supprimer un élément du menu")
    print("4. Quitter")
    choice = input("Choisissez une option (1-4): ")
    return choice

def add_item_to_menu(manager):
    # Demande à l'utilisateur d'ajouter un élément
    name = input("Nom de l'élément à ajouter: ")
    price = float(input("Prix de l'élément à ajouter: "))
    manager.add_item(name, price)
    print(f"L'élément '{name}' a été ajouté avec succès.")

def remove_item_from_menu(manager):
    # Demande à l'utilisateur de supprimer un élément
    name = input("Nom de l'élément à supprimer: ")
    if manager.remove_item(name):
        print(f"L'élément '{name}' a été supprimé avec succès.")
    else:
        print(f"Erreur: L'élément '{name}' n'existe pas.")

def show_restaurant_menu(manager):
    # Affiche le menu du restaurant
    print("\nMenu du restaurant:")
    for item in manager.menu:
        print(f"{item['name']} - {item['price']}€")

def main():
    manager = load_manager()

    while True:
        choice = show_user_menu()

        if choice == '1':
            show_restaurant_menu(manager)
        elif choice == '2':
            add_item_to_menu(manager)
        elif choice == '3':
            remove_item_from_menu(manager)
        elif choice == '4':
            manager.save_to_file()
            print("Menu sauvegardé.")
            break
        else:
            print("Choix invalide. Essayez à nouveau.")

if __name__ == "__main__":
    main()
