import socket
import threading

class TicTacToe:
    def __init__(self):
        self.rep = 1
        self.socket = None
        self.conn = None
        self.field = [" "] * 10
        self.game_over = False
        self.is_host = False
        self.lock = threading.Lock()
        self.current_turn = 'X'
    
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

    @staticmethod
    def decider(self):
        while True:
            choice = input("Do you want to create a game (c) or join a game (j): ").strip().lower()
            if choice not in ("c", "j"):
                print("Please decide between (c/j): ")
                continue
            else:
                return choice

    def checkwin(self):
        win_patterns = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),
            (1, 4, 7), (2, 5, 8), (3, 6, 9),
            (1, 5, 9), (3, 5, 7)
        ]
        for pattern in win_patterns:
            if self.field[pattern[0]] == self.field[pattern[1]] == self.field[pattern[2]] and self.field[pattern[0]] != " ":
                return True
        return False

    def playermove(self, move):   
        with self.lock:
            if self.field[move] == "X" or self.field[move] == "O":
                return False
            self.field[move] = self.my_character
            self.rep += 1
            return True

    def opponent_move(self, move):
        with self.lock:
            self.field[move] = self.opponent_character
            self.rep += 1

    def activate_game(self):
        print("game is active")
        choice = self.decider()
        if choice == "c":
            self.is_host = True
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind(("", 55000))
            self.socket.listen(1)
            print("Waiting for connection...")
            self.conn, addr = self.socket.accept()
            print(f"Connected to {addr}")
        else:
            ip = input("Please enter the IP-Address of the other player: ").strip()
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((ip, 55000))
            self.conn = self.socket

    def send_move(self, move):
        self.conn.sendall(str(move).encode())

    def receive_move(self):
        return int(self.conn.recv(1024).decode())
