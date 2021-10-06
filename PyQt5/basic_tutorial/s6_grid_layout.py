import sys
from PyQt5.QtWidgets import *


class synferlo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_status_bar()
        self.init_label_button_layout()

    def init_window(self):
        self.setWindowTitle('this is my dataframe')
        self.resize(400, 300)
        self.move(600, 400)

    def init_status_bar(self):
        self.statusBar().showMessage('Home Page')

    def init_label_button_layout(self):
        label_1 = QLabel('First Label')
        label_2 = QLabel('Second Label')

        button_1 = QPushButton('First Button')
        button_2 = QPushButton('Second Button')

        # create GridLayout()
        grid_layout = QGridLayout()

        grid_layout.addWidget(label_1, 0, 0)
        grid_layout.addWidget(label_2, 1, 0)
        grid_layout.addWidget(button_1, 0, 1)
        grid_layout.addWidget(button_2, 1, 1)

        layout_widget = QWidget()
        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win =  synferlo()
    win.show()
    app.exit(app.exec())