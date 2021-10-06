import time
"""
析构函数：
在真实删除实例对象时被调用
    真实删除：当前对象的引用数为0或者当前程序退出（python垃圾回收）
    如果一个对象的引用数量不为0，即使你用del删除了这个对象，也不会调用__del__
    
使用__del__()作为析构函数

class <class name>:
    def __del__(self):
        <coding>
        ....
"""
class DemoClass:
    def __init__(self,name):
        self.name = name
    def __del__(self):
        print("bye", self.name)
dc1 = DemoClass("wang")
##删除dc1
del dc1
"""
真实删除：当前对象的引用数为0或者当前程序退出（python垃圾回收）
    如果一个对象的引用数量不为0，即使你用del删除了这个对象，也不会调用__del__
下面的例子中，我们预期打印的是：
    bye wang
    wang
因为我们先用del dc3删除了dc3，按理说应该执行__del__
但没有执行，因为我们把dc3赋值给了dc4，所以其实wang还在被引用，
当我们print(dc4.name)后，整个程序结束了。这个时候才调用了__del__
"""
class DemoClass_1:
    def __init__(self,name):
        self.name = name
    def __del__(self):
        print("bye",self.name)
dc3 = DemoClass_1("wang")
dc4 = dc3
del dc3
print(dc4.name)

"""
那如何获得对象的引用次数呢：
sys.getrefcount(<object name>)
    返回值为被引用值+1
    
"""
import sys
class DemoClass_3:
    def __init__(self,name):
        self.name = name
    def __del__(self):
        return "bye" + self.name
dc5 = DemoClass_3("wang")
dc6 = dc5
print(sys.getrefcount(dc5))
"""
返回值：
3
bye wang
"""




