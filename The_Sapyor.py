import random
import time

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

LEVELS = (
    (8, 10),
    (16, 40),
    (24, 99)
    )


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.level = 0
        self.bort_size, self.mines_count = LEVELS[self.level]

        self.setWindowTitle('Сапёр')
        self.setFixedSize(300, 300)
        self.show()
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        toolbar = QHBoxLayout()

        self.mines = QLabel(str(self.mines_count))
        self.mines.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.clock = QLabel("000")
        self.clock.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        font = self.mines.font()
        font.setPointSize(24)
        font.setWeight(75)
        self.mines.setFont(font)
        self.clock.setFont(font)

        self.button = QPushButton()
        self.button.setFixedSize(32, 32)
        self.button.setIconSize(QSize(32, 32))
        self.button.setIcon(QIcon('./images/smiley.png'))
        self.button.setFlat(True)

        toolbar.addWidget(self.mines)
        toolbar.addWidget(self.button)
        toolbar.addWidget(self.clock)

        main_layout = QVBoxLayout()
        main_layout.addLayout(toolbar)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec()