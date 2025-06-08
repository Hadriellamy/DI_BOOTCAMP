
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