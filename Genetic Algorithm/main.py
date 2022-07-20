from pickle import GLOBAL
import random
from sqlite3 import apilevel
import string

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 ± ! @ # $ % ^ & * ( ) _ + - = § £ ™ ¡ ¢ ∞ § ¶ • ª º – ≠ È É Ê Ë Ē Ė Ę À Á Â Ä Æ Ã Ā Ś Š Ÿ Û Ü Ù Ú Ū Î Ï Í Ī Į Ì Ô Ö Ò Ó Œ Ō Õ Ł Ž Ź Ż Ç Ć Č Ñ Ń è é ê ë ē ė ę à á â ä æ ã ā ś š ÿ û ü ù ú ū î ï í ī į ì ô ö ò ó œ ō õ ł ž ź ż ç ć č ñ ń'
alphabet = alphabet.replace(" ", "")
alphabet += " " # Defines the alphabet


class individuals(object): # Init 
    def __init__(self, chromosome, target):
        self.chromosome = chromosome
        self.target = target
        self.fitness = self.getFitness()

    def getFitness(self): # Gets the number of genes that matches with the target value
        fitness = 0
        target = self.target
        chromosome = self.chromosome

        for i, j in enumerate(chromosome):
            if (target[i] != j): # If they don't match, increase the fitness
                fitness += 1

        return fitness

    @classmethod
    def mutation(self):
        global alphabet
        random_gene = random.choice(alphabet) # Choose a random gene from the alphabet
        return random_gene

    @classmethod
    def create_gnome(self, target): # Creates a new gene based on the alphabet
        targe_size = len(target)
        gnome = ''
        for _ in range(targe_size):
            gnome += self.mutation() 

        return gnome

    def mate(self, second_par): # Mates two chromosomes
        new_chromosome = ''
        for gene1, gene2 in zip(self.chromosome, second_par.chromosome): # Accesses both chromosomes
            prob = random.random()

            if (prob < 0.45): # (Half-half chance of choosing either the gene from the first or second chromosome)
                new_chromosome += gene1
            elif (prob < 0.9):
                new_chromosome += gene2

            else: # The mutation probability is 10% (100% - 90%)
                new_chromosome  += self.mutation()

        return individuals(new_chromosome, self.target)


def main():
    Target = "ablu able" # Target
    generation = 1 
    pop_size = 10 # How many 'people' I will have
    population = []

    for i in range(pop_size):
        gnome = individuals.create_gnome(Target) # Creates the first population
        population.append(individuals(gnome, Target))

    was_found = False
    while (was_found == False):
        population = sorted(population, key=lambda x: x.fitness) # Sorts it based on the fitness score

        print(population[0].fitness, population[0].chromosome, generation) 
        # Prints the best person's chromosomes and fitness

        if (population[0].fitness == 0):
            was_found = True
            break

        new_pop = []
        top_10 = int(pop_size*0.10) # Top 10% of the population
        half = int(pop_size/2) 
        new_pop.extend(population[:top_10]) # Imports the top10% into the new population

        last_90 = pop_size  - top_10 # The last 90%
        for _ in range(last_90): 

            """ chooses the parents based on the top 50% """
            parent1_gnome = random.choice(population[:half])  # Top 50% 
            parent2_gnome = random.choice(population[:half])  # Top 50%

            child = parent1_gnome.mate(parent2_gnome) # Mate
            new_pop.append(child)
        
        population = new_pop # Subtitutes the old population by the new one
        
        generation += 1

if __name__ == '__main__':
    main()
