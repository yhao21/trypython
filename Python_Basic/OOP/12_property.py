import time

"""
属性方法： property


通过装饰器，把一个方法变成一个静态的属性
"""

class Student:

    def __init__(self,name):
        self.name = name

    @property
    def fly(self):
        print(self.name, ' is flying')

s = Student('Simon')
#s.fly()  ###这时候不能按照方法的调用方式去调用fly了，因为他现在已经不是一个方法了，而是一个属性
"""
我们调用属性的方法是：实例名.属性名
调用方法的方式是：实例名.方法名()
"""
s.fly
"""Simon  is flying"""


"""那为什么我们不直接定义一个属性而还要定义这个方法呢。。。因为直接定义变量不会执行函数，但是定义方法后，他会用执行一些动作"""