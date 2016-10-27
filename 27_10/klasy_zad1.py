class Napis:
    txt = "pierwsza klasa"
    def wyswietl(self):
        return "Witaj"

napis = Napis()

print napis.wyswietl()

print napis.txt

class Zespolona:
    def __init__(self,rzeczywista,urojona):
        self.r = rzeczywista
        self.i = urojona

x = Zespolona(5.0,-3.2)
print x.r, x.i