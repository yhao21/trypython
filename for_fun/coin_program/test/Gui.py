from PyQt5.QtWidgets import *
import sys, time
from PyQt5.QtCore import QThread, pyqtSignal
import os

from threading import Thread




class Gui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.run = False
        self.init_window()
        # self.checkstatus()


    def init_window(self):
        self.resize(400, 300)
        self.move(600, 200)

        self.main = QWidget()
        self.main_layout = QGridLayout()
        self.main.setLayout(self.main_layout)

        self.board = QWidget()
        self.board_layout = QHBoxLayout()
        self.board.setLayout(self.board_layout)

        self.list = QListWidget()



        self.button1 = QPushButton('button_1')
        self.button1.clicked.connect(lambda: self.gogogo())

        self.button2 = QPushButton('button_2')
        self.button2.clicked.connect(lambda: os._exit(0))

        self.browser = QTextBrowser()

        self.board_layout.addWidget(self.list)

        self.main_layout.addWidget(self.board, 5, 0, 3, 6)
        self.main_layout.addWidget(self.browser,0,0,2,4)
        self.main_layout.addWidget(self.button1,0,5,1,1)
        self.main_layout.addWidget(self.button2,0,7,1,1)

        self.setCentralWidget(self.main)

    def gogogo(self):

        thread1 = my_print(self)
        thread1.start()

    def checkstatus(self):
        while True:
            if self.run == False:
                pass
            # if self.run == True:
            #     thread1 = my_print(self)
            #     thread1.start()


class my_print(Thread):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.a = 0
        self.Run = True

    def run(self):
        while self.Run:
            self.a += 1
            print(self.a)
            self.ui.list.addItem(str(self.a))
            time.sleep(1)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Gui()
    win.show()

    app.exit(app.exec_())