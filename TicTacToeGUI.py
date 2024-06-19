from tkinter import *

def button_press(row, col):
    global counter
    if counter % 2 == 0:
        buttons[row][col].config(text="X", state=DISABLED)
    else:
        buttons[row][col].config(text="O", state=DISABLED)

    pressedButtonrow = row
    pressedButtoncol = col
    counter += 1
    print(pressedButtonrow, pressedButtoncol, counter)


buttons = []
pressedButtonrow = 0
pressedButtoncol = 0
counter = 0

fenster = Tk()
fenster.geometry("420x430")

for r in range(3):
    row = []

    for c in range(3):
        b = Button(text="", height=9, width=19, command=lambda r=r, c=c: button_press(r, c))
        b.grid(row=r, column=c)
        row.append(b)
    buttons.append(row)
    
print(buttons)

fenster.mainloop()
