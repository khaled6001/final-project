import re
from tkinter import*
from tkinter import ttk
# ==================================== definition =================================
total_row=0; total_column=0; f_list=[]
# =================================================================================
def org(par):
    condition = []#[[["x"],["y"],["equal"]]]
    arrayX =[];arrayY = [""];equal = [""];start =0;end = 0
    for i in range(len(par)):
        if par[i]=="x":end = i;arrayX.append(par[start:end]);start = i+1
        elif par[i]=="y":end = i;arrayY.append(par[start:end]);start = i
        elif par[i]=="<" and par[i+1]=="=" or par[i]==">" and par[i+1]=="=":end = i+2;equal.append(par[end:]);start = i
        elif par[i]=="<"or par[i]==">":end = i+1;equal.append(par[end:]);start = i
    condition.append([arrayX, arrayY, equal])
    return condition
#=================create table ===================================
class table:
    global total_row, total_column, f_list
    def __init__(self, root):
        for i in range (total_row):
            for j in range(total_column):
                self.e = Entry(root, width=20, font=("italic", 16, "bold"))
                self.e.grid(row=i, column=j)
                self.e.insert(END, f_list[i][j])
#=====================================================
windows = Tk()
windows.title("Programme Linier Graphic")
windows.geometry("400x200+200+200")
windows.resizable(False, False)
#===========================fonction object======================================
def show_message_object(error='', color='black'):   label_error['text'] = error;text_field['foreground'] = color
def validate(value):
    pattern = r'^-?|^-?\d*|^-?\d*[xy]|^-?\d*[xy][+-]|^-?\d*[xy][+-]\d*|^-?\d*[xy][+-]\d*[xy]'
    if value == "": show_message_condition();return True
    elif re.fullmatch(pattern, value) is None: return False
    show_message_object();label_error.destroy();return True
def on_invalid_object(): show_message_object('Please enter a valid value', 'red');label_error.grid(row= 1, column=1)
#===========================fonction condition======================================
def show_message_condition(error='', color='black'):    label_error['text'] = error;text_entring['foreground'] = color
def validate_condition(value):
    pattern = r'^(-?\d*(?:\.\d+)?[a-z]\s*[+-]?\s*)+(<=|>=|<|>)\s*-?\d+(\.\d+)?$'
    if value == "":show_message_condition();return True
    elif re.fullmatch(pattern, value) is None:return False
    show_message_condition();return True
def on_invalid_conditio():show_message_condition('Please enter a valid value1', 'red');label_error.grid(row= 3, column=1)

#===========================fonction adding ======================================
def add_element():
    if text_entring.get()=="":show_message_object('Please enter value', 'red');label_error.grid(row= 3, column=1)
    else :
        deleting["state"]=NORMAL
        f_list = org(text_entring.get());total_row = len(f_list);total_column = len(f_list[0])
        add["state"]=DISABLED

#===========================fonction deleting=========================================
def delet_element():
    add["state"]=NORMAL
    return
#====================================================================================
operation_field = Frame(windows ); operation_field.pack(padx=10, pady=20, anchor='w')
label_error= Label(operation_field, fg= "red");
check_validate_object = operation_field.register(validate), "%P"
check_validate_condition = operation_field.register(validate_condition), "%P"
check_invalidate_object= operation_field.register(on_invalid_object)
check_invalidate_condition= operation_field.register(on_invalid_conditio)
#===============================PART MIN MAX======================================
Min_Max = ttk.Combobox(operation_field, values=["Max Z", "Min Z"], width= 7);Min_Max.current(0);Min_Max.grid(row= 0, column= 0)
text_field = Entry(operation_field, width= 20, validate="key", validatecommand=check_validate_object, invalidcommand=check_invalidate_object); text_field.grid(row= 0, column= 1)
addObject= Button(operation_field, text ="add", command=add_element);addObject.grid(row= 0, column= 2, padx=5)
deletingObject= Button(operation_field, text ="delet", command=delet_element, state=DISABLED);deletingObject.grid(row= 0, column= 3, padx=5)
#===============================PART CONDITION======================================
conditions = Label(operation_field, text = "Enter your conditions", width= 20);conditions.grid(row= 2, column= 0)
text_entring = Entry(operation_field, width= 20, validate="key", validatecommand=check_validate_condition, invalidcommand=check_invalidate_condition, ); text_entring.grid(row= 2, column= 1)
add= Button(operation_field, text ="add", command=add_element);add.grid(row= 2, column= 2, padx=5)
deleting= Button(operation_field, text ="delet", command=delet_element, state=DISABLED);deleting.grid(row= 2, column= 3, padx=5)

#===============================END PROGRAM======================================
windows.mainloop()