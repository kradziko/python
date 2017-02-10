'''opisz klase obiektow R liczb zadanych w postaci rzymskiej lub arabskiej (tak aby instancje R(MLX) i R(153) czyly poprawne)
Utworz metody init, toroman, fromroman, oraz metody potrzebne do przesloniencia operacji +,-,*'''

class R:
    def __init__(self,liczba):
        self.l = liczba

    def toRoman(self):
        if isinstance(self.l, int):
            pom = self.l
            wynik = ["","","","",""]
            liczba_tysiecy = pom/1000
            pom = pom%1000
            liczba_setek = pom/100
            pom = pom%100
            liczba_dziesiatek = pom/10
            pom = pom%10
            wynik[0] = liczba_tysiecy*'M'
            if liczba_setek<4:
                wynik[1] = liczba_setek*"C"
            elif liczba_setek == 4:
                wynik[1] = "CD"
            elif liczba_setek == 9:
                wynik[1] = "CM"
            else :
                wynik[1] = "D"+(liczba_setek-5)*"C"

            if liczba_dziesiatek<4:
                wynik[2] = liczba_dziesiatek*"X"
            elif liczba_dziesiatek == 4:
                wynik[2] = "XL"
            elif liczba_dziesiatek == 9:
                wynik[2] = "XC"
            else :
                wynik[2] = "L"+(liczba_dziesiatek-5)*"X"

            if pom<4:
                wynik[3] = pom*"I"
            elif pom == 4:
                wynik[3] = "IV"
            elif pom == 9:
                wynik[3] = "IV"
            else :
                wynik[3] = "V"+(pom-5)*"I"

            return "".join(wynik)

        else:
            print self.l

    def fromRoman(self):
        map = {'I':1 ,'V':5 ,'X':10 ,'L':50 ,'C': 100 ,'D': 500 ,'M': 1000}
        wynik =0
#      for x in range(len(self.l)-1,-1,-2):
        x = len(self.l)-1
        while(x>=0):
            if(x > 0):
                if map[self.l[x-1]] < map[self.l[x]]:
                    wynik += (map[self.l[x]] - map[self.l[x-1]])
                else:
                    wynik += map[self.l[x]]
                    x += 1
            else:
                wynik += map[self.l[x]]
                x += 1
            x -= 2
        print self.l ,": ",wynik
        return wynik

