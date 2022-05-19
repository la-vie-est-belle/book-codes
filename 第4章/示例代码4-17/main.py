import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('文件')

        open_action = QAction(QIcon('open.ico'), '打开', self)	# 1
        save_action = QAction(QIcon('save.ico'), '保存', self)
        quit_action = QAction(QIcon('quit.ico'), '退出', self)
        open_action.triggered.connect(self.open)			    # 2
        save_action.triggered.connect(self.save)
        quit_action.triggered.connect(self.quit)

        file_menu.addAction(open_action)				        # 3
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(quit_action)

        self.edit = QTextEdit()
        self.setCentralWidget(self.edit)

    def open(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '打开', './', '*.txt')
        if file_path:
            with open(file_path, 'r') as f:
                self.edit.setText(f.read())

    def save(self):
        text = self.edit.toPlainText()
        if text:
            with open('saved.txt', 'w') as f:
                f.write(text)

    def quit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())