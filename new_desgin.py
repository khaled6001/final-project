import graph
import re
from tkinter import*
from tkinter import ttk
from graph import*
from result import filtter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# ==================================== definition =================================
x, xO, y, yO, equal, compare='', '', '', '', '', ''
listValueX, listValueY, listValueE, listOfEquation=[], [], [], []
tr, item_index = 0, 0
# =================================================================================
def get_clicked_item(event):
    try:
        global item_index
        deleting["state"]=NORMAL
        edit["state"]=NORMAL
        item_id = event.widget.focus()
        text_entring.delete(0, END)    
        item_index = table.index(item_id)
        if listValueY[item_index]>0:text_entring.insert(0 ,f"{listValueX[item_index]}x+{listValueY[item_index]}y{listOfEquation[item_index]}{listValueE[item_index]}")    
        else:text_entring.insert(0 ,f"{listValueX[item_index]}x+{listValueY[item_index]}y{listOfEquation[item_index]}{listValueE[item_index]}")    
        num_items = len(table.get_children())
        if num_items == 0: deleting["state"]=DISABLED;edit["state"]=DISABLED
    except:show_message_condition("sorry, there is some problems")
# ===============================================================
def org(par, g):
    start=0;global x,y,equal,compare
    xCalc, yCalc = [], []
    if par.find("x")==-1 or par.find("X")==-1:x= "0"
    if par.find("y")==-1 or par.find("Y")==-1:y= "0"
    for i in range(len(par)):
        if (par[i]=="x" or par[i]=="X") and i==0:xCalc.append("+1");start = i+1;
        elif (par[i]=="x" or par[i]=="X") and par[i-1]=="-" :xCalc.append("-1");start = i+1
        elif (par[i]=="x" or par[i]=="X") and par[i-1]=="+" :xCalc.append("1");start = i+1
        elif (par[i]=="x" or par[i]=="X") and par[i-1]=="-" :xCalc.append("-1");start = i+1
        elif (par[i]=="x" or par[i]=="X"):end = i;xCalc.append(par[start:end]);start = i+1
        elif (par[i]=="y" or par[i]=="Y") and i== 0:yCalc.append("+1");start = i+1;
        elif (par[i]=="y" or par[i]=="Y") and par[i-1]=="-" :yCalc.append("-1");start = i+1
        elif (par[i]=="y" or par[i]=="Y") and par[i-1]=="+" :yCalc.append("1");start = i+1
        elif (par[i]=="y" or par[i]=="Y") and par[i-1]=="-" :yCalc.append("-1");start = i+1
        elif (par[i]=="y" or par[i]=="Y"):end = i;yCalc.append(par[start:end]);start = i+1
        elif par[i]=="=":end = i+1;equal=par[end:];compare ="=";break
        elif par[i]=="<" and par[i+1]=="=":end = i+2;equal=par[end:];compare ="<=";break
        elif par[i]==">" and par[i+1]=="=":end = i+2;equal=par[end:];compare =">=";break
        elif par[i]=="<":end = i+1;equal=par[end:];compare ="<";break
        elif par[i]==">":end = i+1;equal=par[end:];compare =">";break
    if g == 1:
        x = round(sum([float(val) for val in xCalc]), 2) 
        y = round(sum([float(val) for val in yCalc]), 2)
        equal =eval(equal) 
    else :
        xO = round(sum([float(val) for val in xCalc]), 2) 
        yO = round(sum([float(val) for val in yCalc]), 2)
        return xO, yO 
#=====================================================
windows = Tk();windows.title("Linear Program Graphic");windows.geometry("900x350+200+200");#windows.resizable(False, False); windows.iconbitmap("test.ico")
#===========================fonction limit======================================
def limNumForO(val):
    show_message_object()
    if len(val)<25:return True
    else:show_message_object("Sorry, you reach the numbers limit allow", "red");return False
def limNumForC(val):
    show_message_condition()
    if len(val)<25:return True
    else:show_message_condition("Sorry, you reach the numbers limit allow", "red"); return False
