'''
skrypt ktory bedzie dzialal jak gra w kolo fortuny. na poczatku gry podaje sie liczbe uczestnikow
oraz losowo wybierana jest kategoria i haslo z pliku txt. Nastepnie kazdy z uczestnikow losuje
liczbe od 1 do iloci uczestnikow. w ten sposob ustala sie kolejnosc gry przy pierwszym kreceniu kolem.
na kole znajduja sie liczby od -10 do 10 liczby te symbolizuja punkty. uzytkownik kreci kolem
czyli losuje liczbe. Liczba 0 symbolizuje bankruta (czyli zdobyte do tej pory punkty kasuja sie) i kolejny uczestnik losuje
nastepnie podaje literke. jesli literka znajduje sie w hasle i pkt sa ujemne nie otrzymuje ich
podajac litere i majac punkty dodatnie mnozymy je przez ilosc wystapien tej litery
'''
import random


class kategoria:
    id = 0
    kategorie = open("kategorie.txt", "ab")
    hasla = open("hasla.txt", "ab")
    def dodaj_kategorie(self):
        kat = raw_input("Podaj nowa kategorie ")
        self.kategorie.write(str(self.__class__.id) + kat + "\n")
        print "Twoja kategoria ma numer " + str(self.id)
        self.__class__.id = self.id + 1
    def dodaj_haslo(self,nr_kat):
        haslo = raw_input("Podaj nowe haslo ")
        self.hasla.write(str(nr_kat) + haslo + "\n")

class kolo_fortuny:
    kategorie = open("kategorie.txt", "rb")
    hasla = open("hasla.txt", "rb")
    punkty = open("punkty.txt", "wb")
    liczba = input("Podaj liczbe uczestnikow ")
    uczestnicy = []
    def losuj_kategorie(self):
        random.seed()
        los = self.kategorie.readlines()
        los11 = los[random.randint(0,len(los)-1)]
        los2 = self.hasla.readlines()
        los22 = los2[random.randint(0, len(los2)-1)]
        while(los11[0]!=los22[0]):
            los22 = los2[random.randint(0, len(los2) - 1)]
        print los11
        print los22
    def losuj_kolejnosc(self):
        pom = 2
        print self.liczba
        los = random.randint(1, self.liczba)
        self.uczestnicy.append(los)
        while(pom < self.liczba):
            p = 1
            los = random.randint(1, self.liczba)
            while(p<pom):
                while(los == self.uczestnicy[p]):
                    los = random.randint(1, self.liczba)
                p += 1
            self.uczestnicy.append(los)
            pom += 1
        print self.uczestnicy



#p = kategoria()
#p.dodaj_kategorie()
#p.dodaj_haslo(0)
k = kolo_fortuny()
k.losuj_kategorie()
k.losuj_kolejnosc()