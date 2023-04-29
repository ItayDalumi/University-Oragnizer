import tkinter as tk
from student import Student
from studnent_list import StudentList

FONT = ("Arial", 25)

def on_confirm_button_click():
    name = name_entry.get()
    sector = sector_entry.get()
    student = Student(name, sector)
    student_list.add_student(student)

def on_show_list_button_click():
    list_label.configure(text=str(student_list))

window = tk.Tk()
window.title("Student List")

# Create widgets
label = tk.Label(window, text="Enter Full Name:", font=FONT)
name_entry = tk.Entry(window, font=FONT)

sector_label = tk.Label(window, text="Enter Sector:", font=FONT)
sector_entry = tk.Entry(window, font=FONT)

confirm_button = tk.Button(window, text="Confirm", font=FONT, fg="blue",
                           command=on_confirm_button_click)
show_list_button = tk.Button(window, text="Show Student List", font=FONT, fg="green",
                             command=on_show_list_button_click)
list_label = tk.Label(window, font=FONT)

# Layout widgets
label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
sector_label.grid(row=1, column=0)
sector_entry.grid(row=1, column=1)
confirm_button.grid(row=2, column=0, columnspan=2, sticky="nsew")
show_list_button.grid(row=3, column=0, columnspan=2, sticky="nsew")
list_label.grid(row=4, column=0, columnspan=2, sticky="nsew")

# Initialize data
student_list = StudentList()

window.mainloop()
