from PyQt5.QtWidgets import *
import sys, os
from threading import Thread


class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_layout()
        self.init_fb()
        # self.open_browser()
        self.init_action()


    def init_window(self):
        self.resize(600, 500)
        self.move(400, 200)

    def init_layout(self):
        self.Main = QWidget()
        self.Main_layout = QGridLayout()
        self.Main.setLayout(self.Main_layout)

        self.fb = QWidget()
        self.fb_layout = QGridLayout()
        self.fb.setLayout(self.fb_layout)

        self.Main_layout.addWidget(self.fb, 1, 1, 3, 3)
        self.setCentralWidget(self.Main)

    def init_fb(self):

        self.button1 = QPushButton('Open')
        self.path = QLineEdit()

        self.fb_layout.addWidget(self.button1, 0, 0, 1, 1)
        self.fb_layout.addWidget(self.path, 1, 0, 1, 1)

    def init_action(self):
        self.button1.clicked.connect(lambda: self.view())


    def view(self):
        file_path = QFileDialog.getExistingDirectory(self, 'View', os.getcwd())
        self.path.setText(file_path)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = GUI()
    win.show()
    app.exit(app.exec_())