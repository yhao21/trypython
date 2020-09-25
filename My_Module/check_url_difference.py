import re

class DID():
    def __init__(self, obj1, obj2):
        self.start = 0
        self.end = len(obj1)
        self.obj1 = obj1
        self.obj2 = obj2
        self.init_index = 0
        self.end_index = 0
        self.round = 0
        self.same = ''
        self.df = []
        self.wrong_index = 0

    def diff(self):
        for i in range(self.start, self.end):
            print(i)
            if self.round == 0:
                self.end_index = i + 1
            else:
                self.init_index = self.start
                self.end_index = i + 1

            sample = self.obj1[self.init_index : self.end_index]
            comparison = self.obj2[self.init_index : self.end_index]
            print(sample)

            if self.init_index == 0 and self.end_index == 1:
                if re.match(sample, comparison).group() != None:
                    self.same = re.match(sample, comparison).group()

            if 0 < i < len(self.obj1) - 1:
                if re.findall(sample, comparison) != []:
                    self.same = re.findall(sample, comparison)[0]
                else:
                    if self.wrong_index != i - 1:
                        self.df.append(self.same)
                    self.wrong_index = i
                    self.df.append('*')
                    self.round += 1
                    print('wrong', i)
                    self.start = i + 1
                    self.diff()

            if i == len(self.obj1) - 1 and self.round == 0:
                if re.findall(sample, comparison) != []:
                    self.df.append(sample)
            elif i == len(self.obj1) - 1 and self.round > 0:
                if re.findall(sample, comparison) != []:
                    self.df.append(sample)
                else:
                    self.df.append('*')

        return self.df, self.same


if __name__ == '__main__':
    # url1 = 'https://coinmarketcap.com/rankings/exchanges/1/'
    # url2 = 'https://coinmarketcap.com/rankings/exchanges/2/'
    # df, same = DID(url1, url2).diff()
    # print(df)
    url1 = 'www.baidu.163.com'
    url2 = 'www.baidu.222.com'
    df, same = DID(url1, url2).diff()
    print(df)