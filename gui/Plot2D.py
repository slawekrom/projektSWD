import random

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog, QVBoxLayout
from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Plot2D(QDialog):
    def __init__(self, data, column_x, column_y, column_class, parent=None):
        QDialog.__init__(self, parent)
        self.data_ = data
        self.x = column_x
        self.y = column_y
        self.c = column_class

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure` it takes the `figure` instance as a parameter to __init__

        self.canvas = FigureCanvas(self.figure)
        self.canvas.resize(500, 400)

        # this is the Navigation widget it takes the Canvas widget and a paren
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.plot(self.figure)

        # set the layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def plot(self, figure):
        figure.clear()
        # create an axis -> we cann add more than one -> 1 = 2d, 2 = 3d etc. :P
        ax = figure.add_subplot(111)
        # plot data
        #ax.scatter(self.df['X'], self.df['Y'], alpha=0.7, label='cholesterol/age', color='green')
        if self.c:
            colours = ['blue', 'green', 'red', 'black', 'cyan', 'magenta', 'orange', 'purple', 'gray', 'olive', 'lime',
                       'salmon', 'deepskyblue']
            classes = self.data_[self.c].unique()

            for idx, class_ in enumerate(classes):
                x_ = self.data_[self.data_[self.c] == class_][self.x]
                y_ = self.data_[self.data_[self.c] == class_][self.y]
                if len(classes) <= len(colours):
                    ax.scatter(x_, y_, cmap=colours[idx], label=class_)
                else:
                    ax.scatter(x_, y_, cmap=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
                               label=class_)

            ax.set_xlabel(self.x)
            ax.set_ylabel(self.y)
            ax.legend()

        else:
            ax.scatter(self.data_[self.x], self.data_[self.y])
            ax.set_xlabel(self.x)
            ax.set_ylabel(self.y)
        #refresh canvas
        self.canvas.draw()