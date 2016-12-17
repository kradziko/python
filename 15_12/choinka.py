from Tkinter import *

root=Tk()
root.title(u'Przyk\u0142ad Canvas')

canvas = Canvas(root, width=400, height=600, bg='white')
canvas.pack(expand=YES, fill=BOTH)
points = [300,30,200,80,250,80,150,130,200,130,100,180,500,180,400,130,450,130,350,80,400,80,300,30]
canvas.create_polygon(points,fill='green')
canvas.create_line(260,50,270,45,280,55,290,45,300,55,310,45,320,55,330,45,340,50)

for x in range(210,390,10):
    y = 100
    canvas.create_line(x,y+5,x+10,y)

canvas.create_oval(220,120,210,130 , fill='yellow')
canvas.create_oval(380,120,390,130 , fill='yellow')
canvas.create_oval(450,170,440,160 , fill='red')
canvas.create_oval(150,170,140,160 , fill='yellow')
canvas.create_oval(200,170,210,160 , fill='purple')
canvas.create_oval(300,170,310,160 , fill='yellow')
canvas.create_oval(370,170,360,160 , fill='yellow')
canvas.create_oval(370,100,360,110 , fill='red')
canvas.create_oval(300,100,310,110 , fill='yellow')
canvas.create_oval(300,60,310,70 , fill='purple')
canvas.create_oval(280,50,270,60 , fill='yellow')


points = [300,30,282,40,290,25,275,15,290,15,300,0,310,15,325,15,310,25,318,40,300,30]

canvas.create_polygon(points,fill='yellow', width=3)


root.mainloop()