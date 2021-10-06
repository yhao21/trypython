class DemoClass:
    ##count是一个被定义的类属性
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        DemoClass.count += 1
dc1 = DemoClass("wang",45)
dc2 = DemoClass("Lee",21)
##count运算，类当中每多一个实例对象，count就+1，，现在有两个实例对象所以是2
print("sum",DemoClass.count)
##打印dc1和dc2的名字（参数）
print(dc1.name,dc2.name)


"""
类对象的属性，所有的实例对象均可使用
实例对象的属性只能自己使用

class <class name>:
    <class attribute name> = <initial value of class attribute>
    def __init__(self,<parameters>)
        self.<name of instance object attributes> = <instance object attibutes>
DemoClass.count是访问类属性
    注意，类属性的访问是通过 类名+属性名实现
dc1.name是访问实例对象的属性
    注意，实例对象属性访问：实例对象名+属性名
"""

