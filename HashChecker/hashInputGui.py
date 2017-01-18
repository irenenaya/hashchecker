# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hashInput.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HashTable(object):
    def setupUi(self, HashTable):
        HashTable.setObjectName("HashTable")
        HashTable.resize(724, 211)
        self.gridLayout = QtWidgets.QGridLayout(HashTable)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(HashTable)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.openPython = QtWidgets.QLabel(HashTable)
        self.openPython.setObjectName("openPython")
        self.gridLayout_2.addWidget(self.openPython, 4, 0, 1, 1)
        self.functionName = QtWidgets.QLabel(HashTable)
        self.functionName.setObjectName("functionName")
        self.gridLayout_2.addWidget(self.functionName, 1, 0, 1, 1)
        self.tableSizeLabel = QtWidgets.QLabel(HashTable)
        self.tableSizeLabel.setObjectName("tableSizeLabel")
        self.gridLayout_2.addWidget(self.tableSizeLabel, 3, 0, 1, 1)
        self.OpenInput = QtWidgets.QLabel(HashTable)
        self.OpenInput.setObjectName("OpenInput")
        self.gridLayout_2.addWidget(self.OpenInput, 5, 0, 1, 1)
        self.FunctionName = QtWidgets.QLineEdit(HashTable)
        self.FunctionName.setObjectName("FunctionName")
        self.gridLayout_2.addWidget(self.FunctionName, 1, 1, 1, 1)
        self.tableSizeEdit = QtWidgets.QLineEdit(HashTable)
        self.tableSizeEdit.setObjectName("tableSizeEdit")
        self.gridLayout_2.addWidget(self.tableSizeEdit, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PythonPath = QtWidgets.QLineEdit(HashTable)
        self.PythonPath.setObjectName("PythonPath")
        self.horizontalLayout.addWidget(self.PythonPath)
        self.OpenPyButton = QtWidgets.QPushButton(HashTable)
        self.OpenPyButton.setObjectName("OpenPyButton")
        self.horizontalLayout.addWidget(self.OpenPyButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.InputPath = QtWidgets.QLineEdit(HashTable)
        self.InputPath.setObjectName("InputPath")
        self.horizontalLayout_2.addWidget(self.InputPath)
        self.OpenInputButton = QtWidgets.QPushButton(HashTable)
        self.OpenInputButton.setObjectName("OpenInputButton")
        self.horizontalLayout_2.addWidget(self.OpenInputButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 5, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(HashTable)
        QtCore.QMetaObject.connectSlotsByName(HashTable)

    def retranslateUi(self, HashTable):
        _translate = QtCore.QCoreApplication.translate
        HashTable.setWindowTitle(_translate("HashTable", "Enter Details"))
        self.openPython.setText(_translate("HashTable", "Open Python File"))
        self.functionName.setText(_translate("HashTable", "Enter name of Function"))
        self.tableSizeLabel.setText(_translate("HashTable", "Enter size of Hash Table "))
        self.OpenInput.setText(_translate("HashTable", "Open Input File"))
        self.OpenPyButton.setText(_translate("HashTable", "Open"))
        self.OpenInputButton.setText(_translate("HashTable", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HashTable = QtWidgets.QWidget()
    ui = Ui_HashTable()
    ui.setupUi(HashTable)
    HashTable.show()
    sys.exit(app.exec_())

