import re
import time
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
# ==================================== definition =================================
total_row=0; total_column=0; f_list=[];x='';y='';equal='';listValue=[]
# =================================================================================
def org(par):
    condition = [];start=0;listOfEquation=[]
    global x,y,equal
    for i in range(len(par)):
        if par[i]=="x" and i==0:x= "1";start = i+1;
        elif par[i]=="x" and par[i-1]=="-" :x= "-1";start = i+1
        elif par[i]=="x":end = i;x= par[start:end];start = i+1
        elif par[i]=="y" and par[i-1]=="+" :y= "1";start = i+1
        elif par[i]=="y" and par[i-1]=="-" :y= "-1";start = i+1
        elif par[i]=="y":end = i;y= par[start:end];start = i+1
        elif par[i]=="<" and par[i+1]=="=":end = i+2;equal=par[end:];listOfEquation.append("<=")
        elif par[i]==">" and par[i+1]=="=":end = i+2;equal=par[end:];listOfEquation.append(">=")
        elif par[i]=="<":end = i+1;equal=par[end:];listOfEquation.append("<")
        elif par[i]==">":end = i+1;equal=par[end:];listOfEquation.append(">")
#=====================================================
windows = Tk();windows.title("Programme Linier Graphic");windows.geometry("400x300+200+200");windows.resizable(False, False)
#===========================fonction object======================================
def show_message_object(error='', color='black'):   label_error_object['text'] = error;text_field['foreground'] = color; 
def validate(value):
    show_message_condition()
    pattern = r"^-?\d*\.?\d*[xy][+-]\d*\.?\d*[xy]"
    # r'^-?|^-?\d*\.?\d*|^-?\d*\.?\d*[xy]|^-?\d*\.?\d*[xy][+-]|^-?\d*\.?\d*[xy][+-]\d*\.?\d*|^-?\d*\.?\d*[xy][+-]\d*\.?\d*[xy]'
    if value == "": show_message_condition();return True
    elif re.fullmatch(pattern, value) is None: return False
    show_message_object();return True#;label_error.destroy()
def on_invalid_object():show_message_object('invalid value', 'red')
#===========================fonction condition======================================
def show_message_condition(error='', color='black'):    label_error_condition['text'] = error;text_entring['foreground'] = color
def validate_condition(value):
    show_message_condition()
    pattern =  r"^-?\d*\.?\d*[xy][+-]\d*\.?\d*[xy][<>]=?-?\d*\.?\d*"
    if value == "":show_message_condition();return True
    elif re.fullmatch(pattern, value) is None:return False
    show_message_condition();return True
def on_invalid_conditio():show_message_condition('invalid value1', 'red')
#===========================fonction adding ======================================
def add_element():
    pattern =  r"^-?\d*\.?\d*[xy][+-]\d*\.?\d*[xy][<>]=?-?\d*\.?\d*"
    if text_entring.get()=="":show_message_object("Value is required", 'red')
    elif re.fullmatch(pattern, text_entring.get()) is None:show_message_condition('invalid value', 'red')
    else :
        show_message_condition()
        global x, y, equal, listValue
        deleting["state"]=NORMAL
        org(text_entring.get())
        table.insert('',END, values=(x, y, equal))
        listValue.append([x, y, equal])
#===========================fonction deleting=========================================
def delet_element(): 
    
    select = table.selection()
    for item in select:
        table.delete(item)
    num_items = len(table.get_children())
    if num_items == 0:
        deleting["state"]=DISABLED
    

#==============================FRANM ONE============================================
operation_field = Frame(windows ); operation_field.pack(padx=10, pady=20, anchor='w')
label_error_object= Label(operation_field, fg= "red");label_error_object.grid(row= 1, column=1)
label_error_condition= Label(operation_field, fg= "red");label_error_condition.grid(row= 3, column=1)
check_validate_object = operation_field.register(validate), "%P";check_invalidate_object= operation_field.register(on_invalid_object)
check_validate_condition = operation_field.register(validate_condition), "%P";check_invalidate_condition= operation_field.register(on_invalid_conditio)
#===============================PART MIN MAX======================================
Min_Max = ttk.Combobox(operation_field, values=["Max Z", "Min Z"], width= 8);Min_Max.current(0);Min_Max.grid(row= 0, column= 0)
text_field = Entry(operation_field, width= 20,  validate="focus", validatecommand=check_validate_object, invalidcommand=check_invalidate_object, ); text_field.grid(row= 0, column= 1)
addObject= Button(operation_field, text ="add", command=add_element);addObject.grid(row= 0, column= 2, padx=5, sticky="ew")
deletingObject= Button(operation_field, text ="delet", command=delet_element, state=DISABLED);deletingObject.grid(row= 0, column= 3, padx=5)
#===============================PART CONDITION======================================
conditions = Label(operation_field, text = "Enter your conditions", width= 20);conditions.grid(row= 2, column= 0)
text_entring = Entry(operation_field, width= 20, validate="focus", validatecommand=check_validate_condition, invalidcommand=check_invalidate_condition, ); text_entring.grid(row= 2, column= 1)
add= Button(operation_field, text ="add", command=add_element);add.grid(row= 2, column= 2, padx=5)
deleting= Button(operation_field, text ="delet", command=delet_element, state=DISABLED);deleting.grid(row= 2, column= 3, padx=5)
#==============================FRANM TWO============================================
show_field = Frame(windows ); show_field.pack()
table = ttk.Treeview(show_field, columns=("Value 1", "Value 2", "Value 3"), show="headings",height=5)
table.column('Value 1', anchor=CENTER, width=105);table.column('Value 2', anchor=CENTER, width=105);table.column('Value 3', anchor=CENTER, width=105)
table.heading("Value 1", text="x");table.heading("Value 2", text="y");table.heading("Value 3", text="part two")
tree_scroll = ttk.Scrollbar(show_field, orient="vertical", command=table.yview)
table.configure(yscrollcommand=tree_scroll.set)
tree_scroll.pack(side="right", fill="y")
table.pack(side="left", fill="both", expand=True)
draw = Frame(windows ); draw.pack()
ttk.Button(draw, text="draw graph").pack(side="bottom", anchor="center", pady=8)
#===============================END PROGRAM======================================
windows.mainloop()