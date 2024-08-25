from tkinter import *

window = Tk()
window.config(width=400, height=500)
window.title("Calculator")

entry = Entry(window, width=16, bd=4, insertwidth=4, borderwidth=4, font=("Arial", 20, "normal"))
entry.grid(row=0, column=0, columnspan=4)

def evaluate_expression():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

def clear_screen():
    entry.delete(0, END)

def update_expression(number):
    expression = entry.get()
    entry.delete(0, END)
    entry.insert(END, expression + str(number))

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+', '='
]
clear=Button(command=clear_screen,text="Clear",font=("Arial",18),padx=20,pady=20,bd=4,width=20)
clear.grid(row=5,column=0,columnspan=4)

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        Button(window, text=button, padx=20, pady=20, bd=4, font=('Arial', 18),
               command=evaluate_expression).grid(row=row_val, column=col_val, columnspan=4, sticky="nsew")
    elif button == "C":
        Button(window, text=button, padx=20, pady=20, bd=4, font=("Arial", 18, "normal"),
               command=clear_screen).grid(row=row_val, column=col_val, columnspan=3, sticky="nsew")
    else:
        Button(window, text=button, padx=20, pady=20, bd=4, font=('Arial', 18),
               command=lambda b=button: update_expression(b)).grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
