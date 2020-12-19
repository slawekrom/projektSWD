from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox

from gui.Method import Method
from gui.Similarity import Similarity


class SimilarityDialog(QDialog):
    def __init__(self, data_frame):
        self.data_frame = data_frame
        super(SimilarityDialog, self).__init__()
        self.setWindowTitle("Similarity")
        self.__create_layout()
        self.setMinimumSize(400, 150)
        self.resize(400, 150)

    def __create_layout(self):
        self.layout = QVBoxLayout()
        self.__create_columns_layout()
        self.layout.addItem(self.columns_layout)
        self.__create_method_layout()
        self.layout.addItem(self.method_layout)
        self.__add_footer()
        self.setLayout(self.layout)

    def __create_columns_layout(self):
        self.columns_layout = QHBoxLayout()
        self.first_column_combobox = QComboBox()
        for col in self.data_frame.df.columns:
            self.first_column_combobox.addItem(col)
        self.columns_label = QLabel("Class column: ")
        self.second_column_combobox = QComboBox()
        for col in self.data_frame.df.columns:
            self.second_column_combobox.addItem(col)
        self.first_column_label = QLabel("First class column: ")
        self.second_column_label = QLabel("Second class column: ")
        self.columns_layout.addWidget(self.first_column_label)
        self.columns_layout.addWidget(self.first_column_combobox)
        self.columns_layout.addWidget(self.second_column_label)
        self.columns_layout.addWidget(self.second_column_combobox)

    def __add_footer(self):
        self.footer_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.ok_button.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.cancel_button = QPushButton("CANCEL")
        self.cancel_button.setGeometry(QtCore.QRect(200, 150, 93, 28))
        self.footer_layout.addWidget(self.ok_button)
        self.footer_layout.addWidget(self.cancel_button)
        self.layout.addItem(self.footer_layout)

    def __create_method_layout(self):
        self.method_layout = QHBoxLayout()
        self.method_combobox = QComboBox()
        for similarity_methon in Similarity:
            self.method_combobox.addItem(similarity_methon.name)
        self.method_label = QLabel("Method: ")
        self.method_layout.addWidget(self.method_label)
        self.method_layout.addWidget(self.method_combobox)
