import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.name_line_edit = QLineEdit()			# 1
        self.gender_line_edit = QLineEdit()
        self.age_line_edit = QLineEdit()
        self.score_line_edit = QLineEdit()
        self.note_text_edit = QTextEdit()

        self.name_btn = QPushButton('姓名')
        self.gender_btn = QPushButton('性别')
        self.age_btn = QPushButton('年龄')
        self.score_btn = QPushButton('分数')
        self.note_btn = QPushButton('备注')
        self.name_btn.clicked.connect(self.get_name)
        self.gender_btn.clicked.connect(self.get_gender)
        self.age_btn.clicked.connect(self.get_age)
        self.score_btn.clicked.connect(self.get_score)
        self.note_btn.clicked.connect(self.get_note)

        g_layout = QGridLayout()
        g_layout.addWidget(self.name_btn, 0, 0)
        g_layout.addWidget(self.name_line_edit, 0, 1)
        g_layout.addWidget(self.gender_btn, 1, 0)
        g_layout.addWidget(self.gender_line_edit, 1, 1)
        g_layout.addWidget(self.age_btn, 2, 0)
        g_layout.addWidget(self.age_line_edit, 2, 1)
        g_layout.addWidget(self.score_btn, 3, 0)
        g_layout.addWidget(self.score_line_edit, 3, 1)
        g_layout.addWidget(self.note_btn, 4, 0)
        g_layout.addWidget(self.note_text_edit, 4, 1)
        self.setLayout(g_layout)

    def get_name(self):     # 2
        name, isOk = QInputDialog.getText(self, '姓名', '请输入姓名')
        if isOk:
            self.name_line_edit.setText(name)

    def get_gender(self):   # 3
        gender_list = ['Female', 'Male']
        gender, isOk = QInputDialog.getItem(self, '性别', '请选择性别',
                                            gender_list)
        if isOk:
            self.gender_line_edit.setText(gender)

    def get_age(self):      # 4
        age, isOk = QInputDialog.getInt(self, '年龄', '请输入年龄')
        if isOk:
            self.age_line_edit.setText(str(age))

    def get_score(self):    # 4
        score, isOk = QInputDialog.getDouble(self, '分数', '请输入分数')
        if isOk:
            self.score_line_edit.setText(str(score))

    def get_note(self):
        note, isOk = QInputDialog.getMultiLineText(self, '备注', '请输入备注')
        if isOk:
            self.note_text_edit.setText(note)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())