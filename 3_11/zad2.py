'''urzytkownik podaje zakres
losujesz liczbe i zgadujesz ja'''

import random
random.seed()
print "podaj dodatnie zakresy losowania"
a = input()
b = input()
if(a>=b):
    print "zaduza liczba"
pom = random.randint(a, b)
print pom
print "zgadnij liczbe"
zad = input()
k = 10
while(k!=0):
    if(zad<pom):
        print "za mala"
        zad = input()
    elif(zad>pom):
        print "za duza"
        zad = input()
    elif(zad==pom):
        print "ok"
        k =0