import re
import time
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from graph import inter
# ==================================== definition =================================
x, y, equal='','','';
listValueX, listValueY, listValueE, listOfEquation=[], [], [], []
tr, item_index=0, 0;
# =================================================================================
def get_clicked_item(event):
    global item_index
    deleting["state"]=NORMAL
    edit["state"]=NORMAL
    item_id = event.widget.focus()
    item_index = table.index(item_id)
    print (item_index)
    table.update()
    # selected_item = table.selection()[-1]
    # column1_value = table.item(selected_item)['values'][0]
    # column2_value = table.item(selected_item)['values'][1]
    # column3_value = table.item(selected_item)['values'][2]
    # phrase = "{}{}{}".format(column1_value, column2_value, column3_value)
    # text_entring.insert(0, phrase)
    num_items = len(table.get_children())
    if num_items == 0: deleting["state"]=DISABLED;edit["state"]=DISABLED
# ===============================================================
def org(par):
    start=0;
    global x,y,equal,listOfEquation
    for i in range(len(par)):
        if par[i]=="x" and i==0:x= "1";start = i+1;
        elif par[i]=="x" and par[i-1]=="-" :x= "-1";start = i+1
        elif par[i]=="x" and par[i-1]=="+" :x= "1";start = i+1
        elif par[i]=="x" and par[i-1]=="-" :x= "-1";start = i+1
        elif par[i]=="x":end = i;x= par[start:end];start = i+1
        elif par[i]=="y" and i==0:y= "1";start = i+1;
        elif par[i]=="y" and par[i-1]=="-" :y= "-1";start = i+1
        elif par[i]=="y" and par[i-1]=="+" :y= "1";start = i+1
        elif par[i]=="y" and par[i-1]=="-" :y= "-1";start = i+1
        elif par[i]=="y":end = i;y= par[start:end];start = i+1
        elif par[i]=="<" and par[i+1]=="=":end = i+2;equal=par[end:];listOfEquation.append("<=")
        elif par[i]==">" and par[i+1]=="=":end = i+2;equal=par[end:];listOfEquation.append(">=")
        elif par[i]=="<":end = i+1;equal=par[end:];listOfEquation.append("<")
        elif par[i]==">":end = i+1;equal=par[end:];listOfEquation.append(">")
#=====================================================
windows = Tk();windows.title("Programme Linier Graphic");windows.geometry("450x350+200+200");windows.resizable(False, False)
#===========================fonction limit======================================
def limNumForO(val):
    show_message_object()
    if len(val)<20:return True
    else:show_message_object("Sorry, you reach the numbers limit allow", "red");return False
def limNumForC(val):
    show_message_condition()
    if len(val)<20:return True
    else:show_message_condition("Sorry, you reach the numbers limit allow", "red"); return False
#===========================fonction object======================================
def show_message_object(error='', color='black'):   label_error_object['text'] = error;text_field['foreground'] = color; 
#===========================fonction condition======================================
def show_message_condition(error='', color='black'):    label_error_condition['text'] = error;text_entring['foreground'] = color
#===========================fonction adding ======================================
# ==================add obj===============
def add_object():
    show_message_object();global tr
    pattern = r"^(-?\d*\.?\d*[xy])?([+-]\d*\.?\d*[xy])?"
    if text_field.get()=="":show_message_object("Value is required", 'red')
    elif tr==3: show_message_condition('Please enter value at the next form : ax+by>3', 'red'); tr=0
    elif re.fullmatch(pattern, text_field.get()) is None:show_message_object('invalid value', 'red')
    else :addObject["state"]=DISABLED;text_field["state"]=DISABLED;deletingObject["state"]=NORMAL
# ====================add con=============
def add_element():
    show_message_condition();global tr
    pattern =  r"(^-?\d*\.?\d*[xy])?([+-]?\d*\.?\d*[xy])?[<>]=?-?\d*\.?\d*"
    if text_entring.get()=="":show_message_condition("Value is required", 'red')
    elif tr==3: show_message_condition('Please enter value at the next form : ax+by>3', 'red'); tr=0
    elif re.fullmatch(pattern, text_entring.get()) is None:show_message_condition('invalid value', 'red'); tr+=1
    else :
        global x, y, equal
        show_message_condition();
        org(text_entring.get())
        table.insert('',END, values=(x, y, equal));
        listValueX.append(x); listValueY.append(y); listValueE.append(equal)
        text_entring.delete(0, END)
#===========================fonction editing ======================================
# ==================edit obj===============
def editbject():addObject["state"]=NORMAL; text_field["state"]=NORMAL
# ====================edit con=============
def editCondition():
    selected_item = table.selection()[0]
    
    table.item(selected_item, values=(x[item_index], y[item_index], equal[item_index]))
    
#===========================fonction deleting=========================================
# ==================delet obj===============
def delet_object(): text_field["state"]=NORMAL;text_field.delete(0, END);addObject["state"]=NORMAL
# ====================delet con=============
def delet_element(): 
    select = table.selection()
    if select is None: table.delete(table.get_children()[-1])
    for item in select:table.delete(item);
    num_items = len(table.get_children())
    if num_items == 0: deleting["state"]=DISABLED
# ===============================draw=============================

def drawGraph():
    inter(listValueX, listValueY, listValueE, listOfEquation)
#==============================FRANM ONE============================================
ttk.Label(windows, text="Linear Program", font=("italic",15)).pack(pady=10, anchor='center')
operation_field = Frame(windows ); operation_field.pack(padx=0, pady=15, anchor='w')
label_error_object= Label(operation_field, fg= "red", font=("italic", 9));label_error_object.grid(row= 1, column=1, columnspan=4)
label_error_condition= Label(operation_field, fg= "red", font=("italic", 9));label_error_condition.grid(row= 3, column=1, columnspan=4)
limitNumO = operation_field.register(limNumForO), "%P"
limitNumC = operation_field.register(limNumForC), "%P"
 #===============================PART MIN MAX=====================================
Min_Max = ttk.Combobox(operation_field, values=["Max Z =", "Min Z ="], width= 8);Min_Max.current(0);Min_Max.grid(row= 0, column= 0)
text_field = Entry(operation_field, width= 25, validate= "key", validatecommand= limitNumO); text_field.grid(row= 0, column= 1)
addObject= Button(operation_field, text ="add", command=add_object);addObject.grid(row= 0, column= 2, padx=4)
editObject= Button(operation_field, text ="edit", command=editbject, state=DISABLED);editObject.grid(row= 0, column= 3, padx=4)
deletingObject= Button(operation_field, text ="delet", command=delet_object, state=DISABLED);deletingObject.grid(row= 0, column= 4, padx=4)
#===============================PART CONDITION======================================
conditions = Label(operation_field, text = "Enter your conditions", width= 20, font= ("italic", 10), justify="left");conditions.grid(row= 2, column= 0)
text_entring = Entry(operation_field, width= 25, validate= "key", validatecommand= limitNumC); text_entring.grid(row= 2, column= 1)
add= Button(operation_field, text ="add", command=add_element);add.grid(row= 2, column= 2, padx=4)
edit= Button(operation_field, text ="edit", command=editCondition, state=DISABLED);edit.grid(row= 2, column= 3, padx=4)
deleting= Button(operation_field, text ="delet", command=delet_element, state=DISABLED);deleting.grid(row= 2, column= 4, padx=4)
#==============================FRANM TWO============================================
show_field = Frame(windows ); show_field.pack()
table = ttk.Treeview(show_field, columns=("Value 1", "Value 2", "Value 3"), show="headings",height=5)
table.column('Value 1', anchor=CENTER, width=110);table.column('Value 2', anchor=CENTER, width=110);table.column('Value 3', anchor=CENTER, width=110)
table.heading("Value 1", text="x");table.heading("Value 2", text="y");table.heading("Value 3", text="part two")
tree_scroll = ttk.Scrollbar(show_field, orient="vertical", command=table.yview)
table.configure(yscrollcommand=tree_scroll.set)
tree_scroll.pack(side="right", fill="y")
table.pack(side="left", fill="both", expand=True)

table.bind('<Button-1>', get_clicked_item)
draw = Frame(windows ); draw.pack()
ttk.Button(draw, text="draw graph", command=drawGraph).pack(side="bottom", anchor="center", pady=8)
#===============================END PROGRAM======================================
windows.mainloop()