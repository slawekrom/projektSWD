# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Plot3DDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(332, 461)
        self.comboBoxColumnX = QtWidgets.QComboBox(Dialog)
        self.comboBoxColumnX.setGeometry(QtCore.QRect(80, 10, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxColumnX.setFont(font)
        self.comboBoxColumnX.setObjectName("comboBoxColumnX")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(180, 370, 71, 31))
        self.okButton.setObjectName("okButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBoxColumnY = QtWidgets.QComboBox(Dialog)
        self.comboBoxColumnY.setGeometry(QtCore.QRect(80, 80, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxColumnY.setFont(font)
        self.comboBoxColumnY.setObjectName("comboBoxColumnY")
        self.comboBoxColumnZ = QtWidgets.QComboBox(Dialog)
        self.comboBoxColumnZ.setGeometry(QtCore.QRect(80, 140, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxColumnZ.setFont(font)
        self.comboBoxColumnZ.setObjectName("comboBoxColumnZ")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.checkBoxColors = QtWidgets.QCheckBox(Dialog)
        self.checkBoxColors.setGeometry(QtCore.QRect(70, 190, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.checkBoxColors.setFont(font)
        self.checkBoxColors.setObjectName("checkBoxColors")
        self.comboBoxClass = QtWidgets.QComboBox(Dialog)
        self.comboBoxClass.setGeometry(QtCore.QRect(80, 240, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBoxClass.setFont(font)
        self.comboBoxClass.setObjectName("comboBoxClass")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 250, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.label_2.setText(_translate("Dialog", "Y"))
        self.label.setText(_translate("Dialog", "X"))
        self.label_3.setText(_translate("Dialog", "Z"))
        self.checkBoxColors.setText(_translate("Dialog", "Zastosuj kolory do klas"))
        self.label_4.setText(_translate("Dialog", "Klasa"))
