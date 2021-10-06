import time

"""
静态方法：staticmethod

与类方法区别：
    类方法只能访问类属性，不能访问实例属性
    
    静态方法更绝：
        任何类与实例的属性和方法都不能访问
"""

class Student:
    role = 'student'

    def __init__(self,name):
        self.name  = name

    def fly(self):
        print(self.name, ' is flying...')

s = Student('jack')
s.fly()
"""
return: jack  is flying...

没有将fly变成静态方法的时候通过实例变量是可以调用这个方法的
"""

class Student1:
    role = 'student'

    def __init__(self,name):
        self.name  = name
    @staticmethod
    def fly(self):
        print(self.name, ' is flying...')

s = Student1('jack')
#s.fly()
"""
return: TypeError: fly() missing 1 required positional argument: 'self'

变成静态方法后，便无法通过实例调用了，但是在s.fly()传入s后，就可以调用了
"""
s.fly(s)
"""jack  is flying..."""

"""
为什么自己传就可以了呢：

因为静态方法隔断了这个方法与类、实例和任何其下的方法的关系，如果你先写好@staticmethod在def一个方法，会发现，方法的括号里是没有self的

"""
class Student2:
    role = 'student'

    def __init__(self,name):
        self.name  = name
    @staticmethod
    def run():
        print('running')

s = Student2('mjj')