#===========================fonction object======================================
def show_message_object(error='', color='black'):   label_error_object['text'] = error;text_field['foreground'] = color; 
#===========================fonction condition======================================
def show_message_condition(error='', color='black'):    label_error_condition['text'] = error;text_entring['foreground'] = color
#===========================fonction adding ======================================
def add_object():
    show_message_object();global tr
    pattern = r"^(-?\d*\.?\d*[xy])?([+-]\d*\.?\d*[xy])?([+-]\d*\.?\d*[xy])?([+-]\d*\.?\d*[xy])?"
    if text_field.get()=="":show_message_object("Value is required", 'red');
    elif tr==3: show_message_object('Please enter value at the next form : ax+by', 'red'); tr=0
    elif re.fullmatch(pattern, text_field.get()) is None:show_message_object('invalid value', 'red'); tr+=1
    else :
        try:
            xyo = org(text_field.get(), 2);text_field.delete(0, END);
            if xyo[1]>=0:text_field.insert(0, f"{xyo[0]}x+{xyo[1]}y")
            else:text_field.insert(0, f"{xyo[0]}x{xyo[1]}y")
            addObject["state"]=DISABLED;text_field["state"]=DISABLED;deletingObject["state"]=NORMAL;editObject["state"]=NORMAL; reset["state"] = NORMAL
        except:
            show_message_object("sorry, there is some problems")
def add_element():
    show_message_condition();global tr
    pattern =  r"(^-?\d*\.?\d*[xyXY])?([+-]?\d*\.?\d*[xyXY])?([+-]?\d*\.?\d*[xyXY])?([+-]?\d*\.?\d*[xyXY])?[<>=]=?-?\d*\.?\d*[+-]?\d*\.?\d*"
    if text_entring.get()=="":show_message_condition("Value is required", 'red')
    elif tr==3: show_message_condition('Please enter value at the next form : ax+by>3', 'red'); tr=0
    elif re.fullmatch(pattern, text_entring.get()) is None:show_message_condition('invalid value', 'red'); tr+=1
    elif len(table.get_children())==26:show_message_condition("sorry but there is lot condition", "red")
    else :
        try:
            show_message_condition();org(text_entring.get(), 1)
            for i in range(len(table.get_children())):
                if text_entring.get() == f"{listValueX[i]}x+{listValueY[i]}y{listOfEquation[i]}{listValueE[i]}":show_message_condition("the condition is already found", "red");return
            table.insert('',END, values=(x, y, compare, equal));text_entring.delete(0, END);reset["state"] = NORMAL
            listValueX.append(x); listValueY.append(y); listValueE.append(equal); listOfEquation.append(compare)
            update_plot()
            if len(table.get_children())==2:calcu["state"] = NORMAL
        except:show_message_condition("sorry, there is some problems", "red")
def addObenter (event):add_object()
def addElenter (event):add_element()
#===========================fonction editing ======================================
def editbject():
    try:addObject["state"]=NORMAL; text_field["state"]=NORMAL;editObject["state"]=DISABLED; calcu["state"] = DISABLED
    except:show_message_object("sorry, there is some problems")
def editCondition():
    try:
        selected_item = table.focus();org(text_entring.get(), 1)
        table.item(selected_item, values=(x, y, compare, equal)); calcu["state"] = DISABLED
        listValueX[item_index] = x; listValueY[item_index] = y; listValueE[item_index] = equal;listOfEquation[item_index] = compare
        update_plot()
    except:show_message_condition("there is no iteam selection to edit", "red"); edit["state"]=DISABLED
#=========================== fonction deleting =========================================
def delet_object(): 
    try:text_field["state"]=NORMAL;text_field.delete(0, END);addObject["state"]=NORMAL; calcu["state"] = DISABLED
    except:show_message_object("sorry, there is some problems")
def delet_element(): 
    try:
        table.delete(table.selection());num_items = len(table.get_children())
        listValueX.remove(listValueX[item_index]); listValueY.remove(listValueY[item_index]); listValueE.remove(listValueE[item_index]);listOfEquation.remove(listOfEquation[item_index])
        calcu["state"] = DISABLED
        update_plot()
    except:show_message_condition("sorry, there is some problems", "red")
# =============================== draw & calcul =============================
def update_plot():
    global canvas ,ax 
    fig = inter(Min_Max.get(), listValueX, listValueY, listValueE, listOfEquation) 
    plt.close(fig)
    ax = fig.gca()
    canvas.get_tk_widget().destroy()
    canvas = FigureCanvasTkAgg(fig, part_output)
    canvas.draw()
    canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=True)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
    # toolbar.destroy()
    # toolbar = NavigationToolbar2Tk(canvas, part_output)
    # toolbar.update()
    # toolbar.pack()
    
def calcul():
    try:points = graph.reference; object =org(text_field.get(), 2); filtter(points, object[0], object[1], Min_Max.get(), graph.infinity_solution, graph.sol_notfount)
    except:show_message_condition("sorry, there is some problems", "red")
