# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addWindow(object):
    def setupUi(self, addWindow):
        addWindow.setObjectName("addWindow")
        addWindow.resize(507, 312)
        self.labelWebsite = QtWidgets.QLabel(addWindow)
        self.labelWebsite.setGeometry(QtCore.QRect(30, 30, 111, 16))
        self.labelWebsite.setObjectName("labelWebsite")
        self.labelID = QtWidgets.QLabel(addWindow)
        self.labelID.setGeometry(QtCore.QRect(30, 90, 111, 16))
        self.labelID.setObjectName("labelID")
        self.labelPw = QtWidgets.QLabel(addWindow)
        self.labelPw.setGeometry(QtCore.QRect(30, 150, 111, 16))
        self.labelPw.setObjectName("labelPw")
        self.lineeditWebsite = QtWidgets.QLineEdit(addWindow)
        self.lineeditWebsite.setGeometry(QtCore.QRect(30, 50, 451, 21))
        self.lineeditWebsite.setObjectName("lineeditWebsite")
        self.lineeditID = QtWidgets.QLineEdit(addWindow)
        self.lineeditID.setGeometry(QtCore.QRect(30, 110, 451, 21))
        self.lineeditID.setObjectName("lineeditID")
        self.lineeditPw = QtWidgets.QLineEdit(addWindow)
        self.lineeditPw.setGeometry(QtCore.QRect(30, 170, 451, 21))
        self.lineeditPw.setObjectName("lineeditPw")
        self.yesbtn = QtWidgets.QPushButton(addWindow)
        self.yesbtn.setGeometry(QtCore.QRect(30, 260, 201, 28))
        self.yesbtn.setObjectName("yesbtn")
        self.cancelbtn = QtWidgets.QPushButton(addWindow)
        self.cancelbtn.setGeometry(QtCore.QRect(280, 260, 201, 28))
        self.cancelbtn.setObjectName("cancelbtn")
        self.auto_az = QtWidgets.QCheckBox(addWindow)
        self.auto_az.setGeometry(QtCore.QRect(31, 205, 51, 19))
        self.auto_az.setChecked(True)
        self.auto_az.setObjectName("auto_az")
        self.auto_AZ = QtWidgets.QCheckBox(addWindow)
        self.auto_AZ.setGeometry(QtCore.QRect(89, 205, 51, 19))
        self.auto_AZ.setChecked(True)
        self.auto_AZ.setObjectName("auto_AZ")
        self.auto_num = QtWidgets.QCheckBox(addWindow)
        self.auto_num.setGeometry(QtCore.QRect(147, 205, 51, 19))
        self.auto_num.setChecked(True)
        self.auto_num.setObjectName("auto_num")
        self.auto_char = QtWidgets.QCheckBox(addWindow)
        self.auto_char.setGeometry(QtCore.QRect(205, 205, 83, 19))
        self.auto_char.setObjectName("auto_char")
        self.pwLen = QtWidgets.QSpinBox(addWindow)
        self.pwLen.setGeometry(QtCore.QRect(295, 203, 54, 24))
        self.pwLen.setMinimum(1)
        self.pwLen.setMaximum(100)
        self.pwLen.setProperty("value", 16)
        self.pwLen.setObjectName("pwLen")
        self.genPw = QtWidgets.QPushButton(addWindow)
        self.genPw.setGeometry(QtCore.QRect(370, 200, 111, 28))
        self.genPw.setObjectName("genPw")

        self.retranslateUi(addWindow)
        QtCore.QMetaObject.connectSlotsByName(addWindow)

    def retranslateUi(self, addWindow):
        _translate = QtCore.QCoreApplication.translate
        addWindow.setWindowTitle(_translate("addWindow", "Add"))
        self.labelWebsite.setText(_translate("addWindow", "Website"))
        self.labelID.setText(_translate("addWindow", "ID"))
        self.labelPw.setText(_translate("addWindow", "Password"))
        self.yesbtn.setText(_translate("addWindow", "Yes"))
        self.cancelbtn.setText(_translate("addWindow", "Cancel"))
        self.auto_az.setText(_translate("addWindow", "a-z"))
        self.auto_AZ.setText(_translate("addWindow", "A-Z"))
        self.auto_num.setText(_translate("addWindow", "0-9"))
        self.auto_char.setText(_translate("addWindow", "!@#$..."))
        self.genPw.setText(_translate("addWindow", "Generate"))
