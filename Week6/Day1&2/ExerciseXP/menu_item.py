"""""
Exercise 1 : Restaurant Menu Manager

Instructions

Description: Create a restaurant menu management system for a manager. The program should allow the manager to view the menu, add an item and delete an item.



PART 1

In this exercise we will use PostgreSQL and Python.

Create a new database and a new table in pgAdmin (or in psql). The table is named Menu_Items and contains the columns

item_id : SERIAL PRIMARY KEY
item_name : VARCHAR(30) NOT NULL
item_price : SMALLINT DEFAULT 0

In the file menu_item.py, create a new class called MenuItem, the attributes should be the name and price of each item.


Create several methods (save, delete, update) these methods will allow a user to save, delete and update items from the Menu_Items table. The update method can update the name as well as the price of an item.

In the file menu_manager.py, create a new class called MenuManager
Create a Class Method called get_by_name that will return a single item from the Menu_Items table depending on it’s name, if an object is not found (there is no item matching the name in the get_by_name method) return None.

Create a Class Method called all_items which will return a list of all the items from the Menu_Items table.



Codebox:

item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuManager.get_by_name('Beef Stew')
items = MenuManager.all()
"""
##############################################################################################################################################################################################

import psycopg2

class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price
        self.item_id = None  # Sera rempli après l'insertion en DB

    def save(self):
        try:
            conn = psycopg2.connect("dbname=restaurant_menu user=hadriellamy password=170423") 
            cur = conn.cursor()
            cur.execute("INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s) RETURNING item_id;", (self.item_name, self.item_price))
            self.item_id = cur.fetchone()[0]
            conn.commit()
            print(f"Article '{self.item_name}' ajouté avec succès !")
        except psycopg2.Error as e:
            print(f"Erreur lors de l'ajout de '{self.item_name}' : {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def delete(self):
        if self.item_id is None:
            print("L'article n'a pas encore été enregistré.")
            return

        try:
            conn = psycopg2.connect("dbname=restaurant_menu user=hadriellamy password=170423") 
            cur = conn.cursor()
            cur.execute("DELETE FROM menu_items WHERE item_id = %s;", (self.item_id,))
            conn.commit()
            print(f"Article '{self.item_name}' supprimé avec succès !")
        except psycopg2.Error as e:
            print(f"Erreur lors de la suppression de '{self.item_name}' : {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def update(self, new_name, new_price):
        if self.item_id is None:
            print("L'article n'a pas encore été enregistré.")
            return

        try:
            conn = psycopg2.connect("dbname=restaurant_menu user=hadriellamy password=170423") 
            cur = conn.cursor()
            cur.execute("UPDATE menu_items SET item_name = %s, item_price = %s WHERE item_id = %s;", (new_name, new_price, self.item_id))
            conn.commit()
            self.item_name = new_name
            self.item_price = new_price
            print(f"Article '{self.item_name}' mis à jour avec succès !")
        except psycopg2.Error as e:
            print(f"Erreur lors de la mise à jour de '{self.item_name}' : {e}")
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()