import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.table = QTableWidget()		                        # 1
        self.table.setColumnCount(6)
        self.table.setRowCount(6)
        self.table.verticalHeader().hide()
        self.table.clicked.connect(self.show_cell_info)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setHorizontalHeaderLabels(['第1列', '第2列', '第3列',
                                              '第4列', '第5列', '第6列'])
        for row in range(6):
            for column in range(6):
                item = QTableWidgetItem(f'({row}, {column})')   # 2
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(row, column, item)

        row_count = self.table.rowCount()		                # 3
        self.table.setRowCount(row_count+1)
        for column in range(6):
            self.table.setItem(6, column, QTableWidgetItem(f'(6, {column})'))

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.table)
        self.setLayout(h_layout)

    def show_cell_info(self):			                        # 4
        item = self.table.currentItem()
        print(item.text())


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())