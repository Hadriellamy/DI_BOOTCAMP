import psycopg2
from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        try:
            conn = psycopg2.connect("dbname=restaurant_menu user=hadriellamy password=170423") # Remplacez par vos infos
            cur = conn.cursor()
            cur.execute("SELECT item_id, item_name, item_price FROM menu_items WHERE item_name = %s;", (item_name,))
            row = cur.fetchone()
            if row:
                item = MenuItem(row[1], row[2])
                item.item_id = row[0]
                return item
            else:
                return None
        except psycopg2.Error as e:
            print(f"Erreur lors de la recherche de '{item_name}' : {e}")
            return None
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    @classmethod
    def all_items(cls):
        conn = None
        cur = None
        try:
            conn = psycopg2.connect("dbname=restaurant_menu user=hadriellamy password=170423")
            cur = conn.cursor()
            cur.execute("SELECT item_id, item_name, item_price FROM menu_items;")
            rows = cur.fetchall()
            items = []
            for row in rows:
                item = MenuItem(row[1], row[2])
                item.item_id = row[0]
                items.append(item)
            return items
        except psycopg2.Error as e:
            print(f"Erreur lors de la récupération de tous les articles : {e}")
            return []
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()