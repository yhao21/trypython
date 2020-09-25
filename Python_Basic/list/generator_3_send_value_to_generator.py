import time

"""
前情回顾：
yield后面接变量可以制作生成器，而不是一次性执行文件

"""
def fib(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        old_a = a
        a = b
        b = old_a + b
        yield (a)
        count += 1
print(fib(10))
"""
那么，我们可不可以从外部给生成器传入值呢？
可以的，但是这时候yield后面不能接变量。
yield后面接变量是返回后面的变量到函数外部


我们想要的效果是通过for循环生成一些列数值，然后传入到def当中，按常理：
我们想到用next对吧，因为我们定义test时候没有指定他接收的参数，所以next也不能传参数：
    for i in range(10):
        g.__next__()
        
返回值：receive n as  None
发现返回的都是空值，

于是我们尝试把i放进next：
    for i in range(10):
        g.__next__(i)
但是程序报错：
    TypeError: expected 0 arguments, got 1
因为我们定义test时候没有定义让他接收外部的值，即（）里没有参数
那这个时候我们可以通过send函数来达到目的
但是程序又报错了：
TypeError: can't send non-None value to a just-started generator

给生成器传输的第一个值不能是非空值，（即，必须是空值）。怎么办呢？
那我们就在g = test()后面用next给test发一个空值,

完美！！

"""
def test():
    while True:
        n = yield
        print('receive n as ',n)
g = test()
g.__next__()

for i in range(10):
    g.send(i)

"""
return:
    receive n as  0
    receive n as  1
    receive n as  2
    receive n as  3
    receive n as  4
    receive n as  5
    receive n as  6
    receive n as  7
    receive n as  8
    receive n as  9

"""


