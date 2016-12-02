'''przyciski w geometrii pack'''

import Tkinter
class App:
    def __init__(self, master):
        Tkinter.Button(master, text="Przycisk 1",command=self.say_hi).pack(side=Tkinter.TOP)
        Tkinter.Button(master, text="Przycisk 2").pack(side=Tkinter.LEFT)
        Tkinter.Button(master, text="Przycisk 3").pack(side=Tkinter.RIGHT)
    def say_hi(self):
        print "Hej!"
root = Tkinter.Tk()
root.option_add('*font',('veranda',12,'bold'))
root.title(u"Przyk\u0142ad geometrii pack ")
display = App(root)
root.mainloop()