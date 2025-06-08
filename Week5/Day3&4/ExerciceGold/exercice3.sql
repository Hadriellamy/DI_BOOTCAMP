
Exercise 3 : Items And Customers

Instructions

We will work on the public database that we created yesterday.

Part I

Create a table named purchases. It should have 3 columns :
id : the primary key of the table
customer_id : this column references the table customers
item_id : this column references the table items
quantity_purchased : this column is the quantity of items purchased by a certain customer

Insert purchases for the customers, use subqueries:
Scott Scott bought one fan
Melanie Johnson bought ten large desks
Greg Jones bougth two small desks
The table purchases should look like this:

id	customer_id	item_id	quantity_purchased
1	3	3	1
2	5	2	10
3	1	1	2


Here is the explanation of the first row:

id = 1, this is the auto-incrementing primary key
customer_id = 3, because the id of Scott Scott in the customers table is 3
item_id = 3, because the id of a fan in the items table is 3
quantity_purchased = 1, because Scott Scott bought one fan


Part II

Use SQL to get the following from the database:
All purchases. Is this information useful to us?
All purchases, joining with the customers table.
Purchases of the customer with the ID equal to 5.
Purchases for a large desk AND a small desk

Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
Customer first name
Customer last name
Item name

Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?



#####################################################################################################################################################


✅ Part I – Création et insertion dans la table purchases

1. Créer la table purchases
CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    item_id INTEGER REFERENCES items(id),
    quantity_purchased INTEGER NOT NULL
);
2. Insérer les achats (avec sous-requêtes)
Scott Scott a acheté un fan

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'),
    (SELECT id FROM items WHERE name = 'fan'),
    1
);
Melanie Johnson a acheté 10 large desks

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'),
    (SELECT id FROM items WHERE name = 'large desk'),
    10
);
Greg Jones a acheté 2 small desks

INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (
    (SELECT id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
    (SELECT id FROM items WHERE name = 'small desk'),
    2
);
✅ Part II – Requêtes diverses

1. Toutes les lignes de la table purchases
SELECT * FROM purchases;
💡 Utilité ? : Seul, ce tableau est limité — il montre qui a acheté quoi, mais pas les noms des clients ou des objets.

2. Tous les achats avec les noms des clients
SELECT p.*, c.first_name, c.last_name
FROM purchases p
JOIN customers c ON p.customer_id = c.id;
3. Achats du client ayant l’ID = 5
SELECT *
FROM purchases
WHERE customer_id = 5;
4. Achats pour large desk ET small desk
SELECT *
FROM purchases
WHERE item_id IN (
    SELECT id FROM items WHERE name IN ('large desk', 'small desk')
);
5. Tous les clients ayant fait un achat, avec le nom de l’objet acheté
SELECT c.first_name, c.last_name, i.name AS item_name
FROM purchases p
JOIN customers c ON p.customer_id = c.id
JOIN items i ON p.item_id = i.id;
6. Tentative d’insérer un achat SANS item_id
INSERT INTO purchases (customer_id, item_id, quantity_purchased)
VALUES (1, NULL, 1);
❌ Est-ce que ça marche ? Pourquoi ?

Non, ça ne fonctionne pas, car item_id est une clé étrangère qui référence la table items, et par défaut, une clé étrangère ne peut pas être NULL si la colonne ne l’autorise pas explicitement (et encore moins si une contrainte d'intégrité empêche l'insertion de références invalides).

✅ Pour que cela fonctionne, il faudrait :

soit autoriser NULL dans item_id
soit créer une version temporaire ou incomplète de la transaction (peu recommandé sans vérifications supplémentaires)
Exemple de définition qui autoriserait l’insertion :

CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    item_id INTEGER REFERENCES items(id) ON DELETE SET NULL,
    quantity_purchased INTEGER NOT NULL
);