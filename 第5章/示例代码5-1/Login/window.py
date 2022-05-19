from PyQt5.QtWidgets import *
from login_ui import Ui_Form				            # 1


class Window(QWidget, Ui_Form):				            # 2
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.login_btn.clicked.connect(self.check)		# 3

    def check(self):
        username = self.username_line.text().strip()
        password = self.password_line.text().strip()

        if username=='Hello' and password=='PyQt5':
            QMessageBox.information(self, '提示','登录成功！')
        else:
            QMessageBox.critical(self, '错误', '账号或密码错误！')

        self.username_line.clear()
        self.password_line.clear()