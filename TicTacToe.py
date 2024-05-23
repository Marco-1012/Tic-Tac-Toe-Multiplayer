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

    def playermove(self):
        rep = 1
        move = input("choose a field: ")
        try:
            move = int(move)
        except ValueError:
            print("enter a number\n")
        except 1 >= move >= 9:
            print("Value must be between 1 and 9!")
        if self.field[move] != "X" or "O":
            if (rep % 2) == 0:
                self.field[move] = "O"
                rep += 1
            else:
                self.field[move] = "X"
                rep += 1

    def activgame(self):
        self.printfield()
        self.playermove()
