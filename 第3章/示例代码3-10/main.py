import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.left_model = QStringListModel()			        # 1
        self.right_model = QStringListModel()

        self.left_list = [f'item {i}' for i in range(20)]		# 2
        self.left_model.setStringList(self.left_list)

        self.left_list_view = QListView()
        self.right_list_view = QListView()
        self.left_list_view.setModel(self.left_model)
        self.left_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.left_list_view.doubleClicked.connect(self.choose)	# 3
        self.right_list_view.setModel(self.right_model)
        self.right_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.right_list_view.doubleClicked.connect(self.cancel)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.left_list_view)
        h_layout.addWidget(self.right_list_view)
        self.setLayout(h_layout)

    def choose(self):		# 4
        index = self.left_list_view.currentIndex()
        data = index.data()

        row_count = self.right_model.rowCount()
        self.right_model.insertRow(row_count)
        row_index = self.right_model.index(row_count)
        self.right_model.setData(row_index, data)

    def cancel(self):		# 5
        index = self.right_list_view.currentIndex()
        row_numer = index.row()
        self.right_model.removeRow(row_numer)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())