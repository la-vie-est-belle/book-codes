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

        self.sql_model = QSqlQueryModel()                       # 1
        self.sql_model.setHeaderData(0, Qt.Horizontal, 'id')
        self.sql_model.setHeaderData(1, Qt.Horizontal, 'name')
        self.sql_model.setHeaderData(2, Qt.Horizontal, 'class')
        self.sql_model.setHeaderData(3, Qt.Horizontal, ' score')

        self.table_view = QTableView()
        self.table_view.setModel(self.sql_model)
        self.exec_sql()

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.table_view)
        self.setLayout(v_layout)

    def connect_db(self):
        self.db.setDatabaseName('./info.db')
        if not self.db.open():
            error = self.db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)

    def closeEvent(self, event):
        self.db.close()
        event.accept()

    def exec_sql(self):		                                    # 2
        sql = "SELECT id, name, class, score FROM students"
        self.sql_model.setQuery(sql)

        for i in range(self.sql_model.rowCount()):
            id = self.sql_model.record(i).value('id')
            name = self.sql_model.record(i).value(1)
            print(id, name)

        for i in range(self.sql_model.rowCount()):
            id = self.sql_model.data(self.sql_model.index(i, 0))
            name = self.sql_model.data(self.sql_model.index(i, 1))
            print(id, name)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())