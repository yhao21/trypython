import pandas as pd
import numpy as np


class csv_file():

    def __init__(self, file_path):
        self.file = file_path


    def csv(self):
        if '.csv' in self.file:
            df = pd.read_csv(self.file)
            #取消过长行、列的自动省略，展示完整表格
            pd.set_option('display.max_columns',None)
            pd.set_option('display.max_rows',None)
            print(df)
        else:
            print('Error: This is not a csv file.')


    def csv_head(self):
        if '.csv' in self.file:
            df = pd.read_csv(self.file)
            pd.set_option('display.max_columns',None)
            #取消自动换行
            pd.set_option('expand_frame_repr',False)
            print(df.head())
        else:
            print('Error: This is not a csv file.')




