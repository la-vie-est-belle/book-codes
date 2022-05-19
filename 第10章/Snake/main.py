import sys
from PyQt5.QtWidgets import *
from game import GameWindow


if __name__ == '__main__':
    app = QApplication([])
    game_window = GameWindow()
    game_window.show()
    sys.exit(app.exec())
