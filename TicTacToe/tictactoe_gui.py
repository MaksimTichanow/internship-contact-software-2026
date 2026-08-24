import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,  
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

class TitleWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(500, 500))
        self.setWindowTitle("Maksim's Tic-Tac-Toe Game")

        #* Main Menu

        self.titel_text = QtWidgets.QLabel("Tic-Tac-Toe", alignment=QtCore.Qt.AlignHCenter)

        # Player 1
        self.player_1_dropdown = QtWidgets.QComboBox()
        self.player_1_dropdown.addItems(["X", "O"])
        self.player_1_name_label = QtWidgets.QLabel("Player 1 Name:")
        self.player_1_symbol_label = QtWidgets.QLabel("Player 1 Symbol:")
        self.player_1_input_box = QtWidgets.QLineEdit()


        # Player 2
        self.player_2_dropdown = QtWidgets.QComboBox()
        self.player_2_dropdown.addItems(["X", "O"])
        self.player_2_name_label = QtWidgets.QLabel("Player 2 Name:")
        self.player_2_symbol_label = QtWidgets.QLabel("Player 2 Symbol:")
        self.player_2_input_box = QtWidgets.QLineEdit()

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



    def start_button_clicked(self):
        self.game_window = GameWindow()
        self.game_window.show()
        


class GameWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(500, 500))
        self.setWindowTitle("Game")

        # Spielfeld
        self.spielfeld = QtWidgets.QGridLayout()
        self.spielfeld.setHorizontalSpacing(0)
        self.spielfeld.setVerticalSpacing(0)
        for i in range(3):
            for x in range(3):
                button = QtWidgets.QPushButton("")
                button.setFixedSize(QSize(100, 100))
                button.setStyleSheet("font-size: 24px;")
                self.spielfeld.addWidget(button, i, x)


        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addLayout(self.spielfeld)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    title_window = TitleWindow()

    title_window.show()

    sys.exit(app.exec())