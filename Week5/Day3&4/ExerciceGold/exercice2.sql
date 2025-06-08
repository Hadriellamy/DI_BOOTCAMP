
Exercise 2: Students Table

Instructions

Continuation of the Day1 Exercise XPGold : students table



Update

‘Lea Benichou’ and ‘Marc Benichou’ are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
Change the last_name of David from ‘Grez’ to ‘Guez’.


Delete

Delete the student named ‘Lea Benichou’ from the table.


Count

Count how many students are in the table.
Count how many students were born after 1/01/2000.


Insert / Alter

Add a column to the student table called math_grade.
Add 80 to the student which id is 1.
Add 90 to the students which have ids of 2 or 4.
Add 40 to the student which id is 6.
Count how many students have a grade bigger than 83
Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although he received 2 different grades because he retook the math exam.
Bonus: Count how many grades each student has.
Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
Tip : Use an alias called total_grade to fetch the grades.
Hint : Use GROUP BY.
SUM

Find the sum of all the students grades.


##########################################################################################################################################################################################################################################


🔄 UPDATE
1. Modifier les dates de naissance des jumeaux :

UPDATE students
SET birth_date = '1998-11-02'
WHERE (first_name = 'Lea' AND last_name = 'Benichou')
   OR (first_name = 'Marc' AND last_name = 'Benichou');
2. Corriger le nom de famille de David Grez :

UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David' AND last_name = 'Grez';
🗑️ DELETE
Supprimer Lea Benichou :

DELETE FROM students
WHERE first_name = 'Lea' AND last_name = 'Benichou';
🔢 COUNT
1. Nombre total d'étudiants :

SELECT COUNT(*) AS total_students
FROM students;
2. Nombre d’étudiants nés après le 1er janvier 2000 :

SELECT COUNT(*) AS born_after_2000
FROM students
WHERE birth_date > '2000-01-01';
➕ INSERT / ALTER
1. Ajouter une colonne math_grade :

ALTER TABLE students ADD COLUMN math_grade INTEGER;
2. Ajouter les notes :

-- Pour l'étudiant avec id = 1
UPDATE students
SET math_grade = 80
WHERE id = 1;

-- Pour les étudiants avec id = 2 ou 4
UPDATE students
SET math_grade = 90
WHERE id IN (2, 4);

-- Pour l'étudiant avec id = 6
UPDATE students
SET math_grade = 40
WHERE id = 6;
3. Compter les étudiants ayant une note > 83 :

SELECT COUNT(*) AS grade_above_83
FROM students
WHERE math_grade > 83;
4. Ajouter un deuxième Omer Simpson (même date de naissance qu’un autre étudiant) :

Supposons qu’il existe déjà un Omer Simpson dans la table :

-- Récupérer sa date de naissance
SELECT birth_date FROM students
WHERE first_name = 'Omer' AND last_name = 'Simpson'
LIMIT 1;
Puis :

INSERT INTO students (first_name, last_name, birth_date, math_grade)
VALUES ('Omer', 'Simpson', 'YYYY-MM-DD', 70); -- Remplace 'YYYY-MM-DD' par la bonne date
Si tu ne connais pas sa date, tu peux la recopier avec une sous-requête :

INSERT INTO students (first_name, last_name, birth_date, math_grade)
SELECT 'Omer', 'Simpson', birth_date, 70
FROM students
WHERE first_name = 'Omer' AND last_name = 'Simpson'
LIMIT 1;
⭐ BONUS : compter combien de notes chaque étudiant a
Ici on suppose que chaque ligne = une note. Donc il faut regrouper par prénom + nom :

SELECT first_name, last_name, COUNT(math_grade) AS total_grade
FROM students
GROUP BY first_name, last_name
ORDER BY total_grade DESC;
➕ SUM des notes
SELECT SUM(math_grade) AS total_math_score
FROM students;
