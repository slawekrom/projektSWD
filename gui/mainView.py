# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainView.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from gui.openFileDialog import OpenFileDialog
from gui.NumDialog import NumDialog
from operation.FileLoader import FileLoader
from data.PandasModel import PandasModel
from data.DataFrame import DataFrame

class Ui_MainWindow(object):

    def __init__(self):
        self.data_frame = DataFrame()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 631, 541))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_data = QtWidgets.QAction(MainWindow)
        self.actionLoad_data.setObjectName("actionLoad_data")
        self.actionChangeValOnNUmber = QtWidgets.QAction(MainWindow)
        self.actionChangeValOnNUmber.setObjectName("actionChangeValOnNUmber")
        self.menuFile.addAction(self.actionLoad_data)
        self.menuEdit.addAction(self.actionChangeValOnNUmber)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.actionLoad_data.triggered.connect(lambda: self.openDialogLoad())
        self.actionChangeValOnNUmber.triggered.connect(lambda: self.openDialogNum())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "Plik"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edycja"))
        self.actionLoad_data.setText(_translate("MainWindow", "Wczytaj dane"))
        self.actionChangeValOnNUmber.setText(_translate("MainWindow", "Zmień na dane numeryczne"))

        

    def openDialogLoad(self):
        print("ASADDADADD")
        self.open_file_dialog = QtWidgets.QDialog()
        self.ui = OpenFileDialog()
        self.ui.setupUi(self.open_file_dialog)
        self.open_file_dialog.show()
        #self.ui.filePathInput.text()
        self.ui.okButton.clicked.connect(lambda: self.open_file())
        self.ui.cancelButton.clicked.connect(lambda: self.close_file_dialog())

    def openDialogNum(self):
        print("ASADDADADD")
        self.num_dialog = QtWidgets.QDialog()
        self.ui_num = NumDialog()
        self.ui_num.setupUi(self.num_dialog)
        lst = ["asas", "rwrw"]
        self.ui_num.comboBoxColumn.addItems(self.data_frame.df.columns)
        self.num_dialog.show()
        self.ui_num.okButton.clicked.connect(lambda: self.change_to_num())
        self.ui_num.cancelButton.clicked.connect(lambda: self.close_num_dialog())

    def change_to_num(self):
        col = self.ui_num.comboBoxColumn.currentText()
        is_alpha = self.ui_num.radioButtonAlpha.isChecked()
        print(col)
        print(is_alpha)
        self.data_frame.change_to_number(col, is_alpha)
        self.close_num_dialog()

    def open_file(self):
        file_path = self.ui.filePathInput.text()
        separator = ''
        if self.ui.tabRadio.isChecked():
            separator = '\t'
        elif self.ui.spaceRadio.isChecked():
            separator = ' '
        elif self.ui.commaRadio.isChecked():
            separator = ','
        elif self.ui.semicolonRadio.isChecked():
            separator = ';'

        is_headers = self.ui.checkBoxHeaders.isChecked()
        print(separator)
        print(is_headers)
        col_index = False
        if is_headers:
            col_index = 0
        file_loader: FileLoader = FileLoader()
        self.data_frame.df = file_loader.loadFile(file_path, separator, col_index)
        self.setup_table(self.data_frame.df)
        print(self.data_frame.df.columns)
        print(self.data_frame.df.dtypes)
        print(self.data_frame.change_to_number('day', False))
        self.close_file_dialog()

    def close_file_dialog(self):
        self.open_file_dialog.close()

    def close_num_dialog(self):
        self.num_dialog.close()

    def setup_table(self, df):
        self.pandas_model: PandasModel = PandasModel(df)
        self.tableView.setModel(self.pandas_model)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
