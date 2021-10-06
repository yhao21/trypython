import time
"""
类之间的关系


依赖关系：狗和主人的关系

关联关系：你和你女朋友

聚合关系：如电脑是由很多硬件组合在一起的（CPU，硬盘，内存等），即使你的电脑坏了，并不等于你所有的硬件都坏了，
          比如你的内存坏了，但是你的硬盘安装到其他地方还可以正常使用

组合关系：比聚合关系更紧密的的一种关系。比如人体的各个器官组成一个人，但如果一个人挂了，，其他地方也跟着挂了

继承关系：类的三大特性之一，子类，父类，超类

"""


"""依赖关系："""

class Dog():
    def __init__(self,name,age,breed,owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner # 传进来的应该是一个人的对象
        self.sayhi() #在实例化的时候调用自己的方法

    def sayhi(self):
        print('Hi, I am [%s], a [%s], and my owner is [%s]' % (self.name,self.breed,self.owner.name))
        """此处如果只用self.owner,而不是self.owner.name,当传入p是，显示的就是它对应的内存地址，而不是人名"""

class Person():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def walk_dog(self,dog_obj):
        print('owner [%s] hang out with dog [%s]' % (self.name,dog_obj.name))

p = Person('Synferlo',26,'M')
d = Dog('Mjj',2,'jin mao', p)
"""
Hi, I am [Mjj], a [jin mao], and my owner is [Synferlo]

这就是依赖关系。两个对象相互调用



"""
p.walk_dog(d)
"""owner [Synferlo] hang out with dog [Mjj]"""

