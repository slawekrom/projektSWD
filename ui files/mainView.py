# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainView.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(965, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 921, 621))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 965, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWy_wietl = QtWidgets.QMenu(self.menubar)
        self.menuWy_wietl.setObjectName("menuWy_wietl")
        self.menuWykresy = QtWidgets.QMenu(self.menubar)
        self.menuWykresy.setObjectName("menuWykresy")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_data = QtWidgets.QAction(MainWindow)
        self.actionLoad_data.setObjectName("actionLoad_data")
        self.actionChangeValOnNUmber = QtWidgets.QAction(MainWindow)
        self.actionChangeValOnNUmber.setObjectName("actionChangeValOnNUmber")
        self.actionDiscretize = QtWidgets.QAction(MainWindow)
        self.actionDiscretize.setObjectName("actionDiscretize")
        self.actionNorm = QtWidgets.QAction(MainWindow)
        self.actionNorm.setObjectName("actionNorm")
        self.actionChangeRange = QtWidgets.QAction(MainWindow)
        self.actionChangeRange.setObjectName("actionChangeRange")
        self.actionSubset = QtWidgets.QAction(MainWindow)
        self.actionSubset.setObjectName("actionSubset")
        self.actionHistogram = QtWidgets.QAction(MainWindow)
        self.actionHistogram.setObjectName("actionHistogram")
        self.action2D = QtWidgets.QAction(MainWindow)
        self.action2D.setObjectName("action2D")
        self.action3D = QtWidgets.QAction(MainWindow)
        self.action3D.setObjectName("action3D")
        self.actionAddObject = QtWidgets.QAction(MainWindow)
        self.actionAddObject.setObjectName("actionAddObject")
        self.actionClassify = QtWidgets.QAction(MainWindow)
        self.actionClassify.setObjectName("actionClassify")
        self.menuFile.addAction(self.actionLoad_data)
        self.menuFile.addAction(self.actionAddObject)
        self.menuFile.addAction(self.actionClassify)
        self.menuEdit.addAction(self.actionChangeValOnNUmber)
        self.menuEdit.addAction(self.actionDiscretize)
        self.menuEdit.addAction(self.actionNorm)
        self.menuEdit.addAction(self.actionChangeRange)
        self.menuWy_wietl.addAction(self.actionSubset)
        self.menuWykresy.addAction(self.actionHistogram)
        self.menuWykresy.addAction(self.action2D)
        self.menuWykresy.addAction(self.action3D)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWy_wietl.menuAction())
        self.menubar.addAction(self.menuWykresy.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "Plik"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edycja"))
        self.menuWy_wietl.setTitle(_translate("MainWindow", "Wyświetl"))
        self.menuWykresy.setTitle(_translate("MainWindow", "Wykresy"))
        self.actionLoad_data.setText(_translate("MainWindow", "Wczytaj dane"))
        self.actionChangeValOnNUmber.setText(_translate("MainWindow", "Zmień na dane numeryczne"))
        self.actionDiscretize.setText(_translate("MainWindow", "Dyskretyzacja"))
        self.actionNorm.setText(_translate("MainWindow", "Normalizacja"))
        self.actionChangeRange.setText(_translate("MainWindow", "Zmiana przedziału"))
        self.actionSubset.setText(_translate("MainWindow", "Procent największych/najniejszych"))
        self.actionHistogram.setText(_translate("MainWindow", "Histogram"))
        self.action2D.setText(_translate("MainWindow", "Wykres 2D"))
        self.action3D.setText(_translate("MainWindow", "Wykres 3D"))
        self.actionAddObject.setText(_translate("MainWindow", "Dodaj obiekt"))
        self.actionClassify.setText(_translate("MainWindow", "Klasyfikacja"))
