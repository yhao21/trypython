import time
import random
"""
通过randint生成随机数
"""
x = random.randint(1,10)
print(x)
"""注意：这里randint和numpy的不同，这里randint只生成一个数字，而numpy是吧1-10所有整数都写出来"""


"""从给定字符串里随机选取一个或多个字符"""
x = random.sample('harry,synferlo',2)
print(x)
"""表示在给定字符串里，随机选取n个字符，并以列表形式返回"""

"""random.choice只能返回一个字符,而且不是列表形式"""
x = random.choice('ajdisjfaioduf1$@')
print(x)


