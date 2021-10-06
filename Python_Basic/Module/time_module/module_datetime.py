import time
import datetime

"""打印当前时间"""
t = datetime.datetime.now()
print(t)
"""2020-02-17 14:46:02.241050"""


"""时间运算"""
x = datetime.timedelta(days = 3, minutes = 5)
t = t - x
print(t)
"""
2020-02-17 14:51:40.103488
2020-02-14 14:46:40.103488
"""
"""
timedelta可以上传的参数有：
days
minutes
hours
weeks
fold
seconds
microseconds
milliseconds
"""


"""replace替换时间"""
a = datetime.datetime.now()
y = a.replace(year = 1999)
print(a)
print(y)
"""
2020-02-17 14:54:34.155696
1999-02-17 14:54:34.155696"""
