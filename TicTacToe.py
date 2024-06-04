class TicTacToe:
    field = [" ",
             "1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    def __init__(self, username):
        self.player = username

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
            if (rep % 2) == 0:
                print("Player O won!")
                return True
            else:
                print("Player X won!")
                return True
        return False

    def playermove(self):
        rep = 1
        while True:
            self.printfield()
            move = input("choose a field: ")
            try:
                move = int(move)
            except ValueError:
                print("enter a number\r")
                continue
            if 1 >= move >= 9:
                print("Value must be between 1 and 9!\r")
                continue
            if self.field[move] == "X" or self.field[move] == "O":
                print("This field is allready occupied!\r")
                continue
            else:
                if (rep % 2) == 0:
                    self.field[move] = "O"
                    rep += 1
                else:
                    self.field[move] = "X"
                    rep += 1
            if rep == 10:
                "draw"
                break
            if self.checkwin(rep):
                break



    def activgame(self):
        self.playermove()


Marco = TicTacToe("marco")
Marco.activgame()
