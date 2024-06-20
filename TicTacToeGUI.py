from tkinter import *
from TicTacToe import TicTacToe
from concurrent.futures import ThreadPoolExecutor

background_thread = ThreadPoolExecutor(1)


def check_result():
    """
    returns True when player has won or it's a draw 
            False if game is still going.
    """
    print("check results started")
    if ttt.checkwin():
        win_fenster = Tk()
        print(ttt.current_turn)
        print(f"Player {ttt.current_turn} won!")
        fenster.destroy()
        win_label = Label(win_fenster, text=f"Player {ttt.current_turn} won!")
        win_label.pack()
        print("WON")
        return True
    elif ttt.rep == 10:
        win_fenster = Tk()
        print("Draw!")
        fenster.destroy()
        win_label = Label(win_fenster, text="Draw")
        win_label.pack()
        return True
    else:
        return False
        

def button_press(row, col):
    if ttt.current_turn == ttt.my_character: 
        move = row * 3 + col
        if ttt.playermove(move):
            buttons[row][col].config(text=ttt.current_turn, state=DISABLED)
            ttt.send_move(move)
            if not check_result():
                ttt.current_turn = 'O' if ttt.current_turn == 'X' else 'X'
                background_thread.submit(wait_for_opponent_move)


def wait_for_opponent_move():
    print("Waiting for opponent move")
    move = ttt.receive_move()
    row, col = divmod(move, 3)
    ttt.opponent_move(move)
    buttons[row][col].config(text=ttt.opponent_character, state=DISABLED)
    if not check_result():
        ttt.current_turn = 'O' if ttt.current_turn == 'X' else 'X'


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

ttt = TicTacToe()


def start_game():
    ttt.activate_game()
    if ttt.current_turn != ttt.my_character:
        wait_for_opponent_move()


background_thread.submit(start_game)

fenster.mainloop()