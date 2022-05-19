import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.model = QStandardItemModel()	# 1
        self.model.setColumnCount(6)
        self.model.setRowCount(6)
        self.model.setHorizontalHeaderLabels(['第1列', '第2列', '第3列',
                                              '第4列', '第5列', '第6列'])

        for row in range(6):			    # 2
            for column in range(6):
                item = QStandardItem(f'({row}, {column})')
                item.setTextAlignment(Qt.AlignCenter)
                self.model.setItem(row, column, item)

        self.new_items = [QStandardItem(f'(6, {column})') for column in range(6)]
        self.model.appendRow(self.new_items)

        self.table = QTableView()			# 3
        self.table.setModel(self.model)
        self.table.verticalHeader().hide()
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.clicked.connect(self.show_cell_info)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.table)
        self.setLayout(h_layout)

    def show_cell_info(self):
        index = self.table.currentIndex()
        data = index.data()
        print(data)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())