from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QThread
import sys, time
from threading import Thread

class Process(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_layout()
        self.init_item()

    def init_window(self):
        self.resize(600, 500)
        self.move(400, 200)

    def init_layout(self):
        self.Main = QWidget()
        self.Main_layout = QGridLayout()
        self.Main.setLayout(self.Main_layout)

        self.table = QWidget()
        self.table_layout = QGridLayout()
        self.table.setLayout(self.table_layout)

        self.Main_layout.addWidget(self.table)

        self.setCentralWidget(self.Main)

    def init_item(self):
        self.pb = QProgressBar()
        self.pb.setValue(0)

        self.button = QPushButton('Push Me')
        self.button.clicked.connect(lambda: self.start_pb())


        self.table_layout.addWidget(self.pb, 0, 0, 1, 3)
        self.table_layout.addWidget(self.button, 1, 1, 1, 1)


    def start_pb(self):
        self.mission = Mission(self, 30)
        self.mission.progressBarValue.connect(self.bar)
        self.mission.start()

    def bar(self, val):
        self.pb.setValue(val)



class Mission(QThread):
    progressBarValue = pyqtSignal(float)

    def __init__(self, ui,job):
        super().__init__()
        self.ui = ui
        self.jb = job
        self.Run = True

    def run(self):
        while self.Run:
            for i in range(self.jb + 1):
                partial = (i/self.jb) * 100
                self.progressBarValue.emit(partial)
                print(partial)
                time.sleep(0.1)
                if partial == 100:
                    self.Run = False




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Process()
    win.show()
    app.exit(app.exec_())