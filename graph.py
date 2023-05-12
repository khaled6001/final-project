import string
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import random
alpa =list(string.ascii_uppercase)

x, y, c, li, lines, intersection_points=["64", "3", "21", "89", "15"], ["35", "5", "13", "56", "99"], ["78", "1", "89", "132", "65"], ["=", ">", "<", "<=", ">="], [], []
# x, y, c,li=["5", "6"], ["4", "5"], ["3", "4"],["=", ">"]
editPar0, editPar1, editPar2, intersection_points=[], [], [], []
def result(x , y):
    win = Tk()
    win.geometry("400x300")
    win.title("Results")
    win.resizable(False, False)
    table = ttk.Treeview(win, columns=("Value 1", "Value 2", "Value 3"))
    table.column('#0', anchor=CENTER, width=30);table.column('Value 1', anchor=CENTER, width=30);table.column('Value 2', anchor=CENTER, width=30);table.column('Value 3', anchor=CENTER, width=30)
    table.heading('#0', text='');table.heading("Value 1", text="x");table.heading("Value 2", text="y");table.heading("Value 3", text="Max\\Min")
    tree_scroll = ttk.Scrollbar(win, orient="vertical", command=table.yview)
    table.configure(yscrollcommand=tree_scroll.set)
    for i in range (len(x)):
            r = 15*x[i]+13*y[i]
            table.insert('',END, text=alpa[i] , values=(x[i], y[i], r));
    tree_scroll.pack(side="right", fill="y")
    table.pack(side="left", fill="both", expand=True)
    win.mainloop()
def filtter(inter):
    xList, yList = [], []
    for point in inter:
        xList.append(point[0])
        yList.append(point[1])
    result(xList, yList)

# =======================================================================

class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def intersect(self, other_line):
        determinant = self.a * other_line.b - other_line.a * self.b
        if determinant == 0:return None
        x = (self.b * other_line.c - other_line.b * self.c) / determinant
        y = (other_line.a * self.c - self.a * other_line.c) / determinant
        return x, y
def extract_intersections(lines):
    global intersection_points
    line_count = len(lines)
    for i in range(line_count):
        for j in range(i + 1, line_count):
            intersection = lines[i].intersect(lines[j])
            if intersection is not None:intersection_points.append(intersection)
    return intersection_points
def read_lines():
    lines = [];global editPar0, editPar1,editPar2
    for i in range (len(editPar0)):line = Line(editPar0[i], editPar1[i], editPar2[i]);lines.append(line)
    return lines
def main():
    lines = read_lines();intersection_points = extract_intersections(lines)
    if len(intersection_points) > 0:
        for point in intersection_points:plt.plot(point[0], point[1], "o")
    else:print("No intersection points found.")
    

# =========================================================================
def real (x, y, z):
    global editPar0, editPar1,editPar2
    for i in range (len(x)):editPar0.append(float(x[i]));editPar1.append(float(y[i]));editPar2.append(float(z[i]))
def random_hex_color():color_code = random.randint(0, 0xFFFFFF);hex_color = '#{:06x}'.format(color_code);return hex_color

def inter(par0 :list, par1 :list, par2 :list, par3 :list):
    real (par0, par1, par2)
    xMax, xMin, yMax, yMin = 0, editPar0[0], 0, editPar1[0]
    plt.figure(figsize=[10, 10])
    x, y= np.linspace(-10, 100), np.linspace(-10, 100)
    for i in range(len(par0)):
        # if xMax <= editPar0[i]:xMax= editPar0[i]elif xMin >= editPar0[i]:xMin = editPar0[i]if yMax <= editPar1[i]:yMax= editPar1[i]elif yMin >= editPar1[i]:yMin = editPar1[i]
        print(i)
        y = -(editPar0[i]*x+editPar2[i])/editPar1[i]
        plt.plot(x, y, color= random_hex_color(), label=f'{editPar0[i]}x+{editPar1[i]}y {par3[i]}+{editPar2[i]}')
    main()
    plt.legend()
    plt.grid()
    plt.xlim(-10, 100)
    plt.ylim(-10, 100)
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Line Graph')
    plt.show()
    filtter(intersection_points)
# inter (x, y, c, li)