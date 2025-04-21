-- Instructions

In this exercise we will be using the actors table from todays lesson.
1. Count how many actors are in the table.
2. Try to add a new actor with some blank fields. What do you think the outcome will be ?


-- Solution 

1. Count how many actors are in the table
To count how many actors are in the table, we can use the COUNT() function in SQL:

SELECT COUNT(*) FROM actors;
This query will return the total number of records (actors) in the actors table.

2. Try to add a new actor with some blank fields
To add a new actor with blank fields, the outcome depends on how the actors table is structured. Specifically:

If NOT NULL constraints are set on any of the columns (such as first_name, last_name, etc.), attempting to insert a record with blank fields for those columns will result in an error.
If the column allows NULL values or has a default value, you can insert blank fields, and the columns without data will either be set to NULL or their default values.
Lets say we try to insert a new actor with some blank fields:

INSERT INTO actors (first_name, last_name, birth_date)
VALUES ('', '', NULL);
Possible outcomes:

If the table enforces NOT NULL constraints on first_name, last_name, or birth_date, the query will fail with an error, indicating that these fields cannot be NULL or empty.
If those fields allow blank or NULL values, the insertion will succeed, but you may end up with rows where first_name and last_name are empty, and birth_date is NULL.
