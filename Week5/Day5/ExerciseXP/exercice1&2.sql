
🌟 Exercise 1: DVD Rental

Instructions

Get a list of all the languages, from the language table.

Get a list of all films joined with their languages – select the following details : film title, description, and language name.

Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.

Create a new table called new_film with the following columns : id, name. Add some new films to the table.

Create a new table called customer_review, which will contain film reviews that customers will make.
Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
It should have the following columns:
review_id – a primary key, non null, auto-increment.
film_id – references the new_film table. The film that is being reviewed.
language_id – references the language table. What language the review is in.
title – the title of the review.
score – the rating of the review (1-10).
review_text – the text of the review. No limit on the length.
last_update – when the review was last updated.

Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

Delete a film that has a review from the new_film table, what happens to the customer_review table?

####################################################################################################################################


✅ 1. Lister toutes les langues
SELECT * FROM language;
➡️ Affiche toutes les langues présentes dans la table language.

✅ 2. Lister tous les films avec leur langue (INNER JOIN)
SELECT film.title, film.description, language.name
FROM film
JOIN language ON film.language_id = language.language_id;
➡️ Résultat : liste des films + leur description + le nom de la langue.
Seuls les films qui ont une langue associée apparaissent.

✅ 3. Lister toutes les langues même si aucun film n’est associé (LEFT JOIN)
SELECT film.title, film.description, language.name
FROM language
LEFT JOIN film ON film.language_id = language.language_id;
➡️ Résultat : toutes les langues apparaissent, même si aucun film ne leur est lié.
Les colonnes film.title et film.description peuvent être NULL pour ces langues sans films.

✅ 4. Créer la table new_film
CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
✅ 5. Insérer des films dans new_film
INSERT INTO new_film (name) VALUES
('The AI Awakens'),
('Ocean Beyond Time'),
('Desert Storm Chronicles');
✅ 6. Créer la table customer_review avec contrainte ON DELETE CASCADE
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES language(language_id),
    title VARCHAR(255),
    score INTEGER CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
➡️ Important :

ON DELETE CASCADE : si un film est supprimé de new_film, toutes ses critiques le seront automatiquement.
✅ 7. Ajouter 2 critiques
INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES 
(1, 1, 'A must-watch', 9, 'Absolutely brilliant and futuristic.'),
(2, 2, 'Mediocre at best', 5, 'The concept was good, but the execution lacked depth.');
➡️ Cela suppose que les langues 1 (ex: English) et 2 (ex: Italian) existent.

✅ 8. Supprimer un film ayant une critique
DELETE FROM new_film WHERE id = 1;
➡️ Résultat attendu :

Le film avec id = 1 est supprimé de new_film.
La critique associée dans customer_review est automatiquement supprimée grâce à ON DELETE CASCADE.
✅ Pour vérifier l’effet :
SELECT * FROM customer_review;
➡️ Il ne doit rester qu’une seule critique (celle du film id = 2).

##############################################################################################################################################################################
##############################################################################################################################################################################


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
