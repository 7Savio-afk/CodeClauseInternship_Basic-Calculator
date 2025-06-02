import tkinter as tk

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

entry = tk.Entry(root, width=16, font=('Arial', 24), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
                  command=lambda t=text: button_click(t)).grid(row=row, column=col)

tk.Button(root, text='C', width=22, height=2, font=('Arial', 18),
          command=clear_entry).grid(row=5, column=0, columnspan=4)

root.mainloop()