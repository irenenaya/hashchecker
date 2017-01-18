__author__ = 'irenenaya'

import sys
import require
import importlib
from PyQt5 import QtGui, QtWidgets
from hashInputGui import Ui_HashTable


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pylab as pyl

class HashTableC(Ui_HashTable):
    def __init__(self, dialog):
        Ui_HashTable.__init__(self)

        self.setupUi(dialog)

        self.dialog = dialog

        self.tableSize = 0
        self.functName = ''
        self.pathToInput = ''
        self.pathToFunct = ''

        self.buttonBox.accepted.connect(self.initializeVars)
        self.OpenInputButton.clicked.connect(self.saveInputPath)
        self.OpenPyButton.clicked.connect(self.savePythonPath)

    def initializeVars(self):
        self.tableSize = self.tableSizeEdit.text()
        self.functName = self.FunctionName.text()
        self.pathToInput = self.InputPath.text()
        self.pathToFunct = self.PythonPath.text()
        self.dialog.close()
        self.runChecker()

    def runChecker(self):
        size = int(self.tableSize)
        myarray = [0]*size
        f = open(self.pathToInput, 'r')
        lines = f.readlines()
        mypath = require(self.pathToFunct)

    #    mod = importlib.import_module(self.pathToFunct)
        hash_it = getattr(mypath, self.functName)

        for st in lines:
            a = hash_it(st, size)
            myarray[a] +=1

        f.close()

        win = Window(myarray)
        win.setWindowTitle("Results")
        win.show()


    def saveInputPath(self):
        filename = QtWidgets.QFileDialog.getOpenFileName()
        self.InputPath.setText(filename[0])

    def savePythonPath(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(filter= "*.py")
        self.PythonPath.setText(filename[0])

class Window(QtWidgets.QDialog):
    def __init__(self, data, parent=None):
        super(Window, self).__init__(parent)

        self.data = data
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.hide()

        self.button = QtWidgets.QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        self.button1 = QtWidgets.QPushButton('Zoom')
        self.button1.clicked.connect(self.zoom)

        self.button2 = QtWidgets.QPushButton('Pan')
        self.button2.clicked.connect(self.pan)

        self.button3 = QtWidgets.QPushButton('Home')
        self.button3.clicked.connect(self.home)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

    def home(self):
        self.toolbar.home()

    def zoom(self):
        self.toolbar.zoom()

    def pan(self):
        self.toolbar.pan()

    def plot(self):
       # PlotCanvas(self.data)

        data = self.data
        ax = self.figure.add_subplot(111)
        ax.hold(False)
        ax.set_title("Basic Distribution")


        ax.plot(data, 'r*-')
        self.canvas.draw()
    

"""
class PlotCanvas(FigureCanvas):

    def __init__(self, data, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        self.data = data

        FigureCanvas.setSizePolicy(self,
                QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot(self.data)


    def plot(self, data):
     #   data = [random.random() for i in range(25)]
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()

"""


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QWidget()

    prog = HashTableC(dialog)

    dialog.show()

    sys.exit(app.exec_())


