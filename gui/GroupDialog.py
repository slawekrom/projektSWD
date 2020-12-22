from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QSpinBox, QHBoxLayout, QLabel, QPushButton, QComboBox

from gui.Method import Method


class GroupDialog(QDialog):
    def __init__(self, data_frame):
        self.data_frame = data_frame
        super(GroupDialog, self).__init__()
        self.setWindowTitle("K mean")
        self.__create_layout()
        self.setMinimumSize(400, 150)
        self.resize(400, 150)

    def __create_layout(self):
        self.layout = QVBoxLayout()
        self.__create_columns_layout()
        self.layout.addItem(self.columns_layout)
        self.__create_class_layout()
        self.layout.addItem(self.class_layout)
        self.__create_method_layout()
        self.layout.addItem(self.method_layout)
        self.__add_footer()
        self.setLayout(self.layout)

    def __create_class_layout(self):
        self.class_layout = QHBoxLayout()
        self.class_number = QSpinBox()
        self.class_number.setMinimum(1)
        self.class_number.setMaximum(99)
        self.class_label = QLabel("Number of classes to divide: ")
        self.class_layout.addWidget(self.class_label)
        self.class_layout.addWidget(self.class_number)

    def __create_columns_layout(self):
        self.columns_layout = QHBoxLayout()
        self.columns_combobox = QComboBox()
        for col in self.data_frame.columns:
            self.columns_combobox.addItem(col)
        self.columns_label = QLabel("Class column: ")
        self.columns_layout.addWidget(self.columns_label)
        self.columns_layout.addWidget(self.columns_combobox)

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
        for method in Method:
            self.method_combobox.addItem(method.name)
        self.method_label = QLabel("Method: ")
        self.method_layout.addWidget(self.method_label)
        self.method_layout.addWidget(self.method_combobox)
