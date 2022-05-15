# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modify(object):
    def setupUi(self, modify):
        modify.setObjectName("modify")
        modify.resize(394, 246)
        self.lineEdit = QtWidgets.QLabel(modify)
        self.lineEdit.setGeometry(QtCore.QRect(30, 20, 121, 16))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLabel(modify)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 80, 72, 15))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLabel(modify)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 140, 121, 16))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineeditWebsite = QtWidgets.QLineEdit(modify)
        self.lineeditWebsite.setGeometry(QtCore.QRect(30, 40, 341, 21))
        self.lineeditWebsite.setObjectName("lineeditWebsite")
        self.lineeditID = QtWidgets.QLineEdit(modify)
        self.lineeditID.setGeometry(QtCore.QRect(30, 100, 341, 21))
        self.lineeditID.setObjectName("lineeditID")
        self.lineeditPw = QtWidgets.QLineEdit(modify)
        self.lineeditPw.setGeometry(QtCore.QRect(30, 160, 341, 21))
        self.lineeditPw.setObjectName("lineeditPw")
        self.yesbtn = QtWidgets.QPushButton(modify)
        self.yesbtn.setGeometry(QtCore.QRect(30, 200, 141, 28))
        self.yesbtn.setObjectName("yesbtn")
        self.cancelbtn = QtWidgets.QPushButton(modify)
        self.cancelbtn.setGeometry(QtCore.QRect(230, 200, 141, 28))
        self.cancelbtn.setObjectName("cancelbtn")

        self.retranslateUi(modify)
        QtCore.QMetaObject.connectSlotsByName(modify)

    def retranslateUi(self, modify):
        _translate = QtCore.QCoreApplication.translate
        modify.setWindowTitle(_translate("modify", "Modify"))
        self.lineEdit.setText(_translate("modify", "New Website"))
        self.lineEdit_2.setText(_translate("modify", "New ID"))
        self.lineEdit_3.setText(_translate("modify", "New Password"))
        self.yesbtn.setText(_translate("modify", "Yes"))
        self.cancelbtn.setText(_translate("modify", "Cancel"))
