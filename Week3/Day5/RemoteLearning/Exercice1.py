#Exercice
"""
Part 1

You will have to create two classes:
Human
Queue


Human

Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), priority (bool) and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.

This class has no methods.



Queue

Represents a queue of humans waiting for their vaccine.
It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.

This class is useful to manage who will get vaccinated in priority. It has the following methods:

add_person(self, person) : Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the list (at index 0) before every other.

find_in_queue(self, person) : Returns the index of a human in the queue.

swap(self, person1, person2): Swaps person1 with person2.

get_next(self) : Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.

get_next_blood_type(self, blood_type) : Returns the first human with this specific blood type.

sort_by_age(self) : Sorts the queue
first the priority people
then, the older people
then the younger people
Every human returned by get_next and get_next_blood_type is removed from the list.
Those functions return None if the list is empty (ie. no one in the list).

Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.



Part 2

Human

Create an attribute family for the Human class.

Initialized as empty, family is a list of all the humans that are living in the same house with this human.
Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.



Queue

Add the rearrange_queue(self) method to the Queue class, so that there won’t be two members of the same family one after the other in the line.
##############################################################################################################################################################


🧠 PARTIE 1 — Objectif

Créer 2 classes :

1. Human
Un être humain avec les attributs suivants :

id_number (str)
name (str)
age (int)
priority (bool) → personnes prioritaires
blood_type (str) → "A", "B", "AB", "O"
⚠️ Pas de méthode pour cette classe (à part dans la Partie 2).

2. Queue
Une file d’attente de personnes à vacciner.

Attribut : humans → une liste des personnes dans la file (initialement vide).
Objectif : gérer les priorités de vaccination.
📌 Méthodes à implémenter
✅ add_person(self, person)

Ajoute une personne à la liste.
Si la personne a plus de 60 ans ou est prioritaire, elle est ajoutée au début.
Sinon à la fin.
Bonus : Ne pas utiliser insert, index, etc.
✅ find_in_queue(self, person)

Retourne l’indice de la personne dans la file.
✅ swap(self, person1, person2)

Échange la position de deux personnes.
✅ get_next(self)

Renvoie et retire la personne en position 0 (prochaine à se faire vacciner).
Si la file est vide → retourne None.
✅ get_next_blood_type(self, blood_type)

Renvoie et retire la première personne avec le bon groupe sanguin.
Sinon None.
✅ sort_by_age(self)

Tri personnalisé :

Les prioritaires
Les personnes âgées
Les autres
On ne peut pas utiliser sort ni sorted.


"""
class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        if person not in self.family:
            self.family.append(person)
        if self not in person.family:
            person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        new_list = []
        if person.age > 60 or person.priority:
            new_list.append(person)
            for h in self.humans:
                new_list.append(h)
        else:
            for h in self.humans:
                new_list.append(h)
            new_list.append(person)
        self.humans = new_list

    def find_in_queue(self, person):
        for i in range(len(self.humans)):
            if self.humans[i] == person:
                return i
        return -1

    def swap(self, person1, person2):
        i1 = self.find_in_queue(person1)
        i2 = self.find_in_queue(person2)
        if i1 != -1 and i2 != -1:
            self.humans[i1], self.humans[i2] = self.humans[i2], self.humans[i1]

    def get_next(self):
        if len(self.humans) == 0:
            return None
        next_person = self.humans[0]
        self.humans = self.humans[1:]
        return next_person

    def get_next_blood_type(self, blood_type):
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                person = self.humans[i]
                self.humans = self.humans[:i] + self.humans[i+1:]
                return person
        return None

    def sort_by_age(self):
        priority = []
        aged = []
        young = []

        for h in self.humans:
            if h.priority:
                priority.append(h)
            elif h.age > 60:
                aged.append(h)
            else:
                young.append(h)

        self.humans = priority + aged + young

    def rearrange_queue(self):
        i = 0
        while i < len(self.humans) - 1:
            person1 = self.humans[i]
            person2 = self.humans[i + 1]
            if person2 in person1.family:
                # Cherche une personne plus loin qui n'est pas dans la famille
                found = False
                for j in range(i + 2, len(self.humans)):
                    if self.humans[j] not in person1.family and self.humans[j] not in person2.family:
                        # Échange person2 avec cette personne
                        self.humans[i + 1], self.humans[j] = self.humans[j], self.humans[i + 1]
                        found = True
                        break
                if not found:
                    i += 1  # rien à faire, on avance
            else:
                i += 1

#Explication


"""
✅ Ce code :
Gère les ajouts prioritaires dans la file.
Peut retrouver une personne, les échanger, les sortir selon leur ordre ou leur groupe sanguin.
Trie selon la logique de priorité/âge.
Et surtout : évite que des membres de la même famille soient côte à côte.
"""
