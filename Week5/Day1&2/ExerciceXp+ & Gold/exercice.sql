#Exercise 1 : Students Table

Instructions

For this exercise, you will have to find some requests on your own!



Create

Create a database called bootcamp.
Create a table called students.
Add the following columns:
id
last_name
first_name
birth_date
The id must be auto_incremented.
Make sure to choose the correct data type for each column.
To help, here is the data that you will have to insert. (How do we insert a date to a table?)


Here is the data:

id	first_name	last_name	birth_date
1	Marc	Benichou	02/11/1998
2	Yoan	Cohen	03/12/2010
3	Lea	Benichou	27/07/1987
4	Amelia	Dux	07/04/1996
5	David	Grez	14/06/2003
6	Omer	Simpson	03/10/1980


Insert

Insert the data seen above to the students table. Find the most efficient way to insert the data.
Insert your last_name, first_name and birth_date to the students table (Take a look at the id given).


Select

Fetch all of the data from the table.
Fetch all of the students first_names and last_names.
For the following questions, only fetch the first_names and last_names of the students.
Fetch the student which id is equal to 2.
Fetch the student whose last_name is Benichou AND first_name is Marc.
Fetch the students whose last_names are Benichou OR first_names are Marc.
Fetch the students whose first_names contain the letter a.
Fetch the students whose first_names start with the letter a.
Fetch the students whose first_names end with the letter a.
Fetch the students whose second to last letter of their first_names are a (Example: Leah).
Fetch the students whose id’s are equal to 1 AND 3 .

Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).




-- Create Database
CREATE DATABASE bootcamp;

-- Use the bootcamp database
USE bootcamp;

-- Create the students table
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE
);

-- Insert Data into the students table
INSERT INTO students (first_name, last_name, birth_date)
VALUES
('Marc', 'Benichou', '1998-11-02'),
('Yoan', 'Cohen', '2010-12-03'),
('Lea', 'Benichou', '1987-07-27'),
('Amelia', 'Dux', '1996-04-07'),
('David', 'Grez', '2003-06-14'),
('Omer', 'Simpson', '1980-10-03');

-- Fetch all data from the table
SELECT * FROM students;

-- Fetch only first_name and last_name
SELECT first_name, last_name FROM students;

-- Fetch the student with id = 2
SELECT * FROM students WHERE id = 2;

-- Fetch the student with last_name = 'Benichou' and first_name = 'Marc'
SELECT * FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- Fetch students whose last_name is 'Benichou' or first_name is 'Marc'
SELECT * FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- Fetch students whose first_name contains the letter 'a'
SELECT * FROM students WHERE first_name LIKE '%a%';

-- Fetch students whose first_name starts with the letter 'a'
SELECT * FROM students WHERE first_name LIKE 'a%';

-- Fetch students whose first_name ends with the letter 'a'
SELECT * FROM students WHERE first_name LIKE '%a';

-- Fetch students whose second to last letter of their first_name is 'a'
SELECT * FROM students WHERE SUBSTRING(first_name, LENGTH(first_name) - 1, 1) = 'a';

-- Fetch students whose id is equal to 1 AND 3
SELECT * FROM students WHERE id IN (1, 3);

-- Fetch students whose birth_date is equal to or after 2000-01-01
SELECT * FROM students WHERE birth_date >= '2000-01-01';



-- Fetch the first four students, ordered alphabetically by last_name
SELECT first_name, last_name, birth_date 
FROM students 
ORDER BY last_name 
LIMIT 4;

-- Fetch the details of the youngest student
SELECT first_name, last_name, birth_date 
FROM students 
ORDER BY birth_date DESC 
LIMIT 1;

-- Fetch three students, skipping the first two students
SELECT first_name, last_name, birth_date 
FROM students 
LIMIT 3 OFFSET 2;



