import tkinter as tk
import turtle
import importlib
importlib.reload(turtle)
from tkinter import ttk
from turtle import RawTurtle,TurtleScreen
import sys
from tkinter import *
global win
class morpion(tk.Frame):
    def __init__(self,*args,**kwargs):
        """
         A1|B1|C1
        ---------
        A2|B2|C2
        --------
        A3|B3|C3
        """
        self.score_cross = 0
        self.score_circle = 0
        tk.Frame.__init__(self, *args, **kwargs)
        self.c = args
        turtle.TurtleScreen._RUNNING = True
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.wn = TurtleScreen(self.canvas)
        self.canvas.pack()
        self.t = RawTurtle(self.wn)
        self.cords = cord = {"A1":[-170,170],"B1":[-36.67,170],"C1":[96.66,170],"A2":[-170,36.67],"B2":[-36.67,36.67],"C2":[96.66,36.67],"A3":[-170,-96.66],"B3":[-36.67,-96.66],"C3":[96.66,-96.66]}
        self.actualsign = "x"
        self.status = [NORMAL,NORMAL,NORMAL,NORMAL,NORMAL,NORMAL,NORMAL,NORMAL,NORMAL]
        self.gridplaced = False
        self.grid = {"A1":None,"A2":None,"A3":None,"B1":None,"B2":None,"B3":None,"C1":None,"C2":None,"C3":None}
        self.A1C1 = [self.grid["A1"], self.grid["B1"], self.grid["B1"]]
        self.A2C2 = [self.grid["A2"], self.grid["B2"], self.grid["C2"]]
        self.A3C3 = [self.grid["A3"], self.grid["B3"], self.grid["C3"]]
        self.A1A3 = [self.grid["A1"],self.grid["A2"],self.grid["A3"]]
        self.B1B3 = [self.grid["B1"],self.grid["B2"],self.grid["B3"]]
        self.C1C3 = [self.grid["C1"],self.grid["C2"],self.grid["C3"]]
        self.A1C3 = [self.grid["A1"],self.grid["B2"],self.grid["C3"]]
        self.C1A3 = [self.grid["C1"],self.grid["B2"],self.grid["A3"]]
        self.solutions = [self.A1C1,self.A2C2,self.A3C3,self.A1A3,self.B1B3,self.C1C3,self.A1C3,self.C1A3]
    def add(self,pos,sign):
        self.grid[pos] = sign
        self.A1C1 = [self.grid["A1"], self.grid["B1"], self.grid["C1"]]
        self.A2C2 = [self.grid["A2"], self.grid["B2"], self.grid["C2"]]
        self.A3C3 = [self.grid["A3"], self.grid["B3"], self.grid["C3"]]
        self.A1A3 = [self.grid["A1"], self.grid["A2"], self.grid["A3"]]
        self.B1B3 = [self.grid["B1"], self.grid["B2"], self.grid["B3"]]
        self.C1C3 = [self.grid["C1"], self.grid["C2"], self.grid["C3"]]
        self.A1C3 = [self.grid["A1"], self.grid["B2"], self.grid["C3"]]
        self.C1A3 = [self.grid["C1"], self.grid["B2"], self.grid["A3"]]
        self.solutions = [self.A1C1, self.A2C2, self.A3C3, self.A1A3, self.B1B3, self.C1C3, self.A1C3, self.C1A3]
        if sign == "x":
            self.draw_cross(pos)
        elif sign == "o":
            self.draw_circle(pos)
    def checkwin(self):
        print("---------------------")
        for i in self.solutions:
            print(i)
            if i[0] == i[1] and i[0] == i[2] and i[0] != None and i[1] != None and i[2] != None:
                return [True,self.solutions.index(i),i[0]]

        return [False]
    def draw_grid(self):
        self.t.penup()
        self.t.goto(-200, 200)
        self.t.forward(133.33)
        self.t.pendown()
        self.t.right(90)
        self.t.forward(400)
        self.t.penup()
        self.t.left(90)
        self.t.forward(133.33)
        self.t.left(90)
        self.t.pendown()
        self.t.forward(400)
        self.t.penup()
        self.t.right(90)
        self.t.forward(133.33)
        self.t.right(90)
        self.t.forward(133.33)
        self.t.right(90)
        self.t.pendown()
        self.t.forward(400)
        self.t.penup()
        self.t.left(90)
        self.t.forward(133.33)
        self.t.left(90)
        self.t.pendown()
        self.t.forward(400)
        self.t.penup()
    def draw_cross(self,cord):
        self.t.goto(self.cords[cord][0], self.cords[cord][1])
        self.t.setheading(0)
        self.t.right(45)
        self.t.pendown()
        self.t.color("red")
        self.t.forward(113.33)
        self.t.penup()
        self.t.left(135)
        self.t.forward(80.14)
        self.t.left(135)
        self.t.pendown()
        self.t.forward(113.33)
        self.t.penup()
    def draw_circle(self,cord):
        self.t.setheading(0)
        self.t.goto((self.cords[cord][0]) + 33.33, self.cords[cord][1] - 66.66)
        self.t.pendown()
        self.t.color("blue")
        self.t.circle(40.07)
        self.t.penup()
    def protocol(self,pos,sign):
        match pos:
            case "A1":
                self.status[0]= DISABLED
            case "B1":
                self.status[1]= DISABLED
            case "C1":
                self.status[2] = DISABLED
            case "A2":
                self.status[3] = DISABLED
            case "B2":
                self.status[4] = DISABLED
            case "C2":
                self.status[5] = DISABLED
            case "A3":
                self.status[6]= DISABLED
            case "B3":
                self.status[7]=DISABLED
            case "C3":
                self.status[8]=DISABLED
        self.add(pos,sign)
        if self.checkwin()[0] == True:
            emp = self.checkwin()[1]
            self.t.penup()
            match emp:
                #horizontal
                case 0:
                    self.t.setheading(0)
                    self.t.goto(-200,133.335)
                    self.t.pendown()
                    self.t.forward(400)
                    turtle.done()
                    win.destroy()
                case 1:
                    self.t.setheading(0)
                    self.t.goto(-200,0)
                    self.t.pendown()
                    self.t.forward(400)
                    turtle.done()
                    win.destroy()
                case 2:
                    self.t.setheading(0)
                    self.t.goto(-200,-133.335)
                    self.t.pendown()
                    self.t.forward(400)
                    turtle.done()
                    win.destroy()
                #vertical
                case 3:
                    self.t.setheading(270)
                    self.t.goto(-133.335,200)
                    self.t.pendown()
                    self.t.forward(400)
                    turtle.done()
                    win.destroy()
                case 4:
                    self.t.setheading(270)
                    self.t.goto(0,200)
                    self.t.pendown()
                    self.t.forward(400)
                    turtle.done()
                    win.destroy()
                case 5:
                    self.t.setheading(270)
                    self.t.goto(133.335,200)
                    self.t.pendown()
                    self.t.forward(400)
                    turtle.done()
                    win.destroy()
                #diagonal
                case 6:
                    self.t.setheading(315)
                    self.t.goto(-200,200)
                    self.t.pendown()
                    self.t.forward(565.68)
                    turtle.done()
                    win.destroy()
                case 7:
                    self.t.setheading(225)
                    self.t.goto(200,200)
                    self.t.pendown()
                    self.t.forward(565.68)
                    turtle.done()
                    win.destroy()
        else:
            if sign == "x":
                self.actualsign = "o"
            elif sign == "o":
                self.actualsign = "x"
            self.control()
    def control(self):
        if self.gridplaced == False:
            self.draw_grid()
            self.gridplaced = True
        t = tk.Toplevel()
        t.geometry("500x500")
        t.minsize(500, 500)
        t.maxsize(500, 500)
        def quit():
            sys.exit()
        def submit(pos,actual_player):
            t.destroy()
            self.protocol(pos,actual_player)
        t.resizable(False, False)
        t.protocol("WM_DELETE_WINDOW", lambda: quit())
        actual_player = self.actualsign
        lab = "tour de " + actual_player
        tk.Label(t, text=lab).grid(row=0, column=1)
        A1 = ttk.Button(t, text="A1",state=self.status[0], command=lambda: submit("A1", actual_player))
        A1.grid(row=1, column=0)
        B1 = ttk.Button(t, text="B1",state=self.status[1], command=lambda: submit("B1", actual_player))
        B1.grid(row=1, column=1)
        C1 = ttk.Button(t, text="C1",state=self.status[2], command=lambda: submit("C1", actual_player))
        C1.grid(row=1, column=2)
        A2 = ttk.Button(t, text="A2",state=self.status[3], command=lambda: submit("A2", actual_player))
        A2.grid(row=2, column=0)
        B2 = ttk.Button(t, text="B2",state=self.status[4], command=lambda: submit("B2", actual_player))
        B2.grid(row=2, column=1)
        C2 = ttk.Button(t, text="C2",state=self.status[5], command=lambda: submit("C2", actual_player))
        C2.grid(row=2, column=2)
        A3 = ttk.Button(t, text="A3",state=self.status[6], command=lambda: submit("A3", actual_player))
        A3.grid(row=3, column=0)
        B3 = ttk.Button(t, text="B3",state=self.status[7], command=lambda: submit("B3", actual_player))
        B3.grid(row=3, column=1)
        C3 = ttk.Button(t, text="C3",state=self.status[8], command=lambda: submit("C3", actual_player))
        C3.grid(row=3, column=2)
