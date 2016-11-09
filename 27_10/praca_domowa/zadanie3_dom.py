'''napisz skrypt ktory wyszukuje liczby pierwsze za pomoca sila eratostenesa
2 tygodnie na oddanie zadania, udostepnic na git'''
import math
class sito_Eratostenesa:
    a = []
    def __init__(self,liczba):
        self.n = liczba
        self.zerowanie()
        self.przesiewanie()
        self.wyswietlanie()
    def zerowanie(self):
        for i in range(0,self.n+1):
            self.a.append(True)
    def przesiewanie(self):
        for i in range(2,int(math.sqrt(self.n))+1):
            if (self.a[i]==True):
                for j in range(i*i,self.n+1,i):
                        self.a[j] = False
    def wyswietlanie(self):
        for i in range(2,self.n+1):
            if self.a[i] == True:
                print i,




sito = sito_Eratostenesa(30)


