import subprocess


class Spielfeld:
    def __init__(self):
        self.spielfeld = [

            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],

        ]

    def set_field_value(self, x, y, val):
        self.spielfeld[x][y] = val

    def check_horizontal(self):
        win_X = False
        win_O = False
        for zeile in self.spielfeld:
            win_X = win_X or (zeile[0] == 'X' and zeile[1] == 'X' and zeile[2] == 'X')
            win_O = win_O or (zeile[0] == 'O' and zeile[1] == 'O' and zeile[2] == 'O')
        return win_X, win_O

    def check_vertical(self):
        win_X = False
        win_O = False
        for spalte in range(3):
            win_X = win_X or (self.spielfeld[0][spalte] == 'X' and self.spielfeld[1][spalte] == 'X' and self.spielfeld[2][spalte] == 'X')
            win_O = win_O or (self.spielfeld[0][spalte] == 'O' and self.spielfeld[1][spalte] == 'O' and self.spielfeld[2][spalte] == 'O')
        return win_X, win_O

    def check_diagonal(self):
        win_X = False
        win_O = False

        win_X = win_X or (self.spielfeld[0][0] == 'X' and self.spielfeld[1][1] == 'X' and self.spielfeld[2][2] == 'X')
        win_O = win_O or (self.spielfeld[0][0] == 'O' and self.spielfeld[1][1] == 'O' and self.spielfeld[2][2] == 'O')

        if not win_X and not win_O:

            win_X = win_X or (self.spielfeld[0][2] == 'X' and self.spielfeld[1][1] == 'X' and self.spielfeld[2][0] == 'X')
            win_O = win_O or (self.spielfeld[0][2] == 'O' and self.spielfeld[1][1] == 'O' and self.spielfeld[2][0] == 'O')

        return win_X, win_O

    def spielfeld_output(self):
        print("-------")
        for zeile in self.spielfeld:
            print(f"|{zeile[0]}|{zeile[1]}|{zeile[2]}|")
            print("-------")


class TicTacToe:
    def __init__(self):
        self.board=Spielfeld()
        self.p1_name = "NONE"
        self.p2_name = "NONE"
        self.p1_symbol = "NONE"
        self.p2_symbol = "NONE"
        self.p1_turn = False
        self.p2_turn = False

    def get_player_names(self):
        self.p1_name = input("Player 1 Name: ")
        self.p2_name = input("Player 2 Name: ")

    def get_player_symbol(self):
        self.p1_symbol = input (f"{self.p1_name} symbol(X/O): ")
        self.p2_symbol = input (f"{self.p2_name} symbol(X/O): ")

        if self.p1_symbol or self.p2_symbol == '0' or self.p1_symbol or self.p2_symbol == 'o':
            print("Please use Capital Letters!")
            self.get_player_symbol()
        elif self.p1_symbol or self.p2_symbol == 'x':
            print("Please use Capital Letters!")
            self.get_player_symbol()



    def turn_check(self):
        if self.p1_symbol == "X":
            print(f"{self.p1_name} starts!")
            self.p1_turn = True
            self.p2_turn = False
            self.player_input()

        elif self.p2_symbol == "X":
            self.p1_turn = False
            self.p2_turn = True
            print(f"{self.p2_name} starts!")
        

    def player_input(self):
        self.turn_check()
        board.set_field_value(z, s, self.get_player_symbol())
        if self.p1_turn == True:
            print(f"{self.p1_name}'s Turn")
            z = int(input("Zeile: "))
            s = int(input("Spalte: "))

        elif self.p2_turn == True:
            print(f"{self.p2_name}'s Turn")
            z = int(input("Zeile: "))
            s = int(input("Spalte: "))


board = Spielfeld()


# Win Check Test
board.set_field_value(0, 0, 'X')
board.set_field_value(0, 1, 'X')
board.set_field_value(0, 2, 'X')
board.spielfeld_output()
win_X, win_O = board.check_horizontal()
print(f"X won! {win_X}")
print(f"O won! {win_O}")