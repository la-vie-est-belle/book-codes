import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.stacked_widget = QStackedWidget()

        self.text_edit1 = QTextEdit()
        self.text_edit2 = QTextEdit()
        self.text_edit3 = QTextEdit()
        self.text_edit1.setPlaceholderText('edit 1')
        self.text_edit2.setPlaceholderText('edit 2')
        self.text_edit3.setPlaceholderText('edit 3')

        self.stacked_widget.addWidget(self.text_edit1)		        # 1
        self.stacked_widget.insertWidget(0, self.text_edit2)
        self.stacked_widget.addWidget(self.text_edit3)
        self.stacked_widget.currentChanged.connect(self.show_text)	# 2

        self.btn1 = QPushButton('show edit 1')			            # 3
        self.btn2 = QPushButton('show edit 2')
        self.btn3 = QPushButton('show edit 3')
        self.btn1.clicked.connect(self.change_edit)
        self.btn2.clicked.connect(self.change_edit)
        self.btn3.clicked.connect(self.change_edit)

        btn_h_layout = QHBoxLayout()
        window_v_layout = QVBoxLayout()
        btn_h_layout.addWidget(self.btn1)
        btn_h_layout.addWidget(self.btn2)
        btn_h_layout.addWidget(self.btn3)
        window_v_layout.addLayout(btn_h_layout)
        window_v_layout.addWidget(self.stacked_widget)
        self.setLayout(window_v_layout)

    def show_text(self):
        edit = self.stacked_widget.currentWidget()
        print(edit.placeholderText())

    def change_edit(self):
        btn = self.sender()
        if btn.text() == 'show edit 1':
            self.stacked_widget.setCurrentIndex(1)
        elif btn.text() == 'show edit 2':
            self.stacked_widget.setCurrentIndex(0)
        else:
            self.stacked_widget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())