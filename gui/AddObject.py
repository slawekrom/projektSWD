from PyQt5 import QtCore, QtGui, QtWidgets


class AddObject(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(777, 530)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 721, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.newValues = QtWidgets.QLineEdit(Dialog)
        self.newValues.setGeometry(QtCore.QRect(20, 70, 691, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newValues.setFont(font)
        self.newValues.setObjectName("newValues")
        self.metricBox = QtWidgets.QGroupBox(Dialog)
        self.metricBox.setGeometry(QtCore.QRect(30, 130, 271, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.metricBox.setFont(font)
        self.metricBox.setObjectName("metricBox")
        self.euklidianRadio = QtWidgets.QRadioButton(self.metricBox)
        self.euklidianRadio.setGeometry(QtCore.QRect(10, 20, 181, 31))
        self.euklidianRadio.setObjectName("euklidianRadio")
        self.manhattanRadio = QtWidgets.QRadioButton(self.metricBox)
        self.manhattanRadio.setGeometry(QtCore.QRect(10, 60, 141, 21))
        self.manhattanRadio.setObjectName("manhattanRadio")
        self.chebyshevRadio = QtWidgets.QRadioButton(self.metricBox)
        self.chebyshevRadio.setGeometry(QtCore.QRect(10, 90, 141, 21))
        self.chebyshevRadio.setObjectName("chebyshevRadio")
        self.mahalanobisRadio = QtWidgets.QRadioButton(self.metricBox)
        self.mahalanobisRadio.setGeometry(QtCore.QRect(10, 120, 181, 31))
        self.mahalanobisRadio.setObjectName("mahalanobisRadio")
        self.label_K = QtWidgets.QLabel(Dialog)
        self.label_K.setGeometry(QtCore.QRect(30, 310, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_K.setFont(font)
        self.label_K.setObjectName("label_K")
        self.K_value = QtWidgets.QLineEdit(Dialog)
        self.K_value.setGeometry(QtCore.QRect(200, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.K_value.setFont(font)
        self.K_value.setObjectName("K_value")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(170, 390, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(80, 390, 75, 23))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Dane nowego elementu - wprować dane nowego elementu, wartość kolejych atrybutów oddzielone spacją"))
        self.metricBox.setTitle(_translate("Dialog", "Metryka"))
        self.euklidianRadio.setText(_translate("Dialog", "Euklidesowa"))
        self.manhattanRadio.setText(_translate("Dialog", "Manhattan"))
        self.chebyshevRadio.setText(_translate("Dialog", "Czebyszewa"))
        self.mahalanobisRadio.setText(_translate("Dialog", "Mahalanobisa"))
        self.label_K.setText(_translate("Dialog", "K najbliższych sąsiadów"))
        self.cancelButton.setText(_translate("Dialog", "Anuluj"))
        self.okButton.setText(_translate("Dialog", "OK"))
