from tkinter import *
from TicTacToe import TicTacToe

def button_press(row, col):

    if TicTacToe.rep%2 == 0:
    
        buttons[row][col].config(text = "0", state = DISABLED)
    else:
        buttons[row][col].config(text = "x", state = DISABLED)

    pressedButtonrow = row
    pressedButtoncol = col
    print(pressedButtonrow, pressedButtoncol)

#Marco objekt
Marco = TicTacToe("Marco")

buttons=[]
pressedButtonrow = 0
pressedButtoncol = 0

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