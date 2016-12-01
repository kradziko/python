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
i) zastapi wielokrotnosci liczby 2 litera A, 3 litera E, 5 litera L
j) wyszuka liczby pierwsze i zastapi je listera Z
k) wyszuka litery w liscie i utworzy z nich losowe napisy
'''
import random

#from random import *
#from random import randint

def czy_pierwsza(liczba):
    if liczba<2:
        return False
    i = 2
    while(i*i<=liczba):
        if liczba%i == 0:
            return False
        i += 1
    return True

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
            for x in range(0, len(value)):
                a = value[x]
                for y in range(x + 1, len(value)):
                    if a == value[y]:
                        if value[y] not in lista_duplikatow:
                            lista_duplikatow.append(value[y])
        return lista_duplikatow
    def duplikaty_na_X(self):
        for x in range(0, len(self.l)):
            a = self.l[x]
            for y in range(x + 1, len(self.l)):
                if a == self.l[y]:
                    self.l[y]="X"
    def usun_duplikaty(self):
        for x in range(0, len(self.l)):
            a = self.l[x]
            for y in range(x+1, len(self.l)):
                if a == self.l[y]:
                    print a
                    #jak usunac elementy ?
    def srednia_i_do_potegi_3(self):
        suma = 0
        for x in range(0, len(self.l)):
            suma = suma + self.l[x]
            self.l[x] = pow(self.l[x],3)
        return suma/float(len(self.l))
    def zastap_wielokrotnosci_235_AEL(self,x =2,y=3,z=5,*inne):
        for t in range(0, len(self.l)):
            if not (self.l[t] % x):
                self.l[t] = "A"
            if isinstance(self.l[t],int) and not (self.l[t] % y):
                self.l[t] = "E"
            if isinstance(self.l[t],int) and not (self.l[t] % z):
                self.l[t] = "L"
    def zastap_pierwsze_Z(self):
        for t in range(0, len(self.l)):
            if isinstance(self.l[t],int) and czy_pierwsza(self.l[t]):
                self.l[t]="Z"
    def losowe_napisy(self):
        s={}
        x = random.randint(1,7)
        for i in range(0,x):
            s[i] = ""
            y = random.randint(1, 12)
            for j in range(0,y):
                if isinstance(self.l[random.randint(0,len(self.l)-1)],str) :
                    s[i] += self.l[random.randint(0,len(self.l)-1)]
        for i in range(0, x):
            print s[i]



listx = [1,4,5,7,2,7,3,8]
listx = list(set(listx))
a = {}
a[1] = "ty"
print a[1]

a = listy()
lista = a.utworz_liste()
#print lista
a.losowe_wartosci()
print lista
#for x in range(0,len(lista)):
#    print lista[x]
#a.usun_duplikaty()
#a.duplikaty_na_X()
#print lista
#
a.zastap_wielokrotnosci_235_AEL()
a.zastap_pierwsze_Z()
print lista

a.losowe_napisy()
'''b = a.wysukaj_wielokrotnosci(2,3,5,7)
print b
print a.duplikaty_do_nowej(b)'''

'''srednia = a.srednia_i_do_potegi_3()
print lista
print srednia'''

