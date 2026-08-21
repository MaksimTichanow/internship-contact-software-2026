import unittest
import sys

def exit():
    sys.exit()

class Spielfeld:
    def __init__(self):
        self.spielfeld = [

            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],

        ]
        self.games_played = 0

    def banner(self):
        print(f"""
############################################################################################
                
░██████████░██           ░██████████                      ░██████████                      
    ░██                      ░██                              ░██                          
    ░██    ░██ ░███████      ░██     ░██████    ░███████      ░██     ░███████   ░███████  
    ░██    ░██░██    ░██     ░██          ░██  ░██    ░██     ░██    ░██    ░██ ░██    ░██ 
    ░██    ░██░██            ░██     ░███████  ░██            ░██    ░██    ░██ ░█████████ 
    ░██    ░██░██    ░██     ░██    ░██   ░██  ░██    ░██     ░██    ░██    ░██ ░██        
    ░██    ░██ ░███████      ░██     ░█████░██  ░███████      ░██     ░███████   ░███████  

############################################################################################
""")  

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

        # check diagonal uper left to lower right
        win_X = self.spielfeld[0][0] == 'X' and self.spielfeld[1][1] == 'X' and self.spielfeld[2][2] == 'X'
        win_O = self.spielfeld[0][0] == 'O' and self.spielfeld[1][1] == 'O' and self.spielfeld[2][2] == 'O'

        # check diagonal lower right to uper left
        if not win_X and not win_O:
            win_X = self.spielfeld[0][2] == 'X' and self.spielfeld[1][1] == 'X' and self.spielfeld[2][0] == 'X'
            win_O = self.spielfeld[0][2] == 'O' and self.spielfeld[1][1] == 'O' and self.spielfeld[2][0] == 'O'

        return win_X, win_O

    def draw_check(self):
        h_win_X, h_win_O = self.check_horizontal()
        d_win_X, d_win_O = self.check_diagonal()
        v_win_X, v_win_O = self.check_vertical()
        if h_win_X == False and h_win_O == False and d_win_X == False and d_win_O == False and v_win_X == False and v_win_O == False and self.games_played > 9:
            print("Draw!")
            exit()
  

    def all_checks(self):    
        # Horizontal
        h_win_X, h_win_O = self.check_horizontal()

        # Vertikal
        v_win_X, v_win_O = self.check_vertical()

        # Diagonal
        d_win_X, d_win_O = self.check_diagonal()


        if h_win_X == True or v_win_X == True or d_win_X == True:
            if game.p2_symbol == 'O':
                print(f"{game.p1_name} won!")
                exit()
            else:
                print(f"{game.p2_name} won!")
                exit()

        elif h_win_O == True or v_win_O == True or d_win_O == True:
            if game.p1_symbol == 'X':
                print(f"{game.p2_name} won!")
                exit()
            else:
                print(f"{game.p1_name} won!")
                exit()

        elif self.games_played >= 9:
            print("Draw!")
            exit()
            


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
        self.p1_turn = None
        self.p2_turn = None
        self.winner = self.board.all_checks()

    def get_player_names(self):
        self.p1_name = input("Player 1 Name: ")
        self.p2_name = input("Player 2 Name: ")

    def get_player_symbol(self):
        self.p1_symbol = input(f"{self.p1_name} symbol(X/O): ")
        self.p2_symbol = input(f"{self.p2_name} symbol(X/O): ")

        if self.p1_symbol == '0' or self.p2_symbol == '0':
            print("Please use Letters!")
            self.get_player_symbol()
        elif self.p1_symbol == 'x' or self.p2_symbol == 'x':
            print("Please use Capital Letters!")
            self.get_player_symbol()


    def start_turn_check(self):
        if self.p1_symbol == "X":
            print(f"{self.p1_name} starts!")
            self.p1_turn = True
            self.p2_turn = False

        elif self.p2_symbol == "X":
            self.p1_turn = False
            self.p2_turn = True
            print(f"{self.p2_name} starts!")
        

    def player_input(self):
        # Player 1
        if self.p1_turn == True:
            print(f"{self.p1_name}'s Turn")
            z = int(input("Zeile: "))
            s = int(input("Spalte: "))
            self.board.set_field_value(z, s, self.p1_symbol)
            self.p1_turn = False
            self.p2_turn = True

        # Player 2
        elif self.p2_turn == True:
            print(f"{self.p2_name}'s Turn")
            z = int(input("Zeile: "))
            s = int(input("Spalte: "))
            self.board.set_field_value(z, s, self.p2_symbol)
            self.p2_turn = False
            self.p1_turn = True


game = TicTacToe()


# Spielablauf
game.board.banner()
game.get_player_names()
game.get_player_symbol()
game.start_turn_check()

while True:
    game.board.spielfeld_output()
    game.board.all_checks()
    game.player_input()







# Win Check Test
# board.set_field_value(0, 0, 'X')
# board.set_field_value(0, 1, 'X')
# board.set_field_value(0, 2, 'X')
# board.spielfeld_output()
# win_X, win_O = board.check_horizontal()
# print(f"X won! {win_X}")
# print(f"O won! {win_O}")
