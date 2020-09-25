import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont, QCursor, QPalette, QBrush, QPixmap
from PyQt5 import QtCore
from coin_scrapping import Scrapping
from threading import Thread





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
        self.init_console()
        self.init_action()
        self.init_instruction()
        self.init_win_title()
        self.init_disable()
        self.init_font()
        self.win_decoration()


    def init_window(self):
        self.setWindowTitle('Synferlo GUI V1.0')
        self.resize(600, 700)
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

        self.Console = QWidget()
        self.Console_layout = QGridLayout()
        self.Console.setLayout(self.Console_layout)

        self.Main_layout.addWidget(self.Info, 1, 0, 4, 4)
        self.Main_layout.addWidget(self.Single, 6, 0, 4, 4)
        self.Main_layout.addWidget(self.Multi, 10, 0, 4, 4)
        self.Main_layout.addWidget(self.Action, 14, 0, 1, 4)
        self.Main_layout.addWidget(self.Instruction, 1, 6, 14, 4)
        self.Main_layout.addWidget(self.win_title, 0, 0, 1, 10)
        self.Main_layout.addWidget(self.Console, 16, 0, 3, 10)

        self.setCentralWidget(self.Main)


    def init_info(self):

        self.font = QFont()
        self.font.setFamily('Consolas')
        self.font.setPointSize(9)

        self.method = QLabel('Method:')
        self.folder = QLabel('Folder Path:')
        self.mode = QLabel('Url Mode:')

        self.method.setFixedHeight(30)
        self.folder.setFixedHeight(30)
        self.mode.setFixedHeight(30)

        self.combo = QComboBox()
        self.combo.addItems(['Requests', 'Selenium'])
        self.folder_LE = QLineEdit()
        self.folder_LE.setPlaceholderText('Select your saving path...')
        self.cb_1 = QCheckBox('Single Page')
        self.cb_2 = QCheckBox('Multi Pages')
        self.view = QPushButton('...')
        self.view.setFixedSize(20, 20)
        self.view.setStyleSheet('QPushButton{background: white;border-radius: 5px}QPushButton:hover{background: grey}')

        self.view.clicked.connect(lambda: self.view_folder_path())

        self.Info_layout.addWidget(self.method, 1, 0, 1, 1)
        self.Info_layout.addWidget(self.combo, 1, 1, 1, 4)
        self.Info_layout.addWidget(self.folder, 2, 0, 1, 1)
        self.Info_layout.addWidget(self.folder_LE, 2, 1, 1, 3)
        self.Info_layout.addWidget(self.view, 2, 4, 1, 1)
        self.Info_layout.addWidget(self.mode, 3, 0, 1, 1)
        self.Info_layout.addWidget(self.cb_1, 3, 1, 1, 1)
        self.Info_layout.addWidget(self.cb_2, 3, 2, 1, 1)


    def view_folder_path(self):
        file_path = QFileDialog.getExistingDirectory(self, 'Select Folder', os.getcwd())
        self.folder_LE.setText(file_path)



    def init_single(self):
        self.single = QLabel('Single Page')
        self.file = QLabel('File Name:')
        self.url = QLabel('Url:')

        self.single.setFixedHeight(30)
        self.file.setFixedHeight(30)
        self.url.setFixedHeight(30)

        self.file_LE = QLineEdit()
        self.file_LE.setPlaceholderText('Name the html file...')
        self.url_LE = QLineEdit()
        self.url_LE.setPlaceholderText('Input the page Url...')

        self.Single_layout.addWidget(self.single, 1, 0, 1, 1)
        self.Single_layout.addWidget(self.file, 2, 0, 1, 1)
        self.Single_layout.addWidget(self.url, 3, 0, 1, 1)
        self.Single_layout.addWidget(self.file_LE, 2, 1, 1, 4)
        self.Single_layout.addWidget(self.url_LE, 3, 1, 1, 4)


    def init_multi(self):
        self.multi = QLabel('Multi Pages')
        self.front = QLabel('Front Url:')
        self.rear = QLabel('Rear Url:')
        self.page = QLabel('Page Range:')
        self.to = QLabel('to')
        self.indexing = QLabel('Indexing:')

        self.multi.setFixedHeight(30)
        self.front.setFixedHeight(30)
        self.rear.setFixedHeight(30)
        self.indexing.setFixedHeight(30)
        self.page.setFixedHeight(30)

        self.front_LE = QLineEdit()
        self.front_LE.setPlaceholderText('Url before page indexing.')
        self.rear_LE  = QLineEdit()
        self.rear_LE.setPlaceholderText('Url after page indexing.')
        self.page_LE_1 = QLineEdit()
        self.page_LE_1.setPlaceholderText('Start page.')
        self.page_LE_2 = QLineEdit()
        self.page_LE_2.setPlaceholderText('End page.')
        self.indexing_combo = QComboBox()
        self.indexing_combo.addItems(['1,2,3,...','0,5,10,...','0,50,100,...'])

        self.multi.setStyleSheet('''QLabel{color:while;}''')

        self.Multi_layout.addWidget(self.multi, 0, 0, 1, 1)
        self.Multi_layout.addWidget(self.front, 2, 0, 1, 1)
        self.Multi_layout.addWidget(self.rear, 3, 0, 1, 1)
        self.Multi_layout.addWidget(self.indexing, 4, 0, 1, 1)
        self.Multi_layout.addWidget(self.page, 5, 0, 1, 1)
        self.Multi_layout.addWidget(self.front_LE, 2, 1, 1, 3)
        self.Multi_layout.addWidget(self.rear_LE, 3, 1, 1, 3)
        self.Multi_layout.addWidget(self.indexing_combo, 4, 1, 1, 3)
        self.Multi_layout.addWidget(self.page_LE_1, 5, 1, 1, 1)
        self.Multi_layout.addWidget(self.to, 5, 2, 1, 1)
        self.Multi_layout.addWidget(self.page_LE_2, 5, 3, 1, 1)


    def init_console(self):
        self.console = QListWidget()
        self.Console_layout.addWidget(self.console, 2, 0, 2, 10)


    def init_action(self):
        self.scrapping = QPushButton('Scrapping')
        self.cancel  = QPushButton('Cancel')

        self.scrapping.setFixedSize(160, 25)
        self.cancel.setFixedSize(160, 25)
        self.scrapping.setDisabled(True)

        self.Action_layout.addWidget(self.scrapping)
        self.Action_layout.addWidget(self.cancel)

        self.scrapping.setStyleSheet('QPushButton{background: white; border-radius:5px}QPushButton:hover{background:grey}')
        self.cancel.setStyleSheet('QPushButton{background: white; border-radius:5px}QPushButton:hover{background:grey}')

        self.scrapping.clicked.connect(lambda: self.do_scrapping())
        self.cancel.clicked.connect(lambda: os._exit(0))


    def check_scrapping_status(self):
        if self.file_LE.text() != '' and self.url_LE.text() != '' and self.folder_LE.text() != '':
            self.scrapping.setEnabled(True)


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
        self.browser.setText("""\nThis program helps you solving web scrapping project. We offer two methods to do web scrapping: Requests, and Selenium.
You may need selenium mode if the website is configured with Async Attribute.\n
Besides, this program also supports single web page scrapping and multi pages scrapping. You can only choose one of them for each scrapping process.\n
By using Multi Pages mode, you should carefully divide the url into two parts and choose the correct indexing mode. Indexing indicates how the page # is described in the url.
Some websites use 0 for the first page, 50 for the second, and so forth. Select the correct indexing, otherwise, you may not be able to scrape correctly.
\n\n                 Good Luck!
        """)

        self.Instruction_layout.addWidget(self.instruction, 0, 0, 1, 1)
        self.Instruction_layout.addWidget(self.browser, 1, 0, 6, 4)


    def init_win_title(self):
        self.min = QPushButton()
        self.shutdown = QPushButton()
        self.title = QLabel('SynFerlo Scrapping v1.0')

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
        self.shutdown.clicked['bool'].connect(lambda: os._exit(0))

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
        self.cb_1.clicked['bool'].connect(self.check_single)

        self.cb_2.clicked['bool'].connect(self.cb_1.setDisabled)
        self.cb_2.clicked['bool'].connect(self.file_LE.setDisabled)
        self.cb_2.clicked['bool'].connect(self.file_LE.clear)
        self.cb_2.clicked['bool'].connect(self.url_LE.setDisabled)
        self.cb_2.clicked['bool'].connect(self.url_LE.clear)
        self.cb_2.clicked['bool'].connect(self.check_multi)


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
        self.console.setFont(self.font)


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
        # self.setStyleSheet('QMainWindow{background-color: white;border-radius: 10px}')
        self.Main_layout.setSpacing(0)

        win_bg = QPalette()
        win_bg.setBrush(self.backgroundRole(), QBrush(QPixmap('bg2.png')))
        self.setPalette(win_bg)

        # widgets_bg = QGraphicsOpacityEffect()
        # widgets_bg.setOpacity(0.5)
        # self.console.setGraphicsEffect(widgets_bg)
        # self.console.setAutoFillBackground(True)

        # set opacity
        self.setWindowOpacity(0.85)


    def do_scrapping(self):
        self.console.clear()
        mission = DoScrapping(self)
        mission.start()


    def check_single(self):
        mission = CheckScrapping(self)
        mission.start()


    def check_multi(self):
        mission = CheckScrapping(self)
        mission.start()



