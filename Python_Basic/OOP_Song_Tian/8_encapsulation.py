import time
"""
属性：
    公开类属性
        class <class name>:
            <class attribute name> = <class attribute initial value>
            def __init__(self,<parameter>):
                self.<object attribute name> = <object attribute initial value>
    私有类属性
        仅供当前类访问的类属性，子类亦不能访问    
        私有类属性名开始需要有两个下划线如：__count
        
        class <class name>:
            <__private class attribute name> = <class attribute initial value>
            def __init__(self,<parameter>):
                ...
    公开实例属性
        class <class name>:
            <class attribute name> = <class attribute initial value>
            def __init__(self,<parameter>)
                self.<object attribute name> = <object attribute initial value>
                    ...
    私有实例属性
        class <class name>:
            def __init__(self,<parameter>)
                self.<__private object attribute name> = <object attribute initial value>
        私有实例属性名开始也需要两个下划线: __name
        私有实例属性，只能在类内部被访问，不能通过 “类名.属性名” 或者 “对象名.属性名” 访问
"""
"""
私有类属性：
    为什么要通过类方法getCount来访问私有属性，而不是直接把私有属性定义为公开属性呢？
    原因：
        通过类方法调用私有属性，我们可以在类方法里添加更多的代码满足程序需求，
        此外，可以通过getCount这个类方法控制外部对类私有属性的访问
"""
class DemoClass:
    __count = 0
    def __init__(self,name):
        self.name = name
        DemoClass.__count += 1

    @classmethod
    def getCount(cls):
        return DemoClass.__count
dc1 = DemoClass("wang")
dc2 = DemoClass("Lee")
#外部想要获取类的私有属性需要定义一个类方法，getCount
print(DemoClass.getCount())

"""
私有实例属性
"""
class DemoClass_1:
    def __init__(self,name):
        ##两个下划线是私有实例属性名字
        self.__name = name
    def getName(self):
        return self.__name
dc3 = DemoClass_1("wang")
dc4 = DemoClass_1("Lee")
print (dc3.getName(), dc4.getName())

"""
方法
    私有方法
        只在类内部使用的方法
            class <class name>:
                def <__method name>(self,<parameter>):
                    ...
        私有方法名字开头需要两个下划线
    
    公开方法
"""
"""
私有方法：
"""
class DemoClass_2:
    def __init__(self,name):
        self.__name = name

    def __getName(self):
        if self.__name != "":
            return self.__name
        else:
            return "Zhang"
    def printName(self):
        return "Mr. {}".format(self.__getName())
dc5 = DemoClass_2("Wang")
dc6 = DemoClass_2("")
print(dc5.printName(),dc6.printName())

"""
类的保留属性 special attributes

仅用类名访问的保留属性
    __name__        类的名字
    __qualname__    以.分隔从模块全局命名空间开始的完整类名称
    __bases__       类所继承的基类名称
"""
class DemoClass_3:
    "A Demo Class"
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name
dc7 = DemoClass_3("Wang")
print(DemoClass_3.__qualname__, DemoClass_3.__name__, DemoClass_3.__bases__)
##返回：DemoClass_3 DemoClass_3 (<class 'object'>,)

"""
其他的保留属性：
<class>.__dict__    包含类成员信息的字典，key是属性和方法名，value是地址
<object>.__dict__   包含对象属性信息的字典，key是属性名，value是值
__class__           对象所对应的类信息，即type信息
__doc__             类描述，不可继承
__module__          类所在模块的名称
"""
class DemoClass_4:
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name
dc8 = DemoClass_4("wang")
print(DemoClass_4.__module__, DemoClass_4.__class__)
print(DemoClass_4.__dict__)
"""
返回：
    __main__ <class 'type'>
    {'__module__': '__main__', '__init__': <function DemoClass_4.__init__ at 0x000002E3F387B700>, 'getName': <function DemoClass_4.getName at 0x000002E3F387B790>, '__dict__': <attribute '__dict__' of 'DemoClass_4' objects>, '__weakref__': <attribute '__weakref__' of 'DemoClass_4' objects>, '__doc__': None}
"""

"""
类的保留方法 special method
双下划綫开头和结尾
需要重写预留方法

常用保留方法              对应操作                    描述
obj.__init__()          obj = ClassName()           初始化实例对象
obj.__del__()           del obj                     删除实例对象的函数逻辑
obj.__repr__()          repr(obj)                   定义对象可打印字符串的函数逻辑
obj.__str__()           str(obj)                    定义对象字符串转换操作的函数逻辑
obj.__bytes__()         bytes(obj)                  定义对象字节串转换操作
obj.__format__()        obj.format()                定义对象格式化输出
obj.__hash__()          hash(obj)                   定义对象哈希操作的函数逻辑
obj.__bool__()          bool(obj)                   定义对象布尔运算的函数逻辑
obj.__len__()           len(obj)                    定义对象长度
obj.__reversed__()      obj.reversed()              定义对象逆序的函数
obj.__abs__()           abs(obj)                    绝对值操作
obj.__int__()           int(obj)                    整数转换

"""
class DemoClass_5:
    def __init__(self,name):
        self.name = name







