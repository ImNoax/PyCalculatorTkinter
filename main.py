import tkinter as tk

calculation = ""
empty = True
#Add to entry
def add_to_calculation(symbol, isOpe):
    global calculation
    global empty
    if empty | isOpe:
        empty = True
        calculation += str(symbol)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    else:
        clear_field()
        add_to_calculation(symbol, False)
#Evaluate entry
def evaluate_calculation():
    global calculation
    global empty
    empty = False
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
        
    except ZeroDivisionError:
        clear_field()
        text_result.insert(1.0, "Error: Div by zero")
    except SyntaxError:
        clear_field()
        text_result.insert(1.0, "Error: Invalid syntax")
    except Exception as e:
        clear_field()
        text_result.insert(1.0, "Error")
#Clear entry
def clear_field():
    global calculation
    global empty
    empty = True
    calculation = ""
    text_result.delete(1.0, "end")

def disable_keyboard(event):
    return "break"  # Bloquer l'événement de clavier

root = tk.Tk() #Object creation
root.geometry("300x275") #Base size
root.resizable(False, False) #Block resizing

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)
text_result.bind("<Key>", disable_keyboard) #Stop keyboard entry

# Numbers placements
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1, False), width=5, font =("Arial", 14))
btn_1.grid(row = 2, column = 1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2, False), width=5, font =("Arial", 14))
btn_2.grid(row = 2, column = 2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3, False), width=5, font =("Arial", 14))
btn_3.grid(row = 2, column = 3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4, False), width=5, font =("Arial", 14))
btn_4.grid(row = 3, column = 1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5, False), width=5, font =("Arial", 14))
btn_5.grid(row = 3, column = 2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6, False), width=5, font =("Arial", 14))
btn_6.grid(row = 3, column = 3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7, False), width=5, font =("Arial", 14))
btn_7.grid(row = 4, column = 1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8, False), width=5, font =("Arial", 14))
btn_8.grid(row = 4, column = 2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9, False), width=5, font =("Arial", 14))
btn_9.grid(row = 4, column = 3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0, False), width=5, font =("Arial", 14))
btn_0.grid(row = 5, column = 2)

#Button Operation
btn_Add = tk.Button(root, text="+", command=lambda: add_to_calculation("+", True), width=5, font =("Arial", 14))
btn_Add.grid(row = 2, column = 4)

btn_Sub = tk.Button(root, text="-", command=lambda: add_to_calculation("-", True), width=5, font =("Arial", 14))
btn_Sub.grid(row = 3, column = 4)

btn_Mul = tk.Button(root, text="x", command=lambda: add_to_calculation("*", True), width=5, font =("Arial", 14))
btn_Mul.grid(row = 4, column = 4)

btn_Div = tk.Button(root, text="/", command=lambda: add_to_calculation("/", True), width=5, font =("Arial", 14))
btn_Div.grid(row = 5, column = 4)

#Button parentheses
btn_OpenP = tk.Button(root, text="(", command=lambda: add_to_calculation("(", False), width=5, font =("Arial", 14))
btn_OpenP.grid(row = 5, column = 1)

btn_CloseP = tk.Button(root, text=")", command=lambda: add_to_calculation(")", False), width=5, font =("Arial", 14))
btn_CloseP.grid(row = 5, column = 3)

## Button Equal and Clear
btn_Clear = tk.Button(root, text="Clear", command=clear_field, width=11, font =("Arial", 14))
btn_Clear.grid(row = 6, column = 1, columnspan=2)

btn_Equal = tk.Button(root, text="=", command=evaluate_calculation, width=11, font =("Arial", 14))
btn_Equal.grid(row = 6, column = 3, columnspan=2)

root.mainloop()