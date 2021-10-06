import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont



class TerminalGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_layout()
        self.init_console()
        self.win_decoration()

    def init_window(self):
        self.setWindowTitle('SynFerlo Terminal v1.0')
        self.resize(900, 500)
        self.move(400, 200)

    def init_layout(self):
        self.Main = QWidget()
        self.Main_layout = QHBoxLayout()
        self.Main.setLayout(self.Main_layout)

        self.setCentralWidget(self.Main)

    def init_console(self):
        self.console = QPlainTextEdit()
        self.console.insertPlainText('Synferlo OS v1.0 ~$ ')

        self.Main_layout.addWidget(self.console)
        self.console.blockCountChanged.connect(lambda: self.submit_())

    def submit_(self):
        self.console.insertPlainText('Synferlo OS v1.0 ~$ ')

    def win_decoration(self):
        # self.Main.setStyleSheet('QWidget{background:black}')
        # self.console.setStyleSheet('QPlainTextEdit{border:black}')

        tfont = QFont()
        tfont.setFamily('Consolas')
        tfont.setPointSize(12)


        self.console.setFont(tfont)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TerminalGUI()
    win.show()
    app.exit(app.exec_())