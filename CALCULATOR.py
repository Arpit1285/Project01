# tkinter is a standard  library module used for create GUI elements.
import tkinter as tk
root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
def on_click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def percent():
    try:
        value = float(entry.get())
        result = value / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

import math
def square_root():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square():
    try:
        value = float(entry.get())
        result = value ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def double_zero():
    entry.insert(tk.END, '00')

buttons = [
    ('AC', 1, 0), ('%', 1, 1), ('⌫', 1, 2), ('/', 1, 3),
    ('7', 2, 0),  ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0),  ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0),  ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('00', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=calculate, bg='blue', fg='white')
    elif text == 'AC':
        btn = tk.Button(root, text=text, width=5, height=2, command=clear, bg='red', fg='white')
    elif text == '%':
        btn = tk.Button(root, text=text, width=5, height=2, command=percent, bg='seagreen', fg='white')
    elif text == '⌫':
        btn = tk.Button(root, text=text, width=5, height=2, command=backspace, bg='darkred', fg='white')
    elif text == '00':
        btn = tk.Button(root, text=text, width=5, height=2, command=double_zero, bg='grey', fg='white')
    elif text in ('+','-','/','*'):
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: on_click(t), bg='orange', fg='white')
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: on_click(t), bg='grey', fg='white')

    btn.grid(row=row, column=col, padx=5, pady=5)
root.mainloop()

