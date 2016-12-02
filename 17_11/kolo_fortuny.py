import random

class Uczestnik:
    id = 0
    name = ""
    punkty = 0
    kolejnosc = 0
    def __init__(self,name=None):
        self.__class__.id +=1
        if name==None:
            self.name = "Uczestnik" + str(self.id)
        else:
            self.name = name
        self.punkty = 0
        self.kolejnosc = 0
    def zapisz_do_pliku(self):
        punkty = open("punkty.txt", "ab")
        punkty.write(self.name+" = "+str(self.punkty)+"\n")
    def dodaj_punkty(self,p):
        self.punkty += p
    def pomnoz_punkty(self,p):
        self.punkty *= p

class Gra:
    kategoria = ""
    haslo = ""
    liczba_uczestnikow = 0
    uczestnicy = []
    def losowanie_kategorii(self):
        kategorie = open("kategorie.txt", "rb")
        hasla = open("hasla.txt", "rb")
        random.seed()
        los = kategorie.readlines()
        self.kategoria = los[random.randint(0,len(los)-1)]
        los2 = hasla.readlines()
        self.haslo = los2[random.randint(0, len(los2)-1)]
        while(self.kategoria[0]!=self.haslo[0]):
            self.haslo = los2[random.randint(0, len(los2) - 1)]
        print self.kategoria
        print self.haslo
    def przygotowanie_gry(self):
        random.seed()
        self.liczba_uczestnikow = input("Ilu uczestnikow?")
        for x in range(0,self.liczba_uczestnikow):
            self.uczestnicy.append(Uczestnik())
    def losowanie_kolejnosci(self):
        for x in range(0,self.liczba_uczestnikow):
            self.uczestnicy[x].kolejnosc = random.randint(0,self.liczba_uczestnikow)
            for y in range(0,x):
                while(self.uczestnicy[x].kolejnosc==self.uczestnicy[y].kolejnosc):
                    self.uczestnicy[x].kolejnosc = random.randint(0, self.liczba_uczestnikow)
                    #nie dziala

'''u = Uczestnik()
u.punkty = 2
u.zapisz_do_pliku()
u2 =Uczestnik()
u2.zapisz_do_pliku()
u3 = Uczestnik("Jan")
u3.punkty = 10
u3.zapisz_do_pliku()
u4 = Uczestnik()
u4.zapisz_do_pliku()
print u.name
print u2.name
print u3.name
print u4.name'''

g = Gra()
g.losowanie_kategorii()
g.przygotowanie_gry()
g.losowanie_kolejnosci()
for x in g.uczestnicy:
    print x.name
    print x.kolejnosc