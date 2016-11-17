'''skrypt ktory bedzie dzialal jak ksiazka adresowa(imie, nazwisko, adres zamieszkania, kraj, nr tel, email) ,
dane powinno mozna wprowadzic usunac(id)
i zmodyfikowac i wyswietlic, dane powinny byc wyswietlone w postaci tabeli'''

class Osoba:
    def __init__(self,imie=None,nazwisko=None,adres=None,kraj=None,numer=None,mail=None):
        if(imie==None):
            self.imie = raw_input('podaj imie ')
            self.nazwisko = raw_input('podaj nazwisko ')
            self.adres = raw_input('podaj adres ')
            self.kraj = raw_input('podaj kraj ')
            self.nr = raw_input('podaj numer telefonu ')
            self.email = raw_input('podaj mail ')
        else:
            self.imie = imie
            self.nazwisko = nazwisko
            self.adres = adres
            self.kraj = kraj
            self.nr = numer
            self.email = mail
    def wyswietl(self):
        return "%-12s%#-16s%#-25s%#-12s%#-12s%#-10s" % (self.imie, self.nazwisko, self.adres,self.kraj,self.nr,self.email)
    def edytuj(self,args):
        if(args[0]):
            self.imie = raw_input('EDYCJA : podaj imie ')
        if(args[1]):
            self.nazwisko = raw_input('EDYCJA : podaj nazwisko ')
        if(args[2]):
            self.adres = raw_input('EDYCJA : podaj adres ')
        if(args[3]):
            self.kraj = raw_input('EDYCJA : podaj kraj ')
        if(args[4]):
            self.nr = raw_input('EDYCJA : podaj numer telefonu ')
        if(args[5]):
            self.email = raw_input('EDYCJA : podaj mail ')

class Ksiazka():
    id = 0
    a = {}
    def dodaj_rekord(self,os=None):
            if(os==None):
                self.a[self.id] = Osoba()
            else:
                self.a[self.id] = os
            self.__class__.id = self.id  + 1
    def wyswietl_ksiazke(self):
        i =0
        while(i<self.__class__.id):
            print str(i) + ". " +self.a[i].wyswietl()
            i=i+1
    def edytuj_rekord(self):
        ida = input("Podaj numer wiersza ktory chcesz edytowac (wiersze sa numerowane od zera!) ")
        kol = input("Podaj krotke kolumn ktore chcesz edytowac, wpisz 0 - nie, 1 -tak ")
        self.a[ida].edytuj(kol)
    def usun_rekord(self):
        ida = input("Podaj numer wiersza ktory chcesz usunac (wiersze sa numerowane od zera!) ")
        pom = len(self.a)-ida-1
        i = 1
        j= 0
        while(pom!=0):
            self.a[ida+j] = self.a[ida+i]
            i+=1
            j+=1
            pom -= 1
        self.__class__.id = self.id - 1
        del self.a[len(self.a)-1]
    def zarzadzaj_ksiazka(self):
        a = 1
        print "Witam w programie obslugi ksiazki telefonicznej"
        print "Mozesz tutaj dodawac nowe kontakty (numer 1)"
        print "Edytowac juz istniejace (numer 2)"
        print "Usuwac niepotrzebne (numer 3)"
        print "Oraz wyswietlac cala zawartosc ksiazki (numer 4)"
        while(a):

            pomoc = input("Podaj numer komendy ")
            if(pomoc==1):
                self.dodaj_rekord()
            if(pomoc==2):
                self.edytuj_rekord()
            if(pomoc==3):
                self.usun_rekord()
            if(pomoc==4):
                self.wyswietl_ksiazke()

karolina = Osoba("Karolina","Radzikowska","Pilsudskiego 35a/16","Polska","073654861","karola@gmail.com")
kamil = Osoba("Kamil","Lipski","Langiewicza","Polska","048576334","kamil@kamil.com")
jozef = Osoba("Jozef","Pilsudski","Sulejowek","Polska","","")
jozef2 = Osoba("Jozef","Pilsudski","jowek","Polska","","")
Leon = Osoba("Leon","Radzikowski","Bychawa","Polska","","leon@gmail.com")
Fela = Osoba("Fela","Lipska","Zawieprzyce","Polska","","")
adresowa = Ksiazka()
adresowa.dodaj_rekord(karolina)
adresowa.dodaj_rekord(kamil)
adresowa.dodaj_rekord(jozef)
adresowa.dodaj_rekord(jozef2)
adresowa.dodaj_rekord(Leon)
adresowa.dodaj_rekord(Fela)
adresowa.zarzadzaj_ksiazka()