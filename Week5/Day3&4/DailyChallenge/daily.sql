

Instructions

In this puzzle you have to go through all the SQL queries and provide us the output of the requests before executing them (ie. make an assumption).
Then, execute them to make sure you were correct.



Queries

CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

SELECT * FROM FirstTab

CREATE TABLE SecondTab (
    id integer 
)

INSERT INTO SecondTab VALUES
(5),
(NULL)


SELECT * FROM SecondTab


DATA

Table1 – FirstTab
ID  Name
5   Pawan
6   Sharlee
7   Krish
NULL    Avtaar


Table2 – SecondTab
ID
5
NULL


Questions

Q1. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )


Q2. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )


Q3. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )


Q4. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )


##################################################################################################################################



✅ Données disponibles :
Table FirstTab

id	name
5	Pawan
6	Sharlee
7	Krish
NULL	Avtaar
Table SecondTab

id
5
NULL
🔍 Q1.

SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
🔸 Sous-requête :
SELECT id FROM SecondTab WHERE id IS NULL
→ Résultat : NULL
🔸 Clause WHERE :
WHERE ft.id NOT IN (NULL)
→ Cela renvoie UNKNOWN pour toutes les lignes avec id non NULL.
✅ Prédiction du résultat :
👉 0 lignes car NOT IN (NULL) est indéterminé (UNKNOWN) → aucune ligne ne passe le filtre.

🔍 Q2.

SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
🔸 Sous-requête :
SELECT id FROM SecondTab WHERE id = 5
→ Résultat : 5
Donc :

WHERE ft.id NOT IN (5)
→ ft.id ≠ 5
✅ Lignes valides :
6 → ok
7 → ok
NULL → ignorée (NULL in comparaison)
✅ Prédiction du résultat :
👉 2

🔍 Q3.

SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
🔸 Sous-requête :
SELECT id FROM SecondTab
→ Résultat : (5, NULL)
🔸 Clause WHERE :
WHERE ft.id NOT IN (5, NULL)
→ Cela rend toute comparaison UNKNOWN → aucune ligne ne passe
✅ Prédiction du résultat :
👉 0

🔍 Q4.

SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
🔸 Sous-requête :
SELECT id FROM SecondTab WHERE id IS NOT NULL
→ Résultat : 5
Donc :

WHERE ft.id NOT IN (5)
→ Même chose que Q2
✅ Prédiction du résultat :
👉 2

📊 RÉSUMÉ DES RÉPONSES PRÉDITES

Question	Résultat Prédit
Q1	0
Q2	2
Q3	0
Q4	2


