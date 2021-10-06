import sys
from PyQt5.QtWidgets import QApplication, QWidget
"""
sys模块提供了访问由解释器使用或维护的变量和与解释器进行交互的函数

"""
# 我们实例化了一个应用程序对象QApplication()，在PyQt5中，每个应用程序都必须实例化一个QApplication()
app = QApplication(sys.argv)
# 然后我们创建了一个QWidget()对象，它是pyqt5中所有的图形用户界面的基类
win = QWidget()
win.show()

# 最后，我们调用应用程序对象的exec_()方法来运行程序的主循环，并使用sys.exit()方法确保程序能够完美的退出
sys.exit(app.exec())



