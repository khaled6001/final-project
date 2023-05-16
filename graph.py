import string
import matplotlib.pyplot as plt
import numpy as np
import random

alpa =list(string.ascii_uppercase)
intersection_points, reference, editPar0, editPar1, editPar2, listInequality, conditions, condition= [], [], [], [], [], [], [], []
x, y, c, li, lines, =["0", "3", "6", "89", "15"], ["4", "0", "13", "46", "25"], ["3", "8", "54", "142", "76"], [">", "<", "<", "<=", ">="], []
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
# # def plot_solution_regions(constraints):
#     global conditions ;xc = np.linspace(-2, 100);yc = np.linspace(-2, 100);X, Y = np.meshgrid(xc, yc); points = ref()
#     conditions, condition, solution= [], [], []
#     i=0; xList, yList =[], []
#     for i in points:
#         xList.append(i[0])
#         yList.append(i[1])
    
#     for constraint in constraints:
#         a, b, op, c = constraint
#         lhs = a * X + b * Y
#         if op == '<':region = lhs < c
#         elif op == '>':region = lhs > c
#         elif op == '>=':region = lhs >= c
#         elif op == '<=':region = lhs <= c
#         elif op == '=': region = lhs == c
#         condition.append(region)
#         for i in range (len (xList)):
#             try:
#                 lhs0 = a * xList[i] + b * yList[1]
#                 if op == '<':region_s = lhs0 < c
#                 elif op == '>':region_s = lhs0 > c
#                 elif op == '>=':region_s = lhs0 >= c
#                 elif op == '<=':region_s = lhs0 <= c
#                 elif op == '=':region_s = lhs0 == c
#                 solution.append(region_s)
#             except:
#                 print(type(a))
#     solution_point = np.all(solution, axis=0).astype(float)
#     conditions = np.all(condition, axis=0).astype(float)
#     solution_indices = np.where(solution_point)[0]
#     non_solution_indices = np.where(np.logical_not(solution_point))[0]
#     solution_points = list(zip(xList[solution_point], yList[solution_point]))
#     non_solution_points = list(zip(xList[~solution_point], yList[~solution_point]))

    # print(f"The points {solution_points} are solutions.")
    # print(f"The points {non_solution_points} are not solutions.")
    # plt.imshow(conditions, extent=(-2, 100, -2, 100), origin="lower", cmap="Greys", alpha = 0.3)
# =========================================================================
def real (x, y, z):
    global editPar0, editPar1,editPar2
    for i in range (len(x)):editPar0.append(float(x[i]));editPar1.append(float(y[i]));editPar2.append(float(z[i]))
def random_hex_color():color_code = random.randint(0, 0xFFFFFF);hex_color = '#{:06x}'.format(color_code);return hex_color
def inter(par0 :list, par1 :list, par2 :list, par3 :list, xo, yo):
    global  editPar0, editPar1, editPar2, listInequality ;constraint =[]
    editPar0, editPar1, editPar2, listInequality =  [1, 0], [0, 1], [0, 0], [];par3.insert(0, ">=");par3.insert(0, ">=")
    real (par0, par1, par2)
    plt.figure()
    x, y= np.linspace(-2, 1000), np.linspace(-2, 1000)
    for i in range(len(editPar0)):
            if i<2:plt.axvline( 0, linestyle='-', color="black");plt.axhline( 0, linestyle='-', color="black");constraint.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
            elif (par3[i] == "=" or par3[i] == "<" or par3[i] == ">" or par3[i] == ">=" or par3[i] == "<=") and editPar0[i] == 0:plt.axhline(editPar2[i] / editPar1[i], linestyle='--', color=random_hex_color(), label=f'{editPar1[i]}y {par3[i]}+{editPar2[i]}');constraint.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
            elif (par3[i] == "=" or par3[i] == "<" or par3[i] == ">" or par3[i] == ">=" or par3[i] == "<=") and editPar1[i] == 0:plt.axvline(editPar2[i] / editPar0[i], linestyle='--', color=random_hex_color(), label=f'{editPar0[i]}x {par3[i]}+{editPar2[i]}');constraint.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
            else:y = (-editPar0[i]*x+editPar2[i])/editPar1[i];plt.plot(x, y, color= random_hex_color(), label=f'{editPar0[i]}x+{editPar1[i]}y {par3[i]}+{editPar2[i]}');constraint.append((editPar0[i], editPar1[i], par3[i], editPar2[i]))
    main(xo, yo); #plot_solution_regions(constraint)
    plt.xlim(-1, 20);plt.ylim(-1, 20);plt.legend();plt.grid()
    plt.xlabel('X values');plt.ylabel('Y values');plt.title('Line Graph')
    plt.show()
def ref ():return reference
# inter (x, y, c, li, 14, 22)


