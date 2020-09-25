import time
"""
如何生命继承关系：
    在定义新的类是，在类名后面的括号内声明要继承的基类名即可
        class <class name>(<base class name>):
            def __init__(self,<parameters>):
                <coding>
                    ...
                    
    注意，基类名可以使带路径的：ModuleName.BaseClassName
    
    
派生类可以使用基类的各种属性和方法
派生类使用类属性和类方法是，要通过基类的名字调用
注意，派生类只能继承基类的公开属性和方法，不能继承私有属性和方法
"""
class DemoClass:
    count = 0
    def __init__(self,name):
        self.name = name
        DemoClass.count += 1
    def getName(self):
        return self.name

class HumanNameClass(DemoClass):
    def printName(self):
        return str(DemoClass.count) + self.name + "hello"
dc1 = HumanNameClass("wang")
print(dc1.getName())
print(dc1.printName())
"""
调用派生类的printName起始是执行了：
    def __init__(self,name):
        self.name = name
        DemoClass.count += 1
    def getName(self):
        return self.name
    def printName(self):
        return str(DemoClass.count) + self.name + "hello"
先把父类执行一遍，然后继续执行自己新添加的函数printName
"""
"""
两个与继承关系判断有关的内置函数：
函数                          描述
isinstance(obj,cls)           判断对象obj是否是类cls的实例或子类实例，返回True/False
issubclass(cls1,cls2)         判断类cls1是否是类cls2的子类，返回True/False
"""
class DemoClass_1:
    count = 0
    def __init__(self,name):
        self.name = name
        DemoClass.count += 1
    def getName(self):
        return self.name

class HumanNameClass_1(DemoClass_1):
    def printName(self):
        return str(DemoClass_1.count) + self.name + "hello"
dc2 = HumanNameClass_1("wang")
print(isinstance(dc2,DemoClass_1))
print(isinstance(dc2,HumanNameClass_1))
print(issubclass(HumanNameClass_1,DemoClass_1))
"""
返回值：
    True
    True
    True
"""
"""
python的最基础类是object类
所有类都继承了object类
"""
"""
重载：：派生类对基类属性或方法的再定义
属性重载：派生类定义并使用了与基类相同名称的属性
    属性重载采用就近覆盖原则：重载无需特殊标记
        步骤：
            对于派生类下定义实例对象，当对象引用属性和方法时：
            1. 优先使用派生类重新定义的属性和方法
            2. 然后寻找基类的属性和方法
            3. 在寻找超类的属性和方法 
            
方法重载：派生类定义并使用了与基类相同名称的方法
"""
class DemoClass_2:
    #基类属性
    count = 0
    def __init__(self,name):
        self.name = name
        DemoClass.count += 1
class HumanNameClass_2(DemoClass_2):
    #派生类重载的属性
    count = 99
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        HumanNameClass_2.count -= 1
    def printCount(self):
        return str(HumanNameClass_2.count) + self.name
dc3 = HumanNameClass_2("wang")
print(dc3.printCount())
##返回：98wang，而不是-1wang，说明派生类的count类属性已经替换了基类的count类属性


""""
类的方法重载
    完全重载：
        派生类完全重定义与积累相同名称的方法，直接在派生类中定义同名方法即可
    增量重载：
        派生类扩展定义与积累相同名称的方法
"""
"""
增量重载：使用super（）方法
class <subclass name>(<base class name>):
    def <method name>(self,<parameters>)
        super().<base class method name>(<parameters>)
"""
class DemoClass_3:
    count = 0
    def __init__(self,name):
        self.name = name
        DemoClass_3.count += 1
    def printCount(self):
        return str(DemoClass_3.count) + self.name

class HumanNameClass_3(DemoClass_3):
    def __init__(self,name):
        self.name = name
    def printCount(self):
        return super().printCount() + "hello"
dc4 = HumanNameClass_3("wang")
print(dc4.printCount())




