import time
"""
例子：让你生成1000个数字，如果i>100则跳出循环
"""
for i in range(1000):
    print (i)
    if i>100:
        break
"""
这种方法后面900次循环都是无用功，占用内存空间



这里我们用while循环更好
while 是边执行边做加法运算，而if是先把1000个数生成好，然后进行后面的判断，所以，在大数据情况下，if速度很慢

这种边执行边计算后面元素的机制叫：：生成器

但while不是生成器
"""
count = 0
while count < 1000:
    print(count)
    count += 1
    if count > 100:
        break

"""
之前if循环可以这么写：
"""
a = [x+1 for x in range(10)]
print (a)
"""[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
这样操作后列表就已经生成了。
如果我们把循环的方括号改成小括号，就是我们所说的“”“生成器”“”

生成器保存的是这个x+1的算法，里面并没有实际执行后产生的列表，所以是很节省空间的
"""
a = (x+1 for x in range(10))
print(a)
"""<generator object <genexpr> at 0x000001D4E7F4CF90>"""
"""想要执行生成器，除了通过循环以外，还可以通过next命令来一个一个的得到结果。
通过next可以看出，生成器是边执行边计算
即，惰性运算
"""
print(next(a))
"""return: 1"""
print(next(a))
"""return: 2"""


