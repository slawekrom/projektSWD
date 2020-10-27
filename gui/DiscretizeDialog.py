from PyQt5 import QtCore, QtGui, QtWidgets


class DiscretizeDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(522, 453)
        self.comboBoxColumn = QtWidgets.QComboBox(Dialog)
        self.comboBoxColumn.setGeometry(QtCore.QRect(130, 30, 291, 41))
        self.comboBoxColumn.setObjectName("comboBoxColumn")
        self.columnLabel = QtWidgets.QLabel(Dialog)
        self.columnLabel.setGeometry(QtCore.QRect(30, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.columnLabel.setFont(font)
        self.columnLabel.setObjectName("columnLabel")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 110, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineSetNumber = QtWidgets.QLineEdit(Dialog)
        self.lineSetNumber.setGeometry(QtCore.QRect(180, 110, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineSetNumber.setFont(font)
        self.lineSetNumber.setObjectName("lineSetNumber")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(280, 390, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(390, 390, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.columnLabel.setText(_translate("Dialog", "Kolumna"))
        self.label.setText(_translate("Dialog", "Liczba przedziałów"))
        self.okButton.setText(_translate("Dialog", "OK"))
        self.cancelButton.setText(_translate("Dialog", "Anuluj"))
