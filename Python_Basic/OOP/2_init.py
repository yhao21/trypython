import time


"""
如过我们想通过模板生成对象自己特有的属性，而不是公有属性怎么操作呢？

这时候需要__init__()初始化来解决。这个函数在类被调用的时候会自动执行。比如我在调用Dog的时候他会自动print hello
"""
class Dog():
    d_type = '京巴'

    def __init__(self):
        print('hello')
        print()


d = Dog()
"""return: hello"""

"""我想设计每个对象自己的名字和年龄属性，只需要在init中加入name和age参数，然后在调用Dog时，传入这两个参数即可"""

class Dog1():
    d_type = '京巴'

    def __init__(self,name,age):
        print('hi, i am ' + name + ". i am " + str(age) + " years old~")

d1 = Dog1('Jack','13')
"""注意，传入的值必须是字符串格式，或者在print中将age字符串化"""
"""return: hi, i am Jack. i am 13 years old~"""



"""
say_hi明明是一个函数，为什么我们在外部调用这个函数的时候即便括号内是空，程序也不会报错呢？
原因如下：

"""
class Dog2():
    d_type = '京巴'

    def __init__(self,name,age):
        print('hi, i am ' + name + ". i am " + str(age) + " years old~")

    def say_hi(self):
        print('Hello ' + self.d_type)

d2 = Dog2('synferlo',1)  #hi, i am synferlo. i am 1 years old~
d2.say_hi() #Hello 京巴
"""
这里say_hi里没有参数但是程序没报错因为类自动将d2作为参数传给了say_hi
即，d2.say_hi(d2)
此时say_hi执行的是：print('Hello ' + d2.d_type)
而，d2.d_type 是‘京巴’,所以打印出来的是：hello 京巴。
这也是为什么在使用d2.say_hi()之前必须先d2 = Dog2('synferlo',1)调用类
"""



"""在类方法中想要调用name和age，需要将两个参数与实例绑定。self是实例本身"""
class Dog2():
    d_type = 'jin mao'

    def __init__(self,name,age):
        self.name2 = name #绑定参数值到实例对象中，参数值为name，实例对象d2（self）
        self.age2 = age

    def say_hi(self):
        print('Hello ' + self.name2)

d2 = Dog2('synferlo',1)  #hi, i am synferlo. i am 1 years old~
d2.say_hi()#Hello synferlo

"""
这里将对象d2的属性：name，即d2.name2(self.name2)与传入的参数synferlo绑定。这样，即使init函数结束后，也依然可以在say_hi中调用

若不想通过self.name的方式提前设定，也可以通过d.属性名 的方式来实现：
"""
d2.gender ='male'
print(d2.gender)
"""return：male"""



"""
总结：
之所以类中的方法必备的参数是self是为了打通实例在类中各方法的使用。通过self共享
"""