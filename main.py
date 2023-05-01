from tkinter import ttk
import tkinter as tk

screen = ""

def add_to_screen(symbol):
    global screen
    screen += str(symbol)
    text_field.delete(1.0, "end")
    text_field.insert(1.0, screen)


def eval_screen():
    global screen
    try:
        result = eval(screen)
        text_field.delete(1.0, "end")
        screen = str(result)
        text_field.insert(1.0, result)
    except:
        text_field.delete(1.0, "end")
        text_field.insert(1.0, "Error")

def clear_screen():
    global screen
    screen = ""
    text_field.delete(1.0, "end")
    text_field.insert(1.0, screen)


root = tk.Tk(
    className= "Calculator"
)
# root.geometry()

text_field = tk.Text(root, height=2, width=16, font= ("Arrial", 24) )
text_field.grid(columnspan=5)
button_1 = ttk.Button(root, text="9", command=lambda: add_to_screen(9)).grid(column=0, row=1)
button_2 = ttk.Button(root, text="8", command=lambda: add_to_screen(8)).grid(column=1, row=1)
button_3 = ttk.Button(root, text="7", command=lambda: add_to_screen(7)).grid(column=2, row=1)
button_4 = ttk.Button(root, text="6", command=lambda: add_to_screen(6)).grid(column=0, row=2)
button_5 = ttk.Button(root, text="5", command=lambda: add_to_screen(5)).grid(column=1, row=2)
button_6 = ttk.Button(root, text="4", command=lambda: add_to_screen(4)).grid(column=2, row=2)
button_7 = ttk.Button(root, text="3", command=lambda: add_to_screen(3)).grid(column=0, row=3)
button_8 = ttk.Button(root, text="2", command=lambda: add_to_screen(2)).grid(column=1, row=3)
button_9 = ttk.Button(root, text="1", command=lambda: add_to_screen(1)).grid(column=2, row=3)
button_10 = ttk.Button(root, text="0", command=lambda: add_to_screen(0)).grid(column=0, row=4)
button_11 = ttk.Button(root, text="(", command=lambda: add_to_screen("(")).grid(column=1, row=4)
button_12 = ttk.Button(root, text=")", command=lambda: add_to_screen(")")).grid(column=2, row=4)
button_13 = ttk.Button(root, text="+", command=lambda: add_to_screen("+")).grid(column=3, row=1)
button_14 = ttk.Button(root, text="-", command=lambda: add_to_screen("-")).grid(column=3, row=2)
button_15 = ttk.Button(root, text="*", command=lambda: add_to_screen("*")).grid(column=3, row=3)
button_16 = ttk.Button(root, text="/", command=lambda: add_to_screen("/")).grid(column=3, row=4)
button_equal = ttk.Button(root, text="=", command= eval_screen).grid(column=0, row=5,columnspan=3)
button_clear = ttk.Button(root, text="C", command= clear_screen).grid(column=1, row=5,columnspan=4)
root.mainloop()