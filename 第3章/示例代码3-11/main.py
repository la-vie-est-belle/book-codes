import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.model = QFileSystemModel()
        self.model.setRootPath('.')		        # 1
        self.model.setReadOnly(False)

        self.tree_view = QTreeView()		    # 2
        self.tree_view.setModel(self.model)
        self.tree_view.setAnimated(True)
        self.tree_view.header().setStretchLastSection(True)
        self.tree_view.doubleClicked.connect(self.show_info)	# 3

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.tree_view)
        self.setLayout(h_layout)

    def show_info(self):
        index = self.tree_view.currentIndex()
        self.tree_view.scrollTo(index)
        self.tree_view.expand(index)

        file_name = self.model.fileName(index)
        file_path = self.model.filePath(index)
        file_size = self.model.size(index)
        print(file_name, file_path, file_size)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())