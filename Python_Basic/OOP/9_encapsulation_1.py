import time

"""
类的封装：encapsulation
    封装的目的是防止外部随便修改类的参数值

"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.life_val = 100

"""
我们要的效果是，生命值只有在被攻击时候才会边，但是现在可以在外部随便修改：
"""

p = Person('Synferlo',25)
p.life_val -= 40
print(p.life_val)
"""
现在生命值就变成60了。。。
随意我们要封装类，让外部无法直接访问

我们只需要把公有属性变成私有属性即可
"""


class Person1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__life_val = 100

p1 = Person1('Mjj',25)
#p1.__life_val -=40
"""
return: 'Person' object has no attribute '__life_val'
这时你再想从外部修改，程序会报错
但是你从内部是可以访问的
"""


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__life_val = 100

    def get_life_val(self):
        print('remaining HP is %s' % self.__life_val)
        return self.__life_val

p2 = Person2('Mjj', 25)
p2.get_life_val()
"""remaining HP is 100"""

"""这样既可以防止外部直接篡改生命值，又可以把生命值返回给外部，即外部只有只读权限"""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__life_val = 100

    def get_life_val(self):
        print('remaining HP is %s' % self.__life_val)
        return self.__life_val

    def got_attack(self):
        self.__life_val -= 20
        print('you are attacked by an enemy, remaining HP is %s' % self.__life_val)


p3 = Human('Mjj', 25)
p3.got_attack()
"""you are attacked by an enemy, remaining HP is 80"""




"""注意：方法也是可以被私有化的。私有化的过程就是封装"""


class Human1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__life_val = 100

    def get_life_val(self):
        print('remaining HP is %s' % self.__life_val)
        return self.__life_val

    def got_attack(self):
        self.__life_val -= 20
        print('you are attacked by an enemy, remaining HP is %s' % self.__life_val)
        self.__breath()

    def __breath(self):
        print('%s is breathing' % self.name)

h1 = Human1('Yan',25)
#h1.__breath()
"""
AttributeError: 'Human1' object has no attribute '__breath'、

这时候外部是无法调用这个私有方法的
只能内部访问
"""
h1.got_attack()
"""
    you are attacked by an enemy, remaining HP is 80
    Yan is breathing
"""



"""
但如果你真的想访问这个私有方法可以通过：

实例名._类名__方法名()    来实现

私有属性可以通过这个方法访问和修改
"""
h1._Human1__breath()
"""Yan is breathing"""

h1._Human1__life_val = 10
h1.get_life_val()
"""remaining HP is 10"""

"""
但是实例一旦生成，就无法从外部创建新的私有属性了，，是能在类内初始化时候可以创建：
"""
h1.__love = 444
print(h1.__love)
"""
return: 444
你看，这里虽然样子长得像私有属性，但其实他不是私有属性，外不可以直接访问。这就是为什么说私有属性只能初始化时候创建
"""


