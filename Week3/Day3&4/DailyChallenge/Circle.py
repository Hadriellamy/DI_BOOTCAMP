#Instructions :
"""
The goal is to create a class that represents a simple circle.
A Circle can be defined by either specifying the radius or the diameter.
The user can query the circle for either its radius or diameter.

Other abilities of a Circle instance:

Compute the circle’s area
Print the attributes of the circle - use a dunder method
Be able to add two circles together, and return a new circle with the new radius - use a dunder method
Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
Be able to put them in a list and sort them
Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

##########################################################################################################################################################
Résumé des exigences de l'énoncé :

Définir un cercle :
Un cercle peut être défini par son rayon ou son diamètre.
La classe doit permettre de spécifier soit le rayon, soit le diamètre du cercle, mais pas les deux en même temps.
Vous devez pouvoir récupérer le rayon ou le diamètre d'un cercle via des méthodes.
Calculer l'aire du cercle :
La classe doit être capable de calculer l'aire du cercle, en utilisant la formule de l'aire d'un cercle :
Aire
=
π
×
rayon
2
Aire=π×rayon 
2
 
Impression des attributs du cercle :
Implémenter un dunder method (méthode spéciale en Python), tel que __str__() ou __repr__(), pour afficher de manière lisible les informations du cercle (par exemple, rayon ou diamètre).
Ajouter deux cercles :
Implémenter la méthode d’addition via le dunder method __add__(). Lorsque deux cercles sont additionnés, leur rayon doit être additionné pour créer un nouveau cercle avec ce rayon.
Comparer deux cercles pour savoir lequel est plus grand :
Implémenter la méthode __gt__() pour comparer les cercles et retourner un booléen (True ou False) selon que l'un est plus grand que l'autre (comparaison par rapport au rayon).
Comparer deux cercles pour savoir s'ils sont égaux :
Implémenter la méthode __eq__() pour comparer deux cercles et savoir si leurs rayons sont égaux.
Placer les cercles dans une liste et les trier :
Vous pouvez trier une liste de cercles en fonction de leur rayon en utilisant les méthodes de comparaison implémentées.
Bonus :
Si vous le souhaitez, vous pouvez utiliser le module Turtle pour dessiner les cercles triés, mais ce n'est pas obligatoire.


"""


import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        # Si le rayon est fourni, on l'utilise, sinon on utilise le diamètre pour calculer le rayon.
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Un cercle doit être défini avec un rayon ou un diamètre.")
    
    # Calcul de l'aire du cercle
    def area(self):
        return math.pi * (self.radius ** 2)
    
    # Affichage de l'objet (par exemple, le rayon du cercle)
    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
    # Additionner deux cercles (additionner leurs rayons)
    def __add__(self, other):
        if isinstance(other, Circle):
            new_radius = self.radius + other.radius
            return Circle(radius=new_radius)
        return NotImplemented
    
    # Comparer si le premier cercle est plus grand que le second
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented
    
    # Comparer si les deux cercles sont égaux (rayon identique)
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented




# Exemple de cercles à trier
circle1 = Circle(radius=3)
circle2 = Circle(radius=5)
circle3 = Circle(radius=2)

# Liste de cercles
circles = [circle1, circle2, circle3]

# Trier les cercles par rayon
sorted_circles = sorted(circles, key=lambda x: x.radius)

# Afficher les cercles triés
for circle in sorted_circles:
    print(circle)



#Bonus 
"""
import turtle

def draw_circle(radius):
    turtle.penup()
    turtle.goto(0, -radius)  # Déplace la tortue au bas du cercle
    turtle.pendown()
    turtle.circle(radius)  # Dessine un cercle de rayon spécifié

# Initialisation de la fenêtre Turtle
turtle.speed(1)

# Dessiner les cercles triés
for circle in sorted_circles:
    draw_circle(circle.radius)

turtle.done()  # Lancer le dessin

"""