def rest ():
    global listValueX, listValueY, listValueE, listOfEquation
    try:
        calcu["state"] = DISABLED; addObject["state"] = NORMAL; text_field["state"] = NORMAL; reset["state"] = DISABLED
        table.delete(*table.get_children());text_field.delete(0, END);text_entring.delete(0, END)
        listValueX.clear(); listValueY.clear(); listValueE.clear(); listOfEquation.clear()
        update_plot()
    except:show_message_condition("sorry, there is some problems", "red")
#==============================FRANM ONE============================================
part_inputs = Frame(windows, width=400); part_inputs.pack(side=LEFT)
ttk.Label(part_inputs, text="Linear Program", font=("italic",15)).pack(pady=10, anchor='center')
operation_field = Frame(part_inputs ); operation_field.pack(padx=0, pady=15, anchor='w')
label_error_object= Label(operation_field, fg= "red", font=("italic", 9));label_error_object.grid(row= 1, column=1, columnspan=4)
label_error_condition= Label(operation_field, fg= "red", font=("italic", 9));label_error_condition.grid(row= 3, column=1, columnspan=4)
limitNumO = operation_field.register(limNumForO), "%P";limitNumC = operation_field.register(limNumForC), "%P"
 #===============================PART MIN MAX=====================================
Min_Max = ttk.Combobox(operation_field, values=["Max Z =", "Min Z ="], width= 8, state="readonly");Min_Max.current(0);Min_Max.grid(row= 0, column= 0)
text_field = Entry(operation_field, width= 25, validate= "key", validatecommand= limitNumO); text_field.grid(row= 0, column= 1); text_field.bind("<Return>", addObenter)
addObject= Button(operation_field, text ="add", command=add_object);addObject.grid(row= 0, column= 2, padx=4)
editObject= Button(operation_field, text ="edit", command=editbject, state=DISABLED);editObject.grid(row= 0, column= 3, padx=4)
deletingObject= Button(operation_field, text ="delet", command=delet_object, state=DISABLED);deletingObject.grid(row= 0, column= 4, padx=4)
#===============================PART CONDITION======================================
conditions = Label(operation_field, text = "Enter your conditions", width= 20, font= ("italic", 10), justify="left");conditions.grid(row= 2, column= 0)
text_entring = Entry(operation_field, width= 25, validate= "key", validatecommand= limitNumC); text_entring.grid(row= 2, column= 1); text_entring.bind("<Return>", addElenter)
add= Button(operation_field, text ="add", command= add_element);add.grid(row= 2, column= 2, padx=4)
edit= Button(operation_field, text ="edit", command=editCondition, state=DISABLED);edit.grid(row= 2, column= 3, padx=4)
deleting= Button(operation_field, text ="delet", command=delet_element, state=DISABLED);deleting.grid(row= 2, column= 4, padx=4)
#==============================FRANM TWO============================================
show_field = Frame(part_inputs ); show_field.pack()
table = ttk.Treeview(show_field, columns=("Value 1", "Value 2", "Value 3", "Value 4"), show="headings",height=5, selectmode="browse")
table.column('Value 1', anchor=CENTER, width=90);table.column('Value 2', anchor=CENTER, width=90);table.column('Value 3', anchor=CENTER, width=90);table.column('Value 4', anchor=CENTER, width=90)
table.heading("Value 1", text="x");table.heading("Value 2", text="y");table.heading("Value 3", text="operation");table.heading("Value 4", text="part two")
tree_scroll = ttk.Scrollbar(show_field, orient="vertical", command=table.yview)
table.configure(yscrollcommand=tree_scroll.set)
tree_scroll.pack(side="right", fill="y")
table.pack(side="left", fill="both", expand=True)
table.bind('<Double-1>', get_clicked_item)
draw = Frame(part_inputs ); draw.pack()
reset = Button(draw, text="Rest", command=rest, state= "disabled");reset.pack(side = "left", pady=8, padx = 5)
calcu = Button(draw, text= "Solution", command=calcul, state = "disabled");calcu.pack(side = "left", pady=8, padx = 5)
#===============================part two PROGRAM======================================
part_output = Frame(windows, width = 500); part_output.pack(padx= 5, pady= 5)
fig = Figure(figsize=(4.5, 3.5), dpi=100)
fig.subplots_adjust(left=0.125, bottom=0.155, right=0.93, top=0.95)
ax = fig.add_subplot(111)
ax.grid();ax.set_ylim(0, 30);ax.set_xlim(0, 30);ax.set_xlabel("X values");ax.set_ylabel("Y values")
canvas = FigureCanvasTkAgg(fig, part_output)
canvas.draw()
toolbar = NavigationToolbar2Tk(canvas, part_output)
toolbar.update()
canvas.get_tk_widget().config(width=450, height=300)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
#===============================END PROGRAM======================================
windows.mainloop()