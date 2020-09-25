import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor
from PyQt5 import QtCore
from coin_scrapping import Scrapping
from threading import Thread


import requests, os, time
import time_countdown as cd
from selenium import webdriver




class Synferlo(QMainWindow):

    def __init__(self):
        super().__init__()
        # have to init mouse_flag = False, otherwise, error occurs when using combobox and do scrapping.
        # Error: class Synferlo does not have attribute self.mouse_flag.
        self.mouse_flag = False
        self.init_window()
        self.init_layout()
        self.init_info()
        self.init_single()
        self.init_multi()
        self.init_action()
        self.init_instruction()
        self.init_win_title()
        self.init_disable()
        self.init_font()
        self.win_decoration()




        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        self.url_list = None
        self.url = ''
        self.file_name = None
        self.folder_name = None
        self.path = os.getcwd()
        self.html = 0
        self.page_count = 0
        self.file_index = 0
        self.file_path = ''
        self.st = None
        self.et = None
        self.method = None
        self.spage = None
        self.epage = None
        self.full_url = None
        self.front_url = None
        self.rear_url = None
        self.page_rule = None





    def init_window(self):
        self.setWindowTitle('Synferlo GUI V1.0')
        self.resize(600, 530)
        self.move(600, 200)

    def init_layout(self):
        self.Main = QWidget()
        self.Main_layout = QGridLayout()
        self.Main.setLayout(self.Main_layout)

        self.Info = QWidget()
        self.Info_layout = QGridLayout()
        self.Info.setLayout(self.Info_layout)

        self.Single = QWidget()
        self.Single_layout = QGridLayout()
        self.Single.setLayout(self.Single_layout)

        self.Multi = QWidget()
        self.Multi_layout = QGridLayout()
        self.Multi.setLayout(self.Multi_layout)

        self.Action = QWidget()
        self.Action_layout = QHBoxLayout()
        self.Action.setLayout(self.Action_layout)

        self.Instruction = QWidget()
        self.Instruction_layout = QGridLayout()
        self.Instruction.setLayout(self.Instruction_layout)

        self.win_title = QWidget()
        self.win_title_layout = QGridLayout()
        self.win_title.setLayout(self.win_title_layout)

        self.Main_layout.addWidget(self.Info, 1, 0, 4, 4)
        self.Main_layout.addWidget(self.Single, 5, 0, 4, 4)
        self.Main_layout.addWidget(self.Multi, 10, 0, 4, 4)
        self.Main_layout.addWidget(self.Action, 14, 0, 1, 4)
        self.Main_layout.addWidget(self.Instruction, 1, 6, 14, 4)
        self.Main_layout.addWidget(self.win_title, 0, 0, 1, 10)

        self.setCentralWidget(self.Main)

    def init_info(self):

        self.font = QFont()
        self.font.setFamily('Consolas')
        self.font.setPointSize(9)

        self.method = QLabel('Method:')
        self.folder = QLabel('Folder Name:')
        self.mode = QLabel('Url Mode:')

        self.combo = QComboBox()
        self.combo.addItems(['requests', 'selenium'])
        self.folder_LE = QLineEdit()
        self.folder_LE.setPlaceholderText('Name the folder...')
        self.cb_1 = QCheckBox('Single Page')
        self.cb_2 = QCheckBox('Multi Pages')

        self.Info_layout.addWidget(self.method, 1, 0, 1, 1)
        self.Info_layout.addWidget(self.combo, 1, 1, 1, 4)
        self.Info_layout.addWidget(self.folder, 2, 0, 1, 1)
        self.Info_layout.addWidget(self.folder_LE, 2, 1, 1, 4)
        self.Info_layout.addWidget(self.mode, 3, 0, 1, 1)
        self.Info_layout.addWidget(self.cb_1, 3, 1, 1, 1)
        self.Info_layout.addWidget(self.cb_2, 3, 2, 1, 1)

    def init_single(self):
        self.single = QLabel('Single Page')
        self.file = QLabel('File Name:')
        self.url = QLabel('Url:')

        self.file_LE = QLineEdit()
        self.file_LE.setPlaceholderText('Name the html file...')
        self.url_LE = QLineEdit()
        self.url_LE.setPlaceholderText('Input the page Url...')

        self.Single_layout.addWidget(self.single, 0, 0, 1, 1)
        self.Single_layout.addWidget(self.file, 1, 0, 1, 1)
        self.Single_layout.addWidget(self.url, 2, 0, 1, 1)
        self.Single_layout.addWidget(self.file_LE, 1, 1, 1, 4)
        self.Single_layout.addWidget(self.url_LE, 2, 1, 1, 4)

    def init_multi(self):
        self.multi = QLabel('Multi Pages')
        self.front = QLabel('Front Url:')
        self.rear = QLabel('Rear Url:')
        self.page = QLabel('Page Range:')
        self.to = QLabel('to')
        self.indexing = QLabel('Indexing:')

        self.front_LE = QLineEdit()
        self.front_LE.setPlaceholderText('Url before page number.')
        self.rear_LE = QLineEdit()
        self.rear_LE.setPlaceholderText('Url after page number.')
        self.page_LE_1 = QLineEdit()
        self.page_LE_1.setPlaceholderText('Start page.')
        self.page_LE_2 = QLineEdit()
        self.page_LE_2.setPlaceholderText('End page.')
        self.indexing_combo = QComboBox()
        self.indexing_combo.addItems(['1,2,3,...', '0,5,10,...', '0,50,100,...'])

        self.multi.setStyleSheet('''QLabel{color:while;}''')

        self.Multi_layout.addWidget(self.multi, 0, 0, 1, 1)
        self.Multi_layout.addWidget(self.front, 1, 0, 1, 1)
        self.Multi_layout.addWidget(self.rear, 2, 0, 1, 1)
        self.Multi_layout.addWidget(self.indexing, 3, 0, 1, 1)
        self.Multi_layout.addWidget(self.page, 4, 0, 1, 1)
        self.Multi_layout.addWidget(self.front_LE, 1, 1, 1, 3)
        self.Multi_layout.addWidget(self.rear_LE, 2, 1, 1, 3)
        self.Multi_layout.addWidget(self.indexing_combo, 3, 1, 1, 3)
        self.Multi_layout.addWidget(self.page_LE_1, 4, 1, 1, 1)
        self.Multi_layout.addWidget(self.to, 4, 2, 1, 1)
        self.Multi_layout.addWidget(self.page_LE_2, 4, 3, 1, 1)

    def init_action(self):
        self.scrapping = QPushButton('Scrapping')
        self.cancel = QPushButton('Cancel')

        self.Action_layout.addWidget(self.scrapping)
        self.Action_layout.addWidget(self.cancel)

        self.scrapping.clicked.connect(lambda: self.do_scrapping())
        self.cancel.clicked.connect(lambda: self.cancellation())

    def init_instruction(self):
        self.instruction = QLabel('Words from the designer:')
        # self.browser = QTextBrowser()
        self.browser = QLabel()
        # auto wrap
        self.browser.setWordWrap(True)
        self.browser.setAlignment(Qt.AlignLeft)
        self.browser.setFrameShape(QFrame.Box)
        # set border style
        self.browser.setFrameShadow(QFrame.Sunken)
        self.browser.setText("""\nThis program will help you dealing with web scrapping problem. We offer two methods to do web scrapping: requests, and selenium.\n
Besides, this program also supports single web page scrapping and multi pages scrapping. You can only choose one of them for each scrapping process.\n
By using Multi Pages mode, you should carefully divide the url into two parts and choose indexing mode. Indexing indicates how the page # is described in url.
Some websites use 0 for the first page, 50 for the second, and so forth. Find the correct indexing, otherwise, you may not be able to scrap correctly.
\n\n                 Good Luck!
        """)

        self.Instruction_layout.addWidget(self.instruction, 0, 0, 1, 1)
        self.Instruction_layout.addWidget(self.browser, 1, 0, 10, 4)

    def init_win_title(self):
        self.min = QPushButton()
        self.shutdown = QPushButton()
        self.title = QLabel('Synferlo Scrapping v1.0')

        title_font = QFont()
        title_font.bold()
        title_font.setFamily('Consolas')
        title_font.setPointSize(12)

        self.title.setFont(title_font)
        self.title.setAlignment(Qt.AlignCenter)

        self.min.setFixedSize(15, 15)
        self.shutdown.setFixedSize(15, 15)

        self.min.setStyleSheet("""QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}""")
        self.shutdown.setStyleSheet("""QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}""")

        # minimize the window
        self.min.clicked['bool'].connect(self.showMinimized)
        self.shutdown.clicked['bool'].connect(self.close)

        self.win_title_layout.addWidget(self.title, 0, 0, 1, 8)
        self.win_title_layout.addWidget(self.min, 0, 8, 1, 1)
        self.win_title_layout.addWidget(self.shutdown, 0, 9, 1, 1)

    def init_disable(self):
        self.cb_1.clicked['bool'].connect(self.cb_2.setDisabled)
        self.cb_1.clicked['bool'].connect(self.front_LE.setDisabled)
        self.cb_1.clicked['bool'].connect(self.front_LE.clear)
        self.cb_1.clicked['bool'].connect(self.rear_LE.setDisabled)
        self.cb_1.clicked['bool'].connect(self.rear_LE.clear)
        self.cb_1.clicked['bool'].connect(self.page_LE_1.setDisabled)
        self.cb_1.clicked['bool'].connect(self.page_LE_1.clear)
        self.cb_1.clicked['bool'].connect(self.page_LE_2.setDisabled)
        self.cb_1.clicked['bool'].connect(self.page_LE_2.clear)
        self.cb_1.clicked['bool'].connect(self.indexing_combo.setDisabled)

        self.cb_2.clicked['bool'].connect(self.cb_1.setDisabled)
        self.cb_2.clicked['bool'].connect(self.file_LE.setDisabled)
        self.cb_2.clicked['bool'].connect(self.file_LE.clear)
        self.cb_2.clicked['bool'].connect(self.url_LE.setDisabled)
        self.cb_2.clicked['bool'].connect(self.url_LE.clear)

    def init_font(self):
        self.method.setFont(self.font)
        self.folder.setFont(self.font)
        self.mode.setFont(self.font)
        self.combo.setFont(self.font)
        self.cb_1.setFont(self.font)
        self.cb_2.setFont(self.font)
        self.folder_LE.setFont(self.font)
        self.single.setFont(self.font)
        self.file.setFont(self.font)
        self.url.setFont(self.font)
        self.file_LE.setFont(self.font)
        self.url_LE.setFont(self.font)
        self.multi.setFont(self.font)
        self.front.setFont(self.font)
        self.rear.setFont(self.font)
        self.page.setFont(self.font)
        self.to.setFont(self.font)
        self.front_LE.setFont(self.font)
        self.rear_LE.setFont(self.font)
        self.page_LE_1.setFont(self.font)
        self.page_LE_2.setFont(self.font)
        self.indexing.setFont(self.font)
        self.instruction.setFont(self.font)
        self.browser.setFont(self.font)

    # As I use frameless window, I have to rewrite the mouseEvent, so that user can use mouse to move window.
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

    # # setup shortcuts
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Escape:
    #         self.close()

    def win_decoration(self):
        # use frameless window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setStyleSheet('QMainWindow{background-color: white;border-radius: 10px}')

        self.Main_layout.setSpacing(0)
        # set opacity
        self.setWindowOpacity(0.85)

        self.Main.setStyleSheet(
            """
            QWidget#Main{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-left:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            """
        )

        self.win_title.setStyleSheet(
            """
            QWidget#win_title{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-left:1px solid darkGray;
                border-top-right-radius:10px;
                border-top-left-radius:10px;

            }
            """
        )

    def do_scrapping(self):
        if self.cb_1.isChecked() == True and self.cb_1.isEnabled() == True:
            mode = 'Single Page'
            method = self.combo.currentText()
            folder = self.folder_LE.text()
            file = self.file_LE.text()
            url = self.url_LE.text()

            Scrapping().init_machine(method=method, url_mode=mode, folder_name=folder, file_name=file, full_url=url)

        if self.cb_2.isChecked() == True and self.cb_2.isEnabled() == True:
            mode = 'Multi Pages'
            method = self.combo.currentText()
            folder = self.folder_LE.text()
            front = self.front_LE.text()
            rear = self.rear_LE.text()
            indexing = self.indexing_combo.currentText()
            start = self.page_LE_1.text()
            end = self.page_LE_2.text()

            Scrapping().init_machine(method=method, url_mode=mode, folder_name=folder, start_page=start, end_page=end, front_url=front,
                                     rear_url=rear, page_rule=indexing)

    def cancellation(self):
        self.gogogo = False










    def init_machine(self, method, url_mode, folder_name, start_page = 0, end_page = 0, file_name = None, full_url = '', front_url = '', rear_url = '', page_rule = ''):
        self.method = method
        self.folder_name = folder_name

        if url_mode == 'Single Page':
            self.file_name = [file_name]
            self.full_url = full_url
            self.one_part_url()

        if url_mode == 'Multi Pages':

            self.front_url = front_url
            self.rear_url = rear_url
            self.spage = int(start_page)
            self.epage = int(end_page)
            self.file_name = ['page' + str(i) for i in range(self.spage, self.epage + 1)]
            self.page_rule = page_rule
            self.n_part_url()


    def one_part_url(self):
        self.url_list = [self.full_url]
        self.folder_setup()


    def n_part_url(self):
        if self.page_rule == '1,2,3,...':
            self.url_list = [self.front_url + str(page) + self.rear_url for page in range(self.spage, self.epage + 1)]
        if self.page_rule == '0,50,100,...':
            self.url_list = [self.front_url + str((page - 1) * 50) for page in range(self.spage, self.epage + 1)]
        if self.page_rule == '0,5,10,...':
            self.url_list = [self.front_url + str((page - 1) * 5) for page in range(self.spage, self.epage + 1)]

        self.folder_setup()


    def folder_setup(self):
        self.path = os.path.join(self.path, self.folder_name)
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        self.check_file_exists()


    def check_file_exists(self):
        self.page_count = len(self.url_list)
        for url in self.url_list:
            # round_start time
            self.st = time.time()

            self.url = url
            self.file_index = self.url_list.index(url)
            self.file_path = os.path.join(self.path, self.file_name[self.file_index])

            if not os.path.exists(self.file_path + '.html'):
                self.scrapping_()
            else:
                self.page_count -= 1
                print('\n[' +self.file_name[self.file_index] + ']' + 'has already existed.......' + '%s/%s' % (str(len(self.url_list) - self.page_count), len(self.url_list)))


    def file_setup(self):
        with open(self.file_path + '.temp', 'w', encoding = 'utf-8') as f:
            f.write(self.html)
        os.rename(self.file_path + '.temp', self.file_path+ '.html')


    def scrapping_(self):
        if self.method == 'requests':
            # r = requests.get(self.url, headers = self.headers)
            # self.html = r.text
            self.html = 'you are using requests'

        if self.method == 'selenium':
            # driver = webdriver.Chrome()
            # driver.get(self.url)
            # self.html = driver.page_source
            # driver.close()
            self.html = 'you are using selenium'

        self.file_setup()
        sleep = 2
        time.sleep(sleep)
        self.page_count -=1
        print('\nFinish downloading [' + self.file_name[self.file_index] + ']'+ '.......' + '%s/%s' % (str(len(self.url_list) - self.page_count), len(self.url_list)))
        # round_end time
        self.et = time.time()
        round_time = self.et - self.st
        cd.left_time_estimation(round_time, sleep, self.page_count)





















if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Synferlo()
    win.show()
    app.exit(app.exec_())
