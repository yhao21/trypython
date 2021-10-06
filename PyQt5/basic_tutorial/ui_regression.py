# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_regression.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 569)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 140, 571, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        # 再加三个选项
        for i in range(7):
            self.comboBox_3.addItem("")
        # self.comboBox_3.addItem("")
        # self.comboBox_3.addItem("")
        # self.comboBox_3.addItem("")
        # self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Regression Tool"))
        self.label_2.setText(_translate("MainWindow", "Regression Model"))

        combo = ['OLS','FGLS','Random Effect','Fixed Effect','DID','RDD','Bootstrapping']
        for i in range(7):
            self.comboBox_3.setItemText(i, _translate("MainWindow", combo[i]))


        # self.comboBox_3.setItemText(0, _translate("MainWindow", "OLS"))
        # self.comboBox_3.setItemText(1, _translate("MainWindow", "FGLS"))
        # self.comboBox_3.setItemText(2, _translate("MainWindow", "Random Effect"))
        # self.comboBox_3.setItemText(3, _translate("MainWindow", "Fixed Effect"))
        self.label_4.setText(_translate("MainWindow", "Dummy"))
