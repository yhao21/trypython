import time
"""
继承

继承的主要目的是为了增加代码复用，减少重复输入代码
继承用在：子类不仅有父类的共性，还有他们自己的特性如：人吃饭，狗追兔子
"""

class Animal:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print("%s eating right now" % self.name)

class Person(Animal):
    #继承Animal这个父类，也就继承了他下面的属性和方法
    a_type = 'senior mammal'
    def talk(self):
        print('%s is talking' % self.name)

    def eat(self):
        print('%s is eating gently'%self.name)

class Dog(Animal):
    a_type = 'mammal'
    def chase_rabbit(self):
        print('%s is chasing rabbit'%self.name)



p = Person('Synferlo',26,'M')
p.eat()
"""return: Synferloi eating right now"""

d = Dog('Mjj',12,'f')
d.eat()
"""return: Mjji eating right now"""
d.chase_rabbit()
"""Mjj is chasing rabbit"""

"""
注意：如果子类用的方法与父类的方法同名，则执行子类中的方法
"""

p.eat()
"""Synferlo is eating gently"""


"""子类也可以有自己的属性，比如我们把物种分类加入各个子类中"""
print(d.a_type)
"""return: mammal"""

print(p.a_type)
"""return: senior mammal"""