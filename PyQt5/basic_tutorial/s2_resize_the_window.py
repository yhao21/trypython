import sys
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)

win = QWidget()
# 窗口长、宽
win.resize(450,150)
# 窗口运行时候在屏幕的位置
win.move(900,500)
# 窗口标题
win.setWindowTitle('my first GUI')
win.show()


sys.exit(app.exec())
