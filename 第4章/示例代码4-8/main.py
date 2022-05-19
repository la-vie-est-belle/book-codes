import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.is_saved = True        # 1

        self.edit = QTextEdit()
        self.edit.textChanged.connect(self.update_save_status)
        self.save_btn = QPushButton('保存')
        self.save_btn.clicked.connect(self.save)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.edit)
        v_layout.addWidget(self.save_btn)
        self.setLayout(v_layout)

    def update_save_status(self):
        if self.edit.toPlainText():
            self.is_saved = False
        else:
            self.is_saved = True

    def save(self):
        self.is_saved = True
        with open('saved.txt', 'w') as f:
            f.write(self.edit.toPlainText())

    def closeEvent(self, event):    # 2
        if not self.is_saved:
            choice = QMessageBox.question(self, '', '是否保存文本内容?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        if choice == QMessageBox.Yes:
            self.save()
            event.accept()
        elif choice == QMessageBox.No:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())