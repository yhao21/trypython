import time

"""
公共属性：类属性，类变量
私有属性：实例属性，实例变量（又称成员变量），由每个实例独享

"""

class Dog2():
    d_type = 'jin mao'

    def __init__(self,name,age):
        self.name2 = name
        self.age2 = age

    def say_hi(self):
        print('Hello ' + self.name2)

d2 = Dog2('synferlo',1)
d2.say_hi()

"""
类属性调用：可通过类名+类属性，或者实例名.类属性调用，两者效果相同
通过实例对象调用类属性，最后也是返回类的内存空间寻找属性值
"""
print(Dog2.d_type)
print(d2.d_type)
"""returns: jin mao"""


"""
类属性修改：
"""
Dog2.d_type = 'bashahei'
print(d2.d_type)
print(Dog2.d_type)
"""returns: bashahei"""


"""
实例属性的调用：
实例名.实例属性名,注意self.name2中的name2是属性名

实例属性只能通过实例调用，不能通过类调用
"""
print(d2.name2)
"""return: synferlo"""