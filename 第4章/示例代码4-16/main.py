import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.edit1 = QTextEdit()					            # 1
        self.edit2 = QTextEdit()
        self.center_edit = QTextEdit()

        self.dock1 = QDockWidget('停靠区域1')
        self.dock2 = QDockWidget('停靠区域2')
        self.dock1.setWidget(self.edit1)
        self.dock2.setWidget(self.edit2)
        self.dock1.setAllowedAreas(Qt.RightDockWidgetArea)		# 2
        self.dock2.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dock1.setFeatures(QDockWidget.DockWidgetFloatable)
        self.dock2.setFeatures(QDockWidget.DockWidgetMovable)

        self.addDockWidget(Qt.RightDockWidgetArea, self.dock1)	# 3
        self.addDockWidget(Qt.TopDockWidgetArea, self.dock2)
        self.setCentralWidget(self.center_edit)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())