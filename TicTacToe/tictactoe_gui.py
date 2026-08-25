import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
)
from skills import MySystemUtils


def start_game():
    game_window = GameWindow(player_1_name = title_window.player_1_input_box.text(), player_2_name = title_window.player_2_input_box.text(), player_1_symbol = title_window.player_1_dropdown.currentText(), player_2_symbol = title_window.player_2_dropdown.currentText())
    game_window.show()
    title_window.close()



class TitleWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(500, 500))
        self.setWindowTitle("Maksim's Tic-Tac-Toe Game")

        #* Main Menu

        self.titel_text = QtWidgets.QLabel("Tic-Tac-Toe", alignment=QtCore.Qt.AlignHCenter)

        # Player 1
        player_1_symbol = self.player_1_dropdown = QtWidgets.QComboBox()  # noqa: F841
        self.player_1_dropdown.addItems(["X", "O"])
        self.player_1_dropdown.setCurrentText("X")
        self.player_1_name_label = QtWidgets.QLabel("Player 1 Name:")
        self.player_1_symbol_label = QtWidgets.QLabel("Player 1 Symbol:")
        player_1_name = self.player_1_input_box = QtWidgets.QLineEdit()  # noqa: F841


        # Player 2
        player_2_symbol = self.player_2_dropdown = QtWidgets.QComboBox()  # noqa: F841
        self.player_2_dropdown.addItems(["X", "O"])
        self.player_2_dropdown.setCurrentText("O")
        self.player_2_name_label = QtWidgets.QLabel("Player 2 Name:")
        self.player_2_symbol_label = QtWidgets.QLabel("Player 2 Symbol:")
        player_2_name = self.player_2_input_box = QtWidgets.QLineEdit()  # noqa: F841

        self.player_1_dropdown.currentIndexChanged.connect(self._sync_player_symbols)
        self.player_2_dropdown.currentIndexChanged.connect(self._sync_player_symbols)

        self.start_button = QtWidgets.QPushButton("Start")


        # Layout
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(80, 40, 80, 40)
        self.layout.setSpacing(16)
        self.layout.addWidget(self.titel_text)

        self.player_layout = QtWidgets.QGridLayout()
        self.player_layout.setHorizontalSpacing(12)
        self.player_layout.setVerticalSpacing(10)
        self.player_layout.setColumnStretch(1, 1)
        self.player_layout.addWidget(self.player_1_name_label, 0, 0)
        self.player_layout.addWidget(self.player_1_input_box, 0, 1)
        self.player_layout.addWidget(self.player_1_symbol_label, 1, 0)
        self.player_layout.addWidget(self.player_1_dropdown, 1, 1)
        self.player_layout.addWidget(self.player_2_name_label, 2, 0)
        self.player_layout.addWidget(self.player_2_input_box, 2, 1)
        self.player_layout.addWidget(self.player_2_symbol_label, 3, 0)
        self.player_layout.addWidget(self.player_2_dropdown, 3, 1)
        self.layout.addLayout(self.player_layout)
        self.layout.addStretch()
        self.layout.addWidget(self.start_button)



        self.start_button.clicked.connect(self.start_button_clicked)

    def _sync_player_symbols(self):
        player_1_symbol = self.player_1_dropdown.currentText()
        player_2_symbol = self.player_2_dropdown.currentText()

        if player_1_symbol == player_2_symbol:
            sender = self.sender()
            if sender == self.player_1_dropdown:
                self.player_2_dropdown.setCurrentText("O" if player_1_symbol == "X" else "X")
            elif sender == self.player_2_dropdown:
                self.player_1_dropdown.setCurrentText("O" if player_2_symbol == "X" else "X")

    def start_button_clicked(self):
        start_game()






class GameWindow(QtWidgets.QWidget):
    def __init__(self, player_1_name, player_2_name, player_1_symbol, player_2_symbol):
        super().__init__()

        # TODO: Implement the game logic and UI for Tic Tac Toe

        
        self.TitleLabel = QtWidgets.QLabel("Tic Tac Toe", alignment=QtCore.Qt.AlignHCenter)
        title_font = QFont()
        title_font.setBold(True)
        self.TitleLabel.setFont(title_font)
        self.setFixedSize(QSize(500, 500))
        self.setWindowTitle("Game")
        
        self.player_1_label = QtWidgets.QLabel(
            f"{player_1_name} ({player_1_symbol})"
        )
        self.player_2_label = QtWidgets.QLabel(
            f"{player_2_name} ({player_2_symbol})"
        )

        self.spielfeld = QtWidgets.QGridLayout()
        self.spielfeld.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spielfeld.setHorizontalSpacing(10)
        self.spielfeld.setVerticalSpacing(10)

        for row in range(3):
            for column in range(3):
                button = QtWidgets.QPushButton()
                button.setFixedSize(100, 100)
                button.setStyleSheet("font-size: 24px;")
                self.spielfeld.addWidget(button, row, column)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.player_1_label)
        self.layout.addWidget(self.player_2_label)
        self.layout.addWidget(self.TitleLabel)
        self.layout.addLayout(self.spielfeld)


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
            MySystemUtils.exit()


    def all_checks(self):    
        # Horizontal
        h_win_X, h_win_O = self.check_horizontal()

        # Vertikal
        v_win_X, v_win_O = self.check_vertical()

        # Diagonal
        d_win_X, d_win_O = self.check_diagonal()


        if h_win_X == True or v_win_X == True or d_win_X == True:
            if GameWindow.p2_symbol == 'O':  
                print(f"{GameWindow.p1_name} won!")
                MySystemUtils.exit()
            else:
                print(f"{GameWindow.p2_name} won!")
                MySystemUtils.exit()

        elif h_win_O == True or v_win_O == True or d_win_O == True:
            if GameWindow.p1_symbol == 'X':
                print(f"{GameWindow.p2_name} won!")
                MySystemUtils.exit()
            else:
                print(f"{GameWindow.p1_name} won!")
                MySystemUtils.exit()

        elif self.games_played >= 9:
            print("Draw!")
            MySystemUtils.exit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    title_window = TitleWindow()

    title_window.show()

    sys.exit(app.exec())