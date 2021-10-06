from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from menu_bar import Ui_MainWindow





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = QMainWindow()
    ui = Ui_MainWindow().setupUi(win)
    win.show()
    app.exit(app.exec_())
