# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifyLogin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modifyLogin(object):
    def setupUi(self, modifyLogin):
        modifyLogin.setObjectName("modifyLogin")
        modifyLogin.resize(400, 268)
        self.labelOldPw = QtWidgets.QLabel(modifyLogin)
        self.labelOldPw.setGeometry(QtCore.QRect(30, 30, 201, 16))
        self.labelOldPw.setObjectName("labelOldPw")
        self.labelNewAcc = QtWidgets.QLabel(modifyLogin)
        self.labelNewAcc.setGeometry(QtCore.QRect(30, 90, 141, 16))
        self.labelNewAcc.setObjectName("labelNewAcc")
        self.labelNewPw = QtWidgets.QLabel(modifyLogin)
        self.labelNewPw.setGeometry(QtCore.QRect(30, 150, 151, 16))
        self.labelNewPw.setObjectName("labelNewPw")
        self.oldpw = QtWidgets.QLineEdit(modifyLogin)
        self.oldpw.setGeometry(QtCore.QRect(30, 50, 341, 21))
        self.oldpw.setObjectName("oldpw")
        self.newacc = QtWidgets.QLineEdit(modifyLogin)
        self.newacc.setGeometry(QtCore.QRect(30, 110, 341, 21))
        self.newacc.setObjectName("newacc")
        self.newpw = QtWidgets.QLineEdit(modifyLogin)
        self.newpw.setGeometry(QtCore.QRect(30, 170, 341, 21))
        self.newpw.setObjectName("newpw")
        self.queren = QtWidgets.QPushButton(modifyLogin)
        self.queren.setGeometry(QtCore.QRect(30, 220, 161, 28))
        self.queren.setObjectName("queren")
        self.quxiao = QtWidgets.QPushButton(modifyLogin)
        self.quxiao.setGeometry(QtCore.QRect(210, 220, 161, 28))
        self.quxiao.setObjectName("quxiao")

        self.retranslateUi(modifyLogin)
        QtCore.QMetaObject.connectSlotsByName(modifyLogin)

    def retranslateUi(self, modifyLogin):
        _translate = QtCore.QCoreApplication.translate
        modifyLogin.setWindowTitle(_translate("modifyLogin", "Modify Login Information"))
        self.labelOldPw.setText(_translate("modifyLogin", "Original Password"))
        self.labelNewAcc.setText(_translate("modifyLogin", "New Username"))
        self.labelNewPw.setText(_translate("modifyLogin", "New Password"))
        self.queren.setText(_translate("modifyLogin", "Modify"))
        self.quxiao.setText(_translate("modifyLogin", "Cancel"))
