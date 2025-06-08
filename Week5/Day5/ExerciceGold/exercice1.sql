
Exercise 1 : DVD Rentals

Instructions

Get a list of all rentals which are out (have not been returned). How do we identify these films in the database?

Get a list of all customers who have not returned their rentals. Make sure to group your results.

Get a list of all the Action films with Joe Swank.
Before you start, could there be a shortcut to getting this information? Maybe a view?

#########################################################################################################################################

✅ 1. Liste de toutes les locations encore en cours (films non retournés)
➡️ Un film est encore loué s’il est dans la table rental et que la colonne return_date est NULL.

SELECT *
FROM rental
WHERE return_date IS NULL;
✅ 2. Liste de tous les clients qui n’ont pas retourné leurs films
➡️ On sélectionne les clients associés à des locations sans date de retour, et on groupe pour éviter les doublons.

SELECT c.customer_id, c.first_name, c.last_name, COUNT(*) AS outstanding_rentals
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
WHERE r.return_date IS NULL
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY outstanding_rentals DESC;
✅ 3. Liste de tous les films d’action avec Joe Swank
Étapes nécessaires :

Trouver l’acteur Joe Swank
Vérifier s’il existe une vue utile (ex: film_list, actor_info, nicer_but_slower_film_list, etc.)
Chercher les films du genre Action avec cet acteur
✅ Requête complète (sans vue) :

SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE a.first_name = 'Joe' AND a.last_name = 'Swank'
AND c.name = 'Action';
❗️Alternative : utiliser une vue ?
➡️ Vérifie si la base DVD Rental contient une vue nommée film_list :

SELECT * FROM film_list LIMIT 5;
Mais film_list ne contient pas les acteurs, donc pas de raccourci direct avec cette vue pour cette question.

✅ Résumé des réponses :

	
Question : Films non retournés	
Requête principale : SELECT * FROM rental WHERE return_date IS NULL


Question : Clients n’ayant pas retourné leurs films	
Requête principale: Requête avec JOIN et GROUP BY sur customer et rental


Question: Films daction avec Joe Swank	
Requête principale: Requête avec JOIN sur film_actor, actor, film_category, category