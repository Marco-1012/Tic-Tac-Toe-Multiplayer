from tkinter import *

def button_press(row, col):

    buttons[row][col].grid_forget()
    ersetzen = Label(fenster, text = "x")
    ersetzen.grid(row = row, column = col)

buttons=[]

fenster = Tk()

fenster.geometry("420x430")

for r in range(3):
    row=[]

    for c in range(3):
        b = Button(text = "Hallo", height = 9, width = 19, command = lambda r = r, c = c: button_press(r, c))
        b.grid(row = r, column = c)
        row.append(b)
    buttons.append(row)
    
print(buttons)
buttons[0][1].config(text = "Tshuss")

fenster.mainloop()