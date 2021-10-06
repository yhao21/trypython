import time


"""
如何根据combobox中选中的内容执行不同的代码

这里我们可以


self.comboBox.currentIndexChanged.connect(lambda: self.print_you())


def print_you(self):
    # print the text you have chosen. we can use this method to link other function in web scrapping
    print(self.comboBox.currentText())
    if self.comboBox.currentText() == 'requests':
        print('use requests do the web scrapping')
    if self.comboBox.currentText() == 'selenium':
        print('use selenium')

"""