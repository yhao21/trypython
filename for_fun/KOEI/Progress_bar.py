import time
from PyQt5.QtCore import *




def init_progress_bar(ui, mission_time):
    mission =



class Mission(QThread):
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
                self.progressBarValue.emit(partial)
                time.sleep(1)
                if partial == 100:
                    self.Run = False