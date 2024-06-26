# Planing
The goal is to build a TicTacToe-Multiplayer. The Project will be splitt in the following steps:

* The Base Game Tic-Tac-Toe in Terminal
* The Multiplayer extension
* The GUI 

In the base game everthing will be utilised in the python Terminal. </br>
During the Multiplayer extension the GUI can be started.

## UML
| TicTacToe                                      |
|------------------------------------------------|
| field: list<br/>match: int                     |
| printfield()<br/>playermove()<br/>activegame() |
 
TacTacToe will be changed to TicTacToe-MP (**M**ulti**p**layer)

| TicTacToe-MP                                                   |
|----------------------------------------------------------------|
| field: list<br/>match: int<br/>user: str                       |
| printfield()<br/>playermove()<br/>activegame()<br/>surrender() |

## Use-case Diagram
```mermaid
graph TD;
    User1-->SetX;
    User1-->SetO;
    User2-->SetX;
    User2-->SetO;
```
---

# Tic-Tac-Toe
Before making the game Multiplayer the base game will be Programmed to work for both users on one client in the [TicTacToe.py](./TicTacToe.py) and will later be extended to work in multiplayer on two clients

## The playingfield
To make the editing of the list easier an empty string has been positioned on field[0].
```python
field = [" ",
         "1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
```
Because now the player-chosen moves can directly be put into the list.

To output the playingfield like a normal tic-tac-toe field lines have been added.
```python
def printfield(self):
    print(self.field[1] + "|" + self.field[2] + "|" + self.field[3])
    print(self.field[4] + "|" + self.field[5] + "|" + self.field[6])
    print(self.field[7] + "|" + self.field[8] + "|" + self.field[9])
```
## Playermove
to keep track of whos turn it is the variable rep for repetition has been added.
```python
rep = 1
```
To garantie that the user has input an integer between one and nine a try except has been added.
The user also should not be able to take a field which allready has been used so each field is checked if it is occupied by an *X* or *O*.
```python
try:
    move = int(move)
except ValueError:
    print("enter a number\n")
if 1 >= move >= 9:
    print("Value must be between 1 and 9!")
if self.field[move] == "X" or "O":
    print("This field is allready occupied!")
```
If there are no exceptions the players will alternatingly get *X* and *O*'s
```python
else:
    if (rep % 2) == 0:
        self.field[move] = "O"
        rep += 1
    else:
        self.field[move] = "X"
        rep += 1
```
After each move by the player the repetition-counter will be increased by one.

## Check for a winner
To check for a winner the function **checkwinner()** has been added. </br>
For this every single winning condition has been written out with ...
* the first three being the rows
* the next three for the columns
* and the last two for the diagonals
```python
def checkwin(self, rep):
    if (
            (self.field[1] == self.field[2] == self.field[3]) or
            (self.field[4] == self.field[5] == self.field[6]) or
            (self.field[7] == self.field[8] == self.field[9]) or
            (self.field[1] == self.field[4] == self.field[7]) or
            (self.field[2] == self.field[5] == self.field[8]) or
            (self.field[3] == self.field[6] == self.field[9]) or
            (self.field[1] == self.field[5] == self.field[9]) or
            (self.field[3] == self.field[5] == self.field[7])
    ):
```
In case one of the statements has been fullfiled, the player at move will win and the function returns TRUE, if not the function will return FALSE, meaning nobody won yet
```python
if (rep % 2) == 0:
    print("Player O won!")
    return True
else:
    print("Player X won!")
    return True
return False
```
For the case of a draw following lines have been added to the **playermove()** function:
```python
if rep == 10:
    "draw"
    break
```
---
# TicTacToe Multiplayer extension
For the game to work in multiplayer, the socket library will be used.</br>

## Decision
TicTacToe will be played peer to peer, which means the programm will be either working as client and as server.</br>
When starting the .py the user will be asked if he wants to create or join a game, this will decide if the user is the server or the Client.</br>
Before we can make a server or a client we need to filter the input in the same way as in the base game.
```python
def decider(self):
    while True:
        try:
            choice = str(input("Do you want to create a game (c) or join a game (j): "))
        except ValueError:
            print("Please decide between (c/j): ")
        if choice not in ("c", "j"):
            print("Please decide between (c/j): ")
            continue
```
The choice will define the options given, to play you need to know the other players ip address.
```python
else:
    if choice == "c":
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(("", 55000))
            s.listen(1)
            print(socket.gethostbyname(socket.gethostname()))
            break
        else:
            ip = input("please enter the IP-Address of the other player: ")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                
            s.connect((ip, 55000))
            break
```
After choosing to be the server the user should wait until another player joins. 
```python
        print("Waiting for connection...")
        self.conn, addr = self.socket.accept()
        print(f"Connected to {addr}")
```

## The game itself
After the player has decided we can start the game. The Server will begin as **X**. To implement this the activegame() function has been changed.

