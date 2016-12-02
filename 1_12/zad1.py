import Tkinter
class App:
    def __init__(self, master):
        self.master = master
        Tkinter.Button(master, text="Policz fibbonaci",command=self.fib).pack(side=Tkinter.TOP)
        #self.Label1 = Tkinter.Label(master, text="F%-2i = %-3i" % (i, b)).pack(side=Tkinter.BOTTOM)
    def fib(self):
        i ,a ,b= 1,0,1
        while (i <= 10):
            Tkinter.Label(self.master, text="F%-2i = %-3i" % (i, b)).pack(side=Tkinter.BOTTOM)
            b +=a
            a = b-a
            i+=1

root = Tkinter.Tk()
root.option_add('*font',('veranda',12,'bold'))
root.title(u"Przyk\u0142ad geometrii pack ")
display = App(root)
root.mainloop()