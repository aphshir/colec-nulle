from tkinter import *
from tkinter import ttk
import sys
class player:
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.streak = 0
        self.selc = None
        self.win = None
        self.sign = None
    def resets(self):
        self.score = 0
    def adds(self,score=1):
        self.score += score

def playint(n):
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    def quit():
        sys.exit()
    root.protocol("WM_DELETE_WINDOW", lambda:quit())
    root.resizable(False, False)
    root.geometry("150x80")
    root.minsize(150, 80)
    root.maxsize(150, 80)
    label = "entrer le nom du joueur "+str(n)
    ttk.Label(frm, text=label).grid(column=0, row=0)
    ent = ttk.Entry(frm)
    ent.grid(column=0, row=1)
    def submit():
        global glsubmit
        glsubmit = ent.get()
        root.destroy()
    b1 = ttk.Button(frm, text="soumettre", command=lambda: submit())
    b1.grid(column=0, row=2)
    root.mainloop()
def gmatch():
    global result
    def selc(cl):
        root = Tk()
        root.geometry("100x100")
        root.minsize(100, 95)
        root.maxsize(100 , 95)
        root.resizable(False, False)
        label = "tour de " + cl.name
        def peir(cl):
            cl.selc = 1
            root.destroy()
        def feuil(cl):
            cl.selc = 2
            root.destroy()
        def cis(cl):
            cl.selc = 3
            root.destroy()
        def quit():
            sys.exit()
        root.protocol("WM_DELETE_WINDOW", lambda: quit())
        ttk.Label(root, text=label).grid(column=0, row=0)
        ttk.Button(root, text="pierre", command=lambda: peir(cl)).grid(column=0,row=1)
        ttk.Button(root, text="feuille", command=lambda: feuil(cl)).grid(column=0, row=2)
        ttk.Button(root, text="ciseaux", command=lambda: cis(cl)).grid(column=0, row=3)
        root.mainloop()
    selc(p1)
    selc(p2)
    if p1.selc == p2.selc:
        return 0
    elif p1.selc == 1 and p2.selc == 3:
        return 1
    elif p1.selc == 2 and p2.selc == 1:
        return 1
    elif p1.selc == 3 and p2.selc == 2:
        return 1
    elif p2.selc == 1 and p1.selc == 3:
        return 2
    elif p2.selc == 2 and p1.selc == 1:
        return 2
    elif p2.selc == 3 and p1.selc == 2:
        return 2
def endg(r):
    if r == 0:
        label = "match nul !"
        p1.win="égalité"
        p2.win = "égalité"
    elif r == 1:
        label = p1.name + " gagne !"
        p1.adds()
        p1.win = "gagne"
        p2.win = "perd"
    elif r == 2:
        label = p2.name + " gagne !"
        p2.adds()
        p1.win= "perd"
        p2.win= "gagne"
    match p1.selc:
        case 1:
            p1.sign="pierre"
        case 2:
            p1.sign="feuille"
        case 3:
            p1.sign="ciseaux"
    match p2.selc:
        case 1:
            p2.sign="pierre"
        case 2:
            p2.sign="feuille"
        case 3:
            p2.sign="ciseaux"
    root = Tk()
    ttk.Frame(root, padding=10)
    if r == 0:
        root.geometry("226x120")
        root.minsize(244, 120)
        root.maxsize(244, 120)
    else:
        root.geometry("206x120")
        root.minsize(220, 120)
        root.maxsize(220, 120)
    def quit():
        sys.exit()
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", lambda:quit())
    ttk.Label(root, text=label).grid(column=1, row=0)
    lb1 = ttk.Labelframe(root, text=p1.name)
    lb1.grid(column=0, row=1)
    lb2 = ttk.LabelFrame(root, text= p2.name)
    lb2.grid(column=3, row=1)
    ttk.Label(lb1, text="status: "+p1.win).grid(column=0,row=1)
    ttk.Label(lb1, text="signe: "+p1.sign).grid(column=0,row=2)
    ttk.Label(lb1, text="score: "+str(p1.score)).grid(column=0,row=3)
    ttk.Label(root, text="contre").grid(column=1,row=1)
    ttk.Label(lb2, text="status: "+p2.win).grid(column=0,row=1)
    ttk.Label(lb2, text="signe: "+p2.sign).grid(column=0,row=2)
    ttk.Label(lb2, text="score: "+str(p2.score)).grid(column=0,row=3)
    def rematch():
        root.destroy()
    def end():
        global loop
        loop = False
        root.destroy()
    ttk.Button(root, text="rematch", command=lambda:rematch()).grid(column=0,row=2)
    ttk.Button(root, text="fin", command=lambda:end()).grid(column=3,row=2)
    root.mainloop()
def game():
    global p1
    global p2
    playint(1)
    p1 = player(glsubmit)
    playint(2)
    p2 = player(glsubmit)
    global loop
    loop=True
    while loop:
        endg(gmatch())
        print(loop)