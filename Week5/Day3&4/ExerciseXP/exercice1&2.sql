Exercise 1 : Items And Customers

Instructions

We will work on the public database that we created yesterday.

Use SQL to get the following from the database:
All items, ordered by price (lowest to highest).
Items with a price above 80 (80 included), ordered by price (highest to lowest).
The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
All last names (no other columns!), in reverse alphabetical order (Z-A)

######################################################################################################################################

#All items, ordered by price (lowest to highest).

SELECT * 
FROM items
ORDER BY price ASC;


#Items with a price above 80 (80 included), ordered by price (highest to lowest).

SELECT * 
FROM items
WHERE price >= 80
ORDER BY price DESC;


#The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.

SELECT first_name, last_name 
FROM customers
ORDER BY first_name ASC
LIMIT 3;


#All last names (no other columns!), in reverse alphabetical order (Z-A)

SELECT last_name
FROM customers
ORDER BY last_name DESC;


#######################################################################################################################################################
#######################################################################################################################################################




Exercice 2 


We will use the newly installed dvdrental database.

In the dvdrental database write a query to select all the columns from the “customer” table.

Write a query to display the names (first_name, last_name) using an alias named “full_name”.

Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).

Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.

Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.

Write a query to retrieve all movie details where the movie id is either 15 or 150.

Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.

No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.

Write a query which will find the 10 cheapest movies.

Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
Bonus: Try to not use LIMIT.

Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).

You need to check your inventory. Write a query to get all the movies which are not in inventory.

Write a query to find which city is in which country.

Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.

####################################################################################################################################################################################################################################################################################

1. Select all columns from the “customer” table
SELECT * 
FROM customer;

2. Display first_name, last_name using alias "full_name"
SELECT first_name || ' ' || last_name AS full_name 
FROM customer;


3. Select unique create_date from customer table
SELECT DISTINCT create_date 
FROM customer;


4. All customer details in descending order by first_name
SELECT * 
FROM customer
ORDER BY first_name DESC;


5. Get film_id, title, description, release_year, rental_rate ordered by rental rate
SELECT film_id, title, description, release_year, rental_rate 
FROM film
ORDER BY rental_rate ASC;


6. Address and phone of customers living in Texas (from address table)
Assuming "district" column is present in address:

SELECT address, phone 
FROM address
WHERE district = 'Texas';


7. Movie details where film_id is 15 or 150
SELECT * 
FROM film
WHERE film_id IN (15, 150);


8. Check if your favorite movie exists (e.g. title = 'Inception')
Adapt title accordingly:

SELECT film_id, title, description, length, rental_rate 
FROM film
WHERE title = 'Inception';


9. Search by the first two letters of the title (e.g. 'In')
SELECT film_id, title, description, length, rental_rate 
FROM film
WHERE title ILIKE 'In%';


10. Find the 10 cheapest movies
SELECT * 
FROM film
ORDER BY rental_rate ASC
LIMIT 10;


11. Next 10 cheapest movies (rows 11-20), without LIMIT (PostgreSQL-specific using OFFSET)
SELECT * 
FROM film
ORDER BY rental_rate ASC
OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;
Ou avec subquery + ROW_NUMBER (standard SQL approach) :

SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (ORDER BY rental_rate ASC) AS row_num
    FROM film
) AS sub
WHERE row_num BETWEEN 11 AND 20;


12. Join customer and payment tables to get names, amount, and date
SELECT c.first_name, c.last_name, p.amount, p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY c.customer_id;


13. Movies not in inventory
SELECT * 
FROM film
WHERE film_id NOT IN (
    SELECT DISTINCT film_id 
    FROM inventory
);


14. Find which city is in which country
Join city and country tables:

SELECT ci.city, co.country
FROM city ci
JOIN country co ON ci.country_id = co.country_id;



BONUS: See how your sellers (staff) have been doing
SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, p.staff_id
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
ORDER BY p.staff_id;

