from tkinter import *
from TicTacToe import TicTacToe
import threading

def button_press(row, col):
    move = row * 3 + col + 1
    if ttt.playermove(move):
        buttons[row][col].config(text="X" if ttt.rep % 2 == 0 else "O", state=DISABLED)
        if ttt.checkwin():
            result = "Player X won!" if ttt.rep % 2 == 1 else "Player O won!"
            end_game(result)
        elif ttt.rep == 10:
            end_game("Draw!")
        else:
            ttt.send_move(move)
            fenster.after(100, wait_for_opponent_move)

def wait_for_opponent_move():
    move = ttt.receive_move()
    row, col = divmod(move - 1, 3)
    ttt.opponent_move(move)
    buttons[row][col].config(text="X" if ttt.rep % 2 == 1 else "O", state=DISABLED)
    if ttt.checkwin():
        result = "Player X won!" if ttt.rep % 2 == 0 else "Player O won!"
        end_game(result)
    elif ttt.rep == 10:
        end_game("Draw!")

def end_game(result):
    ttt.game_over = True
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
        b = Button(fenster, text="", height=9, width=19, command=lambda r=r, c=c: button_press(r, c))
        b.grid(row=r, column=c)
        row.append(b)
    buttons.append(row)

ttt = TicTacToe("marco")

def start_game():
    ttt.activegame()
    if not ttt.is_host:
        wait_for_opponent_move()

threading.Thread(target=start_game).start()

fenster.mainloop()
