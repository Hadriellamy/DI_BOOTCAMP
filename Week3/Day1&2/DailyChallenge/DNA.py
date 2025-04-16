#Instructions :
"""
This challenge is about Biology that will put emphasis on your knowledge of classes, inheritance and polymorphism.

Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
A Gene is a single value 0 or 1, it can mutate (flip).
A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
A DNA is a series of 10 chromosomes, and it can also mutate the same way Chromosomes can mutate.

Implement these classes as you see fit.

Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.

Instantiate a number of Organism and let them mutate until one gets to a DNA which is only made of 1s. Then stop and record the number of generations (iterations) it took.
Write your results in you personal biology research notebook and tell us your conclusion :).

"""

import random

class Gene:
    def __init__(self, value=None):
        self.value = value if value is not None else random.choice([0, 1])

    def mutate(self):
        self.value = 1 - self.value  # Flip: 0 → 1, 1 → 0

    def __repr__(self):
        return str(self.value)


class Chromosome:
    def __init__(self, genes=None):
        self.genes = genes if genes else [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:  # 50% chance to flip
                gene.mutate()

    def is_all_ones(self):
        return all(g.value == 1 for g in self.genes)

    def __repr__(self):
        return ''.join(str(g) for g in self.genes)


class DNA:
    def __init__(self, chromosomes=None):
        self.chromosomes = chromosomes if chromosomes else [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()

    def is_all_ones(self):
        return all(chromosome.is_all_ones() for chromosome in self.chromosomes)

    def __repr__(self):
        return '\n'.join(str(c) for c in self.chromosomes)


class Organism:
    def __init__(self, dna=None, environment=0.01):
        self.dna = dna if dna else DNA()
        self.environment = environment

    def attempt_mutation(self):
        if random.random() < self.environment:
            self.dna.mutate()

    def is_perfect(self):
        return self.dna.is_all_ones()


#Simulation jusqu'a ADN parfait

def run_simulation():
    organism = Organism(environment=0.4)  # Mutation probabilité ajustable
    generation = 0

    while not organism.is_perfect():
        organism.attempt_mutation()
        generation += 1
        if generation % 100 == 0:
            print(f"Generation {generation}... not perfect yet.")

    print(f"\nPerfect DNA found in {generation} generations!")
    print("Final DNA:\n")
    print(organism.dna)

run_simulation()


