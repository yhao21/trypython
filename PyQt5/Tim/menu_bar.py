# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_bar.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 140, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(190, 300, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.resize(200,20)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        # use print_you to get the text you have chosen in comboBox
        self.comboBox.currentIndexChanged.connect(lambda: self.print_you())



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
        self.actionNew_file = QtWidgets.QAction(MainWindow)
        self.actionNew_file.setObjectName("actionNew_file")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.menuFile.addAction(self.actionNew_file)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.actionQuit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def print_you(self):
        # print the text you have chosen. we can use this method to link other function in web scrapping
        print(self.comboBox.currentText())
        if self.comboBox.currentText() == 'requests':
            print('use request to download')
        if self.comboBox.currentText() == 'selenium':
            print('use selenum')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.comboBox.setItemText(0, _translate("MainWindow", "choose a method to scrapping..."))
        self.comboBox.setItemText(1, _translate("MainWindow", "requests"))
        self.comboBox.setItemText(2, _translate("MainWindow", "selenium"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew_file.setText(_translate("MainWindow", "New File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setStatusTip(_translate("MainWindow", "quit the program"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