"""
def round():
    game=morpion()
    t = tk.Toplevel()
    t.geometry("500x500")
    t.minsize(500, 500)
    t.maxsize(500, 500)
    def quit():
        sys.exit()
    t.resizable(False, False)
    t.protocol("WM_DELETE_WINDOW", lambda: quit())
    actual_player="x"
    while True:
        lab = "tour de "+actual_player
        tk.Label(t,text=lab).grid(row=0,column=1)
        A1= ttk.Button(t,text="A1",command=lambda:game.add("A1",actual_player))
        A1.grid(row=1,column=0)
        B1 = ttk.Button(t, text="B1", command=lambda: game.add("B1", actual_player))
        B1.grid(row=1, column=1)
        C1 = ttk.Button(t, text="C1", command=lambda:game.add("C1",actual_player))
        C1.grid(row=1,column=2)
        A2 = ttk.Button(t,text="A2", command=lambda:game.add("A2",actual_player))
        A2.grid(row=2,column=0)
        B2= ttk.Button(t,text="B2", command=lambda: game.add("B2",actual_player))
        B2.grid(row=2,column=1)
        C2 = ttk.Button(t,text="C2", command=lambda: game.add("C2", actual_player))
        C2.grid(row=2,column=2)
        A3 = ttk.Button(t,text="A3",command=lambda: game.add("A3",actual_player))
        A3.grid(row=3,column=0)
        B3 = ttk.Button(t,text="B3",command=lambda:game.add("B3",actual_player))
        B3.grid(row=3,column=1)
        C3 = ttk.Button(t,text="C3",command=lambda:game.add("C3",actual_player))
        C3.grid(row=3,column=2)

round()
"""
def start():
    root = tk.Tk()
    win = root
    fonc = morpion(root)
    fonc.pack(side="top", fill="both", expand=True)
    fonc.control()
    root.mainloop()