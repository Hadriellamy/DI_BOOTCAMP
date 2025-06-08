
Exercise 1 : DVD Rentals

Instructions

We want to encourage families and kids to enjoy our movies.

Retrieve all films with a rating of G or PG, which are are not currently rented (they have been returned/have never been borrowed).

Create a new table which will represent a waiting list for children’s movies. This will allow a child to add their name to the list until the DVD is available (has been returned). Once the child takes the DVD, their name should be removed from the waiting list (ideally using triggers, but we have not learned about them yet. Let’s assume that our Python program will manage this). Which table references should be included?

Retrieve the number of people waiting for each children’s DVD. Test this by adding rows to the table that you created in question 2 above.

###################################################################################################################################################################################################################################################################################################################################################################################################################################################################


🎞️ 1. Films "G" ou "PG" qui ne sont pas loués actuellement

Pour cela :

Films avec rating 'G' ou 'PG'
Le film nest pas actuellement loué, donc :
soit jamais loué (rental inexistant)
soit retourné (return_date IS NOT NULL)
✅ Requête :
SELECT DISTINCT f.film_id, f.title, f.rating
FROM film f
JOIN inventory i ON f.film_id = i.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE f.rating IN ('G', 'PG')
  AND (r.return_date IS NOT NULL OR r.rental_id IS NULL);
📋 2. Créer une table waiting_list pour les films enfants

🎯 Objectif :
Permettre aux enfants de sinscrire pour un DVD
Supprimer leur nom dès que le film est loué (via programme Python)
Lier avec les bonnes clés étrangères : film_id, peut-être customer_id, ou au moins un nom
✅ Requête de création :
CREATE TABLE waiting_list (
    waiting_id SERIAL PRIMARY KEY,
    film_id INTEGER NOT NULL,
    child_name VARCHAR(100) NOT NULL,
    request_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_film FOREIGN KEY (film_id) REFERENCES film(film_id)
);
🔎 Remarques :
On utilise film_id comme clé étrangère (vers film)
Pas besoin dinventaire spécifique ici (c’est une attente pour n’importe quel exemplaire du film)
On pourrait aussi ajouter customer_id si on voulait lier à la table customer
🔢 3. Combien de personnes attendent chaque film enfants ?

✅ Requête :
SELECT f.film_id, f.title, COUNT(w.waiting_id) AS nb_waiting
FROM waiting_list w
JOIN film f ON w.film_id = f.film_id
GROUP BY f.film_id, f.title
ORDER BY nb_waiting DESC;
🧪 4. Ajout de données de test dans waiting_list

✅ Exemples d’insertion :
INSERT INTO waiting_list (film_id, child_name) VALUES (12, 'Tommy');
INSERT INTO waiting_list (film_id, child_name) VALUES (12, 'Sarah');
INSERT INTO waiting_list (film_id, child_name) VALUES (8, 'Leo');
✅ Puis, relancer :
SELECT f.title, COUNT(*) AS nb_waiting
FROM waiting_list w
JOIN film f ON w.film_id = f.film_id
GROUP BY f.title;
📌 Résumé

Étape	Objectif	Requête
1	Films "G" ou "PG" actuellement disponibles	SELECT ... avec rating et return_date
2	Créer table waiting_list	CREATE TABLE waiting_list (...)
3	Nombre denfants en attente par film	SELECT ... COUNT(*) FROM waiting_list
4	Tester	INSERT INTO waiting_list (...)
