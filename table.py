from tkinter import *


class table:
    def __init__(self, root):
        for i in total_row:
            for j in total_column:
                self.e = Entry(root, width=20, font=("italic", 16, "bold"))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])