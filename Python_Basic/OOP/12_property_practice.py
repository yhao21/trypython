import time

"""
航班信息案例：


查机票
    1. 连接各个机场的航班系统
    2. 查询信息
    3. 对返回的信息进行处理，解析（机场返回的文件可能不是用一个类型，有的是json有的不是）
    4. 将解析后的信息显示给用户
    
    
    
对于用户来说，他不在意过程，只在意飞机的状态，机票价格（这些是静态数据）

flight.status = 查找航班信息

用户每次执行这个命令时，系统都会执行1-4这四个步骤
"""


class Flight:
    def __init__(self,name):
        self.flight_name = name

    def check_status(self):
        print('connecting airline API')
        print('checking flight %s status' % self.flight_name)
        return 1 ##假装查询后返回结果为1

    @property
    def flight_status(self):
        status = self.check_status()

        if status == 0:
            print('flight is canceled...')
        elif status == 1:
            print('flight is arrived')
        elif status == 2:
            print('flight has departured already...')
        else:
            print('no info, please try again later')

f = Flight('CA870')
f.flight_status

"""那么既然是静态属性，能不能给flight_status赋值能？

比如： f.flight_status = 0

但程序会报错



如果你非要修改
需要重写一遍flight_status并用@flight_status.setter注明这是对上面的同名函数做修改

"""



class Flight:
    def __init__(self,name):
        self.flight_name = name

    def check_status(self):
        print('connecting airline API')
        print('checking flight %s status' % self.flight_name)
        return 1 ##假装查询后返回结果为1

    @property
    def flight_status(self):
        status = self.check_status()

        if status == 0:
            print('flight is canceled...')
        elif status == 1:
            print('flight is arrived')
        elif status == 2:
            print('flight has departured already...')
        else:
            print('no info, please try again later')

    @flight_status.setter
    def flight_status(self,status_code):    ##这里传入的status_code是你传入的修改值，即，你想让status状态变成数字几
        print('changing status...')
        status = {
            0:'canceled',
            2: 'departured',
            1:'arrived'

        }
        print(status[status_code])

    @flight_status.deleter
    def flight_status(self):
        print('del...')

a = Flight('CA111')
a.flight_status = 2
"""使用这个方法可以完成自己修改的效果，但他不是对原来property下的方法做修改，而是对setter下的做修改"""
"""如果你想删除一个状态怎么办呢，同理，重写一个，然后用@flight_status.deleter装饰"""

del a.flight_status

