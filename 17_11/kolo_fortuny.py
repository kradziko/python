# -*- coding: utf-8 -*-
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
    def zapisz_do_pliku(self,punkty_plik):
        punkty_plik.write(self.name+" = "+str(self.punkty)+"\n")
    def dodaj_punkty(self,p):
        self.punkty += p
    def pomnoz_punkty(self,p):
        self.punkty *= p

class Gra:
    kategoria = ""
    haslo = ""
    liczba_uczestnikow = 0
    uczestnicy = []
    ukryte_haslo = ""
    liczba_nieodkrytych = 0
    def __init__(self,*args):
        print "Wylosowana kategoria to ",
        self.losowanie_kategorii()
        if(args):
            self.przygotowanie_gry(args)
        else:
            self.przygotowanie_gry()
        print "Losowanie kolejnosci: "
        self.losowanie_kolejnosci()
        print "wylosowana kolejnosc to: "
        for x in self.uczestnicy:
            print "   " + x.name
        self.krec_kolem()
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
        self.haslo = self.haslo[3:]
        #print self.haslo
        self.zainicjuj_haslo()
    def przygotowanie_gry(self,args):
        random.seed()
        self.liczba_uczestnikow = input("Podaj liczbe uczestnikow ")
        for x in args:
            self.uczestnicy.append(Uczestnik(x))
        for x in range(len(args),self.liczba_uczestnikow):
            self.uczestnicy.append(Uczestnik())
    def losowanie_kolejnosci(self):
        random.shuffle(self.uczestnicy)
        for x in range(0,self.liczba_uczestnikow):
            self.uczestnicy[x].kolejnosc = x + 1
    def krec_kolem(self):
        while self.liczba_nieodkrytych != 0:
            for x in range(0,self.liczba_uczestnikow):
                pkt = random.randint(-10,10)
                print "Zgaduje uczestnik " + self.uczestnicy[x].name
                if pkt != 0 :
                    litera = raw_input("Wylosowales pole %s podaj litere " % pkt)
                    if litera in self.haslo:
                        liczba_liter = self.haslo.count(litera)
                        self.liczba_nieodkrytych -= liczba_liter
                        print "brawo"
                        self.uzupelnij_haslo(litera)
                        if(pkt > 0):
                            self.uczestnicy[x].dodaj_punkty(pkt*liczba_liter)
                        odgadnac_haslo = raw_input("czy chcesz odgadnac haslo? wpisz T/N")
                        if(odgadnac_haslo=="T"):
                            self.odgadnij_haslo(self.uczestnicy[x])
                    else:
                        print "buuuu"
                else:
                    self.uczestnicy[x].punkty = 0
                    print "Wylosowałeś 0, tracisz swoje punkty"
                if x == self.liczba_uczestnikow:
                    x = 0
    def odgadnij_haslo(self,uczestnik):
        podane_haslo = raw_input("Podaj haslo")
        #print "podales",  podane_haslo, "a haslo to", self.haslo[-1], "test"
        if(podane_haslo==self.haslo[:-1]):
            print "Brawo!"
            uczestnik.pomnoz_punkty(self.liczba_nieodkrytych)
            self.liczba_nieodkrytych = 0
            self.zapisz_wszystkich()
            exit()
    def zainicjuj_haslo(self):
        for x in range(0,len(self.haslo)-1):
            if(self.haslo[x] == " "):
                self.ukryte_haslo += " "
            else:
                self.liczba_nieodkrytych += 1
                self.ukryte_haslo += "_"
        self.wyswietl_haslo()
    def uzupelnij_haslo(self,litera):
        for x in range(0,len(self.haslo)-1):
            if(self.haslo[x] == litera):
                self.ukryte_haslo = self.ukryte_haslo[:x] + litera + self.ukryte_haslo[x+1:]
        self.wyswietl_haslo()
    def wyswietl_haslo(self):
        for x in range(0,len(self.ukryte_haslo)):
            print self.ukryte_haslo[x],
        print "\n"
    def zapisz_wszystkich(self):
        punkty_plik = open("punkty.txt", "wb")
        for x in range(0,self.liczba_uczestnikow):
            self.uczestnicy[x].zapisz_do_pliku(punkty_plik)



g = Gra('Karolka','Kamil','Ala','Lena')

