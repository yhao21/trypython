from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def clicked():
    print('Clicked button')




def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    # use setGeometry to setup the location and size of the window
    # four parameters are : xposition, yposition, width, height
    win.setGeometry(500, 400, 600, 400)
    win.setWindowTitle('my first GUI')
    # in QLabel() you can put a name for this label, or input where this label is positioned.
    # for here, we input the location in the bracket.
    label = QtWidgets.QLabel(win)
    label.setText('my first label')
    label.move(50, 50)


    button1 = QtWidgets.QPushButton(win)
    button1.setText('my first button')
    # when you click the button, it will print "clicked button" in console
    button1.clicked.connect(clicked)







    win.show()
    # it means we are waiting for the window to close. if you click the close button, then the window will close.
    sys.exit(app.exec_())



window()