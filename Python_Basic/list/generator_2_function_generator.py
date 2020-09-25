import time
"""
！！函数生成器！！

"""
"""
斐波那契数列
第一个数是0第二个数是1之后每个数都是前两个之和
"""
Fibonacci_sequence = []
a = 0
b = 1
count = 0
while count < 20:
    old_a = a
    a = b
    b = old_a + b
    Fibonacci_sequence.append(a)
    count += 1

print (Fibonacci_sequence)
"""[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]"""
"""接下来把这个运算变成一个函数生成器：

只需要把print变成yield就可以了
"""

def fib(n):
    Fibonacci_sequence = []
    a = 0
    b = 1
    count = 0
    while count < n:
        old_a = a
        a = b
        b = old_a + b
        Fibonacci_sequence.append(a)
        count += 1
    yield(Fibonacci_sequence)
print(fib(20))
"""<generator object fib at 0x00000253F264CF90>"""

"""
神奇的事情要发生了::
yield可以使得函数在运行过程中穿插别的打印任务（不一定是打印，其他都可以）完成后从断点处继续执行：


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

#每next一次往下运算一步
f = fib(10)
print(next(f))
print(next(f))
print('can i do sth else?')
print('of course!')
print(next(f))
print(next(f))
print(next(f))
"""
1
1
can i do sth else?
of course!
2
3
5
"""