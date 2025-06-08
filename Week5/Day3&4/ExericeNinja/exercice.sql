
Exercise 1 : Bonus Public Database (Continuation Of XP)

Instructions

Fetch the last 2 customers in alphabetical order (A-Z) – exclude ‘id’ from the results.
Use SQL to delete all purchases made by Scott.
Does Scott still exist in the customers table, even though he has been deleted? Try and find him.
Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will appear, although instead of the customer’s first and last name, you should only see empty/blank. (Which kind of join should you use?).
Use SQL to find all purchases. Join purchases with the customers table, so that Scott’s order will NOT appear. (Which kind of join should you use?)

#############################################################################################################################################################################################################################################



✅ 1. Afficher les 2 derniers clients par ordre alphabétique (A-Z) sans la colonne id :

SELECT first_name, last_name
FROM customers
ORDER BY last_name ASC, first_name ASC
OFFSET (
    SELECT COUNT(*) - 2 FROM customers
);
Ou plus simplement :

SELECT first_name, last_name
FROM customers
ORDER BY last_name ASC, first_name ASC
LIMIT 2 OFFSET (
    SELECT COUNT(*) - 2 FROM customers
);
✅ 2. Supprimer tous les achats faits par "Scott"

DELETE FROM purchases
WHERE customer_id = (
    SELECT id FROM customers
    WHERE first_name = 'Scott' AND last_name = 'Scott'
);
✅ 3. Scott est-il encore dans la table customers ?

SELECT * FROM customers
WHERE first_name = 'Scott' AND last_name = 'Scott';
💡 Réponse attendue : Oui, Scott existe encore dans la table customers car on a seulement supprimé ses achats dans la table purchases.

✅ 4. Afficher tous les achats, avec noms des clients si disponibles ; sinon, afficher vide (Scott doit apparaître)

SELECT p.id, c.first_name, c.last_name, p.item_id, p.quantity_purchased
FROM purchases p
LEFT JOIN customers c ON p.customer_id = c.id;
💡 Quel type de JOIN utiliser ?
👉 Un LEFT JOIN, car on veut TOUS les achats, même si certains clients (comme Scott après suppression) n’existent plus dans customers → leurs first_name et last_name apparaîtront comme NULL.

✅ 5. Afficher tous les achats, mais uniquement ceux dont les clients existent encore (donc Scott ne doit PAS apparaître)

SELECT p.id, c.first_name, c.last_name, p.item_id, p.quantity_purchased
FROM purchases p
INNER JOIN customers c ON p.customer_id = c.id;
💡 Quel type de JOIN utiliser ?
👉 Un INNER JOIN, qui n’affichera que les achats liés à des clients existants.

