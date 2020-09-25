import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

"""
在Designer中 Ctrl + R 可以对设计的界面进行预览
"""



"""
使用QtCore 中的Qt辅助grid layout进行alignment布局
"""
#
#
# class synferlo(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.init_window()
#         self.init_status_bar()
#         self.init_layout()
#
#
#     def init_window(self):
#         self.setWindowTitle('this is synferlo dataset')
#         self.resize(400, 300)
#         self.move(600, 400)
#
#     def init_status_bar(self):
#         self.statusBar().showMessage('Home Page')
#
#     def init_layout(self):
#         label_1 = QLabel('First Label')
#         label_2 = QLabel('Second Label')
#
#         button_1 = QPushButton('First Button')
#         button_2 = QPushButton('Second Button')
#
#         grid = QGridLayout()
#         grid.addWidget(label_1, 0, 0)
#         grid.addWidget(label_2, 1, 0)
#         grid.addWidget(button_1, 0, 1)
#         grid.addWidget(button_2, 1, 1)
#
#         # 整体移动到顶端，顶端对齐
#         grid.setAlignment(Qt.AlignTop)
#
#         # 也可以单独对某一个部件位置进行调整, first label就右对齐了
#         grid.setAlignment(label_1, Qt.AlignRight)
#
#         layout_widget = QWidget()
#         layout_widget.setLayout(grid)
#
#         self.setCentralWidget(layout_widget)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = synferlo()
#     win.show()
#     app.exit(app.exec())


"""

添加button_3 位于第三行，横贯1至5列
"""

class synferlo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_status_bar()
        self.init_menu()
        self.init_layout()



    def init_window(self):
        self.setWindowTitle('this is my program')
        self.resize(400, 300)
        self.move(500, 300)

    def init_status_bar(self):
        self.statusBar().showMessage('Home Page')


    def init_menu(self):
        menu = self.menuBar()
        file = menu.addMenu('File')
        file.addSeparator()
        edit = menu.addMenu('Edit')

        file_open = QAction('open a new file', self)
        file_quit = QAction('quit program    Ctrl + Q', self)
        edit_copy = QAction('copy and paste', self)


        file_quit.triggered.connect(self.close)

        file.addAction(file_open)
        file.addAction(file_quit)
        edit.addAction(edit_copy)

    def init_layout(self):
        label_1 = QLabel('First Label')
        label_2 = QLabel('Second Label')
        button_1 = QPushButton('First Button')
        button_2 = QPushButton('Second Button')
        button_3 = QPushButton('Third Button')

        grid = QGridLayout()
        grid.addWidget(label_1, 0, 0)
        grid.addWidget(label_2, 1, 0)
        grid.addWidget(button_1, 0, 1)
        grid.addWidget(button_2, 1, 1)

        # 后两个数值表示这个button占了几行几列
        grid.addWidget(button_3, 2, 0, 1, 10)

        grid.setAlignment(Qt.AlignTop)

        layout_widget = QWidget()
        layout_widget.setLayout(grid)

        self.setCentralWidget(layout_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = synferlo()
    win.show()
    app.exit(app.exec())