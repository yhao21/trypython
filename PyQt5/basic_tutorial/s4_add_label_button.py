from PyQt5.QtWidgets import *
import sys


class synferlo(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_status_bar()
        self.init_menu()
        self.init_label_button()

    def init_window(self):
        self.setWindowTitle('my GUI program')
        self.resize(400,300)
        self.move(600,300)

    def init_status_bar(self):
        self.statusBar().showMessage('Home Page')

    def init_menu(self):
        menu = self.menuBar()
        file = menu.addMenu('File')
        file.addSeparator()
        edit = menu.addMenu('Edit')

        file_open = QAction('open a new file', self)
        file_quit = QAction('quit program', self)
        edit_copy = QAction('copy', self)

        file_open.setStatusTip('open a new file')
        file_quit.setStatusTip('close the program')
        edit_copy.setStatusTip('copy')

        file_quit.triggered.connect(self.close)

        file.addAction(file_open)
        file.addAction(file_quit)
        edit.addAction(edit_copy)

    def init_label_button(self):
        label_1 = QLabel('my first label', self)
        label_2 = QLabel('my second label', self)
        # check the size of menue bar. 100 long, 30 high
        # PyQt5.QtCore.QSize(100, 30)
        menu_size = self.menuBar().size()
        # 30
        menu_height = self.menuBar().height()
        # 100
        menu_width = self.menuBar().width()
        # position the label below menu bar. so need to move down by menu height
        label_1.move(10, menu_height)
        # # label's height is 30
        # print(label_1.height())
        label_2.move(10, menu_height * 2)

        # 两个button分别于label平行，且两个button在同一垂线位置上对齐
        button_1 = QPushButton('button 1', self)
        button_2 = QPushButton('button 2', self)
        button_1.move(label_1.width(), menu_height)
        button_2.move(label_1.width(), menu_height * 2)

        # 使用move调整非常灵活，但是对于大量部件的位置调整有些乏力。需要我们使用水平和垂直布局，以及网格布局，s5中设计这两个布局





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = synferlo()
    win.show()
    app.exit(app.exec())