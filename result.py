import string
from tkinter import*
from tkinter import ttk
alpa =list(string.ascii_uppercase)

def result(x , y, xO, yO):
    win = Tk()
    win.geometry("400x300")
    win.title("Results")
    win.resizable(False, False)
    table = ttk.Treeview(win, columns=("Value 1", "Value 2", "Value 3"))
    table.column('#0', anchor=CENTER, width=5);table.column('Value 1', anchor=CENTER, width=30);table.column('Value 2', anchor=CENTER, width=30);table.column('Value 3', anchor=CENTER, width=30)
    table.heading('#0', text='');table.heading("Value 1", text="x");table.heading("Value 2", text="y");table.heading("Value 3", text="Max\\Min")
    tree_scroll = ttk.Scrollbar(win, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=tree_scroll.set)
    for i in range (len(x)):
            r = xO*x[i]+yO*y[i]
            if x[i]<0 or 0>y[i]:
                 continue
            else :table.insert('',END, text=alpa[i] , values=(x[i], y[i], r));
    tree_scroll.pack(side="right", fill="y")
    table.pack(side="left", fill="both", expand=True)
    win.mainloop()
    if win.destroy() is TRUE:
         table.destroy()
def filtter(inter, par0, par1):
    xList, yList = [], []
    for point in inter:
        xList.append(point[0])
        yList.append(point[1])
    result(xList, yList, par0, par1)
