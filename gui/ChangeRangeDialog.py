# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChangeRangeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ChangeRangeDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(517, 424)
        self.comboBoxColumn = QtWidgets.QComboBox(Dialog)
        self.comboBoxColumn.setGeometry(QtCore.QRect(140, 10, 291, 41))
        self.comboBoxColumn.setObjectName("comboBoxColumn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 250, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.columnLabel = QtWidgets.QLabel(Dialog)
        self.columnLabel.setGeometry(QtCore.QRect(40, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.columnLabel.setFont(font)
        self.columnLabel.setObjectName("columnLabel")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(290, 370, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(400, 370, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.lineNewMin = QtWidgets.QLineEdit(Dialog)
        self.lineNewMin.setGeometry(QtCore.QRect(200, 250, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineNewMin.setFont(font)
        self.lineNewMin.setObjectName("lineNewMin")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 300, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineNewMax = QtWidgets.QLineEdit(Dialog)
        self.lineNewMax.setGeometry(QtCore.QRect(200, 300, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineNewMax.setFont(font)
        self.lineNewMax.setText("")
        self.lineNewMax.setObjectName("lineNewMax")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.labelMin = QtWidgets.QLabel(Dialog)
        self.labelMin.setGeometry(QtCore.QRect(150, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelMin.setFont(font)
        self.labelMin.setText("")
        self.labelMin.setObjectName("labelMin")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(60, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.labelMax = QtWidgets.QLabel(Dialog)
        self.labelMax.setGeometry(QtCore.QRect(150, 130, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelMax.setFont(font)
        self.labelMax.setText("")
        self.labelMax.setObjectName("labelMax")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Nowe minimun"))
        self.columnLabel.setText(_translate("Dialog", "Kolumna"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.cancelButton.setText(_translate("Dialog", "Anuluj"))
        self.label_2.setText(_translate("Dialog", "Nowe maksimum"))
        self.label_3.setText(_translate("Dialog", "Minimum"))
        self.label_4.setText(_translate("Dialog", "Maksimum"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
