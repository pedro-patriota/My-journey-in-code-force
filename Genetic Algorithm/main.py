import random
from sqlite3 import apilevel
import string

Target = "ablu able"

alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 ± ! @ # $ % ^ & * ( ) _ + - = § £ ™ ¡ ¢ ∞ § ¶ • ª º – ≠ È É Ê Ë Ē Ė Ę À Á Â Ä Æ Ã Ā Ś Š Ÿ Û Ü Ù Ú Ū Î Ï Í Ī Į Ì Ô Ö Ò Ó Œ Ō Õ Ł Ž Ź Ż Ç Ć Č Ñ Ń è é ê ë ē ė ę à á â ä æ ã ā ś š ÿ û ü ù ú ū î ï í ī į ì ô ö ò ó œ ō õ ł ž ź ż ç ć č ñ ń'
alphabet = alphabet.replace(" ", "")

class individuals(object):
    def __init__(self, chromosome, target):
        self.chromosome = chromosome
        self.fitness = self.getFitness()
        self.target = target
            
    def getFitness(self):
        fitness = 0
        target = self.target
        chromosome = self.chromosome

        
        for i, j in enumerate(chromosome):
            if (target[i] != j):
                fitness += 1
        
        return fitness
    
    def mutation(self):
        global alphabet
        random_gene = random.choice(alphabet)
        return random_gene
    
    def create_gnome(self):
        target = self.target
        targe_size = len(target)
        gnome = ''
        for _ in range(targe_size):
            gnome += self.mutation()
        
        return gnome
    

def id_generator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def main():
    generation = 1
    pop_size = 30
    population = []
    
    for _ in range(pop_size):
        population

    print(id_generator(len(population), alphabet))
