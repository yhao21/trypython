import sys, time
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QCursor, QPalette, QBrush, QPixmap
from threading import Thread

from New_construction import NewConstruction
from time_countdown import clock_time_left as ctl


class SanGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mouse_flag = False
        self.resource_value = []
        self.start_construction = False
        self.init_window()
        self.init_layout()
        self.init_title()
        self.init_info()
        self.init_progress()
        self.init_maingame()
        self.init_resource_productivity()

    def init_window(self):
        self.resize(1000, 720)
        self.move(400, 100)

    def init_layout(self):
        self.Main = QWidget()
        self.Main_layout = QGridLayout()
        self.Main.setLayout(self.Main_layout)

        self.Title = QWidget()
        self.Title_layout = QGridLayout()
        self.Title.setLayout(self.Title_layout)

        self.Info = QWidget()
        self.Info_layout = QHBoxLayout()
        self.Info.setLayout(self.Info_layout)

        self.Progress = QWidget()
        self.Progress_layout = QGridLayout()
        self.Progress.setLayout(self.Progress_layout)

        self.MainGame = QWidget()
        self.MainGame_layout = QGridLayout()
        self.MainGame.setLayout(self.MainGame_layout)

        self.Main_layout.addWidget(self.Title, 0, 0, 1, 10)
        self.Main_layout.addWidget(self.Info, 1, 0, 1, 10)
        self.Main_layout.addWidget(self.Progress, 2, 0, 25, 2)
        self.Main_layout.addWidget(self.MainGame, 2, 2, 25, 8)

        self.setCentralWidget(self.Main)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.Main_layout.setSpacing(0)

        win_bg = QPalette()
        win_bg.setBrush(self.backgroundRole(), QBrush(QPixmap('background.jpg')))
        self.setPalette(win_bg)


    def init_title(self):
        # self.Title.setStyleSheet('background:rgb(199,199,199)')
        self.Title.setFixedHeight(40)

        self.closeGUI = QPushButton('关闭')
        self.miniGUI = QPushButton('隐藏窗口')
        self.title_str = QLabel('三国志战略版 v1.0')

        self.title_str.setAlignment(Qt.AlignCenter)
        self.closeGUI.setFixedSize(80, 20)
        self.miniGUI.setFixedSize(80, 20)

        self.title_str.setFont(QFont('楷体', 15))
        self.closeGUI.setFont(QFont('楷体', 10))
        self.miniGUI.setFont(QFont('楷体', 10))

        self.title_str.setStyleSheet('QLabel{color:white}')
        self.closeGUI.setStyleSheet('QPushButton{color: white;border-radius: 10px; background: rgb(255,125,125)}QPushButton:hover{background:rgb(199,199,199)}')
        self.miniGUI.setStyleSheet('QPushButton{color: white; border-radius: 10px; background: rgb(161,245,161)}QPushButton:hover{background:rgb(199,199,199)}')

        self.Title_layout.addWidget(self.title_str, 0, 0, 1, 8)
        self.Title_layout.addWidget(self.miniGUI, 0, 9, 1, 1)
        self.Title_layout.addWidget(self.closeGUI, 0, 10, 1, 1)


        self.closeGUI.clicked['bool'].connect(self.close)
        self.miniGUI.clicked['bool'].connect(self.showMinimized)

    def init_info(self):
        bg = QGraphicsOpacityEffect()
        bg.setOpacity(0.7)
        self.Info.setGraphicsEffect(bg)
        self.Info.setStyleSheet('background:white')
        self.Info.setFixedHeight(35)

        resource = ['金币 : ', '粮食 : ', '木材 : ', '铁矿 : ', '人口 : ']

        for label in range(1, 6):
            self.resource = QLabel()
            self.resource.setText(resource[label - 1])
            self.resource.setObjectName('resource %d' % label)
            self.r_value = QLabel()
            self.r_value.setObjectName('value %d' % label)

            if label != 5:
                self.r_value.setText('10000')
                self.resource_value.append(10000)
            else:
                self.r_value.setText('0')
                self.resource_value.append(0)

            self.resource.setAlignment(Qt.AlignRight)
            self.r_value.setFixedHeight(20)
            self.r_value.setAlignment(Qt.AlignRight)
            self.resource.setFont(QFont('楷体', 11))
            self.r_value.setStyleSheet('border-style: solid; border-width: 2px; border-color: black')

            self.Info_layout.addWidget(self.resource)
            self.Info_layout.addWidget(self.r_value)



    def init_progress(self):
        bg = QGraphicsOpacityEffect()
        bg.setOpacity(0.7)
        self.Progress.setGraphicsEffect(bg)
        self.Progress.setStyleSheet('background:rgb(199,199,199)')
        self.Progress.setFixedWidth(200)
        start_pos = 0

        for mission in range(1, 6):
            # 队列 i
            self.workload_index = QLabel('队列 %d' % mission)
            self.workload_index.setAlignment(Qt.AlignBottom)
            self.workload_index.setFont(QFont('楷体', 11))
            # 任务名称
            self.workload_name = QLabel('空闲队列.....')
            self.workload_name.setAlignment(Qt.AlignCenter)
            self.workload_name.setObjectName('Queue %d' % mission)
            self.workload_name.setFont(QFont('楷体', 11))
            # 剩余时间
            self.time_left = QLabel()
            self.time_left.setAlignment(Qt.AlignRight)
            self.time_left.setObjectName('time %d' % mission)
            self.time_left.setFixedHeight(20)
            self.time_left.setFont(QFont('Consolas', 11))
            # 进度条
            self.p = QProgressBar()
            self.p.setObjectName('p%d' % mission)
            self.p.setValue(0)
            self.p.setFixedHeight(10)

            self.Progress_layout.addWidget(self.workload_index, mission - 1 + start_pos, 0, 1, 1)
            self.Progress_layout.addWidget(self.workload_name, mission + start_pos, 0, 1, 1)
            self.Progress_layout.addWidget(self.time_left, mission + start_pos, 1, 1, 1)
            self.Progress_layout.addWidget(self.p, mission + 1 + start_pos, 0, 1, 2)
            start_pos += 3

        self.blank_pos = QLabel()
        self.Progress_layout.addWidget(self.blank_pos, 16, 0, 10, 2)


    def init_maingame(self):
        bg = QGraphicsOpacityEffect()
        bg.setOpacity(0.7)
        self.MainGame.setGraphicsEffect(bg)
        self.MainGame.setStyleSheet('background:rgb(199,199,199)')

        self.maingame_title = QLabel('主公的城池')
        self.maingame_title.setFont(QFont('楷体', 15))
        self.maingame_title.setAlignment(Qt.AlignCenter)
        self.maingame_title.setFixedHeight(50)

        self.land = []

        for col in range(1, 7):
            for row in range(1, 7):
                self.land.append('land %s-%s' % (row, col))
                self.button_index = self.land.index('land %s-%s' % (row, col))

                self.land[self.button_index] = QPushButton()
                self.land[self.button_index].setObjectName('land %s-%s' % (row, col))
                self.land[self.button_index].setText('空地')
                self.land[self.button_index].setFont(QFont('楷体', 13))
                self.land[self.button_index].setFixedSize(80,80)
                self.MainGame_layout.addWidget(self.land[self.button_index], row, col, 1, 1)

                self.land[self.button_index].clicked.connect(lambda: self.new_building(self.sender()))


        self.MainGame_layout.addWidget(self.maingame_title, 0, 2, 1, 4)
        # 根据objectname查找到控件，用于恢复记录
        # a = self.findChild(QPushButton, 'land 7-6')

    def init_resource_productivity(self):
        # 金币， 粮食， 木材， 铁矿
        self.productivity = {'市场': 0, '农场': 0, '伐木场': 0, '铁矿厂': 0}


    def new_building(self, land):
        self.land_position = land
        newb = NewConstruction(self)
        newb.show()
        newb.exec_()
        self.begin_construction()


    def begin_construction(self):
        if self.start_construction == True:
            self.start_construction = False
            # 接收即将建造建筑的成本信息
            self.new_b_info = self.building_info_list
            # 激活进度条
            self.activate_progress(self.new_b_info[0], self.new_b_info[6])
            self.resource_deduction()


    def activate_progress(self, mission_name, mission_time):
        for self.queue in range(1, 5):
            self.obj_queue = self.findChild(QLabel, 'Queue %d' % self.queue)
            if self.obj_queue.text() == '空闲队列.....':
                self.obj_queue.setText(mission_name)
                self.mission_allocation(mission_time)
                break
            else:
                pass

    def mission_allocation(self, m_time):
        # self.p_mission = Mission1(self, m_time)
        # self.p_mission.progressBarValue.connect(self.show_bar)
        # self.p_mission.start()
        # self.p_mission.exec_()

        self.p_t_mission = TimeMission(self, m_time)
        self.p_t_mission.start()
        self.p_t_mission.exec()

    def finish_construction(self):
        self.obj_queue.setText('空闲队列.....')
        self.show_time.setText('')
        # 传出来的空地按钮
        self.land_position.setText(self.new_b_info[0])


    # def activate_progress(self, mission_name, mission_time):
    #     self.mission_list = ['Mission1', 'Mission2', 'Mission3', 'Mission4']
    #
    #     for self.queue in range(1, 5):
    #         self.obj_queue = self.findChild(QLabel, 'Queue %d' % self.queue)
    #         if self.obj_queue.text() == '空闲队列.....':
    #             self.obj_queue.setText(mission_name)
    #             self.mission_allocation(mission_time)
    #             # self.init_progress_bar(mission_time)
    #             break
    #         else:
    #             pass


    # def mission_allocation(self, m_time):
    #     mission_index = self.queue - 1
    #     self.p_mission = eval(self.mission_list[mission_index])(self, m_time)
    #     self.p_mission.progressBarValue.connect(self.show_bar)
    #     self.p_mission.start()
    #     self.p_mission.exec_()




    def show_bar(self, val):
        self.pb = self.findChild(QProgressBar, 'p%d' % self.queue)
        self.pb.setValue(val)


    def resource_deduction(self):
        for re_index in range(4):
            self.resource_value[re_index] -= self.new_b_info[re_index + 1]
            self.update_resource_info(self.resource_value[re_index], re_index + 1)

    def update_resource_info(self, resource_val, index_num):
        update_item = self.findChild(QLabel, 'value %d' % index_num)
        updated_val = str(resource_val)
        update_item.setText(updated_val)






    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.WaitCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.mouse_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.mouse_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class Mission1(QThread):
    progressBarValue = pyqtSignal(float)

    def __init__(self, ui, m_time):
        super().__init__()
        self.ui = ui
        self.m_time = m_time
        self.Run = True

    def run(self):
        while self.Run:
            for i in range(1, self.m_time + 1):
                partial = (i/self.m_time) * 100
                print(partial)
                self.progressBarValue.emit(partial)
                time.sleep(1)
                if partial == 100:
                    self.Run = False


class Mission2(QThread):
    progressBarValue = pyqtSignal(float)

    def __init__(self, ui, m_time):
        super().__init__()
        self.ui = ui
        self.m_time = m_time
        self.Run = True

    def run(self):
        while self.Run:
            for i in range(1, self.m_time + 1):
                partial = (i/self.m_time) * 100
                print(partial)
                self.progressBarValue.emit(partial)
                time.sleep(1)
                if partial == 100:
                    self.Run = False

class TimeMission(QThread):
    def __init__(self, ui, m_time):
        super().__init__()
        self.ui = ui
        self.m_time = m_time
        self.Run = True

    def run(self):
        while self.Run:
            for i in range(self.m_time + 1):
                time_left = self.m_time - i
                show_time = ctl(time_left)
                self.ui.show_time = self.ui.findChild(QLabel, 'time %d' % self.ui.queue)
                self.ui.show_time.setText(show_time)
                time.sleep(1)

            self.Run = False
            self.ui.finish_construction()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SanGUI()
    win.show()
    sys.exit(app.exec_())