import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
)


class TitleWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.game_window = None
        # Widgets, Variablen, Layouts 

        self.setFixedSize(QSize(400, 350))
        self.setWindowTitle("Maksim's Tic-Tac-Toe Game")

        self.title_label = QtWidgets.QLabel("Tic-Tac-Toe", alignment=QtCore.Qt.AlignHCenter)

        self.player_1_symbol_dropdown = QtWidgets.QComboBox()
        self.player_1_symbol_dropdown.addItems(["X", "O"])
        self.player_1_symbol_dropdown.setCurrentText("X")
        self.player_1_name_label = QtWidgets.QLabel("Player 1 Name:")
        self.player_1_symbol_label = QtWidgets.QLabel("Player 1 Symbol:")
        self.player_1_name_input = QtWidgets.QLineEdit("Player 1")

        self.player_2_symbol_dropdown = QtWidgets.QComboBox()
        self.player_2_symbol_dropdown.addItems(["X", "O"])
        self.player_2_symbol_dropdown.setCurrentText("O")
        self.player_2_name_label = QtWidgets.QLabel("Player 2 Name:")
        self.player_2_symbol_label = QtWidgets.QLabel("Player 2 Symbol:")
        self.player_2_name_input = QtWidgets.QLineEdit("Player 2")

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
        player_1_name = self.player_1_name_input.text()
        player_2_name = self.player_2_name_input.text()
        player_1_symbol = self.player_1_symbol_dropdown.currentText()
        player_2_symbol = self.player_2_symbol_dropdown.currentText()
        self.game_window = GameWindow(player_1_name, player_2_name, player_1_symbol, player_2_symbol)
        self.game_window.show()
        self.hide()


