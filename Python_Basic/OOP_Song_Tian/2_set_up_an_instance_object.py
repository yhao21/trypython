class DemoClass:
    'this is a demon for python class'
    print("hello demo class")
print(DemoClass.__doc__)
print(type(DemoClass))
"""
定义类之后，下一行可以用字符串对类进行说明，相当于注释
如果想打印这个说明，使用：  类名.__doc__
打印类的type

返回：
    hello demo class
    this is a demon for python class
    <class 'type'>
    
类定义后，会直接被执行，即使我们没有调用这个类。如：自动打印hello demo class
所以，我们一般不会在类里面写执行函数

"""

"""
创建类的实例对象：instance object
变量名 = 类名（属性）

"""
class ClassTry:
    print("hello")
cn = ClassTry()
print(type(cn))

"""
将ClassTry赋值给cn变量，就是生成一个类的实例对象的过程，
cn的type是他执行时的type
    <class '__main__.ClassTry'>
一个类只能有一个类对象
但是一个类可以有无数的实例对象
"""

