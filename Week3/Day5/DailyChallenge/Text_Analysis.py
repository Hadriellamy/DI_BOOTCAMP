#Instructions :
"""
The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.



Part I

First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

Create a class called Text that takes a string as an argument and store the text in a attribute.
Hint: You need to manually copy-paste the text, straight into the code

Implement the following methods:
a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
a method that returns the most common word in the text.
a method that returns a list of all the unique words in the text.


Part II

Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

Implement a classmethod that returns a Text instance but with a text file:

    >>> Text.from_file('the_stranger.txt')
Hint: You need to open and read the text from the text file.


Now, use the provided the_stranger.txt file and try using the class you created above.



Bonus:

Create a class called TextModification that inherits from Text.

Implement the following methods:
a method that returns the text without any punctuation.
a method that returns the text without any english stop-words (check out what this is !!).
a method that returns the text without any special characters.
Note: Instead of creating a child class, you could also implements those methods as static methods in the Text class.

Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)


###################################################################
Explication du Code
Classe Text :
__init__(self, text) : Le constructeur prend un texte, le transforme en minuscules, enlève la ponctuation, et le découpe en mots.
word_frequency(self, word) : Retourne la fréquence d'un mot dans le texte.
most_common_word(self) : Trouve le mot le plus fréquent dans le texte.
unique_words(self) : Retourne une liste des mots uniques du texte.
from_file(cls, filename) : Une méthode de classe qui charge un texte à partir d'un fichier.
Classe TextModification (héritée de Text) :
remove_punctuation(self) : Supprime toute la ponctuation du texte.
remove_stop_words(self) : Supprime les mots vides (stop words) du texte.
remove_special_characters(self) : Supprime les caractères spéciaux du texte.
Utilisation
Analyse d'un texte simple : L'exemple dans le code montre comment utiliser la classe Text pour analyser un texte simple. Vous pouvez modifier la variable text pour analyser un autre texte.
Analyse d'un fichier externe : Vous pouvez utiliser la méthode from_file pour charger un fichier texte et analyser son contenu.
Modification du texte : La classe TextModification offre des méthodes pour supprimer la ponctuation, les mots vides et les caractères spéciaux.
Bonus : Test avec le fichier the_stranger.txt
Si vous avez le fichier the_stranger.txt, vous pouvez l'utiliser avec la méthode Text.from_file('the_stranger.txt') pour analyser ce texte. Vous pouvez également appliquer les méthodes de modification du texte à ce fichier.


"""


import string
from collections import Counter

# Classe de base pour l'analyse de texte
class Text:
    def __init__(self, text):
        self.text = text
        self.words = self._process_text(text)
    
    def _process_text(self, text):
        # Retirer la ponctuation et convertir en minuscule
        text = text.lower()
        text = text.translate(str.maketrans("", "", string.punctuation))
        words = text.split()
        return words
    
    # Méthode pour obtenir la fréquence d'un mot
    def word_frequency(self, word):
        word = word.lower()
        return self.words.count(word) if word in self.words else None
    
    # Méthode pour obtenir le mot le plus fréquent
    def most_common_word(self):
        word_counts = Counter(self.words)
        most_common = word_counts.most_common(1)
        return most_common[0] if most_common else None
    
    # Méthode pour obtenir une liste de tous les mots uniques
    def unique_words(self):
        return list(set(self.words))
    
    # Méthode de classe pour charger un texte depuis un fichier
    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename, 'r') as file:
                text = file.read()
            return cls(text)
        except FileNotFoundError:
            return None

# Classe pour modifier le texte en héritant de Text
class TextModification(Text):
    
    def remove_punctuation(self):
        # Retirer la ponctuation
        return self.text.translate(str.maketrans("", "", string.punctuation))
    
    def remove_stop_words(self):
        stop_words = set([
            "i", "me", "my", "myself", "we", "our", "ours", "ourselves", 
            "you", "your", "yours", "yourself", "yourselves", "he", "him", 
            "his", "himself", "she", "her", "hers", "herself", "it", "its", 
            "itself", "they", "them", "their", "theirs", "themselves", 
            "what", "which", "who", "whom", "this", "that", "these", "those", 
            "am", "is", "are", "was", "were", "be", "been", "being", "have", 
            "has", "had", "having", "do", "does", "did", "doing", "a", "an", 
            "the", "and", "but", "if", "or", "because", "as", "until", "while", 
            "of", "at", "by", "for", "with", "about", "against", "between", 
            "into", "through", "during", "before", "after", "above", "below", 
            "to", "from", "up", "down", "in", "out", "on", "off", "over", 
            "under", "again", "further", "then", "once", "here", "there", 
            "when", "where", "why", "how", "all", "any", "both", "each", 
            "few", "more", "most", "other", "some", "such", "no", "nor", 
            "not", "only", "own", "same", "so", "than", "too", "very", 
            "s", "t", "can", "will", "just", "don", "should", "now", 
            "d", "ll", "m", "o", "re", "ve", "y", "ain", "aren", "couldn", 
            "didn", "doesn", "hadn", "hasn", "haven", "isn", "ma", "mightn", 
            "mustn", "needn", "shan", "shouldn", "wasn", "weren", "won", "wouldn"
        ])
        
        words = [word for word in self.words if word not in stop_words]
        return ' '.join(words)
    
    def remove_special_characters(self):
        # Retirer les caractères spéciaux
        return ''.join(e for e in self.text if e.isalnum() or e.isspace())

# Exemple d'utilisation
if __name__ == "__main__":
    # Part I : Analyse d'un texte simple
    text = "A good book would sometimes cost as much as a good house."
    my_text = Text(text)

    print("Word Frequency (good):", my_text.word_frequency("good"))
    print("Most Common Word:", my_text.most_common_word())
    print("Unique Words:", my_text.unique_words())


    # Part II : Analyse d'un texte provenant d'un fichier externe
    #Test
    text_file = Text.from_file('the_stranger.txt')
    if text_file:
        print("Most Common Word in the File:", text_file.most_common_word())



    # Bonus : Modification du texte
    text_mod = TextModification(text)
    print("Text without Punctuation:", text_mod.remove_punctuation())
    print("Text without Stop Words:", text_mod.remove_stop_words())
    print("Text without Special Characters:", text_mod.remove_special_characters())


