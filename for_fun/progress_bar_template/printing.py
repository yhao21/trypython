import sys, time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor


class Stream(QObject):
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))


class GenMast(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        sys.stdout = Stream(newText = self.onUpdateText)


    def onUpdateText(self, text):
        cursor = self.process.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()

    def closeEvent(self, event):
        sys.stdout = sys.__stdout__
        super().closeEvent(event)

    def initUI(self):
        button = QPushButton('run', self)
        button.move(450, 50)
        button.resize(100, 200)
        button.clicked.connect(self.genMastClicked)

        self.process = QTextEdit(self)
        self.process.setReadOnly(True)
        self.process.ensureCursorVisible()
        self.process.setLineWrapColumnOrWidth(500)
        self.process.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.process.setFixedWidth(400)
        self.process.setFixedHeight(200)
        self.process.move(30, 50)

        self.setGeometry(300, 300, 600, 300)
        self.show()

    def printhello(self):
        for i in range(5):
            print('hello')
            time.sleep(1)

    def genMastClicked(self):
        self.printhello()
        loop = QEventLoop()
        QTimer.singleShot(2000, loop.quit)
        loop.exec_()
        print('Done.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    gui = GenMast()
    sys.exit(app.exec_())
