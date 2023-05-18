import graph
import string
from tkinter import*
from tkinter import ttk
alpa =list(string.ascii_uppercase)
def result(x , y, xO, yO, minMax, inf):
    win = Tk();win.geometry("400x300");win.title("Results");win.resizable(False, False)
    partOne = Frame(win, height=5); partOne.pack(padx= 30, pady=20, anchor="w")
    ttk.Label(partOne, text=f"The obtimal solution :", font=("italic", 15)).grid(row=0, column=0,)#
    if len(x) == 0:
        ttk.Label(partOne, text=f"optimal solution not found", font=("italic", 14, "bold")).grid(row=1, column=0, columnspan= 2)#
        if minMax == "Max Z =":ttk.Label(partOne,  text=f"{minMax} {xO:.2f}x+{yO:.2f}y", font=("italic", 15)).grid(row=2, column=0, columnspan= 3, padx=30)
        else:ttk.Label(partOne, text=f"{minMax} {xO:.2f}x+{yO:.2f}y", font=("italic", 14, "bold")).grid(row=2, column=0, columnspan= 3, padx=30)
    elif inf:
        valueFinal = obtimalMax (x , y, xO, yO);ttk.Label(partOne, text=f"{minMax} {xO:.2f}x+{yO:.2f}y", font=("italic", 14)).grid(row=2, column=0, columnspan= 3, padx=30)
        ttk.Label(partOne, text=" Obtimal solution not found ", font=("italic", 14, "bold")).grid(row=1, column=0, columnspan= 2)
    else:
        if minMax == "Max Z =":valueFinal = obtimalMax (x , y, xO, yO);ttk.Label(partOne, text=f"{minMax} {xO:.2f}({valueFinal[1]:.2f})+{yO:.2f}({valueFinal[2]:.2f})", font=("italic", 14)).grid(row=2, column=0, columnspan= 3, padx=30)
        else:valueFinal = obtimalMin (x , y, xO, yO);ttk.Label(partOne, text=f"{minMax} {xO:.2f}({valueFinal[1]:.2f})+{yO:.2f}({valueFinal[2]:.2f})", font=("italic", 14, "bold")).grid(row=2, column=0, columnspan= 3, padx=30)
        ttk.Label(partOne, text=f"{alpa[valueFinal[3]]} (x={valueFinal[1]:.2f} , y={valueFinal[2]:.2f})", font=("italic", 14, "bold")).grid(row=1, column=0, columnspan= 2)
        ttk.Label(partOne, text=f"={valueFinal[0]:.2f}", font=("italic", 14)).grid(row=3, column=0, columnspan= 2)
    partTwo = Frame(win, height=5); partTwo.pack(pady=10)
    table = ttk.Treeview(partTwo, columns=("Value 1", "Value 2", "Value 3"))
    table.column('#0', anchor=CENTER, width=50);table.column('Value 1', anchor=CENTER, width=90);table.column('Value 2', anchor=CENTER, width=90);table.column('Value 3', anchor=CENTER, width=90)
    table.heading('#0', text='Points', anchor="center");table.heading("Value 1", text="X");table.heading("Value 2", text="Y");table.heading("Value 3", text=minMax)
    tree_scroll = ttk.Scrollbar(partTwo, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=tree_scroll.set)
    table.delete(*table.get_children());j=0
    if len(x) != 0:
        for i in range (len(x)):
                r = xO*x[i]+yO*y[i]
                table.insert('',END, text=alpa[j] , values=("%.2f" %x[i], "%.2f" %y[i], "%.2f" %r));j+=1
    tree_scroll.pack(side="right", fill="y")
    table.pack(side="left", fill="both", expand=True)
    win.mainloop()
def filtter(inter, par0, par1, minMax, inf):
    xList, yList = [], []
    if len (inter) !=0:
        for i in inter:xList.append(i[0]);yList.append(i[1])
    result(xList, yList, par0, par1, minMax, inf)
def obtimalMax (xlast, ylast, coefX, coefY):
    global solution; optimal = 0
    solution = []
    for i in range (len(xlast)):
        val = coefX*xlast[i]+coefY*ylast[i]
        if val >= optimal:optimal =val;xmax= xlast[i];ymax = ylast[i]; rank =i
    return optimal, xmax, ymax, rank
def obtimalMin (xlast, ylast, coefX, coefY):
    global solution; optimal = coefX*xlast[0]+coefY*ylast[0]
    solution = []
    for i in range (len(xlast)):
        val = coefX*xlast[i]+coefY*ylast[i]
        if val <= optimal:  optimal =val;xmin= xlast[i];ymin = ylast[i]; rank =i
    return optimal, xmin, ymin, rank
filtter(graph.reference, 14, 22, "Max Z =", graph.infinity_solution)
