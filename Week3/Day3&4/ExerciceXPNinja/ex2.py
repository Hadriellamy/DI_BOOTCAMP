#Exercise 2: In The Quantum Realm
"""
Instructions

Write a class called QuantumParticle and implement the following:
The attributes - The particle has an initial position (x), momentum (y) and spin (p)

The method position() - Position measurement: generate a random position (integer between 1 and 10,000)

The method momentum() - Momentum measurement: generate a random momentum (float - a number between 0 and 1)

The method spin() - Spin measurement: can randomly be 1/2 or -1/2

Create a method that implements a disturbance. A disturbance occurs each time a measurement is made (e.g. one of the measurements method is called). Disturbance changes the position and the momentum of the particle (randomly generated) and then prints ‘Quantum Interferences!!’

Implement a meaningful representation of the particle (repr)

Quantum Entanglement: two particle can be entangled, meaning that if I measure the spin of one of them the second one is automatically set to the opposite value. A quantum particle can only be entangled to another quantum particle (check that when you run the method !!)
Modify as you see fit the attributes and methods of your class to fit the previous definition
When two particles are entangled print: ‘Spooky Action at a Distance !!’
>>>p1 = QuantumParticle(x=1,p=5.0)
>>>p2 = QuantumParticle(x=2,p=5.0)
>>>p1.entangle(p2)
>>>'Particle p1 is now in quantum entanglement with Particle p2'
>>>p1 = QuantumParticle()
>>>p2 = QuantumParticle()
>>>p1.entangle(p2)
>>>'Spooky Action at a Distance'

"""


#💡 Objectif :
"""
Créer une classe QuantumParticle avec :

Des attributs : position x, quantité de mouvement y (momentum), spin p.
Des méthodes de mesure : position(), momentum(), spin(), avec génération aléatoire.
Une méthode de perturbation (_disturbance) déclenchée à chaque mesure.
Une méthode d’intrication quantique (entangle) entre deux particules.
Une représentation textuelle claire avec __repr__.

"""


import random

class QuantumParticle:
    def __init__(self, x=None, y=None, p=None):
        self.x = x if x is not None else random.randint(1, 10000)
        self.y = y if y is not None else random.uniform(0, 1)
        self.p = p if p is not None else random.choice([0.5, -0.5])
        self.entangled_with = None

    def _disturbance(self):
        self.x = random.randint(1, 10000)
        self.y = random.uniform(0, 1)
        print('Quantum Interferences!!')

    def position(self):
        self._disturbance()
        return self.x

    def momentum(self):
        self._disturbance()
        return self.y

    def spin(self):
        self._disturbance()
        if self.entangled_with:
            # Réglage automatique du spin de la particule intriquée
            opposite_spin = -self.p
            self.entangled_with.p = opposite_spin
        return self.p

    def entangle(self, other):
        if not isinstance(other, QuantumParticle):
            print("Impossible d'intriquer avec un objet non-quantique.")
            return
        self.entangled_with = other
        other.entangled_with = self
        # Lors de l'intrication, on force les spins opposés
        if self.p == other.p:
            other.p = -self.p
        print("Spooky Action at a Distance !!")
        print(f"Particle {id(self)} is now in quantum entanglement with Particle {id(other)}")

    def __repr__(self):
        return (f"<QuantumParticle | Position: {self.x}, Momentum: {self.y:.4f}, "
                f"Spin: {self.p}, Entangled: {id(self.entangled_with) if self.entangled_with else None}>")


#Test

# Création de deux particules
p1 = QuantumParticle(x=1, p=0.5)
p2 = QuantumParticle(x=2, p=0.5)

# Intrication quantique
p1.entangle(p2)

# Mesure du spin (automatiquement synchronisé avec la particule liée)
print(f"Spin p1: {p1.spin()}")
print(f"Spin p2: {p2.spin()}")  # devrait être -p1.spin()

# Affichage des particules
print(p1)
print(p2)

# Mesure de la position avec perturbation
print("Nouvelle position p1:", p1.position())
print("Nouveau momentum p1:", p1.momentum())



 
#📌 Résumé :
"""
position() : génère une nouvelle position aléatoire entre 1 et 10 000 + perturbe le système.
momentum() : génère un float aléatoire entre 0 et 1 + perturbe le système.
spin() : génère ±0.5 aléatoirement, met à jour la particule entremêlée si besoin.
entangle() : lie deux particules et force leurs spins à être opposés.
repr : affiche l’état complet de la particule.
"""

