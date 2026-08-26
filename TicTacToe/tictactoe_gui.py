import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
)
from skills import MySystemUtils


def start_game():
    title_window.game_window = GameWindow(
        player_1_name = title_window.player_1_name_input.text(),
        player_2_name = title_window.player_2_name_input.text(),
        player_1_symbol = title_window.player_1_symbol_dropdown.currentText(),
        player_2_symbol = title_window.player_2_symbol_dropdown.currentText(),)
    title_window.game_window.show()
    title_window.close()


class TitleWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Widgets, Variablen, Layouts 

        self.setFixedSize(QSize(400, 350))
        self.setWindowTitle("Maksim's Tic-Tac-Toe Game")

        self.title_label = QtWidgets.QLabel("Tic-Tac-Toe", alignment=QtCore.Qt.AlignHCenter)

        self.player_1_symbol_dropdown = QtWidgets.QComboBox()
        self.player_1_symbol_dropdown.addItems(["X", "O"])
        self.player_1_symbol_dropdown.setCurrentText("X")
        self.player_1_name_label = QtWidgets.QLabel("Player 1 Name:")
        self.player_1_symbol_label = QtWidgets.QLabel("Player 1 Symbol:")
        self.player_1_name_input = QtWidgets.QLineEdit()

        self.player_2_symbol_dropdown = QtWidgets.QComboBox()
        self.player_2_symbol_dropdown.addItems(["X", "O"])
        self.player_2_symbol_dropdown.setCurrentText("O")
        self.player_2_name_label = QtWidgets.QLabel("Player 2 Name:")
        self.player_2_symbol_label = QtWidgets.QLabel("Player 2 Symbol:")
        self.player_2_name_input = QtWidgets.QLineEdit()

        self.player_1_symbol_dropdown.currentIndexChanged.connect(self.check_player_symbols)
        self.player_2_symbol_dropdown.currentIndexChanged.connect(self.check_player_symbols)

        self.start_button = QtWidgets.QPushButton("Start")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(80, 40, 80, 40)
        self.layout.setSpacing(16)
        self.layout.addWidget(self.title_label)

        self.player_layout = QtWidgets.QGridLayout()
        self.player_layout.setHorizontalSpacing(12)
        self.player_layout.setVerticalSpacing(10)
        self.player_layout.setColumnStretch(1, 1)
        self.player_layout.addWidget(self.player_1_name_label, 0, 0)
        self.player_layout.addWidget(self.player_1_name_input, 0, 1)
        self.player_layout.addWidget(self.player_1_symbol_label, 1, 0)
        self.player_layout.addWidget(self.player_1_symbol_dropdown, 1, 1)
        self.player_layout.addWidget(self.player_2_name_label, 2, 0)
        self.player_layout.addWidget(self.player_2_name_input, 2, 1)
        self.player_layout.addWidget(self.player_2_symbol_label, 3, 0)
        self.player_layout.addWidget(self.player_2_symbol_dropdown, 3, 1)
        self.layout.addLayout(self.player_layout)
        self.layout.addStretch()
        self.layout.addWidget(self.start_button)
        self.layout.addStretch()

        self.start_button.clicked.connect(self.start_button_clicked)

    def check_player_symbols(self):
        player_1 = self.player_1_symbol_dropdown.currentText()
        player_2 = self.player_2_symbol_dropdown.currentText()

        if player_1 == player_2:
            if self.sender() == self.player_1_symbol_dropdown:
                self.player_2_symbol_dropdown.setCurrentText("O" if player_1 == "X" else "X")
            else:
                self.player_1_symbol_dropdown.setCurrentText("O" if player_2 == "X" else "X")

    def start_button_clicked(self):
        start_game()


