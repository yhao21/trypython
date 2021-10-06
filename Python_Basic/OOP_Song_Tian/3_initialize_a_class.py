import time

class DemoClass:
    def __init__(self,name):
        print(name)
dc1 = DemoClass("Mr.Wang")
dc2 = DemoClass("Mr.Lee")


"""
类的构造函数：
class <class name>:
    def __init__(self,<parameters>)
        <codes>
    .....

向类传递实例信息（如Mr.Wang）来激活这个类的实例对象，并运行这个类

    
__init__()
self 表示类自身
"""