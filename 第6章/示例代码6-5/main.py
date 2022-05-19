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

        self.sql_model = QSqlTableModel()       # 1
        self.sql_model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.sql_model.setHeaderData(0, Qt.Horizontal, 'id')
        self.sql_model.setHeaderData(1, Qt.Horizontal, 'name')
        self.sql_model.setHeaderData(2, Qt.Horizontal, 'class')
        self.sql_model.setHeaderData(3, Qt.Horizontal, ' score')

        self.table_view = QTableView()
        self.table_view.setModel(self.sql_model)
        self.select_btn = QPushButton('select')
        self.insert_btn = QPushButton('insert')
        self.delete_btn = QPushButton('delete')
        self.select_btn.clicked.connect(self.select_data)
        self.insert_btn.clicked.connect(self.insert_data)
        self.delete_btn.clicked.connect(self.delete_data)

        btn_h_layout = QHBoxLayout()
        window_v_layout = QVBoxLayout()
        btn_h_layout.addWidget(self.select_btn)
        btn_h_layout.addWidget(self.insert_btn)
        btn_h_layout.addWidget(self.delete_btn)
        window_v_layout.addWidget(self.table_view)
        window_v_layout.addLayout(btn_h_layout)
        self.setLayout(window_v_layout)

    def connect_db(self):
        self.db.setDatabaseName('./info.db')
        if not self.db.open():
            error = self.db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)

    def closeEvent(self, event):
        self.db.close()
        event.accept()

    def select_data(self):			            # 2
        self.sql_model.setTable('students')
        self.sql_model.setFilter('score > 95')
        self.sql_model.select()

    def insert_data(self):			            # 3
        self.sql_model.insertRow(0)
        self.sql_model.setData(self.sql_model.index(0, 0), 3)
        self.sql_model.setData(self.sql_model.index(0, 1), '0101')
        self.sql_model.setData(self.sql_model.index(0, 2), 'Jack')
        self.sql_model.setData(self.sql_model.index(0, 3), 85)
        self.sql_model.submit()

    def delete_data(self):			            # 4
        self.sql_model.removeRow(0)
        self.sql_model.submit()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())