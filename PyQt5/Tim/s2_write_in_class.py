from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(600, 500, 400, 300)
        self.setWindowTitle('this is synferlo')
        self.initUI()


    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('my first label')
        self.label.move(50, 50)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('my first button')
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText('you pressed the button')
        self.update()

    def update(self):
        # this will automatically adjust the size of label when a text is given.
        # So, it make sure all the text in the label can be showed correctly.
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()