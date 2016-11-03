'''moduly - generator liczb pseudolosowch'''

#import random

from random import *
#from random import randint

random.seed()
print random.randinit(1,15) #losuje liczbe calkowita z zakresu 1, 15
print random.randinit(1,15)

l = range(1,10)
print random.choice(l)
random.shuffle(l)
print l

print random.random()

print random.uniform(10,30)

print random.normalvariate(5,48)