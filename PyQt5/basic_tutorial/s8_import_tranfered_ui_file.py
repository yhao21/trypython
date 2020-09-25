import sys
import ui_new_ui
from PyQt5.QtWidgets import *
import s9_edit_ui_trans_py

"""
从ui转换的py文件是没法自己直接运行的，需要我们自己创建py文件然后调用转换的py文件生成窗口
"""



if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # mainwindow = QMainWindow()
    # ui = ui_new_ui.Ui_MainWindow()
    # ui.setupUi(mainwindow)
    # mainwindow.show()
    # app.exit(app.exec())


    app = QApplication(sys.argv)
    mainwin = QMainWindow()
    ui = s9_edit_ui_trans_py.Ui_MainWindow()
    ui.setupUi(mainwin)
    mainwin.show()
    app.exit(app.exec())