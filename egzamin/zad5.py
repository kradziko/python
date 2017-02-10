'''stosujac widgety canvas i scale sproboj zaprojektowac zmieniajaca sie kule (promien)'''
from Tkinter import *

class Application(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        self.lastx, self.lasty = 0, 0
        self.canvas = Canvas(self, width=400, height=400, background="bisque")
        self.canvas.pack(expand=YES, fill=BOTH)
        self.scale = Scale(self, from_=1 ,to=100, orient=HORIZONTAL, command=self.changeSize)
        self.scale.pack(expand=YES, fill=BOTH)
        self.oval = self.canvas.create_oval(1,1,10,10, width=2, fill='black')
        self.master.bind("<Left>",self.left)
        self.master.bind("<Right>",self.right)
        #self.canvas.bind(self.scale.get(), self.changeSize)
    def left(self, event):
        self.scale.set(self.scale.get()-1)
    def right(self, event):
        self.scale.set(self.scale.get()+1)
    def changeSize(self,event):
        global lastx, lasty
        lastx, lasty = self.scale.get(), self.scale.get()
        self.canvas.coords(self.oval,1,1,lastx*3,lasty*3)


if __name__ == "__main__":
    root = Tk()
    Application(root).pack(fill="both", expand=True)
    root.mainloop()