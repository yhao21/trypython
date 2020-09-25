from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *

import sys


class SanGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window()
        self.init_menu()
        self.init_info()
        self.init_maingame()
        self.init_progress()
        self.init_background()


    def init_window(self):
        self.resize(1280, 720)
        self.move(300, 100)

        self.Main = QWidget()
        self.Main_layout = QGridLayout()
        self.Main.setLayout(self.Main_layout)

        self.Info = QWidget()
        self.Info_layout = QGridLayout()
        self.Info.setLayout(self.Info_layout)

        self.Progress = QWidget()
        self.Progress_layout = QGridLayout()
        self.Progress.setLayout(self.Progress_layout)

        self.MainGame = QWidget()
        self.MainGame_layout = QGridLayout()
        self.MainGame.setLayout(self.MainGame_layout)

        self.MainGame.setStyleSheet('QWidget{background:url(background.jpg)}')


        self.Main_layout.addWidget(self.Info, 0, 0, 1, 20)
        self.Main_layout.addWidget(self.Progress, 1, 0, 21, 4)
        self.Main_layout.addWidget(self.MainGame, 1, 4, 21, 16)





        self.setCentralWidget(self.Main)

    def init_menu(self):
        self.menu = self.menuBar()
        self.building = self.menu.addMenu('建造')
        self.military = self.menu.addMenu('军事')

        # 建造
        self.b_econ = QMenu('经济建筑', self)
        self.b_mili = QMenu('军事建筑', self)
        self.b_foreign = QMenu('外交建筑', self)

        self.building.addMenu(self.b_econ)
        self.building.addMenu(self.b_mili)
        self.building.addMenu(self.b_foreign)

        # 经济建筑
        self.mkt = QAction('市场', self)
        self.farm = QAction('农场', self)
        self.lumber = QAction('伐木场', self)
        self.ore = QAction('采矿场', self)

        self.b_econ.addAction(self.mkt)
        self.b_econ.addAction(self.farm)
        self.b_econ.addAction(self.lumber)
        self.b_econ.addAction(self.ore)

        # 军事建筑
        self.camp = QAction('兵营', self)
        self.stable = QAction('马厩', self)
        self.range = QAction('射手营', self)
        self.machine = QAction('攻城器械厂', self)

        self.b_mili.addAction(self.camp)
        self.b_mili.addAction(self.stable)
        self.b_mili.addAction(self.range)
        self.b_mili.addAction(self.machine)

        # 外交建筑


        # 军事
        self.m_training = QAction('训练', self)
        self.m_conscription = QAction('征兵', self)

        self.military.addAction(self.m_training)
        self.military.addAction(self.m_conscription)

        # Font
        self.menu_font = self.menu.font()
        self.menu_font.setPointSize(14)
        self.menu_font.setFamily('楷体')

        self.menu.setFont(self.menu_font)
        self.building.setFont(self.menu_font)
        self.b_econ.setFont(self.menu_font)
        self.b_mili.setFont(self.menu_font)
        self.military.setFont(self.menu_font)


    def init_info(self):
        self.money_L = QLabel('金币:')
        self.wheat_L = QLabel('粮食:')
        self.lumber_L = QLabel('木材:')
        self.ore_L = QLabel('铁矿:')
        self.population_L = QLabel('人口:')

        self.money_L.setAlignment(Qt.AlignCenter)
        self.wheat_L.setAlignment(Qt.AlignCenter)
        self.lumber_L.setAlignment(Qt.AlignCenter)
        self.ore_L.setAlignment(Qt.AlignCenter)
        self.population_L.setAlignment(Qt.AlignCenter)

        self.info_font = QFont()
        self.info_font.setPointSize(13)
        self.info_font.setFamily('楷体')

        self.money_L.setFont(self.info_font)
        self.wheat_L.setFont(self.info_font)
        self.lumber_L.setFont(self.info_font)
        self.ore_L.setFont(self.info_font)
        self.population_L.setFont(self.info_font)

        self.money_LE = QLabel()
        self.wheat_LE = QLabel()
        self.lumber_LE = QLabel()
        self.ore_LE = QLabel()
        self.population_LE = QLabel()

        self.money_LE.setFixedSize(150, 25)
        self.wheat_LE.setFixedSize(150, 25)
        self.lumber_LE.setFixedSize(150, 25)
        self.ore_LE.setFixedSize(150, 25)
        self.population_LE.setFixedSize(150, 25)

        self.money_LE.setAlignment(Qt.AlignRight)
        self.wheat_LE.setAlignment(Qt.AlignRight)
        self.lumber_LE.setAlignment(Qt.AlignRight)
        self.ore_LE.setAlignment(Qt.AlignRight)
        self.population_LE.setAlignment(Qt.AlignRight)


        self.money_LE.setStyleSheet('background:white; border-width:1; border-style:solid; border-color:black')
        self.wheat_LE.setStyleSheet('background:white; border-width:1; border-style:solid; border-color:black')
        self.lumber_LE.setStyleSheet('background:white; border-width:1; border-style:solid; border-color:black')
        self.ore_LE.setStyleSheet('background:white; border-width:1; border-style:solid; border-color:black')
        self.population_LE.setStyleSheet('background:white; border-width:1; border-style:solid; border-color:black')


        self.Info_layout.addWidget(self.money_L, 0, 0, 1, 2)
        self.Info_layout.addWidget(self.money_LE, 0, 2, 1, 2)
        self.Info_layout.addWidget(self.wheat_L, 0, 4, 1, 2)
        self.Info_layout.addWidget(self.wheat_LE, 0, 6, 1, 2)
        self.Info_layout.addWidget(self.lumber_L, 0, 8, 1, 2)
        self.Info_layout.addWidget(self.lumber_LE, 0, 10, 1, 2)
        self.Info_layout.addWidget(self.ore_L, 0, 12, 1, 2)
        self.Info_layout.addWidget(self.ore_LE, 0, 14, 1, 2)
        self.Info_layout.addWidget(self.population_L, 0, 16, 1, 2)
        self.Info_layout.addWidget(self.population_LE, 0, 18, 1, 2)

    def init_maingame(self):

        self.maingame_title = QLabel('建筑信息')
        self.mkt1 = QPushButton('市场1')
        self.mkt2 = QPushButton('市场2')
        self.farm1 = QPushButton('农场1')
        self.farm2 = QPushButton('农场2')
        self.lumber1 = QPushButton('伐木场1')
        self.lumber2 = QPushButton('伐木场2')
        self.ore1 = QPushButton('矿场1')
        self.ore2 = QPushButton('矿场2')
        self.camp1 = QPushButton('兵营1')
        self.camp2 = QPushButton('兵营2')
        self.range1 = QPushButton('射手营1')
        self.range2 = QPushButton('射手营2')
        self.stable1 = QPushButton('马厩1')
        self.stable2 = QPushButton('马厩2')
        self.machine = QPushButton('器械厂')
        self.trade = QPushButton('交易市场')
        self.policy = QPushButton('策略营')
        self.tavern = QPushButton('酒馆')

        self.mkt1.setStyleSheet('background:white')

        self.maingame_title.setFont(QFont('楷体', 20))
        self.maingame_title.setAlignment(Qt.AlignCenter)

        self.MainGame_layout.addWidget(self.maingame_title, 1, 0, 1, 12)

        self.MainGame_layout.addWidget(self.mkt1, 1, 1, 2, 3)
        self.MainGame_layout.addWidget(self.mkt2, 1, 5, 2, 3)
        self.MainGame_layout.addWidget(self.farm1, 1, 9, 2, 3)

        self.MainGame_layout.addWidget(self.farm2, 2, 1, 2, 3)
        self.MainGame_layout.addWidget(self.lumber1, 2, 5, 2, 3)
        self.MainGame_layout.addWidget(self.lumber2, 2, 9, 2, 3)

        self.MainGame_layout.addWidget(self.ore1, 3, 1, 2, 3)
        self.MainGame_layout.addWidget(self.ore2, 3, 5, 2, 3)
        self.MainGame_layout.addWidget(self.camp1, 3, 9, 2, 3)

        self.MainGame_layout.addWidget(self.camp2, 4, 1, 2, 3)
        self.MainGame_layout.addWidget(self.range1, 4, 5, 2, 3)
        self.MainGame_layout.addWidget(self.range2, 4, 9, 2, 3)

        self.MainGame_layout.addWidget(self.stable1, 5, 1, 2, 3)
        self.MainGame_layout.addWidget(self.stable2, 5, 5, 2, 3)
        self.MainGame_layout.addWidget(self.machine, 5, 9, 2, 3)

        self.MainGame_layout.addWidget(self.trade, 6, 1, 2, 3)
        self.MainGame_layout.addWidget(self.policy, 6, 5, 2, 3)
        self.MainGame_layout.addWidget(self.tavern, 6, 9, 2, 3)



    def init_progress(self):
        self.upgrade1 = QLabel('队列1')
        self.upgrade2 = QLabel('队列2')
        self.upgrade3 = QLabel('队列3')
        self.upgrade4 = QLabel('队列4')
        self.upgrade5 = QLabel('队列5')

        self.t1 = QLabel()
        self.t2 = QLabel()
        self.t3 = QLabel()
        self.t4 = QLabel()
        self.t5 = QLabel()

        self.p1 = QProgressBar()
        self.p2 = QProgressBar()
        self.p3 = QProgressBar()
        self.p4 = QProgressBar()
        self.p5 = QProgressBar()

        self.p1.setFixedSize(200, 15)
        self.p2.setFixedSize(200, 15)
        self.p3.setFixedSize(200, 15)
        self.p4.setFixedSize(200, 15)
        self.p5.setFixedSize(200, 15)


        self.blank = QLabel()

        self.Progress_layout.addWidget(self.upgrade1, 0, 0, 1, 1)
        self.Progress_layout.addWidget(self.t1, 1, 0, 1, 1)
        self.Progress_layout.addWidget(self.p1, 2, 0, 1, 4)

        self.Progress_layout.addWidget(self.upgrade2, 3, 0, 1, 1)
        self.Progress_layout.addWidget(self.t2, 4, 0, 1, 1)
        self.Progress_layout.addWidget(self.p2, 5, 0, 1, 4)

        self.Progress_layout.addWidget(self.upgrade3, 6, 0, 1, 1)
        self.Progress_layout.addWidget(self.t3, 7, 0, 1, 1)
        self.Progress_layout.addWidget(self.p3, 8, 0, 1, 4)

        self.Progress_layout.addWidget(self.upgrade4, 9, 0, 1, 1)
        self.Progress_layout.addWidget(self.t4, 10, 0, 1, 1)
        self.Progress_layout.addWidget(self.p4, 11, 0, 1, 4)

        self.Progress_layout.addWidget(self.upgrade5, 12, 0, 1, 1)
        self.Progress_layout.addWidget(self.t5, 13, 0, 1, 1)
        self.Progress_layout.addWidget(self.p5, 14, 0, 1, 4)

        self.Progress_layout.addWidget(self.blank, 15, 0, 10, 4)


        self.Progress.setFont(QFont('楷体', 12))

    def init_background(self):

        # opacity = QGraphicsOpacityEffect()
        # opacity.setOpacity(0.5)
        #
        # self.Info.setStyleSheet('background:rgb(199, 199, 199)')
        #
        self.Progress.setStyleSheet('background:rgb(199, 199, 199)')


        self.MainGame.setFont(self.menu_font)
        # self.MainGame.setStyleSheet('background:white')
        # self.MainGame.setGraphicsEffect(opacity)


        self.Main_layout.setSpacing(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SanGUI()
    # win.setStyleSheet('QMainWindow{background:url(background.jpg)}')
    win.show()
    app.exit(app.exec_())
