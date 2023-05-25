import string
import matplotlib.pyplot as plt
import numpy as np
import random
alpa =list(string.ascii_uppercase)
reference, editPar0, editPar1, editPar2, conditions, condition, solution_points= [], [], [], [], [], [], []
infinity_solution = False ;sol_notfount = False
# =======================================================================

class Line:
    def __init__(self, a, b, c):
        self.a = a;self.b = b;self.c = c
    def intersect(self, other_line):
        determinant = self.a * other_line.b - other_line.a * self.b
        if determinant == 0:return None
        x = (other_line.b * self.c - self.b * other_line.c) / determinant
        y = (self.a * other_line.c - other_line.a * self.c) / determinant
        return x, y
def read_lines():
    lines = [];global editPar0, editPar1,editPar2
    line = Line(1, 0, 0);lines.append(line)
    line = Line(0, 1, 0);lines.append(line)
    for i in range (len(editPar0)):line = Line(editPar0[i], editPar1[i], editPar2[i]);lines.append(line)
    return lines
def extract_intersections(lines):
    intersection_points = [];line_count = len(lines)
    for i in range(line_count):
        for j in range(i + 1, line_count):
            intersection = lines[i].intersect(lines[j])
            if intersection is not None:intersection_points.append(intersection)
    return intersection_points
def plot_solution_regions(constraints, ax):
    x = np.linspace(0, 100, 3000);y = np.linspace(0, 100, 3000)
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
    ax.imshow(conditions, origin='lower', extent=(0, 100, 0, 100), cmap='Blues', alpha=0.4)
def check_region(points, conditions):
    solution = []
    for point in points:
        isSol = True
        for condition in conditions:
            a, b, inequality, c  = condition
            if inequality == '<' and not (a*point[0] + b*point[1] < c):isSol = False ; break
            elif inequality == '<=' and not (a*point[0] + b*point[1] <= c):isSol = False ; break
            elif inequality == '>' and not (a*point[0] + b*point[1] > c):isSol = False ; break
            elif inequality == '>=' and not (a*point[0] + b*point[1] >= c):isSol = False ; break
            elif inequality == '=' and not (a*point[0] + b*point[1] == c):isSol = False ; break
        if isSol:
            solution.append((point[0], point[1]))
    return solution
def find_feasible_points(constraints):
    x = np.linspace(0, 100, 3000)
    y = np.linspace(0, 100, 3000)
    X, Y = np.meshgrid(x, y)
    solution = np.ones_like(X, dtype=bool)
    for a, b, op, c in constraints:
        if op == '<':region_s = a * X + b * Y < c
        elif op == '>':region_s = a * X + b * Y > c
        elif op == '>=':region_s = a * X + b * Y >= c
        elif op == '<=':region_s = a * X + b * Y <= c
        elif op == '=':region_s = np.isclose(a * X + b * Y, c)
        solution &= region_s
    solution_indices = np.where(solution)
    solution_points = np.column_stack((X[solution_indices], Y[solution_indices]))
    if len(solution_points) == 0:return []
    return solution_points
def main(object, constraints, ax):
    lines = read_lines(); intersection_points = []; global reference, infinity_solution
    plot_solution_regions(constraints, ax)
    intersection_points = extract_intersections(lines) ; 
    solution = check_region(intersection_points, constraints)
    region = find_feasible_points(constraints)
    i = 0; reference = []
    infinity_solution = False
    if len(region) > 0 :
        if len(region) > 500000 and object == "Max Z =":
            ax.text(25, 25, "there is infinity solution", fontsize=12, ha='center', va='center')
            for point in solution:
                if (point[0] == 0 and point[1] == 0):continue 
                ax.plot(point[0], point[1], "o")
                reference.append(point); infinity_solution = True
                ax.annotate(alpa[i], xy=(point[0], point[1]), xytext=(1.5, 1.5), textcoords="offset points")
                i += 1; 
        else :
            for point in solution:
                    if (point[0] == 0 and point[1] == 0):continue
                    ax.plot(point[0], point[1], "o")
                    reference.append(point)
                    plt.annotate(alpa[i], xy=(point[0], point[1]), xytext=(1.5, 1.5), textcoords="offset points");i += 1; 
    else:ax.text(25, 25, "Not solution", fontsize=12, ha='center', va='center'); sol_notfount = True
# =========================================================================
def real (x, y, z):
    global editPar0, editPar1,editPar2
    for i in range (len(x)):editPar0.append(float(x[i]));editPar1.append(float(y[i]));editPar2.append(float(z[i]))
def random_hex_color():color_code = random.randint(0, 0xFFFFFF);hex_color = '#{:06x}'.format(color_code);return hex_color
def inter(object, par0 :list, par1 :list, par2 :list, par3 :list):
    if len(par0)==0: return
    global  editPar0, editPar1, editPar2 ;constraint =[]
    editPar0, editPar1, editPar2 =  [], [], []
    real (par0, par1, par2)
    fig, ax = plt.subplots()
    fig.subplots_adjust(left=0.125, bottom=0.155, right=0.93, top=0.95)
    x, y= np.linspace(0, 100), np.linspace(0, 100)
    ax.axvline( 0, linestyle='-', color="black");constraint.append((1, 0, ">=", 0))
    ax.axhline( 0, linestyle='-', color="black");constraint.append((0, 1, ">=", 0))
    for i in range(len(editPar0)):
        if (par3[i] == "=" or par3[i] == "<" or par3[i] == ">" or par3[i] == ">=" or par3[i] == "<=") and editPar0[i] == 0:ax.axhline(editPar2[i] / editPar1[i], linestyle='--', color=random_hex_color(), label=f'{editPar1[i]}y {par3[i]}+{editPar2[i]}');constraint.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
        elif (par3[i] == "=" or par3[i] == "<" or par3[i] == ">" or par3[i] == ">=" or par3[i] == "<=") and editPar1[i] == 0:ax.axvline(editPar2[i] / editPar0[i], linestyle='--', color=random_hex_color(), label=f'{editPar0[i]}x {par3[i]}+{editPar2[i]}');constraint.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
        else:y = (-editPar0[i]*x+editPar2[i])/editPar1[i];ax.plot(x, y, color= random_hex_color(), label=f'{editPar0[i]}x+{editPar1[i]}y {par3[i]}+{editPar2[i]}');constraint.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
    main(object, constraint, ax)
    ax.grid();ax.set_ylim(0, 30);ax.set_xlim(0, 30);ax.set_xlabel("X values");ax.set_ylabel("Y values");ax.legend()
    return fig
    