import sys
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.db = QSqlDatabase.addDatabase('QSQLITE')   # 1
        self.connect_db()

    def connect_db(self):                               # 2
        self.db.setDatabaseName('./info.db')
        if not self.db.open():
            error = self.db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)

    def closeEvent(self, event):                        # 3
        self.db.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())