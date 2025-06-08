
Exercise 2 – Happy Halloween

Instructions

There is a zombie plague approaching! The DVD rental company is offering to lend all of its DVDs to the local shelters, so that the citizens can watch the movies together in the shelters until the zombies are destroyed by the armed forces. Prepare tables with the following data:

How many stores there are, and in which city and country they are located.

How many hours of viewing time there are in total in each store – in other words, the sum of the length of every inventory item in each store.

Make sure to exclude any inventory items which are not yet returned. (Yes, even in the time of zombies there are people who do not return their DVDs)

A list of all customers in the cities where the stores are located.

A list of all customers in the countries where the stores are located.

Some people will be frightened by watching scary movies while zombies walk the streets. Create a ‘safe list’ of all movies which do not include the ‘Horror’ category, or contain the words ‘beast’, ‘monster’, ‘ghost’, ‘dead’, ‘zombie’, or ‘undead’ in their titles or descriptions… Get the sum of their viewing time (length).
Hint : use the CHECK contraint

For both the ‘general’ and the ‘safe’ lists above, also calculate the time in hours and days (not just minutes).


###################################################################################################################################################################################################################################################################################################################################################


🎃 1. Nombre de magasins + leur ville et pays

SELECT s.store_id, ci.city, co.country
FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id;
🎬 2. Temps total de visionnage par magasin (exclure les DVD non retournés)

Étapes :

Lier les inventaires (inventory) aux films (film) pour obtenir leur length
Exclure les inventaires loués mais non retournés
Regrouper par store
SELECT i.store_id,
       SUM(f.length) AS total_minutes,
       ROUND(SUM(f.length) / 60.0, 2) AS total_hours,
       ROUND(SUM(f.length) / 1440.0, 2) AS total_days
FROM inventory i
JOIN film f ON i.film_id = f.film_id
LEFT JOIN rental r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NOT NULL OR r.rental_id IS NULL
GROUP BY i.store_id;
🧍 3. Tous les clients vivant dans une ville où il y a un magasin

SELECT DISTINCT c.customer_id, c.first_name, c.last_name, ci.city
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
WHERE ci.city_id IN (
    SELECT a.city_id
    FROM store s
    JOIN address a ON s.address_id = a.address_id
);
🌍 4. Tous les clients dans les pays où il y a un magasin

SELECT DISTINCT c.customer_id, c.first_name, c.last_name, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE co.country_id IN (
    SELECT ci.country_id
    FROM store s
    JOIN address a ON s.address_id = a.address_id
    JOIN city ci ON a.city_id = ci.city_id
);
🛡️ 5. Liste "Safe" – Films sans horreur et sans mots effrayants

Mots à exclure : beast, monster, ghost, dead, zombie, undead

Étape 1 : Exclure les films de la catégorie "Horror"
SELECT f.film_id, f.title, f.description, f.length
FROM film f
WHERE f.film_id NOT IN (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Horror'
)
AND (
    LOWER(f.title) NOT LIKE '%beast%' AND
    LOWER(f.title) NOT LIKE '%monster%' AND
    LOWER(f.title) NOT LIKE '%ghost%' AND
    LOWER(f.title) NOT LIKE '%dead%' AND
    LOWER(f.title) NOT LIKE '%zombie%' AND
    LOWER(f.title) NOT LIKE '%undead%' AND
    LOWER(f.description) NOT LIKE '%beast%' AND
    LOWER(f.description) NOT LIKE '%monster%' AND
    LOWER(f.description) NOT LIKE '%ghost%' AND
    LOWER(f.description) NOT LIKE '%dead%' AND
    LOWER(f.description) NOT LIKE '%zombie%' AND
    LOWER(f.description) NOT LIKE '%undead%'
);
Étape 2 : Somme du temps de visionnage des films "safe"
SELECT 
    SUM(length) AS safe_total_minutes,
    ROUND(SUM(length) / 60.0, 2) AS safe_total_hours,
    ROUND(SUM(length) / 1440.0, 2) AS safe_total_days
FROM film f
WHERE f.film_id NOT IN (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Horror'
)
AND (
    LOWER(f.title) NOT LIKE '%beast%' AND
    LOWER(f.title) NOT LIKE '%monster%' AND
    LOWER(f.title) NOT LIKE '%ghost%' AND
    LOWER(f.title) NOT LIKE '%dead%' AND
    LOWER(f.title) NOT LIKE '%zombie%' AND
    LOWER(f.title) NOT LIKE '%undead%' AND
    LOWER(f.description) NOT LIKE '%beast%' AND
    LOWER(f.description) NOT LIKE '%monster%' AND
    LOWER(f.description) NOT LIKE '%ghost%' AND
    LOWER(f.description) NOT LIKE '%dead%' AND
    LOWER(f.description) NOT LIKE '%zombie%' AND
    LOWER(f.description) NOT LIKE '%undead%'
);
🧾 Résumé des conversions :

Requête	Description
Requête 1	Stores + villes + pays
Requête 2	Durée totale de visionnage par magasin (DVD retournés uniquement)
Requête 3	Clients dans les villes avec magasins
Requête 4	Clients dans les pays avec magasins
Requête 5	Liste des films "safe" sans horreur ni termes effrayants
Requête 6	Total du temps de visionnage des films "safe"