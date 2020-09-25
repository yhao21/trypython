import time

"""
迭代器：
可以直接作用于for循环的对象统称为  可迭代对象： Iterable

    一类是几何数据类型：list，tuple，dict，set，str等
    一类是generator，包括生成器和带yield的generator function
"""
x = 'apple'
for i in x:
    print (i)
"""
a
p
p
l
e
"""
x = (x for x in range(10))
print(x)
"""
一定注意，两侧是小括号才是生成器，方括号就直接执行循环了
<generator object <genexpr> at 0x00000119848B5E40>"""

"""
判断是否为迭代器
    通过isinstance
"""
from collections import Iterable
x = (isinstance((x for x in range(10)), Iterable))
print(x)
"""True"""