class CheckScrapping(Thread):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui


    def run(self):
        Run = True
        while Run:
            if self.ui.file_LE.text() != '' and self.ui.url_LE.text() != '' and self.ui.folder_LE.text() != '':
                self.ui.scrapping.setEnabled(True)
                Run = False


            if self.ui.folder_LE.text() != '' and self.ui.front_LE.text() != '' and self.ui.rear_LE.text() != '' and self.ui.page_LE_1.text() != '' and self.ui.page_LE_2.text() != '':
                self.ui.scrapping.setEnabled(True)
                Run = False



class DoScrapping(Thread):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui


    def run(self):
        Run = True
        while Run:
            if self.ui.cb_1.isChecked() == True and self.ui.cb_1.isEnabled() == True:
                mode = 'Single Page'
                method = self.ui.combo.currentText()
                folder = self.ui.folder_LE.text()
                file = self.ui.file_LE.text()
                url = self.ui.url_LE.text()

                result = Scrapping(progress = self, ui = self.ui).init_machine(method=method, url_mode=mode, folder_name=folder, file_name=file, full_url=url)
                Run = result

            if self.ui.cb_2.isChecked() == True and self.ui.cb_2.isEnabled() == True:
                mode = 'Multi Pages'
                method = self.ui.combo.currentText()
                folder = self.ui.folder_LE.text()
                front = self.ui.front_LE.text()
                rear = self.ui.rear_LE.text()
                indexing = self.ui.indexing_combo.currentText()
                start = self.ui.page_LE_1.text()
                end = self.ui.page_LE_2.text()

                result = Scrapping(progress = self, ui = self.ui).init_machine(method=method, url_mode=mode, folder_name=folder, start_page=start, end_page=end, front_url=front, rear_url=rear, page_rule=indexing)
                Run = result



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Synferlo()
    win.show()
    app.exit(app.exec_())
