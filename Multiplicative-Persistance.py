import copy
import functools
import random
import math

Mut_Rate = 0.5

Digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
length = 10

bestscore = 0
bestanswer = []

class Answer:
    # 15 digits
    def __init__(self, genes=None, rand=False):
        if rand:
            self.genome = [random.choice(Digits) for i in range(0, length)]
        else:
            self.genome = genes
        self.fitness = 0

    def Evaluate(self):
        result = self.genome
        score = 0
        while (len(result) > 1):
            num = functools.reduce(lambda a, b: a*b, result)
            result = list(map(int, str(num)))
            score += 1
        
        global bestscore
        global bestanswer
        if score >= bestscore:
            if (sorted(self.genome) < sorted(bestanswer)):
                bestscore = score
                bestanswer = self.genome
            elif (score > bestscore):
                bestscore = score
                bestanswer = self.genome
            

        self.fitness = score
        return score

    def Mutate(self):
        toMutate = random.randint(0, len(self.genome) - 1)
        if (random.random() > 0.9):
            # completely random
            self.genome[toMutate] = random.randint(0, 9)  # new random int
        else:
            if (self.genome[toMutate] > 0 and self.genome[toMutate] < 9):
                self.genome[toMutate] += (1 if random.random() < 0.5 else -1)
            elif (self.genome[toMutate] <= 0):
                self.genome[toMutate] += 1
            else:
                self.genome[toMutate] -= 1
            # uniform perturb

    def __str__(self):
        return ' '.join([str(g) for g in self.genome])


class Population:
    def __init__(self, creatures=None, rand=False, popSize=100):
        if rand:
            self.creatures = []
            for i in range(0, popSize):
                self.creatures.append(Answer(rand=True))
        else:
            self.creatures = creatures

        for c in self.creatures:
            c.Evaluate()

        # get pop best
        self.maximum = 0
        self.best = None
        for c in self.creatures:
            if c.fitness > self.maximum:
                self.maximum = c.Evaluate()
                self.best = c

    # mutates the population randomly
    def Mutate(self):
        # mutationrate chance to mutate each solution
        for c in self.creatures:
            if (random.random() < Mut_Rate):
                c.Mutate()

    def selectOne(self):
        choices = {c: c.fitness for c in self.creatures}
        largest = sum(choices.values())
        pick = random.uniform(0, largest)
        current = 0
        for key, value in choices.items():
            current += value
            if current > pick:
                return key

    # gets top half of the population and makes new
    def makeNext(self):
        #selected = []
        #parentCopy = copy.deepcopy(self)
        #goal = math.ceil(len(self.creatures) * 0.5)
        # for i in range(0, goal):
        #    selected.append(parentCopy.selectOne())
        newPop = []
        while(len(newPop) < len(self.creatures)):
            parent = copy.deepcopy(self.selectOne())
            parent.Mutate()
            newPop.append(parent)

        return Population(creatures = newPop)

    def __str__(self):
        return('\n'.join([str(c) for c in self.creatures]))

if __name__ == "__main__":
    best = [2, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9]

    pop = Population(rand=True, popSize=1000)

    for i in range (0,500):
        #pop = Population(rand=True, popSize=100)
        print("gen:", i, "-> best:" , pop.maximum, "|| answer: ", end="")
        print(*sorted(pop.best.genome), sep='')
        pop = pop.makeNext()

    BEST = sorted(bestanswer)
    print(*BEST, sep='')
    print(bestscore)