class GameWindow(QtWidgets.QWidget):
    def __init__(self, player_1_name, player_2_name, player_1_symbol, player_2_symbol):
        super().__init__()

        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_1_symbol = player_1_symbol
        self.player_2_symbol = player_2_symbol
        self.player_1_turn = False
        self.player_2_turn = False
        self.games_played = 0
        self.game_over = False
        self.wins = {player_1_name: 0, player_2_name: 0}
        self.leaderboard = None

        self.current_player = self.player_1_symbol

        self.title_label = QtWidgets.QLabel("Tic Tac Toe", alignment=QtCore.Qt.AlignHCenter)
        title_font = QFont()
        title_font.setBold(True)
        self.title_label.setFont(title_font)
        self.status_label = QtWidgets.QLabel("Status: ", alignment=QtCore.Qt.AlignBottom)
        self.setFixedSize(QSize(500, 500))
        self.setWindowTitle("Game")
        self.reset_button = QtWidgets.QPushButton("Reset")
        self.reset_button.setFixedSize(QSize(60, 40))
        self.reset_button.clicked.connect(self.reset_game)

        self.player_1_label = QtWidgets.QLabel(f"{player_1_name} ({player_1_symbol})")
        self.player_2_label = QtWidgets.QLabel(f"{player_2_name} ({player_2_symbol})")
        self.player_label_color()

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
        self.top_layout = QtWidgets.QHBoxLayout()
        self.top_layout.addStretch()
        self.top_layout.addWidget(self.reset_button)
        self.layout.addLayout(self.top_layout)
        self.layout.addWidget(self.player_1_label)
        self.layout.addWidget(self.player_2_label)
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.status_label)
        self.layout.addLayout(self.game_grid)


    def player_label_color(self):
        if self.current_player == self.player_1_symbol:
            self.player_1_label.setStyleSheet("color: yellow;")
            self.player_2_label.setStyleSheet("")
        else:
            self.player_1_label.setStyleSheet("")
            self.player_2_label.setStyleSheet("color: yellow;")


    def player_input(self):
        button = self.sender()

        if self.game_over or button.text():
            return

        if self.current_player == self.player_1_symbol:
            button.setText(self.player_1_symbol)
            self.current_player = self.player_2_symbol
        else:
            button.setText(self.player_2_symbol)
            self.current_player = self.player_1_symbol

        self.games_played += 1
        self.player_label_color()
        self.all_checks()

    def reset_game(self):
        for row in range(3):
            for column in range(3):
                button_widget = self.game_grid.itemAtPosition(row, column)
                button_widget.widget().setText("")

        self.games_played = 0
        self.game_over = False
        self.current_player = self.player_1_symbol
        self.status_label.setText("Status: ")
        self.status_label.setStyleSheet("")
        if self.leaderboard is not None:
            self.leaderboard.close()
        self.player_label_color()



    def read_already_placed_symbols(self):
        spielfeld = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]
        for row in range(3):
            for column in range(3):
                button_widget = self.game_grid.itemAtPosition(row, column)
                button = button_widget.widget()
                button_symbol = button.text()
                spielfeld[row][column] = button_symbol   
        return spielfeld
    

    def check_horizontal(self):
        spielfeld = self.read_already_placed_symbols()
        win_x = False
        win_o = False
        for row in spielfeld:
            win_x = win_x or (row[0] == "X" and row[1] == "X" and row[2] == "X")
            win_o = win_o or (row[0] == "O" and row[1] == "O" and row[2] == "O")
        return win_x, win_o


    def check_vertical(self):
        spielfeld = self.read_already_placed_symbols()
        win_x = False
        win_o = False
        for column in range(3):
            win_x = win_x or (spielfeld[0][column] == "X" and spielfeld[1][column] == "X" and spielfeld[2][column] == "X")
            win_o = win_o or (spielfeld[0][column] == "O" and spielfeld[1][column] == "O" and spielfeld[2][column] == "O")
        return win_x, win_o

    

    def check_diagonal(self):
        spielfeld = self.read_already_placed_symbols()
        win_x = False
        win_o = False

        win_x = spielfeld[0][0] == "X" and spielfeld[1][1] == "X" and spielfeld[2][2] == "X"
        win_o = spielfeld[0][0] == "O" and spielfeld[1][1] == "O" and spielfeld[2][2] == "O"

        if not win_x and not win_o:
            win_x = spielfeld[0][2] == "X" and spielfeld[1][1] == "X" and spielfeld[2][0] == "X"
            win_o = spielfeld[0][2] == "O" and spielfeld[1][1] == "O" and spielfeld[2][0] == "O"

        return win_x, win_o
        

    def draw_check(self):

        h_win_X, h_win_O = self.check_horizontal()
        d_win_X, d_win_O = self.check_diagonal()
        v_win_X, v_win_O = self.check_vertical()

        if (h_win_X == False and h_win_O == False and d_win_X == False and d_win_O == False and v_win_X == False and v_win_O == False and self.games_played >= 9):
            self.status_label.steText("Draw!")
            self.status_label.setStyleSheet("color: yellow;")

    def all_checks(self):
        horizontal_win_x, horizontal_win_o = self.check_horizontal()
        vertical_win_x, vertical_win_o = self.check_vertical()
        diagonal_win_x, diagonal_win_o = self.check_diagonal()

        if horizontal_win_x or vertical_win_x or diagonal_win_x:
            self.game_over = True
            if self.player_2_symbol == "O":
                self.status_label.setText(f"{self.player_1_name} won!")
                self.status_label.setStyleSheet("font-weight: bold;")
                
            else:
                self.status_label.setText(f"{self.player_2_name} won!")
                self.status_label.setStyleSheet("font-weight: bold;")

        elif horizontal_win_o or vertical_win_o or diagonal_win_o:
            self.game_over = True
            if self.player_1_symbol == "X":
                self.status_label.setText(f"{self.player_2_name} won!")
                self.status_label.setStyleSheet("font-weight: bold;")
            else:
                self.status_label.setText(f"{self.player_1_name} won!")
                self.status_label.setStyleSheet("font-weight: bold;")


        elif self.games_played >= 9:
            self.game_over = True
            self.status_label.setText("Draw!")
            self.status_label.setStyleSheet("font-weight: bold;")
            self.show_leaderboard()

class Leaderboard(QtWidgets.QWidget):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("internship-contact-software-2026/TicTacToe/style.qss", "r") as file:
        app.setStyleSheet(file.read())


    title_window = TitleWindow()
    title_window.show()
    sys.exit(app.exec())