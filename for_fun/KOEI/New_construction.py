from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
from threading import Thread
import numpy as np
import pandas as pd
import sys, os

class NewConstruction(QDialog):
    def __init__(self, ui):
        super().__init__()
        self.init_window()
        self.init_layout()
        self.init_construction()
        self.init_database()
        self.ui = ui

    def init_window(self):
        self.resize(500, 600)
        self.move(600, 300)
        self.setWindowTitle('三国志战略版 v1.0')

    def init_layout(self):
        self.Main = QWidget()
        self.Main_layout = QGridLayout()
        self.Main.setLayout(self.Main_layout)

        self.Building = QWidget()
        self.Building_layout = QGridLayout()
        self.Building.setLayout(self.Building_layout)

        self.Main_layout.addWidget(self.Building, 0, 0, 15, 4)

        self.setLayout(self.Main_layout)


    def init_construction(self):

        self.title = QLabel('建筑信息')
        self.title.setFont(QFont('楷体', 20))
        self.title.setAlignment(Qt.AlignCenter)

        self.confirm = QPushButton('建造')
        self.cancellation = QPushButton('取消')
        self.confirm.setFont(QFont('楷体', 13))
        self.cancellation.setFont(QFont('楷体', 13))

        self.confirm.clicked.connect(lambda: self.confirm_construction())
        self.cancellation.clicked.connect(self.close)


        building = [['市场', '农场', '伐木场', '铁矿场'], ['兵营', '靶场', '马厩', '器械厂'], ['策略营', '外交部', '交易所', '军乐台']]
        # 用于存储按钮身份码存入这个列表中
        self.b_button = []

        for row in range(1, 4):
            for col in range(1, 5):
                # 将按钮身份码存入列表中
                self.b_button.append('building %d-%d' % (row, col))
                # 对应身份码在列表中的位置
                self.button_index = self.b_button.index('building %d-%d' % (row, col))
                # 创建对应位置的按钮
                self.b_button[self.button_index] = QPushButton()
                self.b_button[self.button_index].setText(building[row - 1][col - 1])

                self.b_button[self.button_index].setFont(QFont('楷体', 15))
                self.b_button[self.button_index].setFixedSize(80, 80)

                self.Building_layout.addWidget(self.b_button[self.button_index], row + 2, col - 1, 1, 1)
                # 按钮对象传入联动函数
                self.b_button[self.button_index].clicked.connect(lambda: self.building_selection(self.sender()))

        self.b_info = QPlainTextEdit()
        self.b_blank = QLabel()
        self.b_blank1 = QLabel()
        self.b_blank2 = QLabel()
        self.b_blank1.setFixedHeight(10)
        self.b_blank2.setFixedHeight(10)

        self.b_info.setFont(QFont('楷体', 13))

        self.Building_layout.addWidget(self.title, 0, 0, 1, 4)
        self.Building_layout.addWidget(self.b_blank1, 1, 0, 1, 4)
        self.Building_layout.addWidget(self.b_blank, 6, 0, 1, 1)
        self.Building_layout.addWidget(self.confirm, 7, 0, 1, 2)
        self.Building_layout.addWidget(self.cancellation, 7, 2, 1, 2)
        self.Building_layout.addWidget(self.b_blank2, 8, 0, 1, 4)
        self.Building_layout.addWidget(self.b_info, 9, 0, 10, 4)


    def init_database(self):
        self.df = pd.read_excel(os.path.join('data', 'new_construction.xlsx'))


    def building_selection(self, building):
        # 清空文本框
        self.b_info.clear()
        self.b_name = building.text() + ' Lv.1'

        # 根据建筑这一列搜索 （因为我传入的是建筑名）
        self.df.index = self.df['建筑']
        # 根据建筑名将对应建筑名所在的行提取出来 i.e. ['交易所', 2000, 1000, 1000, 500, 0, 20]
        self.ui.building_info_list = list(self.df.loc[self.b_name, :])
        print(self.ui.building_info_list)
        # 获取列名 金币 粮食 木材。。。
        b_items = list(self.df.columns)
        for item in range(len(b_items)):
            self.b_info.insertPlainText('%s : %s\n' % (b_items[item], self.ui.building_info_list[item]))

    def confirm_construction(self):
        for queue in range(1, 5):
            self.ui.obj_queue = self.ui.findChild(QLabel, 'Queue %d' % queue)
            if self.ui.obj_queue.text() == '空闲队列.....':
                self.ui.start_construction = True
                self.close()

        self.b_info.clear()
        self.b_info.insertPlainText('队列已满，请稍后再试！')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = NewConstruction()
    win.show()
    app.exit(app.exec_())