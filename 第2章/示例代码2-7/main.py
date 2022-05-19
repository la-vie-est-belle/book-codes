import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QuestionMessageBox(QMessageBox):
    def __init__(self, parent, title, content):
        super(QuestionMessageBox, self).__init__(parent)
        self.setWindowTitle(title)
        self.setText(content)
        self.setIcon(QMessageBox.Question)

        self.addButton('是', QMessageBox.YesRole)
        self.addButton('否', QMessageBox.NoRole)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = QPushButton('点我')
        self.button.clicked.connect(self.change_text)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button)
        self.setLayout(h_layout)

    def change_text(self):      # 1
        msb_box = QuestionMessageBox(self, '标题', '是否改变文本？')
        msb_box.exec()

        if msb_box.clickedButton().text() == '是':
            self.button.setText('文本改变')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())