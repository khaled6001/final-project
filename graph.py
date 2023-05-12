import string
import matplotlib.pyplot as plt
import numpy as np
import random
import result 
alpa =list(string.ascii_uppercase)
intersection_points, reference = [], []
# =======================================================================

class Line:
    def __init__(self, a, b, c):self.a = a;self.b = b;self.c = c
    def intersect(self, other_line):
        determinant = self.a * other_line.b - other_line.a * self.b
        if determinant == 0:return None
        x = (self.b * other_line.c - other_line.b * self.c) / determinant
        y = (other_line.a * self.c - self.a * other_line.c) / determinant
        return -x, -y
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
    lines = read_lines();intersection_points = extract_intersections(lines); i=0; global reference
    if len(intersection_points) > 0:
        for point in intersection_points: 
            plt.plot(point[0], point[1], "o");reference.append(point)
            plt.annotate(alpa[i], xy=(point[0], point[1]), xytext=(1.5, 1.5), textcoords='offset points');i+=1
    else:print("No intersection points found.")
# =========================================================================
x, y, c, li, lines, =["5", "3", "6", "89", "15"], ["4", "8", "13", "56", "99"], ["3", "7", "89", "132", "65"], ["=", ">", "<", "<=", ">="], []
# x, y, c,li=["5", "6"], ["4", "5"], ["3", "4"],["=", ">"]
editPar0, editPar1, editPar2, listInequality=[], [], [], []
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
        # if xMax <= editPar0[i]:xMax= editPar0[i]
        # elif xMin >= editPar0[i]:xMin = editPar0[i]
        # if yMax <= editPar1[i]:yMax= editPar1[i]
        # elif yMin >= editPar1[i]:yMin = editPar1[i]
        y = (-editPar0[i]*x+editPar2[i])/editPar1[i]
        plt.plot(x, y, color= random_hex_color(), label=f'{editPar0[i]}x+{editPar1[i]}y {par3[i]}+{editPar2[i]}')
    main()
    plt.legend()
    plt.grid()
    plt.xlim(-10, 20)
    plt.ylim(-10, 20)
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Line Graph')
    plt.show()
def ref ():
    return reference
inter (x, y, c, li)
# ax+by=c=>y=(-ax+c)/b