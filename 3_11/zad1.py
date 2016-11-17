'''ktory losuje 6 niepowtarzajacych sie liczb od 1 do 49'''

import random
random.seed()
a = []
k = 6
for i in range(1,6):
    pom = random.randint(1, 49)
    while(pom in a):
            pom = random.randint(1, 49)
    a.append(pom)

print a