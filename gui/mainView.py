import math

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from pandas import np
import pandas as pd

from scipy import linalg

from gui.GroupDialog import GroupDialog
from gui.Method import Method
from gui.Similarity import Similarity
from gui.SimilarityDialog import SimilarityDialog
from gui.openFileDialog import OpenFileDialog
from gui.NumDialog import NumDialog
from gui.DiscretizeDialog import DiscretizeDialog
from gui.NormDialog import NormDialog
from gui.ChangeRangeDialog import ChangeRangeDialog
from gui.SubsetDialog import SubsetDialog
from gui.Plot2DDialog import Plot2DDialog
from gui.Plot2D import Plot2D
from gui.Plot3D import Plot3D
from gui.HistogramDialog import HistogramDialog
from gui.Plot3DDialog import Plot3DDialog
from operation.FileLoader import FileLoader
from data.PandasModel import PandasModel
from data.DataFrame import DataFrame
from gui.Histogram import Histogram
from metrics.Metrics import Metrics
from gui.AddObject import AddObject
from gui.ClassifyDialog import ClassifyDialog
from operation.DecisionTree import DecisionTree


class Ui_MainWindow(object):

    def __init__(self):
        self.data_frame = DataFrame()

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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWyswietl = QtWidgets.QMenu(self.menubar)
        self.menuWyswietl.setObjectName("menuWyswietl")
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
        self.actionGroup = QtWidgets.QAction(MainWindow)
        self.actionGroup.setObjectName("actionGroup")
        self.actionGroupWithSample = QtWidgets.QAction(MainWindow)
        self.actionGroupWithSample.setObjectName("actionGroupWithSample")
        self.actionSimilarity = QtWidgets.QAction(MainWindow)
        self.actionSimilarity.setObjectName("actionSimilarity")
        self.actionDecisionTree = QtWidgets.QAction(MainWindow)
        self.actionDecisionTree.setObjectName("actionDecisionTree")
        self.menuFile.addAction(self.actionLoad_data)
        self.menuFile.addAction(self.actionAddObject)
        self.menuFile.addAction(self.actionClassify)
        self.menuFile.addAction(self.actionGroup)
        self.menuFile.addAction(self.actionGroupWithSample)
        self.menuFile.addAction(self.actionSimilarity)
        self.menuFile.addAction(self.actionDecisionTree)
        self.menuEdit.addAction(self.actionChangeValOnNUmber)
        self.menuEdit.addAction(self.actionDiscretize)
        self.menuEdit.addAction(self.actionNorm)
        self.menuEdit.addAction(self.actionChangeRange)
        self.menuWyswietl.addAction(self.actionSubset)
        self.menuWykresy.addAction(self.actionHistogram)
        self.menuWykresy.addAction(self.action2D)
        self.menuWykresy.addAction(self.action3D)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWyswietl.menuAction())
        self.menubar.addAction(self.menuWykresy.menuAction())

        self.actionLoad_data.triggered.connect(lambda: self.openDialogLoad())
        self.actionChangeValOnNUmber.triggered.connect(lambda: self.openDialogNum())
        self.actionDiscretize.triggered.connect(lambda: self.openDisretizeDialog())
        self.actionNorm.triggered.connect(lambda: self.openNormDialog())
        self.actionChangeRange.triggered.connect(lambda: self.open_change_range_dialog())
        self.actionSubset.triggered.connect(lambda: self.open_subset_dialog())
        self.actionHistogram.triggered.connect(lambda: self.open_hist_dialog())
        self.action2D.triggered.connect(lambda: self.open2d_dialog())
        self.action3D.triggered.connect(lambda: self.open3d_dialog())
        self.actionAddObject.triggered.connect(lambda: self.newobject_dialog())
        self.actionClassify.triggered.connect(lambda: self.classifyDialog())
        self.actionGroup.triggered.connect(lambda: self.groupDialog())
        self.actionGroupWithSample.triggered.connect(lambda: self.groupAllDialog())
        self.actionSimilarity.triggered.connect(lambda: self.similarityDialog())
        self.actionDecisionTree.triggered.connect(lambda: self.build_decision_tree())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "Plik"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edycja"))
        self.menuWyswietl.setTitle(_translate("MainWindow", "Wyświetl"))
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
        self.actionGroup.setText(_translate("MainWindow", "Grupowanie"))
        self.actionGroupWithSample.setText(_translate("MainWindow", "Grupowanie wszystkich"))
        self.actionSimilarity.setText(_translate("MainWindow", "Miara podobienstwa"))
        self.actionDecisionTree.setText(_translate("MainWindow", "Drzewo decyzyjne"))

    def openDialogLoad(self):
        self.open_file_dialog = QtWidgets.QDialog()
        self.ui = OpenFileDialog()
        self.ui.setupUi(self.open_file_dialog)
        self.open_file_dialog.show()
        self.ui.okButton.clicked.connect(lambda: self.open_file())
        self.ui.cancelButton.clicked.connect(lambda: self.close_file_dialog())

    def openDisretizeDialog(self):
        self.disretize_dialog = QtWidgets.QDialog()
        self.ui_disc = DiscretizeDialog()
        self.ui_disc.setupUi(self.disretize_dialog)
        self.ui_disc.comboBoxColumn.addItems(self.data_frame.df.columns)
        self.disretize_dialog.show()
        self.ui_disc.okButton.clicked.connect(lambda: self.discretize())
        self.ui_disc.cancelButton.clicked.connect(lambda: self.close_discretize_dialog())

    def openNormDialog(self):
        self.norm_dialog = QtWidgets.QDialog()
        self.ui_norm = NormDialog()
        self.ui_norm.setupUi(self.norm_dialog)
        self.ui_norm.comboBoxColumn.addItems(self.data_frame.df.columns)
        self.norm_dialog.show()
        self.ui_norm.okButton.clicked.connect(lambda: self.normalize())
        self.ui_norm.cancelButton.clicked.connect(lambda: self.close_norm_dialog())

    def openDialogNum(self):
        self.num_dialog = QtWidgets.QDialog()
        self.ui_num = NumDialog()
        self.ui_num.setupUi(self.num_dialog)
        self.ui_num.comboBoxColumn.addItems(self.data_frame.df.columns)
        self.num_dialog.show()
        self.ui_num.okButton.clicked.connect(lambda: self.change_to_num())
        self.ui_num.cancelButton.clicked.connect(lambda: self.close_num_dialog())

    def open_change_range_dialog(self):
        self.range_dialog = QtWidgets.QDialog()
        self.ui_range = ChangeRangeDialog()
        self.ui_range.setupUi(self.range_dialog)
        self.ui_range.comboBoxColumn.addItems(self.data_frame.df.columns)
        self.range_dialog.show()
        self.set_values()
        self.ui_range.comboBoxColumn.currentIndexChanged.connect(lambda: self.set_values())
        self.ui_range.okButton.clicked.connect(lambda: self.change_range())
        self.ui_range.cancelButton.clicked.connect(lambda: self.close_range_dialog())

    def open2d_dialog(self):
        self.plot2d_dialog = QtWidgets.QDialog()
        self.ui_plot2d = Plot2DDialog()
        self.ui_plot2d.setupUi(self.plot2d_dialog)
        self.ui_plot2d.comboBoxColumnX.addItems(self.data_frame.df.columns)
        self.ui_plot2d.comboBoxColumnY.addItems(self.data_frame.df.columns)
        self.ui_plot2d.comboBoxClass.addItems(self.data_frame.df.columns)
        self.plot2d_dialog.show()
        self.ui_plot2d.okButton.clicked.connect(lambda: self.draw_plot_2d())

    def open3d_dialog(self):
        self.plot3d_dialog = QtWidgets.QDialog()
        self.ui_plot3d = Plot3DDialog()
        self.ui_plot3d.setupUi(self.plot3d_dialog)
        self.ui_plot3d.comboBoxColumnX.addItems(self.data_frame.df.columns)
        self.ui_plot3d.comboBoxColumnY.addItems(self.data_frame.df.columns)
        self.ui_plot3d.comboBoxColumnZ.addItems(self.data_frame.df.columns)
        self.ui_plot3d.comboBoxClass.addItems(self.data_frame.df.columns)
        self.plot3d_dialog.show()
        self.ui_plot3d.okButton.clicked.connect(lambda: self.draw_plot_3d())

    def newobject_dialog(self):
        self.new_object_dialog = QtWidgets.QDialog()
        self.ui_new_obj = AddObject()
        self.ui_new_obj.setupUi(self.new_object_dialog)
        # columns_list = self.data_frame.df.columns
        # columns_list = columns_list[0: len(columns_list)]
        # column_label: str = ''
        # for element in columns_list:
        #     column_label.join(element)
        # self.ui_new_obj.Attributeslabel.setText(column_label)
        self.new_object_dialog.show()
        self.ui_new_obj.okButton.clicked.connect(lambda: self.add_new_object())
        # metrics: Metrics = Metrics(len(self.data_frame.df.index), self.data_frame.df)
        # metrics.classify_euclidean()

    def classifyDialog(self):
        self.classify_dialog = QtWidgets.QDialog()
        self.ui_classify = ClassifyDialog()
        self.ui_classify.setupUi(self.classify_dialog)
        self.classify_dialog.show()
        self.ui_classify.okButton.clicked.connect(lambda: self.classify())

    def groupDialog(self):
        self.group_dialog = GroupDialog(self.data_frame.df.iloc[:, : self.columns_number])
        self.group_dialog.show()
        self.group_dialog.ok_button.clicked.connect(lambda: self.group())
        self.group_dialog.cancel_button.clicked.connect(lambda: self.group_dialog.close())

    def groupAllDialog(self):
        self.group_dialog = GroupDialog(self.data_frame.df.iloc[:, : self.columns_number])
        self.group_dialog.show()
        self.group_dialog.ok_button.clicked.connect(lambda: self.groupAll())
        self.group_dialog.cancel_button.clicked.connect(lambda: self.group_dialog.close())

    def similarityDialog(self):
        self.similarity_dialog = SimilarityDialog(self.data_frame)
        self.similarity_dialog.show()
        self.similarity_dialog.ok_button.clicked.connect(lambda: self.similarity())
        self.similarity_dialog.cancel_button.clicked.connect(lambda: self.similarity_dialog.close())

    def build_decision_tree(self):
        decisionTree: DecisionTree = DecisionTree(self.data_frame.df)
        decisionTree.build_tree()

    def classify(self):
        metrics: Metrics = Metrics(len(self.data_frame.df.index), self.data_frame.df)
        if self.ui_classify.euklidianRadio.isChecked():
            if self.ui_classify.checkBoxNormalize.isChecked():
                metrics.classify_euclidean_normalize()
            else:
                metrics.classify_euclidean()
        elif self.ui_classify.manhattanRadio.isChecked():
            if self.ui_classify.checkBoxNormalize.isChecked():
                metrics.classify_manhattan_normalize()
            else:
                metrics.classify_manhattan()
        elif self.ui_classify.chebyshevRadio.isChecked():
            if self.ui_classify.checkBoxNormalize.isChecked():
                metrics.classify_chebyshev_normalize()
            else:
                metrics.classify_chebyshev()
        elif self.ui_classify.mahalanobisRadio.isChecked():
            if self.ui_classify.checkBoxNormalize.isChecked():
                metrics.classify_mahalanobis_normalize()
            else:
                metrics.classify_mahalanobis()

        self.close_classify_dialog()

    def group(self):
        temp_df = self.data_frame.df.iloc[:, : self.columns_number]
        class_name = self.group_dialog.columns_combobox.currentText()
        k = self.group_dialog.class_number.value()
        centroids = temp_df.sample(k)
        centroids = centroids.drop(class_name, axis=1)
        method = self.group_dialog.method_combobox.currentText()
        while True:
            distances = []
            if method == Method.manhattan.name:
                for c in centroids.iloc:
                    distances.append(self.manhattan_distance(
                        ' '.join(
                            [str(c[column]) for column in temp_df.columns.tolist() if column != class_name])
                        , temp_df
                    ))
            if method == Method.mahalanobis.name:
                for c in centroids.iloc:
                    distances.append(self.mahalanobis_distance(
                        ' '.join([str(c[column]) for column in temp_df.columns.tolist() if column != class_name])
                        , temp_df
                    ))
            if method == Method.euclidean.name:
                for c in centroids.iloc:
                    distances.append(self.euclidean_distance(
                        ' '.join([str(c[column]) for column in temp_df.columns.tolist() if column != class_name])
                        , temp_df
                    ))
            if method == Method.chebyshev.name:
                for c in centroids.iloc:
                    distances.append(self.chebyshev_distance(
                        ' '.join([str(c[column]) for column in temp_df.columns.tolist() if column != class_name])
                        , temp_df
                    ))

            groups = [[] for cu in range(k)]
            for i, distance in enumerate(distances[0]):
                min_value = distances[0][i]
                index = 0
                for row in range(len(distances)):
                    if distances[row][i] < min_value:
                        index = row
                        min_value = distances[row][i]
                groups[index].append(i)
            data = []
            for group in groups:
                group_zero = temp_df.iloc[group]
                means = {}
                for c in temp_df.columns.tolist():
                    if c != class_name:
                        means[c] = group_zero[c].mean()
                data.append(means)
            temp = pd.DataFrame(data)
            classes = []
            if centroids.equals(temp):
                for i in temp_df.index.tolist():
                    for g, c in enumerate(groups):
                        if i in c:
                            classes.append(g + 1)
                self.data_frame.df.insert(len(self.data_frame.df.columns), "Groups: " + method, classes, True)
                self.setup_table(self.data_frame.df)
                self.group_dialog.close()
                break
            centroids = temp

    def group_with_centroids(self, centroids, method):
        temp_df = self.data_frame.df.iloc[:, : self.columns_number]
        class_name = self.group_dialog.columns_combobox.currentText()
        k = self.group_dialog.class_number.value()
        while True:
            distances = []
            if method == Method.manhattan.name:
                for c in centroids.iloc:
                    distances.append(self.manhattan_distance(
                        ' '.join(
                            [str(c[column]) for column in temp_df.columns.tolist() if column != class_name])
                        , temp_df
                    ))
            if method == Method.mahalanobis.name:
                for c in centroids.iloc:
                    distances.append(self.mahalanobis_distance(
                        ' '.join([str(c[column]) for column in temp_df.columns.tolist() if column != class_name])
                        , temp_df
                    ))
            if method == Method.euclidean.name:
                for c in centroids.iloc:
                    distances.append(self.euclidean_distance(
                        ' '.join([str(c[column]) for column in temp_df.columns.tolist() if column != class_name])
                        , temp_df
                    ))
            if method == Method.chebyshev.name:
                for c in centroids.iloc:
                    distances.append(self.chebyshev_distance(
                        ' '.join([str(c[column]) for column in temp_df.columns.tolist() if column != class_name])
                        , temp_df
                    ))

            groups = [[] for cu in range(k)]
            for i, distance in enumerate(distances[0]):
                min_value = distances[0][i]
                index = 0
                for row in range(len(distances)):
                    if distances[row][i] < min_value:
                        index = row
                        min_value = distances[row][i]
                groups[index].append(i)
            data = []
            for group in groups:
                group_zero = temp_df.iloc[group]
                means = {}
                for c in temp_df.columns.tolist():
                    if c != class_name:
                        means[c] = group_zero[c].mean()
                data.append(means)
            temp = pd.DataFrame(data)
            classes = []
            if centroids.equals(temp):
                for i in temp_df.index.tolist():
                    for g, c in enumerate(groups):
                        if i in c:
                            classes.append(g + 1)
                self.data_frame.df.insert(len(self.data_frame.df.columns), "Groups: " + method, classes, True)
                self.setup_table(self.data_frame.df)
                self.group_dialog.close()
                break
            centroids = temp

    def groupAll(self):
        temp_df = self.data_frame.df.iloc[:, : self.columns_number]
        class_name = self.group_dialog.columns_combobox.currentText()
        k = self.group_dialog.class_number.value()
        centroids = temp_df.sample(k)
        centroids = centroids.drop(class_name, axis=1)
        self.group_with_centroids(centroids, Method.euclidean.name)
        self.group_with_centroids(centroids, Method.manhattan.name)
        self.group_with_centroids(centroids, Method.mahalanobis.name)
        self.group_with_centroids(centroids, Method.chebyshev.name)

    def similarity(self):
        first_class = self.similarity_dialog.first_column_combobox.currentText()
        second_class = self.similarity_dialog.second_column_combobox.currentText()
        method = self.similarity_dialog.method_combobox.currentText()
        similarity = 0
        if method == Similarity.jaccard.name:
            similarity = self.jaccard_similarity(list1=self.data_frame.df[first_class].values, list2=self.data_frame.df[second_class].values)
        if method == Similarity.simple_matching.name:
            similarity = self.simple_matching_similarity(list1=self.data_frame.df[first_class].values, list2=self.data_frame.df[second_class].values)
        msg = QMessageBox()
        msg.setText('Similarity: ' + str(similarity))
        msg.setWindowTitle('Similarity value')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(lambda: msg.close())
        msg.show()

    def add_new_object(self):
        k = int(self.ui_new_obj.K_value.text())
        values = self.ui_new_obj.newValues.text()
        if self.ui_new_obj.euklidianRadio.isChecked():
            object_class = Metrics.euclidean_distance(values, self.data_frame.df, k)
        elif self.ui_new_obj.manhattanRadio.isChecked():
            object_class = Metrics.manhattan_distance(values, self.data_frame.df, k)
        elif self.ui_new_obj.chebyshevRadio.isChecked():
            object_class = Metrics.chebyshev_distance(values, self.data_frame.df, k)
        elif self.ui_new_obj.mahalanobisRadio.isChecked():
            object_class = Metrics.mahalanobis_distance(values, self.data_frame.df, k)

        self.data_frame.append(values, object_class)
        self.setup_table(self.data_frame.df)
        self.close_add_new_object_dialog()

    def show_hist(self):
        column = self.ui_hist.comboBoxColumn.currentText()
        if self.ui_hist.checkBoxSets.isChecked():
            number_of_bins = int(self.ui_hist.lineSets.text())
        else:
            number_of_bins = self.data_frame.df[column].nunique()
        self.histogram_plot: Histogram = Histogram(self.data_frame.df, column, number_of_bins)
        self.histogram_plot.show()
        self.close_hist_dialog()

    def draw_plot_2d(self):
        x = self.ui_plot2d.comboBoxColumnX.currentText()
        y = self.ui_plot2d.comboBoxColumnY.currentText()
        is_colors = self.ui_plot2d.checkBoxColors.isChecked()
        if is_colors:
            class_column = self.ui_plot2d.comboBoxClass.currentText()
        else:
            class_column = None
        self.plot2d: Plot2D = Plot2D(self.data_frame.df, x, y, class_column)
        self.plot2d.show()
        self.close_plot2d_dialog()

    def draw_plot_3d(self):
        x = self.ui_plot3d.comboBoxColumnX.currentText()
        y = self.ui_plot3d.comboBoxColumnY.currentText()
        z = self.ui_plot3d.comboBoxColumnZ.currentText()
        is_colors = self.ui_plot3d.checkBoxColors.isChecked()
        if is_colors:
            class_column = self.ui_plot3d.comboBoxClass.currentText()
        else:
            class_column = None
        self.plot3d: Plot3D = Plot3D(self.data_frame.df, x, y, z, class_column)
        self.plot3d.show()
        self.close_plot3d_dialog()

    def open_hist_dialog(self):
        self.hist_dialog = QtWidgets.QDialog()
        self.ui_hist = HistogramDialog()
        self.ui_hist.setupUi(self.hist_dialog)
        self.ui_hist.comboBoxColumn.addItems(self.data_frame.df.columns)
        self.hist_dialog.show()
        self.ui_hist.okButton.clicked.connect(lambda: self.show_hist())

    def open_subset_dialog(self):
        self.subset_dialog = QtWidgets.QDialog()
        self.ui_subset = SubsetDialog()
        self.ui_subset.setupUi(self.subset_dialog)
        self.ui_subset.comboBoxColumn.addItems(self.data_frame.df.columns)
        self.subset_dialog.show()
        self.ui_subset.okButton.clicked.connect(lambda: self.select_subset())
        self.ui_subset.cancelButton.clicked.connect(lambda: self.close_subset_dialog())

    def set_values(self):
        col = self.ui_range.comboBoxColumn.currentText()
        self.ui_range.labelMin.setText(str(self.data_frame.df[col].min()))
        self.ui_range.labelMax.setText(str(self.data_frame.df[col].max()))

    def change_range(self):
        col = self.ui_range.comboBoxColumn.currentText()
        a = self.ui_range.lineNewMin.text()
        b = self.ui_range.lineNewMax.text()
        self.data_frame.change_range(col, float(a), float(b))
        self.setup_table(self.data_frame.df)
        self.close_range_dialog()

    def select_subset(self):
        col = self.ui_subset.comboBoxColumn.currentText()
        percent = int(self.ui_subset.linePercent.text())
        if self.ui_subset.radioButtonMin.isChecked():
            subset = self.data_frame.get_min_subset(col, percent)
        else:
            subset = self.data_frame.get_max_subset(col, percent)

        model: PandasModel = PandasModel(subset)
        self.ui_subset.tableView.setModel(model)

    def change_to_num(self):
        col = self.ui_num.comboBoxColumn.currentText()
        is_alpha = self.ui_num.radioButtonAlpha.isChecked()
        addInNewColumn = self.ui_num.newColumnCheckbox.isChecked()
        if addInNewColumn:
            self.data_frame.add_to_number(col, is_alpha)
            self.setup_table(self.data_frame.df)
        else:
            self.data_frame.change_to_number(col, is_alpha)
        # metrics: Metrics = Metrics(len(self.data_frame.df.index), self.data_frame.df)
        # metrics.calculate_chebyshev(len(self.data_frame.df.index))
        self.close_num_dialog()
        print(self.data_frame.df.columns)

    def discretize(self):
        col = self.ui_disc.comboBoxColumn.currentText()
        sets_number = self.ui_disc.lineSetNumber.text()
        new_column = self.ui_disc.checkBox_newColumn.isChecked()
        self.data_frame.discretize(col, sets_number, new_column)
        self.setup_table(self.data_frame.df)
        self.setup_table(self.data_frame.df)
        #self.close_discretize_dialog()

    def normalize(self):
        col = self.ui_norm.comboBoxColumn.currentText()
        if self.ui_norm.checkBoxNormalizeAll.isChecked():
            self.data_frame.normalize_all()
        else:
            self.data_frame.normalize(col)
        self.setup_table(self.data_frame.df)
        self.close_norm_dialog()

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
        file_loader: FileLoader = FileLoader()
        if is_headers:
            self.data_frame.df = file_loader.loadFile(file_path, separator)
        else:
            self.data_frame.df = file_loader.loadFile_and_add_headers(file_path, separator)
        self.setup_table(self.data_frame.df)
        print(self.data_frame.df.columns)
        print(self.data_frame.df.dtypes)
        self.columns_number = len(self.data_frame.df.columns)
        self.close_file_dialog()

    def close_file_dialog(self):
        self.open_file_dialog.close()

    def close_range_dialog(self):
        self.range_dialog.close()

    def close_subset_dialog(self):
        self.subset_dialog.close()

    def close_discretize_dialog(self):
        self.disretize_dialog.close()

    def close_norm_dialog(self):
        self.norm_dialog.close()

    def close_num_dialog(self):
        self.num_dialog.close()

    def close_plot2d_dialog(self):
        self.plot2d_dialog.close()

    def close_plot3d_dialog(self):
        self.plot3d_dialog.close()

    def close_hist_dialog(self):
        self.hist_dialog.close()

    def close_add_new_object_dialog(self):
        self.new_object_dialog.close()

    def close_classify_dialog(self):
        self.classify_dialog.close()

    def setup_table(self, df):
        self.pandas_model: PandasModel = PandasModel(df)
        self.tableView.setModel(self.pandas_model)

    def manhattan_distance(self, values: str, df):
        values_array = np.array(values.split(" ")).astype(np.float)
        column_count = len(df.columns)
        columns = []
        columns = df.columns
        distance = dict()
        for j in range(len(df.index)):
            sum = 0
            for n in range(column_count - 1):
                sum += math.fabs(values_array[n] - df.at[j, columns[n]])
            distance[j] = sum
        return distance

    def euclidean_distance(self, values: str, df):
        values_array = np.array(values.split(" ")).astype(np.float)
        column_count = len(df.columns)
        columns = []
        columns = df.columns
        distance = dict()
        for j in range(len(df.index)):
            sum = 0
            for n in range(column_count - 1):
                sum += math.pow((values_array[n] - df.at[j, columns[n]]), 2)
            distance[j] = math.sqrt(sum)

        return distance

    def chebyshev_distance(self, values: str, df):
        values_array = np.array(values.split(" ")).astype(np.float)
        column_count = len(df.columns)
        columns = []
        columns = df.columns
        distance = dict()
        for j in range(len(df.index)):
            sum = 0
            for n in range(column_count - 1):
                if math.fabs(values_array[n] - df.at[j, columns[n]]) > sum:
                    sum = math.fabs(values_array[n] - df.at[j, columns[n]])
            distance[j] = sum
        return distance

    def mahalanobis_distance(self, values: str, df):
        values_array_first = np.array(values.split(" ")).astype(np.float)
        column_count = len(df.columns)
        columns = df.columns
        distance = dict()
        cov = df.cov().to_numpy()
        inv_cov = linalg.inv(cov)
        for j in range(len(df.index)):
            values_array_second = []
            for n in range(column_count - 1):
                values_array_second.append(df.at[j, columns[n]])
            subtract = np.subtract(values_array_first, values_array_second)
            subtract_t = subtract.T
            multiply = subtract_t.dot(inv_cov).dot(subtract)
            distance[j] = multiply
        return distance

    def jaccard_similarity(self, list1, list2):
        iter = 0
        for i, item in enumerate(list1):
            if list1[i] == list2[i]:
                iter += 1
        union = (len(list1) + len(list2)) - iter
        return float(iter) / union

    # def dice_similarity(self, list1, list2):
    #     return np.sum(list1[list2 == len(set(list1))])*2.0 / (np.sum(list1) + np.sum(list2))

    def simple_matching_similarity(self, list1, list2):
        iter = 0
        for i, item in enumerate(list1):
            if list1[i] == list2[i]:
                iter += 1
        return iter / len(list1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
