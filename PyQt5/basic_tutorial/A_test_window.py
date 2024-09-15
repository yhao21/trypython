import sys
from PyQt5.QtWidgets import *
import ui_regression
from Widget_in_Window import my_mainwindow


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = QMainWindow()
#     ui = ui_regression.Ui_MainWindow()
#     ui.setupUi(win)
#     win.show()
#     sys.exit(app.exec())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = my_mainwindow.Ui_MainWindow()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec())
