import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.calendar = QCalendarWidget()
        self.calendar.setMinimumDate(QDate(1949, 10, 1))	# 1
        self.calendar.setMaximumDate(QDate(6666, 6, 6))
	    # self.calendar.setDateRange(QDate(1949, 10, 1), QDate(6666, 6, 6))
        self.calendar.setFirstDayOfWeek(Qt.Monday)		    # 2
        self.calendar.setGridVisible(True)			        # 3
        self.calendar.clicked.connect(self.show_date)	    # 4

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.calendar)
        self.setLayout(h_layout)

    def show_date(self):
        date = self.calendar.selectedDate().toString('yyyy-MM-dd')
        print(date)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())