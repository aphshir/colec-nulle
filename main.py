from tkinter import *
from tkinter import ttk
import sys
import importlib
import PFC
import morpion
def g1():
    top.destroy()
    PFC.game()
def g2():
    import morpion
    top.destroy()
    morpion.start()
while True:
    top = Tk()
    top.geometry("250x250")
    top.minsize(250, 250)
    top.maxsize(250, 250)
    def quit():
        sys.exit()
    top.protocol("WM_DELETE_WINDOW", lambda: quit())
    top.title("colec")
    top.resizable(False, False)
    label1 = ttk.Label(top, text = "bienvenue dans la collextion de merde").place(x = 20,y = 5)
    label2 = ttk.Label(top, text = "choissisez le jeu").place(x = 70, y = 20)
    pfc = ttk.Button(top, text="Pierre feuille sciseaux", command= lambda:g1()).place(x = 70, y = 40)
    mor = ttk.Button(top,text="morpion", command= lambda:g2()).place(x=70,y=70)
    top.mainloop()
