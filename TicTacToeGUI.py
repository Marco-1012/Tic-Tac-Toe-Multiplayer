from tkinter import *
from TicTacToe import TicTacToe

def button_press(row, col, counter):
    move = row * 3 + col + 1
    if ttt.playermove(move):
        buttons[row][col].config(text="X" if counter[0] % 2 == 0 else "O", state=DISABLED)
        counter[0] += 1
        if ttt.checkwin():
            result = "Player X won!" if counter[0] % 2 == 1 else "Player O won!"
            print(result)
            ttt.game_over = True
            end_game(result)
        if counter[0] == 9:
            result = "Draw!"
            print(result)
            ttt.game_over = True
            end_game(result)

def end_game(result):
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)
    result_label.config(text=result)

buttons = []
counter = [0]

fenster = Tk()
fenster.geometry("420x430")

result_label = Label(fenster, text="", font=("Helvetica", 16))
result_label.grid(row=3, columnspan=3)

for r in range(3):
    row = []

    for c in range(3):
        b = Button(fenster, text="", height=9, width=19, command=lambda r=r, c=c: button_press(r, c, counter))
        b.grid(row=r, column=c)
        row.append(b)
    buttons.append(row)

ttt = TicTacToe("marco")
ttt.activegame()

fenster.mainloop()
