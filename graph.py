import matplotlib.pyplot as plt
import numpy as np
import random
# x, y, c, li=["64", "3", "21", "89", "15"], ["35", "5", "13", "56", "99"], ["78", "1", "89", "132", "65"], ["=", ">", "<", "<=", ">="]
def random_hex_color():color_code = random.randint(0, 0xFFFFFF);hex_color = '#{:06x}'.format(color_code);return hex_color

def inter(par0 :list, par1 :list, par2 :list, par3 :list):
    editPar0, editPar1, editPar2, listInequality=[], [], [], []
    for i in range (len(par0)):
        editPar0.append(float(par0[i]))
        editPar1.append(float(par1[i]))
        editPar2.append(float(par2[i]))
    plt.figure(num = 2,figsize=[25, 30], edgecolor="blue")
    
    x, y= np.linspace(0, 100, 1000), np.linspace(0, 100, 1000)
    for i in range(len(par0)):
        y = (editPar0[i]*x-editPar2[i])/editPar1[i]
        plt.plot(x, y, color= random_hex_color(), label=f'{editPar0[i]}x+{editPar1[i]}y {par3[i]}+{editPar2[i]}')
        listInequality.append(y)    
    z = np.ones_like(x, dtype=bool)
    for inequality in listInequality:
        z = np.logical_and(z, inequality(x, y))
    plt.contourf(x, y, z, levels=[-1, 0, 1], colors=['white', 'blue'], alpha=0.4)
    plt.legend()
    plt.xlim(0, 50)
    plt.ylim(0, 50)
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Line Graph')
    plt.show()
# inter (x, y, c, li)