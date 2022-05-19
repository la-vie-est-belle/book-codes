import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.tab_widget = QTabWidget()

        self.text_edit1 = QTextEdit()
        self.text_edit2 = QTextEdit()
        self.text_edit3 = QTextEdit()
        self.text_edit1.setPlaceholderText('edit 1')
        self.text_edit2.setPlaceholderText('edit 2')
        self.text_edit3.setPlaceholderText('edit 3')

        self.tab_widget.addTab(self.text_edit1, 'edit 1')		    # 1
        self.tab_widget.insertTab(0, self.text_edit2, 'edit 2')
        self.tab_widget.addTab(self.text_edit3, QIcon('edit.png'), 'edit 3')
        self.tab_widget.currentChanged.connect(self.show_tab_name)	# 2
        self.tab_widget.setTabShape(QTabWidget.Triangular)		    # 3

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.tab_widget)
        self.setLayout(h_layout)

    def show_tab_name(self):
        index = self.tab_widget.currentIndex()
        print(self.tab_widget.tabText(index))


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())