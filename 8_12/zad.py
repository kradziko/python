'''konwersja z dwojkowego, osemkowego i dziesietnego'''

from Tkinter import *
from tkMessageBox import *

class EntryDemo(Frame):
    '''demonstruje 4 pola tekstowe'''
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Testowanie pol tekstowych")
        self.master.geometry("350x180") #width x length
        self.frame1 = Frame(self)
        self.frame1.pack(pady=5)

        self.label = Label(self.frame1, text="Podaj liczbe w systemie dziesietnym").pack(side=TOP)
        self.text1 = Entry(self.frame1, name="podaj liczbe")
        self.text1.bind("<Return>", self.showContents)
        self.text1.pack(side=TOP, padx=5)

        self.label2 = Label(self.frame1, text="Wybierz na jaki system chcesz zamienic \ni nacisnij ENTER").pack(side=TOP)

        self.var = IntVar()
        for text, value in [('Dwojkowy', 1), ('Osemkowy', 2)]:
            Radiobutton(self.frame1, text=text, value=value, variable=self.var).pack(anchor=W)
        self.label4 = Label(self.frame1, text="Wynik: ").pack(side=TOP)
        self.liczba = StringVar("")
        self.label3 = Label(self.frame1, textvariable=self.liczba).pack(side=BOTTOM)

    def showContents(self, event):
        var = self.var.get()
        l2 = int(self.text1.get()) #event.widget.get()
        if var == 1:
            self.liczba.set(bin(l2))
        else:
            self.liczba.set(oct(l2))

def main():
    EntryDemo().mainloop()


if __name__ == "__main__":
    main()