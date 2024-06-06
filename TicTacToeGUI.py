from tkinter import *

buttons=[]

fenster = Tk()

fenster.geometry("400x400")

for r in range(3):
    row=[]

    for c in range(3):
        b = Button(text = "Hallo")
        b.grid(row = r, column = c)
        row.append(b)
    buttons.append(row)
    
print(buttons)
buttons[0][1].config(text = "Tshuss")
fenster.mainloop()