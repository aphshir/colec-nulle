from tkinter import *
from tkinter import ttk
import PFC
import sys
def g1():
    top.destroy()
    PFC.game()
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
    top.mainloop()
