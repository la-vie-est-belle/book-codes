# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 118)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.username_label = QtWidgets.QLabel(Form)
        self.username_label.setObjectName("username_label")
        self.horizontalLayout.addWidget(self.username_label)
        self.username_line = QtWidgets.QLineEdit(Form)
        self.username_line.setObjectName("username_line")
        self.horizontalLayout.addWidget(self.username_line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password_label = QtWidgets.QLabel(Form)
        self.password_label.setObjectName("password_label")
        self.horizontalLayout_2.addWidget(self.password_label)
        self.password_line = QtWidgets.QLineEdit(Form)
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.horizontalLayout_2.addWidget(self.password_line)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.login_btn = QtWidgets.QPushButton(Form)
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout.addWidget(self.login_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "?????????"))
        self.username_label.setText(_translate("Form", "??????"))
        self.username_line.setPlaceholderText(_translate("Form", "???????????????"))
        self.password_label.setText(_translate("Form", "??????"))
        self.password_line.setPlaceholderText(_translate("Form", "???????????????"))
        self.login_btn.setText(_translate("Form", "??????"))
