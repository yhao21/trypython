import time

"""
三种方式表示时间：

timestamp：unix时间戳，从1970年1月1日00:00:00开始按秒计算。第一台unix系统在1970年1月1号诞生

格式化的时间字符串：2020-10-03 17:35

元组（struct_time)：time.struct_time(tm_year = 2020...)


索引（Index）    属性（Attribute）              值（Values）
    0               tm_year（年）                 比如2011
    1               tm_mon（月）                  1 - 12
    2               tm_mday（日）                 1 - 31
    3               tm_hour（时）                 0 - 23
    4               tm_min（分）                  0 - 59
    5               tm_sec（秒）                  0 - 61
    6               tm_wday（weekday）            0 - 6（0表示周日）
    7               tm_yday（一年中的第几天）       1 - 366
    8               tm_isdst（是否是夏令时）        默认为-1


"""
"""按照元组形式打印当前时间"""
x = time.localtime()
print(x)
'''time.struct_time(tm_year=2020, tm_mon=2, tm_mday=17, tm_hour=14, tm_min=8, tm_sec=9, tm_wday=0, tm_yday=48, tm_isdst=0)
如果你在括号里添加一个时间戳的数值，，他会告诉你这个时间戳对应的是哪一年那一天'''


"""将时间戳转换为UTC时区的struct_time，即，格林威治时间"""
x = time.gmtime()
print(x)
"""time.struct_time(tm_year=2020, tm_mon=2, tm_mday=17, tm_hour=19, tm_min=26, tm_sec=35, tm_wday=0, tm_yday=48, tm_isdst=0)"""


"""将一个struct_time转换为时间戳模式"""
x = time.mktime(x)
print(x,time.time())
"""括号里的x是我上一次调用gmtime时候的时间戳，后面time.time是为了对比验证x不是当前的时间戳"""
"""1581985595.0 1581967595.5586004"""


"""返回Mon Feb 17 14:15:35 2020这个格式的时间"""
x = time.asctime()
print(x)
""" Mon Feb 17 14:15:35 2020"""


"""把一个时间戳转换为asctime格式的时间"""
x = time.ctime(0)
print(x)
"""如果括号里没给出时间戳，则用现在的时间"""
"""Wed Dec 31 19:00:00 1969"""


"""自定义格式打印时间"""
x = time.strftime("time %Y.%m.%d %H:%M:%S")
print(x)
"""time 2020.02.17 14:26:35"""


"""把一个给定的时间转换为元组形式"""
print(time.strptime("2020/02/17 14:32", "%Y/%m/%d %H:%M"))
"""注意，逗号后面要告诉电脑你前面的时间是按照什么格式写的，因为电脑只认识%Y。。这种格式"""
"""time.struct_time(tm_year=2020, tm_mon=2, tm_mday=17, tm_hour=14, tm_min=32, tm_sec=0, tm_wday=0, tm_yday=48, tm_isdst=-1)"""
