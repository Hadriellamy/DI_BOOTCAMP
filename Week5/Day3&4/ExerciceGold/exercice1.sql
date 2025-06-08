
Exercise 1: DVD Rental

Instructions

You were hired to babysit your cousin and you want to find a few movies that he can watch with you.
Find out how many films there are for each rating.

Get a list of all the movies that have a rating of G or PG-13.
Filter this list further: look for only movies that are under 2 hours long, and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.

Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE.
Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).

##############################################################################################################################################################################

✅ 1. Combien de films pour chaque rating ?
SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating
ORDER BY rating;

✅ 2. Liste des films avec un rating de G ou PG-13
SELECT *
FROM film
WHERE rating IN ('G', 'PG-13');


✅ 3. Filtrer les films sous 2h et avec un prix de location < 3.00, et trier par titre
PostgreSQL considère la longueur des films en minutes (length), donc < 120.

SELECT title, length, rental_rate, rating
FROM film
WHERE rating IN ('G', 'PG-13')
  AND length < 120
  AND rental_rate < 3.00
ORDER BY title ASC;

✅ 4. Modifier les détails d’un client pour mettre les tiens (exemple : customer_id = 1)
Adapte les champs selon tes infos :

UPDATE customer
SET first_name = 'John',
    last_name = 'Doe',
    email = 'john.doe@example.com'
WHERE customer_id = 1;


✅ 5. Modifier l’adresse de ce client
Il faut d'abord récupérer l'address_id du client :

SELECT address_id
FROM customer
WHERE customer_id = 1;
Supposons que l’adresse ID est 5, on la modifie ainsi :

UPDATE address
SET address = '1234 Maple Street',
    address2 = 'Apt 9B',
    district = 'New York',
    postal_code = '10001',
    phone = '123-456-7890'
WHERE address_id = 5;
