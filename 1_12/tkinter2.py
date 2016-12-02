'''Etykiety i przyciski'''

from Tkinter import *
class LabelDemo(Frame):
    '''dalsza ilustracja etykiet i przyciskow'''
    def __init__(self):
        '''tworzy trzy etykiety i dwa przyciski oraz pakuje je
        tworzy obiekt ramka w ktorym umieszczamy widgety
        ramka jest upakowana w glownym oknie i ma tytul - przyklad'''
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Przyklad")

        #Tworzymy dwa przyciski  o nazwach QUIT i Hej ktorych wcisniecie
        #powoduje wywolanie metod quit1 i say_hi odpowiednio
        #nazwy obiektow to buton i hi_there'''

        self.button = Button(self, text="QUIT", fg="red", command=self.quit1, width=16, height=1)
        self.hi_threre = Button(self, text="Hej", command=self.say_hi, width=16, height=1)
        #tworzymy pola3 etykiet - dwa tekstowe i ikone
        self.Label1 = Label(self, text="Etykieta tekstowa")
        self.Label2 = Label(self, text="Etykieta tekstowa z ikona")
        self.Label3 = Label(self, bitmap="warning")
        #teraz pakujemy wszystko w ramke
        self.button.pack(side=BOTTOM)
        self.hi_threre.pack(side=BOTTOM)
        self.Label1.pack()
        self.Label2.pack(side=LEFT)
        self.Label3.pack(side=LEFT)

    #Metoda wywolana przez wcisniecie przycisku QUIT
    def quit1(self):
        print "Koniec"
        quit()
    #Metoda wywolywana przez wcisniecie przycisku Hej
    def say_hi(self):
        print "Hej - witojcie!"
#(A) program glowny - utworzenie okna lebelDemo i obsluga wszystkich zdarzen
def main():
    LabelDemo().mainloop()
    #jesli nazwa uruchamianego programu to __main__ wywolaj procedure main
if __name__=="__main__":
    main()