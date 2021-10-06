import time

"""
子类重写eat后就只能执行子类的eat了

能不能在父类的eat基础上进行改进。目标效果：先执行父类，然后在执行子类特有的eat

只需要在子类的eat下先引用父类的eat，，，Animal.eat(self)
"""


class Animal:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print("%s eating right now" % self.name)

class Person(Animal):

    a_type = 'senior mammal'

    def talk(self):
        print('%s is talking' % self.name)

    def eat(self):
        Animal.eat(self)
        print('%s is eating gently'%self.name)

class Dog(Animal):

    a_type = 'mammal'

    def chase_rabbit(self):
        print('%s is chasing rabbit'%self.name)


p = Person('Synferlo',26,"M")
p.eat()
"""
returns:
    Synferlo eating right now
    Synferlo is eating gently
"""



"""
另外需要注意：
继承父类的时候，同时也继承了父类的参数，比如虽然Person没有设置init并要求上传参数，
但我们引用Person的时候是需要把name，age，gender这三个参数提交给Person的。


那现在如果我不想上传这么多参数，我只用得到name这个参数，我要求Person中的实例只上传name这个参数怎么办呢？
这时候就需要重新再Person这个子类中定义init

class Person(Animal):
    def __init__(self,name)
        self.name = name
        
p1 = Person("Synferlo")

这个时候就只需要上传name一个参数就可以了
"""


"""
那现在如果我不光想让Person拥有父类的三个参数，我还想额外增加参数怎么办呢，，
同样的，在Person下的init中添加额外参数即可
示例如下：
"""

class Animal1:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        print('___parents____')

    def eat(self):
        print("%s eating right now" % self.name)

class Person1(Animal1):

    a_type = 'senior mammal'

    def __init__(self,name,age,gender,hobbie):
        #name,age,gender都是父类在init里面就已经存在的，所以不需要在用这么多代码，直接用Animal.__init__即可，不过这是基于python2.x系列的，现在都用super
        # self.name = name
        # self.age = age
        # self.gender = gender
        #Animal1.__init__(self,name,age,gender)
        ##super的方法一
        #super(Person1,self).__init__(name,age,gender)
        #或者可以用这种
        super().__init__(name,age,gender)
        self.hobbie = hobbie
        print('_____children________')


    def talk(self):
        print('%s is talking' % self.name)

    def eat(self):
        ##在多继承中，用Animal1.eat()表明我只继承Animal1中的eat方法。即使其他父类中也存在eat方法，但不会被继承
        #Animal1.eat(self)
        ##但如果使用super的话，他会按照父类们的先后顺序依次继承父类的方法
        ##所以在多继承中，我们都用super
        super().eat() ##执行一个或多个父类的方法
        print('%s is eating gently'%self.name)

class Dog1(Animal):

    a_type = 'mammal'

    def chase_rabbit(self):
        print('%s is chasing rabbit'%self.name)


p2 = Person1("Adam",26,'M','Tennis')
"""使用Animal.__init__后，你打印name,age,gender这些父类有的属性可以打出来，说明Animal.__init__中的self已经把p2传给父类了"""
print(p2.name,p2.gender,p2.age,p2.hobbie)
"""
returns:
    ___parents____
    _____children________
    Adam M 26 Tennis

可以看到，这里是先执行了父类，然后执行了子类，最后打印了各个属性
"""
