from tkinter import *

def click(event):
    current = ent.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            ent.delete(0, END)
            ent.insert(END, str(result))
        except Exception as e:
            ent.delete(0, END)
            ent.insert(END, "Error")

    elif text == "C":
        ent.delete(0, END)

    else:
        ent.insert(END, text)

root = Tk()
root.title('Calculator')
root.geometry('300x400')

ent = Entry(root, width=16, font=('Arial', 20), justify=RIGHT)
ent.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    btn = Button(root, text=button, width=5, height=2, font=('Arial', 15), relief="ridge")
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    btn.bind('<Button-1>', click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
