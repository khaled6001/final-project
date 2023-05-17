import math
import string
import matplotlib.pyplot as plt
import numpy as np
import random
alpa =list(string.ascii_uppercase)
intersection_points, reference, editPar0, editPar1, editPar2, conditions, condition, solution_points, xList, yList= [], [], [], [], [], [], [], [], [],[]
x, y, c, li, lines, =["0", "3", "6", "89", "15"], ["4", "0", "13", "46", "25"], ["3", "8", "54", "142", "76"], [">", ">=", "<", ">", ">="], []
# x, y, c, li, lines, =["5", "1"], ["0", "7"], ["0", "1"], ["<=", "<"], []
# =======================================================================
class Line:
    def __init__(self, a, b, c):
        self.a = a;self.b = b;self.c = c
    def intersect(self, other_line):
        determinant = self.a * other_line.b - other_line.a * self.b
        if determinant == 0:return None
        x = (self.b * other_line.c - other_line.b * self.c) / determinant
        y = (other_line.a * self.c - self.a * other_line.c) / determinant
        return -x, -y
def read_lines():
    lines = [];global editPar0, editPar1,editPar2
    for i in range (len(editPar0)):line = Line(editPar0[i], editPar1[i], editPar2[i]);lines.append(line)
    return lines
def extract_intersections(lines):
    intersection_points = [];line_count = len(lines)
    for i in range(line_count):
        for j in range(i + 1, line_count):
            intersection = lines[i].intersect(lines[j])
            if intersection is not None:intersection_points.append(intersection)
    return intersection_points
def plot_solution_regions(constraints):
    x = np.linspace(0, 100, 5000);y = np.linspace(0, 100, 5000)
    X, Y = np.meshgrid(x, y)
    conditions = np.ones_like(X, dtype=bool)
    for constraint in constraints:
        a, b, op, c = constraint
        if op == '<':region = a * X + b * Y < c
        elif op == '>':region = a * X + b * Y > c
        elif op == '>=':region = a * X + b * Y >= c
        elif op == '<=':region = a * X + b * Y <= c
        elif op == '=':region = a * X + b * Y == c
        conditions &= region
    plt.imshow(conditions, origin='lower', extent=(0, 100, 0, 100), cmap='Blues', alpha=0.4)
def sol(constraints):
    x = np.linspace(0, 100, 5000)
    y = np.linspace(0, 100, 5000)
    X, Y = np.meshgrid(x, y)
    solution = np.ones_like(X, dtype=bool)
    for constraint in constraints:
        a, b, op, c = constraint
        if op == '<':region_s = a * X + b * Y < c
        elif op == '>':region_s = a * X + b * Y > c
        elif op == '>=':region_s = a * X + b * Y >= c
        elif op == '<=':region_s = a * X + b * Y <= c
        elif op == '=':region_s = a * X + b * Y == c
        solution &= region_s
    solution_indices = np.where(solution)
    solution_points = [X[solution_indices], Y[solution_indices]]
    if len(solution_points[0]) == 0:
        solution_points = []
    rows = len(solution_points)
    new_solution_points = []
    for i in range(rows):
        rounded_arr = np.round(solution_points[i], 3); new_solution_points.append(rounded_arr)
    return new_solution_points
def main(xo, yo, constraints):
    lines = read_lines(); intersection_points = []
    intersection_points = extract_intersections(lines)
    intersection_points = tuple(tuple(round(num, 3) for num in coord_tuple) for coord_tuple in intersection_points)
    newSolutionPoint = sol(constraints)
    solution = set()
    for tuple_val in intersection_points:
        for list_val in newSolutionPoint:
            if tuple_val[0] in list_val or tuple_val[1] in list_val:solution.add(tuple_val)
    i = 0; j = 0; optimal = 0; xmax = 0; ymax = 0
    reference = []
    intersection_found = False
    if len(newSolutionPoint) > 0 :
        if len(newSolutionPoint) > 500000: 
            plt.annotate("there is infinity solution", xy=(30, 20), xytext=(50, 50), textcoords="offset points")
            plt.title('Linear Graph infinity solution')
            print(True)
            for point in solution:
                if (point[0] < 0 or point[1] < 0) : continue
                else:
                    val = xo * point[0] + yo * point[1]
                    if val >= optimal:optimal = val; xmax = point[0]; ymax = point[1]
                    plt.plot(point[0], point[1], "o"); #print(point)
                    reference.append(point)
                    plt.annotate(alpa[i], xy=(point[0], point[1]), xytext=(1.5, 1.5), textcoords="offset points")
                    i += 1; 
                j += 1
        else :
            plt.title('Linear Graph')
            for point in solution:
                    if (point[0] < 0 or point[1] < 0) : continue
                    else:
                        val = xo * point[0] + yo * point[1]
                        if val >= optimal:optimal = val; xmax = point[0]; ymax = point[1]
                        plt.plot(point[0], point[1], "o");#  print(point)
                        reference.append(point)
                        plt.annotate(alpa[i], xy=(point[0], point[1]), xytext=(1.5, 1.5), textcoords="offset points")
                        i += 1; 
                        intersection_found = True
                    j += 1    
            if intersection_found:plt.annotate( "obtimal", xy=(xmax + 0.2, ymax + 0.2), xytext=(50, 50), arrowprops=dict(arrowstyle="->"), textcoords="offset points")
    else:plt.title('Linear Graph No solution');plt.annotate("Not solution", xy=(0, 0), xytext=(50, 50), textcoords="offset points")
# =========================================================================
def real (x, y, z):
    global editPar0, editPar1,editPar2
    for i in range (len(x)):editPar0.append(float(x[i]));editPar1.append(float(y[i]));editPar2.append(float(z[i]))
def random_hex_color():color_code = random.randint(0, 0xFFFFFF);hex_color = '#{:06x}'.format(color_code);return hex_color
def inter(par0 :list, par1 :list, par2 :list, par3 :list, xo, yo):
    global  editPar0, editPar1, editPar2 ;constraint =[]
    editPar0, editPar1, editPar2 =  [], [], []
    real (par0, par1, par2)
    x, y= np.linspace(0, 100), np.linspace(0, 100)
    plt.axvline( 0, linestyle='-', color="black");constraint.append((1, 0, ">=", 0))
    plt.axhline( 0, linestyle='-', color="black");constraint.append((0, 1, ">=", 0))
    for i in range(len(editPar0)):
        if (par3[i] == "=" or par3[i] == "<" or par3[i] == ">" or par3[i] == ">=" or par3[i] == "<=") and editPar0[i] == 0:plt.axhline(editPar2[i] / editPar1[i], linestyle='--', color=random_hex_color(), label=f'{editPar1[i]}y {par3[i]}+{editPar2[i]}');constraint.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
        elif (par3[i] == "=" or par3[i] == "<" or par3[i] == ">" or par3[i] == ">=" or par3[i] == "<=") and editPar1[i] == 0:plt.axvline(editPar2[i] / editPar0[i], linestyle='--', color=random_hex_color(), label=f'{editPar0[i]}x {par3[i]}+{editPar2[i]}');constraint.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
        else:y = (-editPar0[i]*x+editPar2[i])/editPar1[i];plt.plot(x, y, color= random_hex_color(), label=f'{editPar0[i]}x+{editPar1[i]}y {par3[i]}+{editPar2[i]}');constraint.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
    main(xo, yo, constraint);plot_solution_regions(constraint);
    plt.xlim(0, 20);plt.ylim(0, 20);plt.legend();plt.grid()
    plt.xlabel('X values');plt.ylabel('Y values');plt.show()
def ref ():return reference
# inter (x, y, c, li, 14, 22)