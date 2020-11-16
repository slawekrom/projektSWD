from PyQt5 import QtCore, QtGui, QtWidgets


class ClassifyDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 419)
        self.metricBox = QtWidgets.QGroupBox(Dialog)
        self.metricBox.setGeometry(QtCore.QRect(30, 10, 271, 161))
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
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(140, 230, 75, 23))
        self.cancelButton.setObjectName("cancelButton")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setGeometry(QtCore.QRect(50, 230, 75, 23))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.metricBox.setTitle(_translate("Dialog", "Metryka"))
        self.euklidianRadio.setText(_translate("Dialog", "Euklidesowa"))
        self.manhattanRadio.setText(_translate("Dialog", "Manhattan"))
        self.chebyshevRadio.setText(_translate("Dialog", "Czebyszewa"))
        self.mahalanobisRadio.setText(_translate("Dialog", "Mahalanobisa"))
        self.cancelButton.setText(_translate("Dialog", "Anuluj"))
        self.okButton.setText(_translate("Dialog", "OK"))
