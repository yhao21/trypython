import time

"""
通过random和string模块完成随机生成数字和字母的程序
"""

import string
import random


"""打印所有的大小写a-z"""
x = string.ascii_letters
print(x)
"""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"""


"""打印所有小写字母"""
x = string.ascii_lowercase
print(x)
"""abcdefghijklmnopqrstuvwxyz"""



x = string.digits
y = string.hexdigits
z = string.octdigits
print(x)
"""0123456789"""
print(y)
"""0123456789abcdefABCDEF"""
print(z)
"""01234567"""



x = string.ascii_lowercase + string.digits
"""abcdefghijklmnopqrstuvwxyz0123456789"""
y = random.sample(x,3)
print (y)
"""['l', 'm', 'y']"""
"""随机从小写字母与数字中抽取三个，以列表形式返回"""



"""shuffle 将当前列表里的数据顺序打乱，洗牌"""
a = list(range(10))
print (a)
"""[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""
random.shuffle(a)
print(a)
"""[3, 6, 2, 8, 0, 7, 1, 5, 9, 4]"""
"""顺序被打乱了"""



