import sys
from PyQt5.QtWidgets import *

"""
basic oop
"""

# class my_GUI():
#
#     def __init__(self):
#         self.win = QWidget()
#         self.win.setWindowTitle('my gui')
#
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     gui = my_GUI()
#     gui.win.show()
#     app.exit(app.exec())




"""
inheritage
"""


# class my_GUI(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('my_gui')
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     gui = my_GUI()
#     gui.show()
#     app.exit(app.exec())


"""
MainWindow
"""

# class my_GUI(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('my_window')
#         self.resize(400,100)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     gui = my_GUI()
#     gui.show()
#     app.exit(app.exec())


"""
form your window
"""

# class my_GUI(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setup_window()
#         self.toolbar()
#
#
#     def setup_window(self):
#         self.setWindowTitle("this is synferlo")
#         self.resize(400,300)
#
#
#     def toolbar(self):
#         # 设置状态消息栏文本
#         self.statusBar().showMessage('current status')
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     gui = my_GUI()
#     gui.show()
#
#     app.exit(app.exec())


"""
add menu
"""
#
# class synferlo(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.setup_window()
#         self.status_bar()
#         self.setup_menu()
#
#
#     def setup_window(self):
#         self.setWindowTitle('welcome to my program')
#         self.resize(400,300)
#
#     def status_bar(self):
#         self.statusBar().showMessage('current status')
#
#     def setup_menu(self):
#         # create a menu bar
#         menu = self.menuBar()
#         # add a menu button
#         file_menu = menu.addMenu('File')
#
#         # add actions under File
#         open_file = QAction('open',self)
#         save_file = QAction('save',self)
#
#         # link action
#         file_menu.addAction(open_file)
#         file_menu.addAction(save_file)
#
#         # update status bar
#         open_file.setStatusTip('open a file')
#         save_file.setStatusTip('save current file')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     gui = synferlo()
#     gui.show()
#     app.exit(app.exec())
#





"""
add another menu button, add a quit action under File
"""

class synferlo(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_menu()
        # self.init_statusbar()
        self.init_window()


    def init_window(self):
        self.setWindowTitle('welcome to my program')
        self.resize(400,300)


    def init_statusbar(self):
        self.statusBar().showMessage('Home Page')


    def init_menu(self):
        menu = self.menuBar()
        file = menu.addMenu('File')
        # 添加平行结构菜单需要用 addSeparator()
        file.addSeparator()
        edit = menu.addMenu('Edit')

        file_open = QAction('create a new file ....', self)
        file_quit = QAction('quit', self)
        edit_copy = QAction('copy', self)

        file_open.setStatusTip('create a new file')
        file_quit.setStatusTip('quit the program')
        edit_copy.setStatusTip('copy content')


        file.addAction(file_open)
        edit.addAction(edit_copy)


        # click to close the program
        file_quit.triggered.connect(self.close)
        file.addAction(file_quit)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = synferlo()
    win.show()
    app.exit(app.exec())



