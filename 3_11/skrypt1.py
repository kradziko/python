'''moduly - generator liczb pseudolosowch'''

import random

#from random import *
#from random import randint

random.seed()
print random.randint(1,15) #losuje liczbe calkowita z zakresu 1, 15
print random.randint(1,15)

l = range(1,10)
print random.choice(l) # wybiera losowy element z sekwencji
random.shuffle(l) # wykonuje losowa permutacja z sekwencji
print l

print random.random()  #liczba rzeczywista z zakresu od 0.0 do 1.0

print random.uniform(10,30) #losowa liczba rzeczywista z przedzialu [10,30]

print random.normalvariate(5,48) #zmienna losowa o rozkladzie normalnym o sredniej 5 i odchyleniu 48