from Tkinter import *

class App(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.geometry("200x200")
        self.var = IntVar()
        for x in ["trojkat","kwadrat","kolo"]:
            setattr(self.var,x,IntVar())
            Checkbutton(self,text=x,variable=getattr(self.var,x),command=self.rysuj,name=x).pack(anchor='w')
        self.canvas = Canvas(self,width=180,height=100,background="white")
        self.canvas.pack()
        self.trojkat = self.canvas.create_polygon(0,0,0,0,0,0,0,0)
        self.kwadrat =self.canvas.create_rectangle(0,0,0,0)
        self.kolo = self.canvas.create_oval(0,0,0,0)
    def rysuj(self):
        if getattr(self.var,'trojkat').get() == 1:
            self.canvas.coords(self.trojkat,100, 5, 5, 100, 155, 100, 100, 5)
        else:
            self.canvas.coords(self.trojkat, 0,0,0,0,0,0,0,0)
        if getattr(self.var,'kwadrat').get() == 1:
            self.canvas.coords(self.kwadrat, 10, 10, 40, 40)
        else:
            self.canvas.coords(self.kwadrat, 0,0,0,0)
        if getattr(self.var,'kolo').get() == 1:
            self.canvas.coords(self.kolo, 10, 10, 40, 40)
        else:
            self.canvas.coords(self.kolo, 0,0,0,0)


App().mainloop()