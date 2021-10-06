import time
"""
类方法就是类当中定义的函数def

类方法包括：
1.实例方法：
2.类方法：
3.自由方法：
4.静态方法：
5.保留方法：双下划线构成__init__之类的
"""
"""
实例方法：
    class <class name>:
        实例方法第一个参数必须是self
        def <method name>(self,<parameter>)
"""
class DemoClass:
    def __init__(self,name):
        self.name = name
    def lucky(self):
        s = 0
        ##self.name是每个实例对象特有的属性，
        for c in self.name:
            s += ord(c) % 100
        return s

dc1 = DemoClass("Wang")
dc2 = DemoClass("Lee")
print (dc1.name,"your lucky number is ", dc1.lucky())
print (dc2.name,"your lucky number is ", dc2.lucky())

"""
类方法：
    class <class name>:
        @classmethod
        def <method name>(cls,<parameters>)
            ....
类方法既可以被类名调用，也可以被对象名调用
"""
class DemoClass_1:
    count = 0
    def __init__(self,name):
        self.name = name
        DemoClass_1.count += 1
    @classmethod
    def getChrCount(cls):
        s = "零二一三more"
        ##这里是吧count的结果时2，然后通过s[2]输出s中的第三个内容，也就是“一”
        return s[DemoClass_1.count]
dc1 = DemoClass_1("Wang")
dc2 = DemoClass_1("Lee")
print(dc1.getChrCount())
print (DemoClass_1.getChrCount())
"""
返回值：
    一
    一
"""
"""
自由方法：
    class <class name>:
        def <method name>(<parameters>)
            ....
这是在类中写普通函数的方法，不适用self作为变量            
    访问自由方法的方式：
        类名+方法名
自由方法不需要cls和self参数
自由方法只能操作类属性和类方法，不能操作实例属性和实例方法
自由方法的使用只能使用类名

"""
class DemoClass_2:
    count = 0
    def __init__(self,name):
        self.name = name
        DemoClass_2.count += 1

    def foo():
        ##不能使用self开头的方法，因为那些是对象。自由方法只能使用类属性和类方法
        DemoClass_2.count *= 100
        return DemoClass_2.count
dc1 = DemoClass_2("Wang")
print(DemoClass_2.foo())
"""
返回值：100
"""
"""
静态方法：
    class <class name>:
        @staticmethod
        def <method name>(<parameters>)
            ....
            
静态方法是定义在类中的普通函数，能被所有实例对象共享
把普通函数变成静态函数，只需加上@staticmethod装饰器即可

静态方法也只能使用类属性和类方法，不能使用实例对象的属性和方法。因为没有引入self参数。
注意：只有使用self参数的方法才能调用实例对象及其属性
调用方法：
    <class name>.<method.name>(<parameters>)
or  <object name>.<method.name>(<parameters>)
"""
class DemoClass_3:
    count = 0
    def __init__(self,name):
        self.name = name
        DemoClass_3.count += 1

    @staticmethod
    def foo():
        DemoClass_3.count *= 100
        return DemoClass_3.count
dc4 = DemoClass_3("Wang")
print(DemoClass_3.foo())
print(dc4.foo())

"""
返回值：
    100
    10000
第二个值为10000因为：
第一次调用DemoClass_3.foo()时，运算后Democlass_3.count = 100,并将这个值赋给了count，
所以，当dc4.foo再次调用foo时候，count初始值为100,最后结果就是100*100
"""
"""
保留方法：
    class <class name>:
        def <__method name__>(self):
            ....
            
"""
class DemoClass_4:
    count = 0
    def __init__(self,name):
        self.name = name
        DemoClass_4.count += 1
    def __len__(self):
        return len(self.name)*2
dc5 = DemoClass_4("Wang")
dc6 = DemoClass_4("Lee")
print(dc5.__len__())
print(dc6.__len__())