The server will take following steps after deciding do be the server:
1. make a move
2. send the move to the other player
3. check if this move won the game
4. wait for opponents move and transmission
5. check if the other player won
```python
def activegame(self):
     choice = self.decider()
    if choice == "c":
        while True:
            move = self.playermove()
            self.conn.sendall(str(move).encode())
            if self.rep == 10 or self.checkwin(self.rep - 1):
                break
            print("Waiting for opponent's move...")
            data = self.conn.recv(1024).decode()
            self.opponent_move(int(data))
            if self.rep == 10 or self.checkwin(self.rep - 1):
                break
```
While the server is doing this the client will repeat following steps:
1. wait for opponents move (because the server starts)
2. check if the other player won
3. make a move
4. send the move to the other player
5. check if this move won the game
```python
else:
    while True:
        print("Waiting for opponent's move...")
        data = self.socket.recv(1024).decode()
        self.opponent_move(int(data))
        if self.rep == 10 or self.checkwin(self.rep - 1):
            break
        move = self.playermove()
        self.socket.sendall(str(move).encode())
        if self.rep == 10 or self.checkwin(self.rep - 1):
            break
```

## get the other players move on the board

To bring the other players move onto the board with the right sign the before mentioned opponent_move() function has been added.
```python
def opponent_move(self, move):
    if (self.rep % 2) == 0:
        self.field[move] = "O"
    else:
        self.field[move] = "X"
    self.rep += 1
```


---

# GUI

The Goal is to play the TicTacToe Multiplayer with a graphic interface

# Modules needed

We need to import modules in order to make the GUI work:

```python
from tkinter import *
from TicTacToe import TicTacToe
from concurrent.futures import ThreadPoolExecutor
```

The module TicTacToe is the imported function from the TicTacToe script. We need to implement in order to make it
possible to use the functions in the script.

# Button press function

First we nee a function which let's the programm know, if there is a win or a draw:

```python
def check_result():
    """
    returns True when player has won or it's a draw 
            False if game is still going.
    """
    print("check results started")
    if ttt.checkwin():
        Win_fenster = Tk()
        result = print(f"Player {ttt.current_turn} won!")
        fenster.destroy()
        win_label = Label(Win_fenster, text = f"Player {ttt.current_turn} won!")
        win_label.pack()
        print("WON")
        end_game(result)
        return True
    elif ttt.rep == 10:
        Win_fenster = Tk()
        print("Draw!")
        fenster.destroy()
        win_label = Label(Win_fenster, text = "Draw")
        win_label.pack()
        end_game("Draw!")
        return True
    else:
        return False
```

The checkwin function from the Tictactoe script is used to check if there is a win or a draw and to let the players know who won a
a new window will pop up and display if player **X**, player **O** wins or a draw happens

Next we need a function that lets the programm know which Button to disable 

```python
def button_press(row, col):
    if ttt.current_turn == ttt.my_character: 
        move = row * 3 + col
        if ttt.playermove(move):
            buttons[row][col].config(text=ttt.current_turn, state=DISABLED)
            ttt.send_move(move)
            if not check_result():
                ttt.current_turn = 'O' if ttt.current_turn == 'X' else 'X'
                background_thread.submit(wait_for_opponent_move)
```
And the __**ttt.my_character**__ is a property defined in the TicTacToe script:

```python
@property
    def my_character(self):
        if self.is_host:
            return "X"
        else:
            return "O"
    
    @property
    def opponent_character(self):
        if self.is_host:
            return "O"
        else:
            return "X"
```
It is also important to know that ttt is the Object from the TicTacToe script and is defined a little later:

```python
ttt = TicTacToe("marco")
```
It is checked if the player is the Host. The Host always begins and has the X.
If the player makes a move it is checked with the **playermove** Function. After it is checked the correspondig Button is disabled
and replaced with X or O

After ever round it is checked if there is a winner with the function **check_result**. If somone won the current player will get a message saying "won".

# Wait for opponent move Funtion

This function does like the name implies wat for the opponent to move

```python
def wait_for_opponent_move():
    print("Waiting for opponent move")
    move = ttt.receive_move()
    row, col = divmod(move, 3)
    ttt.opponent_move(move)
    buttons[row][col].config(text=ttt.opponent_character, state=DISABLED)
    if check_result() == False:
        ttt.current_turn = 'O' if ttt.current_turn == 'X' else 'X'
        print("oponenet move ended")
```

It waits to receive a move from the other player. 
After that the funtcion checks if there is a win or a draw and rewards the player who won
At the end of this function it checks if it needs to replace the button with O or with X

# End game

Now we have to know when the game is over.

```python
def end_game(result):
    ttt.game_over = True
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)
    result_label.config(text=result)

```
If the game over variable from the Script is **True** it disables all Buttons and changes the Label to **result**

# Changes to TicTacToe script

In order to make the two codes work together we have to change the TicTacToe script too.

First we need to add some things to the **__innit__** funktion:

The Function **printfield** was removed because it isn't neede anymore when the game is  played with the GUI:

```python
 def printfield(self):
        print(self.field[1] + "|" + self.field[2] + "|" + self.field[3])
        print(self.field[4] + "|" + self.field[5] + "|" + self.field[6])
        print(self.field[7] + "|" + self.field[8] + "|" + self.field[9])
```

