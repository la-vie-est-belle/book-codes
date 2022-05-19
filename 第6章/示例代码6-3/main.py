import sys
from PyQt5.QtSql import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.connect_db()
        self.exec_sql()

    def connect_db(self):
        self.db.setDatabaseName('./info.db')
        if not self.db.open():
            error = self.db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)

    def closeEvent(self, event):
        self.db.close()
        event.accept()

    def exec_sql(self):
        query = QSqlQuery()

        query.exec("CREATE TABLE students "
                    "(id INT(11) PRIMARY KEY, class VARCHAR(4) NOT NULL, "
                    "name VARCHAR(25) NOT NULL, score FLOAT)")
        query.exec("INSERT INTO students (id, class, name, score) "
                    "VALUES (1, '0105', 'Mike', 90.5)")
        query.exec("INSERT INTO students (id, class, name, score) "
                    "VALUES (2, '0115', 'Mary', 99.5)")

        query.exec("SELECT name, class, score FROM students")
        while query.next():
            stu_name = query.value(0)
            stu_class = query.value(1)
            stu_score = query.value(2)
            print(stu_name, stu_class, stu_score)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())