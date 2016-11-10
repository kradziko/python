'''
1. Napisac skrypt ktory wykona nastepujace czynnosci
a) utworzy liste o rozmarze podanym przez uzytkowanika
b) uzupelni liste losowymi wartosciami z zakresu podanego przez uzytkowanika
c) wyswietli liste
d) wyszuka wielokrotnosci liczby 2,3,5 i zapisze kazda do nowej listy
e) wyszuka duplikaty z kazdej listy i utworzy z nich nowa liste
f) zastapi duplikaty znakiem 'X' z listy a)
g) usunie duplikaty z listy a)
h) obliczy wartosc srednia i podniesie kazda wartosc do potegi 3
i) zastapi wielokrotnosci liczby 2 listera A, 3 litera E, 5 litera L
j) wyszuka liczby pierwsze i zastapi je listera Z
k) wyszuka litery w liscie i utworzy z nich losowe napisy
'''
import random

#from random import *
#from random import randint


class listy:
    l =[]
    rozmiar = 0
    def utworz_liste(self):
        self.rozmiar = input("podaj rozmiar listy")
        self.l =[x for x in range(self.rozmiar)]
        return self.l
    def losowe_wartosci(self):
        c = input("podaj zakres")
        b = input("podaj zakres")
        random.seed()
        for x in range(0, self.rozmiar):
            self.l[x] = random.randint(c, b)
    def wysukaj_wielokrotnosci(self,x =2,y=3,z=5,*inne):
        slownik = {}
        slownik[2] = [(t) for t in self.l if not (t % x)]
        slownik[3] = [(u) for u in self.l if not (u % y)]
        slownik[5] = [(t) for t in self.l if not (t % z)]
        for a in range(0, len(inne)):
            slownik[inne[a]] = [(r) for r in self.l if not (r%inne[a])]
        return slownik
    def duplikaty_do_nowej(self,slow):
        lista_duplikatow = []

        for key, value in slow.iteritems():
            for x in range(0,len(slow[key])):
                a = slow[key][x]
                #for y in range(1, len(slow[key])):
                if a == slow[key][x]:
                    lista_duplikatow.append(a)
                a = slow[key][x]
        return lista_duplikatow




a = listy()
lista = a.utworz_liste()
a.losowe_wartosci()
print len(lista)
for x in range(0,12):
    print lista[x]

b = a.wysukaj_wielokrotnosci(2,3,5,7)
print a.duplikaty_do_nowej(b)
