class Konto:
    def __init__(self, nrKonta, stanKonta):
        self.numer = nrKonta
        self.stan = stanKonta
    def __repr__(self):
        return "Nr konta: %d, stan konta: %0.2f" %(self.numer, self.stan)



class Konta(object):
    def __new__(type):
        if not "_instancja" in type.__dict__:
            type._instancja = object.__new__(type)
        return type._instancja
    def wykonaj_przelew(self,kz,kd,ile): ##tu sprawdzac i ustwaic stan
        print "wykonuje przelew z: %d do: %d kwota: %0.2f" % (kz, kd, ile)

class Transakcje:
    def __new__(type):
        if not "_instancja" in type.__dict__:
            type._instancja = object.__new__(type)
        return type._instancja
############## mozna zrobic jeden singleton?


class Przelew:
    def __init__(self,kontoZ, kontoD, kwota):
        self.stan = 0
        self.kontoZrodlowe = kontoZ
        self.kontoDocelowe = kontoD
        self.kwota = kwota
        self.receiver = Konta()
    def wykonaj(self):
        self.receiver.wykonaj_przelew(self.kontoZrodlowe,self.kontoDocelowe,self.kwota)


def main():
    konta={}
    transakcje =[]
    with open("konta.txt","rb") as plik:
        for line in plik.readlines():
            pom = line.split()
            konta[pom[0]] = Konto(int(pom[1]), float(pom[2]))
    pierwszy = Konta()
    pierwszy.konta = konta
    print pierwszy.konta
    with open("transakcje.txt","rb") as plik:
        for line in plik.readlines():
            pom = line.split()
            transakcje.append(Przelew(int(pom[0]),int(pom[1]),float(pom[2])))
    trans = Transakcje()
    trans.transakcje = transakcje
    #print trans.transakcje
    #drugi = Konta()
    #print drugi.konta
    #print pierwszy is drugi

    for x in trans.transakcje:
        x.wykonaj()

if __name__ == '__main__':
    main()