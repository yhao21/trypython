from PyQt5.QtWidgets import *
import sys


class synferlo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_status_bar()
        self.init_label_button()


    def init_window(self):
        self.setWindowTitle('this is synferlo database')
        self.resize(400, 300)
        self.move(600, 300)

    def init_status_bar(self):
        self.statusBar().showMessage('Home Page')

    def init_label_button(self):
        label_1 = QLabel('First Label')
        label_2 = QLabel('Second Label')

        button_1 = QPushButton('Fisrt Button')
        button_2 = QPushButton('Second Button')

        hbox_1 = QHBoxLayout()
        hbox_2 = QHBoxLayout()

        # 将同一行的label和按钮放在一个hbox中
        hbox_1.addWidget(label_1)
        hbox_1.addWidget(button_1)

        hbox_2.addWidget(label_2)
        hbox_2.addWidget(button_2)

        # 将两个hbox使用vbox对齐，这样，hbox中的两个值也就与另外一个hbox中的两个值垂直对齐了
        vbox = QVBoxLayout()

        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        # 创建一个窗口部件
        layout_widget = QWidget()
        layout_widget.setLayout(vbox)

        # 加入这一行，才能显示出label和button
        self.setCentralWidget(layout_widget)

        """
        s6 中使用grid layout完成与vbox hbox相同的布局
        """



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = synferlo()
    win.show()
    app.exit(app.exec())