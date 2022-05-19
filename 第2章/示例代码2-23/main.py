import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.datetime_edit = QDateTimeEdit(QDateTime.currentDateTime())
        self.datetime_edit.setDisplayFormat('yyyy-MM-dd HH:mm:ss')	        # 1
        self.datetime_edit.setDateRange(QDate(1949, 10, 1), QDate(6666, 6, 6))
        self.datetime_edit.setCalendarPopup(True)			                # 2
        self.datetime_edit.dateTimeChanged.connect(self.show_text)	        # 3

        self.date_edit = QDateEdit(QDate.currentDate())
        self.date_edit.setDisplayFormat('yyyy-MM-dd')
        self.date_edit.setDateRange(QDate(1949, 10, 1), QDate(6666, 6, 6))
        self.date_edit.dateChanged.connect(self.show_text)

        self.time_edit = QTimeEdit(QTime.currentTime())
        self.time_edit.setDisplayFormat('HH:mm:ss')
        self.time_edit.setTimeRange(QTime(6, 6, 6), QTime(8, 8, 8))
        self.date_edit.timeChanged.connect(self.show_text)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.datetime_edit)
        v_layout.addWidget(self.date_edit)
        v_layout.addWidget(self.time_edit)
        self.setLayout(v_layout)

    def show_text(self):
        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())