class GameWindow(QtWidgets.QWidget):
    def __init__(self, player_1_name, player_2_name, player_1_symbol, player_2_symbol):
        super().__init__()

        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_1_symbol = player_1_symbol
        self.player_2_symbol = player_2_symbol
        self.player_1_turn = False
        self.player_2_turn = False

        self.title_label = QtWidgets.QLabel("Tic Tac Toe", alignment=QtCore.Qt.AlignHCenter)
        title_font = QFont()
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.status_label = QtWidgets.QLabel("Status: ", alignment=QtCore.Qt.AlignBottom)
        self.setFixedSize(QSize(500, 500))
        self.setWindowTitle("Game")


        self.player_1_label = QtWidgets.QLabel(f"{player_1_name} ({player_1_symbol})")
        self.player_2_label = QtWidgets.QLabel(f"{player_2_name} ({player_2_symbol})")

        self.game_grid = QtWidgets.QGridLayout()
        self.game_grid.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.game_grid.setHorizontalSpacing(10)
        self.game_grid.setVerticalSpacing(10)

        for row in range(3):
            for column in range(3):
                button = QtWidgets.QPushButton()
                button.setFixedSize(100, 100)
                button.setStyleSheet("font-size: 24px;")
                button.clicked.connect(self.player_input)
                self.game_grid.addWidget(button, row, column)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.player_1_label)
        self.layout.addWidget(self.player_2_label)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.status_label)
        self.layout.addLayout(self.game_grid)


    def player_input(self):
        self.player_1_turn = False
        self.player_2_turn = False

        # Spieler der startet
        if self.player_1_symbol == "X":
            self.player_1_turn = True
        else:
            self.player_2_turn = True

        button = self.sender()

        # Player Input
        if button.text() != "":
            return
        if self.player_1_turn:
            button.setText(self.player_1_symbol)
            self.player_1_turn = False
            self.player_2_turn = True
        else:
            button.setText(self.player_2_symbol)
            self.player_1_turn = True
            self.player_2_turn = False

       

    def check_horizontal(self):
            win_x = False
            win_o = False
            for row in self.game_grid:
                win_x = win_x or (row[0] == "X" and row[1] == "X" and row[2] == "X")
                win_o = win_o or (row[0] == "O" and row[1] == "O" and row[2] == "O")
            return win_x, win_o


    def check_vertical(self):
        win_x = False
        win_o = False
        for column in range(3):
            win_x = win_x or (self.game_grid[0][column] == "X" and self.game_grid[1][column] == "X" and self.game_grid[2][column] == "X")
            win_o = win_o or (self.game_grid[0][column] == "O" and self.game_grid[1][column] == "O" and self.game_grid[2][column] == "O")
        return win_x, win_o

    

    def check_diagonal(self):
        win_x = False
        win_o = False

        win_x = self.game_grid[0][0] == "X" and self.game_grid[1][1] == "X" and self.game_grid[2][2] == "X"
        win_o = self.game_grid[0][0] == "O" and self.game_grid[1][1] == "O" and self.game_grid[2][2] == "O"

        if not win_x and not win_o:
            win_x = self.game_grid[0][2] == "X" and self.game_grid[1][1] == "X" and self.game_grid[2][0] == "X"
            win_o = self.game_grid[0][2] == "O" and self.game_grid[1][1] == "O" and self.game_grid[2][0] == "O"

        return win_x, win_o

    def draw_check(self):

        h_win_X, h_win_O = self.check_horizontal()
        d_win_X, d_win_O = self.check_diagonal()
        v_win_X, v_win_O = self.check_vertical()

        if (h_win_X == False and h_win_O == False and d_win_X == False and d_win_O == False and v_win_X == False and v_win_O == False and self.games_played >= 9):
            MySystemUtils.exit()

    def all_checks(self):
        horizontal_win_x, horizontal_win_o = self.check_horizontal()
        vertical_win_x, vertical_win_o = self.check_vertical()
        diagonal_win_x, diagonal_win_o = self.check_diagonal()

        if horizontal_win_x or vertical_win_x or diagonal_win_x:
            if self.player_2_symbol == "O":
                self.status_label.setText(f"{self.player_1_name} won!")
                MySystemUtils.exit()
            else:
                self.status_label.setText(f"{self.player_2_name} won!")
                MySystemUtils.exit()

        elif horizontal_win_o or vertical_win_o or diagonal_win_o:
            if self.player_1_symbol == "X":
                self.status_label.setText(f"{self.player_2_name} won!")
                MySystemUtils.exit()
            else:
                self.status_label.setText(f"{self.player_1_name} won!")
                MySystemUtils.exit()

        elif self.games_played >= 9:
            self.status_label.setText("Draw!")
            MySystemUtils.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    title_window = TitleWindow()
    title_window.show()
    sys.exit(app.exec())
