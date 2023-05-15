import string
import matplotlib.pyplot as plt
import numpy as np
import random

alpa =list(string.ascii_uppercase)
intersection_points, reference, editPar0, editPar1, editPar2, listInequality, grid = [], [], [], [], [], [], []
x, y, c, li, lines, =["0", "3", "6", "89", "15"], ["4", "0", "13", "46", "25"], ["3", "8", "54", "142", "76"], [">", "=", "<", "<=", ">="], []
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
    global intersection_points;intersection_points = [];line_count = len(lines)
    for i in range(line_count):
        for j in range(i + 1, line_count):
            intersection = lines[i].intersect(lines[j])
            if intersection is not None:intersection_points.append(intersection)
    return intersection_points
def read_lines():
    lines = [];global editPar0, editPar1,editPar2
    for i in range (len(editPar0)):line = Line(editPar0[i], editPar1[i], editPar2[i]);lines.append(line)
    return lines
def main(xo, yo):
    lines = read_lines();intersection_points = extract_intersections(lines); i=0; global reference
    reference = []; optimal =0;xmax= 0;ymax = 0
    if len(intersection_points) > 0:
        for point in intersection_points: 
            if (point[0] < 0 or point[1] < 0) or (point[0] == 0 and point[1] == 0):continue
            else:
                val = xo*point[0] + yo*point[1]
                if val >= optimal:optimal =val;xmax= point[0];ymax = point[1]
                plt.plot(point[0], point[1], "o");reference.append(point);plt.annotate(alpa[i], xy=(point[0], point[1]), xytext=(1.5, 1.5), textcoords='offset points');i+=1
    plt.annotate("obtimal solution", xy=(xmax+0.2, ymax+0.2), xytext=(50, 50), arrowprops=dict(arrowstyle='->'), textcoords='offset points')
# =========================================================================
def plot_solution_regions(constraints):
    global grid;xc = np.linspace(-2, 100);yc = np.linspace(-2, 100);X, Y = np.meshgrid(xc, yc)
    grid = np.zeros_like(X, dtype=bool) 
    for constraint in constraints:
        a, b, op, c = constraint;a_arr = np.full_like(X, a);b_arr = np.full_like(Y, b)
        lhs = a_arr * X + b_arr * Y
        if op == '<':region = np.where(lhs < c, 100, 0)
        elif op == '>':region = np.where(lhs > c, 100, 0)
        elif op == '>=':region = np.where(lhs >= c, 100, 0)
        elif op == '<=':region = np.where(lhs <= c, 100, 0)
        elif op == '=': region = np.where(lhs == c, 100, 0)
        grid = np.maximum(grid, region)
        # grid = np.logical_or(grid, region)

# =========================================================================
def real (x, y, z):
    global editPar0, editPar1,editPar2
    for i in range (len(x)):editPar0.append(float(x[i]));editPar1.append(float(y[i]));editPar2.append(float(z[i]))
def random_hex_color():color_code = random.randint(0, 0xFFFFFF);hex_color = '#{:06x}'.format(color_code);return hex_color
def inter(par0 :list, par1 :list, par2 :list, par3 :list, xo, yo):
    global  editPar0, editPar1, editPar2, listInequality ;condition =[]
    editPar0, editPar1, editPar2, listInequality =  [1, 0], [0, 1], [0, 0], [];par3.insert(0, ">=");par3.insert(0, ">=")
    real (par0, par1, par2)
    plt.figure()
    x, y= np.linspace(-2, 100), np.linspace(-2, 100)
    for i in range(len(editPar0)):
            if i<2:plt.axvline( 0, linestyle='-', color="black");plt.axhline( 0, linestyle='-', color="black");condition.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
            elif (par3[i] == "=" or par3[i] == "<" or par3[i] == ">" or par3[i] == ">=" or par3[i] == "<=") and editPar0[i] == 0:plt.axhline(editPar2[i] / editPar1[i], linestyle='--', color=random_hex_color(), label=f'{editPar1[i]}y {par3[i]}+{editPar2[i]}');condition.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
            elif (par3[i] == "=" or par3[i] == "<" or par3[i] == ">" or par3[i] == ">=" or par3[i] == "<=") and editPar1[i] == 0:plt.axvline(editPar2[i] / editPar0[i], linestyle='--', color=random_hex_color(), label=f'{editPar0[i]}x {par3[i]}+{editPar2[i]}');condition.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
            else:y = (-editPar0[i]*x+editPar2[i])/editPar1[i];plt.plot(x, y, color= random_hex_color(), label=f'{editPar0[i]}x+{editPar1[i]}y {par3[i]}+{editPar2[i]}');condition.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
    plot_solution_regions(condition)
    plt.imshow((grid).astype(float) ,extent=(-2, 100, -2, 100),origin="lower", cmap="Greys", alpha = 0.3)
    main(xo, yo);plt.legend();plt.grid()
    plt.xlim(-1, 20);plt.ylim(-1, 20)
    plt.xlabel('X values');plt.ylabel('Y values');
    plt.title('Line Graph');plt.show()
def ref ():return reference
inter (x, y, c, li, 14, 22)


