#Exercise 3: Working On A Paragraph
"""
Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
Paste it to your code, and store it in a variable.
Let’s analyze the paragraph. Print out a nicely formatted message saying:
How many characters it contains (this one is easy…).
How many sentences it contains.
How many words it contains.
How many unique words it contains.
Bonus: How many non-whitespace characters it contains.
Bonus: The average amount of words per sentence in the paragraph.
Bonus: the amount of non-unique words in the paragraph.

"""
import re

# On peut remplacer ce paragraphe par celui que tu souhaites analyser.
paragraph = """La technologie change le monde à une vitesse fulgurante. Chaque jour, de nouvelles innovations transforment notre façon de vivre, de travailler et de communiquer. Cependant, malgré ces progrès, il est important de se rappeler l'importance des relations humaines et de la compassion."""

# 1. Nombre total de caractères (espaces inclus)
total_characters = len(paragraph)

# 2. Nombre de phrases
# On divise le paragraphe à l'aide des signes de ponctuation finaux (. ! ?) et on filtre les chaînes vides.
sentences = [s.strip() for s in re.split(r'[.!?]', paragraph) if s.strip() != ""]
num_sentences = len(sentences)

# 3. Nombre de mots
# On utilise une expression régulière pour extraire les mots (en ignorant la ponctuation).
words = re.findall(r'\b\w+\b', paragraph)
num_words = len(words)

# 4. Nombre de mots uniques (en ignorant la casse)
unique_words = set(word.lower() for word in words)
num_unique_words = len(unique_words)

# Bonus A: Nombre de caractères non blancs (sans espaces, tabulations, etc.)
non_whitespace_chars = len([c for c in paragraph if not c.isspace()])

# Bonus B: Moyenne de mots par phrase
avg_words_per_sentence = num_words / num_sentences if num_sentences > 0 else 0

# Bonus C: Nombre de mots non uniques (total des mots - mots uniques)
non_unique_words = num_words - num_unique_words

# Affichage des résultats
print("Analyse du paragraphe :")
print("-------------------------------------------------")
print(f"Nombre total de caractères (espaces inclus) : {total_characters}")
print(f"Nombre de phrases : {num_sentences}")
print(f"Nombre total de mots : {num_words}")
print(f"Nombre de mots uniques : {num_unique_words}")
print(f"Nombre de caractères non blancs : {non_whitespace_chars}")
print(f"Moyenne de mots par phrase : {avg_words_per_sentence:.2f}")
print(f"Nombre de mots non uniques : {non_unique_words}")


#Explications 
"""
Total de caractères :
On utilise len(paragraph) pour obtenir le nombre de caractères dans le paragraphe, espaces inclus.
Nombre de phrases :
On utilise re.split(r'[.!?]', paragraph) pour découper le paragraphe à chaque ponctuation de fin de phrase, puis on filtre les éléments vides.
Nombre de mots :
L'expression régulière \b\w+\b permet d'extraire tous les mots en ignorant la ponctuation.
Mots uniques :
En passant chaque mot en minuscule (avec word.lower()), on obtient un ensemble (set) qui ne contient que des valeurs uniques.
Caractères non blancs :
On parcourt chaque caractère et on compte ceux qui ne sont pas des espaces ou autres caractères blancs.
Moyenne de mots par phrase :
Calculée en divisant le nombre total de mots par le nombre de phrases.
Mots non uniques :
C'est la différence entre le nombre total de mots et le nombre de mots uniques.

"""
