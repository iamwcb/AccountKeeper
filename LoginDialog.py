# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginDialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginDialog(object):
    def setupUi(self, LoginDialog):
        LoginDialog.setObjectName("LoginDialog")
        LoginDialog.resize(400, 223)
        self.pbCancel = QtWidgets.QPushButton(LoginDialog)
        self.pbCancel.setGeometry(QtCore.QRect(210, 150, 161, 28))
        self.pbCancel.setAutoDefault(False)
        self.pbCancel.setDefault(False)
        self.pbCancel.setObjectName("pbCancel")
        self.pbLogin = QtWidgets.QPushButton(LoginDialog)
        self.pbLogin.setGeometry(QtCore.QRect(30, 150, 151, 28))
        self.pbLogin.setDefault(False)
        self.pbLogin.setObjectName("pbLogin")
        self.lePassword = QtWidgets.QLineEdit(LoginDialog)
        self.lePassword.setGeometry(QtCore.QRect(30, 90, 341, 31))
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword.setObjectName("lePassword")
        self.leName = QtWidgets.QLineEdit(LoginDialog)
        self.leName.setGeometry(QtCore.QRect(30, 30, 341, 31))
        self.leName.setObjectName("leName")
        self.keepPwBtn = QtWidgets.QRadioButton(LoginDialog)
        self.keepPwBtn.setGeometry(QtCore.QRect(30, 190, 151, 19))
        self.keepPwBtn.setObjectName("keepPwBtn")

        self.retranslateUi(LoginDialog)
        QtCore.QMetaObject.connectSlotsByName(LoginDialog)

    def retranslateUi(self, LoginDialog):
        _translate = QtCore.QCoreApplication.translate
        LoginDialog.setWindowTitle(_translate("LoginDialog", "Login"))
        self.pbCancel.setText(_translate("LoginDialog", "Cancel"))
        self.pbLogin.setText(_translate("LoginDialog", "Login"))
        self.lePassword.setPlaceholderText(_translate("LoginDialog", "Password"))
        self.leName.setPlaceholderText(_translate("LoginDialog", "Account"))
        self.keepPwBtn.setText(_translate("LoginDialog", "Keep Password"))