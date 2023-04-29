import re
from tkinter import*
from tkinter import ttk
#=====================================================
windows = Tk()
windows.title("Programme Linier Graphic")
windows.geometry("500x300+200+200")
windows.resizable(False, False)
#===========================fonction object======================================
def show_message_object(error='', color='black'):
        label_error['text'] = error
        text_field['foreground'] = color
def validate(value):
    pattern = r'^(-?\d*(?:\.\d+)?[xy]\s*[+-]?\s*){2}$'
    if value == "":
        show_message_condition()
        return True
    elif re.fullmatch(pattern, value) is None:
        return False
    show_message_object()
    return True
def on_invalid_object():
    show_message_object('Please enter a valid value', 'red');label_error.grid(row= 0, column=3)
#===========================fonction condition======================================
def show_message_condition(error='', color='black'):
        label_error['text'] = error
        text_entring['foreground'] = color
def validate_condition(value):
    pattern = r'^(-?\d*(?:\.\d+)?[a-z]\s*[+-]?\s*)+(<=|>=|<|>)\s*-?\d+(\.\d+)?$'
    if value == "":
        show_message_condition()
        return True
    elif re.fullmatch(pattern, value) is None:
        return False
    show_message_condition()
    return True
def on_invalid_conditio():
    show_message_condition('Please enter a valid value1', 'red');label_error.grid(row= 1, column=4)
#===========================fonction editing======================================

#===========================fonction adding ======================================
def add_element():
    global i
    if text_entring.get()=="":
        show_message_object('Please enter value', 'red');label_error.grid(row= 4, column=0)
    else :
         list_condition.insert(i, text_entring.get());i+=1;print(list_condition.get(0,i));deleting["state"]=NORMAL
    list_condition.update()
i=0
#===========================fonction deleting=========================================
def delet_element():
    global i
    if i==-1:
        deleting["state"]=DISABLED
        return 
    else:
        list_condition.delete(i)
        i-=1
        if i==-1:
            deleting["state"]=DISABLED
    

#====================================================================================
operation_field = Frame(windows ); operation_field.pack(padx=10, pady=20, anchor='w')
label_error= Label(operation_field, fg= "red");
check_validate_object = operation_field.register(validate), "%P"
check_validate_condition = operation_field.register(validate_condition), "%P"
check_invalidate_object= operation_field.register(on_invalid_object)
check_invalidate_condition= operation_field.register(on_invalid_conditio)
#===============================PART MIN MAX======================================

Min_Max = ttk.Combobox(operation_field, values=["Max Z", "Min Z"], width= 7);Min_Max.current(0);Min_Max.grid(row= 0, column= 0)
text_field = Entry(operation_field, width= 20, validate="focusout", validatecommand=check_validate_object, invalidcommand=check_invalidate_object); text_field.grid(row= 0, column= 1)

#===============================PART CONDITION======================================

conditions = Label(operation_field, text = "Enter your conditions", width= 20);conditions.grid(row= 1, column= 0)
text_entring = Entry(operation_field, width= 20, validate="focusout", validatecommand=check_validate_condition, invalidcommand=check_invalidate_condition, ); text_entring.grid(row= 1, column= 1)

#===============================PART LIST AND BUTTON======================================
list_condition = Listbox(operation_field); list_condition.grid(row=3, column=0, columnspan=2)
add= Button(operation_field, text ="add", command=add_element);add.grid(row= 1, column= 3, padx=5)
deleting= Button(operation_field, text ="delet", command=delet_element);deleting.grid(row= 4, column= 3, padx=5)

#===============================END PROGRAM======================================
windows.mainloop()