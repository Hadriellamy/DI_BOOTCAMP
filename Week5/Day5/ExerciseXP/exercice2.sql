
🌟 Exercise 2 : DVD Rental

Instructions

Use UPDATE to change the language of some films. Make sure that you use valid languages.

Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?

We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?

Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

The 2nd film : A short documentary (less than 1 hour long), rated “R”.

The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.


#######################################################################################################################################################################################################



✅ 1. Modifier la langue de certains films (UPDATE)
-- Exemple : Changer la langue de certains films en 'French' (language_id = 2, à confirmer)
UPDATE film
SET language_id = 2
WHERE title IN ('ACADEMY DINOSAUR', 'ACE GOLDFINGER');
➡️ Hypothèse : Si language_id = 2 correspond à "French", les deux films auront désormais le français comme langue.
⚠️ Il faut vérifier les IDs valides dans la table language.

✅ 2. Quelles FOREIGN KEYS dans la table customer ?
\d customer  -- (PostgreSQL)
Ou

SELECT conname, confrelid::regclass AS referenced_table
FROM pg_constraint
WHERE conrelid = 'customer'::regclass AND contype = 'f';
➡️ Généralement, la table customer contient :

address_id ➡️ référence address.address_id
store_id ➡️ référence store.store_id
👉 Donc, pour insérer dans customer, il faut d’abord avoir une adresse existante et un magasin existant.

✅ 3. DROP de customer_review
DROP TABLE customer_review;
➡️ Si des contraintes de FOREIGN KEY ou des dépendances existent, la base peut refuser de supprimer la table.
Mais ici, si la table nest pas référencée ailleurs, le DROP est immédiat et facile.

✅ 4. Combien de locations sont encore en cours (non retournées) ?
SELECT COUNT(*) 
FROM rental 
WHERE return_date IS NULL;
➡️ Résultat : nombre total de films loués mais pas encore retournés.

✅ 5. Top 30 des films les plus chers qui ne sont pas encore retournés
SELECT film.title, film.replacement_cost
FROM rental
JOIN inventory ON rental.inventory_id = inventory.inventory_id
JOIN film ON inventory.film_id = film.film_id
WHERE rental.return_date IS NULL
ORDER BY film.replacement_cost DESC
LIMIT 30;
➡️ Résultat : liste des 30 films encore loués avec le coût de remplacement le plus élevé.

🎬 Ton ami veut retrouver 4 films spécifiques :

✅ 6. 1er film : Sumo + Penelope Monroe
SELECT film.title
FROM film
JOIN film_actor USING (film_id)
JOIN actor USING (actor_id)
WHERE actor.first_name = 'Penelope' AND actor.last_name = 'Monroe'
AND (film.description ILIKE '%sumo%' OR film.title ILIKE '%sumo%');
➡️ Résultat : film avec Penelope Monroe + mot-clé sumo dans titre ou description.

✅ 7. 2e film : documentaire court (< 1h), classé R
SELECT title
FROM film
WHERE length < 60 AND rating = 'R';
➡️ Résultat : films courts, classés R — probablement un documentaire.

✅ 8. 3e film : loué par Matthew Mahan, payé > 4$, retourné entre 28/07 et 01/08/2005
SELECT f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON r.rental_id = p.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND p.amount > 4.00
AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';
➡️ Résultat : film payé +4$ par Matthew Mahan, retourné fin juillet 2005.

✅ 9. 4e film : aussi vu par Matthew Mahan, avec "boat" dans le titre ou description, remplacement coûteux
SELECT f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan'
AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY f.replacement_cost DESC
LIMIT 1;
➡️ Résultat : film lié à un bateau, vu par Matthew, avec un coût de remplacement élevé.