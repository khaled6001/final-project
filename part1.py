from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np
# import matplotlib.pyplot as plt
#=====================================================
def drawing():
    return
#=====================================================
def addO():
    if len(ox.get())==0 or len(oy.get())==0:
        return
    choiseO["state"]=DISABLED
    ox["state"]=DISABLED
    oy["state"]=DISABLED
    btno["state"]=DISABLED
    btnr["state"]=NORMAL
#=====================================================
def removO():
    choiseO["state"]=NORMAL
    ox["state"]=NORMAL;ox.delete(0, END)
    oy["state"]=NORMAL;oy.delete(0, END)
    btno["state"]=NORMAL
    btnr["state"]=DISABLED
#=====================================================
def add():
    x=np.linspace(0, 100, 1)
    y=np.linspace(0, 100, 1)
    
    if len(oxc.get())==0 or len(e.get())==0 or len(oyc.get())==0:
        return
    global i
    # num1 = int(oxc.get())
    # num1 = int(choiseo.get())
    # num1 = int(oyc.get())
    # num1 = int(choiseo2.get())
    # num1 = int(e.get())
    c1= oxc.get()
    c2= oyc.get()
    if float (oyc.get())>0: 
        c2= "+"+ oyc.get() 
    equal= c1+c2+choiseop2.get()+e.get()
    li.insert(i, equal);i+=1
    btn1["state"]=NORMAL
    btn2["state"]=NORMAL
#=====================================================
def remov():
    global i
    if i==-1:
        btn2["state"]=DISABLED
        btn1["state"]=DISABLED
        return 
    else:
        btn2["state"]=NORMAL
        li.delete(i)
        i-=1
        if i==-1:
            btn2["state"]=DISABLED
            btn1["state"]=DISABLED
#=====================================================
def removselected():
    try:
        global i
        selected_indices = li.curselection()
        for i in selected_indices:
            li.delete(i)
            i-=1
        if i==0:
            btn1["state"]=DISABLED
            btn2["state"]=DISABLED
            return
    except:
        messagebox.showwarning("invalide order", "you didn't select any item")
#=====================================================
def onlynum(text):
    if text == "":
        return True
    if text == "-":
        return True
    try:
        float(text)
        return True
    except ValueError:
        return False
#=====================================================     
i=0

scence = Tk()
scence.title("Programme Linier Graphic")
scence.geometry("500x300+200+200")
scence.resizable(False, False)
#============================================Title=======================================================
fr0 = Frame(scence)
fr0.grid(row=0 , columnspan=2, sticky="snew")
nb = ttk.Notebook(fr0)
nb.pack(padx=10)
test = fr0.register(onlynum)
#===========================================frame maxmin Two================================================
frameTwo = Frame(nb, width= 400, height= 200, borderwidth=2 )
nb.add(frameTwo, text="Two variable")
choiseO = ttk.Combobox(frameTwo, values=("MAX=", "MIN="), state="readonly", width=6);choiseO.grid(row=1, column=0);choiseO.current(0)
ox = Entry(frameTwo, width=10, validate="key", validatecommand=(test, "%P"));ox.grid(row=1, column=1);ttk.Label(frameTwo, text="x",).grid(row=1, column=2)
ttk.Label(frameTwo, text="+", width=1).grid(row=1, column=3);
oy = Entry(frameTwo, width=10, validate="key", validatecommand=(test, "%P"));oy.grid(row=1, column=4);ttk.Label(frameTwo, text="y",).grid(row=1, column=5)
btno= Button(frameTwo, text="add", command=addO);btno.grid(row=1, column=6)
btnr= Button(frameTwo, text="remov", command=removO, state=DISABLED);btnr.grid(row=1, column=7)
#=========================================================================================================
subframe = Frame(frameTwo,width= 200, height= 200 )
subframe.grid(row=2, columnspan=7, padx=10)
oxc = Entry(subframe, width=10, validate="key", validatecommand=(test, "%P"));oxc.grid(row=0, column=0);ttk.Label(subframe, text="x", ).grid(row=0, column=1)
ttk.Label(subframe, text="+", width=2).grid(row=0, column=2);
oyc = Entry(subframe, width=10, validate="key", validatecommand=(test, "%P"));oyc.grid(row=0, column=3);ttk.Label(subframe, text="y",).grid(row=0, column=4)
choiseop2 = ttk.Combobox(subframe, values=(">","<",">=", "<="), state="readonly", width=3);choiseop2.grid(row=0, column=5);choiseop2.current(0)
e = Entry(subframe, width=10, validate="key", validatecommand=(test, "%P"));e.grid(row=0, column=6)
li = Listbox(subframe, selectmode=SINGLE, width=30, relief="groove", highlightcolor="black", borderwidth=5);li.grid(row=1, columnspan=7)
btn = Button(subframe, text="add", command=add);btn.grid(row=2, column=4)
btn1 = Button(subframe, text="remov selected", command=removselected, state=DISABLED);btn1.grid(row=2, column=5, padx=5)
btn2 = Button(subframe, text="remov", command=remov, state=DISABLED);btn2.grid(row=2, column=6, padx=5)
draw = Button(subframe, text="draw graph").grid(row= 3, columnspan= 3, column=3, pady=5)
#==============================================the end===================================================
scence.mainloop()
