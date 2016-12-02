import Tkinter
class App:
    def __init__(self, master):
        self.master = master
        self.l1 = 0
        self.l2 = 0
        self.bttn_clicks = 0
        self.wynik = 0
        self.op = ""
        Tkinter.Button(master, text="1", command=lambda:self.liczba(1)).pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="2", command=lambda:self.liczba(2)).pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="3", command=lambda:self.liczba(3)).pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="4", command=lambda:self.liczba(4)).pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="5", command=lambda:self.liczba(5)).pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="6", command=lambda:self.liczba(6)).pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="7", command=lambda:self.liczba(7)).pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="8", command=lambda:self.liczba(8)).pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="9", command=lambda:self.liczba(9)).pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="0", command=lambda:self.liczba(0)).pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="+", command=lambda:self.wynik1("+")).pack(side=Tkinter.TOP)
        Tkinter.Button(master, text="=", command=lambda:self.wynik1("=")).pack(side=Tkinter.TOP)
        Tkinter.Button(master, text="-", command=lambda:self.wynik1("-")).pack(side=Tkinter.TOP)
        '''Tkinter.Button(master, text="*", command=self.mnozenie).pack(side=Tkinter.TOP)
        Tkinter.Button(master, text="/", command=self.dzielenie).pack(side=Tkinter.TOP)'''
        #self.Label1 = Tkinter.Label(master, text="F%-2i = %-3i" % (i, b)).pack(side=Tkinter.BOTTOM)
    def wynik1(self,op):
        self.op = op
        if(op=="+"):
            self.wynik = self.l1 + self.l2
        if(op=="-"):
            self.wynik = self.l1 - self.l2
        if(op=="="):
            Tkinter.Label(self.master, text=str(self.wynik)).pack(side=Tkinter.BOTTOM)
    def liczba(self,num):
        if (self.bttn_clicks == 0):
            self.l1 = num
        else:
            self.l2 = num



root = Tkinter.Tk()
root.option_add('*font',('veranda',12,'bold'))
root.title(u"Przyk\u0142ad geometrii pack ")
display = App(root)
root.mainloop()