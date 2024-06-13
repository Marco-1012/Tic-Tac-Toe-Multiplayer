import socket


class TicTacToe:
    field = [" ",
             "1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    def __init__(self, username):
        self.player = username
        self.score = 0
        self.rep = 1
        self.socket = None
        self.conn = None

    def decider(self):
        while True:
            try:
                choice = str(input("Do you want to create a game (c) or join a game (j): "))
            except ValueError:
                print("Please decide between (c/j): ")
            if choice not in ("c", "j"):
                print("Please decide between (c/j): ")
                continue
            else:
                if choice == "c":
                    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.socket.bind(("", 55000))
                    self.socket.listen(1)
                    print("Waiting for connection...")
                    self.conn, addr = self.socket.accept()
                    print(f"Connected to {addr}")
                    return choice
                else:
                    ip = input("please enter the IP-Address of the other player: ")
                    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.socket.connect((ip, 55000))
                    return choice


    def printfield(self):
        print(self.field[1] + "|" + self.field[2] + "|" + self.field[3])
        print(self.field[4] + "|" + self.field[5] + "|" + self.field[6])
        print(self.field[7] + "|" + self.field[8] + "|" + self.field[9])

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
            if (self.rep % 2) == 0:
                print("Player O won!")
                return True
            else:
                print("Player X won!")
                return True
        return False

    def playermove(self):
        while True:
            self.printfield()
            move = input("choose a field: ")
            try:
                move = int(move)
            except ValueError:
                print("enter a number\r")
                continue
            if not (1 <= move <= 9):
                print("Value must be between 1 and 9!\r")
                continue
            if self.field[move] == "X" or self.field[move] == "O":
                print("This field is already occupied!\r")
                continue
            else:
                if (self.rep % 2) == 0:
                    self.field[move] = "O"
                else:
                    self.field[move] = "X"
                self.rep += 1

            if self.rep == 10:
                print("Draw!")
                self.printfield()
                break
            if self.checkwin(self.rep - 1):
                self.printfield()
                break

            return move

    def opponent_move(self, move):
        if (self.rep % 2) == 0:
            self.field[move] = "O"
        else:
            self.field[move] = "X"
        self.rep += 1

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


Marco = TicTacToe("marco")
Marco.activegame()
