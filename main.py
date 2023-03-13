from tkinter import *

student_list = []
Font = ("ariel",25)

class student:
    def __init__(self,name,sector):
        self.name = name
        self.sector = sector
        student_list.append(self.name + " : " + self.sector)

def confirm():
    name = name_box.get()
    sector = sector_box.get()
    student(name,sector)

def show():
    show_list_label = Label(window,text=student_list,font=Font)
    show_list_label.grid(row=5,column=0,columnspan=2,sticky="nsew")

window = Tk()

label = Label(window,text="Enter Full Name: ",font=Font)
label.grid(row=0,column=0)

name_box = Entry(window,font=Font)
name_box.grid(row=0,column=1)

sector_label = Label(window,text="Enter Sector",font=Font)
sector_label.grid(row=1,column=0)

sector_box = Entry(window,font=Font)
sector_box.grid(row=1,column=1)

Confirm_button = Button(window,text="Confirm",font=Font,fg="Blue",command=confirm)
Confirm_button.config(height=2, width=10)
Confirm_button.grid(row=3,column=0,columnspan=2,sticky="nsew")

show_list = Button(window,text="show student list",font=Font,fg="Green",command=show)
show_list.grid(row=4,column=0,columnspan=2,sticky="nsew")


window.mainloop()
