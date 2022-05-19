import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.left_list_widget = QListWidget()	# 1
        self.right_list_widget = QListWidget()
        self.left_list_widget.doubleClicked.connect(self.choose)
        self.right_list_widget.doubleClicked.connect(self.cancel)
        self.left_list_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.right_list_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for i in range(20):			            # 2
            item = QListWidgetItem(f'item {i}')
            self.left_list_widget.addItem(item)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.left_list_widget)
        h_layout.addWidget(self.right_list_widget)
        self.setLayout(h_layout)

    def choose(self):				            # 3
        item = self.left_list_widget.currentItem()
        new_item = QListWidgetItem(item)
        self.right_list_widget.addItem(new_item)

    def cancel(self):				            # 4
        row = self.right_list_widget.currentRow()
        self.right_list_widget.takeItem(row)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())