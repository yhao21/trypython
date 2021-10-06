import time


"""
多继承中的深度优先与广度优先：

MonkeyKing继承了Monkey和ShenXian，现在这两个父类本身也有自己的父类：MonkeyBase与ShenXianBase

根据代码我们知道MonkeyKing优先继承Monkey，（顺序原因）
那么，如果MonkeyBase与ShenXianBase都有一个方法叫fight，MonkeyKing会继承哪一个呢？

结构图：

                                           ___________________MonkeyBase(超类)
                                          |  
                _________Monkey___________| 
               |        （父类） 
               |
MonkeyKing-----
   (子类)      |
               |________ShenXian___________
                        （父类）            | 
                                            |____________________ShenXianBase(超类） 




MonkeyKing其实继承了这四个类，那么如果在MonkeyKing中调用一下fight方法，（此方法只在两个超类中存在）他会取哪一个超类里找呢

MonkeyKing(Monkey,ShenXian)

深度优先 的查找顺序：Monkey---MonkeyBase---ShenXian---ShenXianBase

广度优先 的查找顺序：Monkey---ShenXian---MonkeyBase---ShenXianBase

python3中，若两个超类没有继承同一个父类，则按照深度优先查找，所以回去MonkeyBase中查找

但是！！
注意！！
python3并不想python2一样始终都是深度优先。
当两个超类继承同一个父类时，是按照广度优先查找的，后面的例子里会讲到

综合起来，其实python两个优先都不算，。。。
"""

class ShenXianBase:
    def fight(self):
        print("ShenXianBase fight")

class MonkeyBase:
    def fight(self):
        print('MonkeyBase fight')


class ShenXian(ShenXianBase):
    """神仙类"""
    def fly(self):
        print('神仙都会飞')

class Monkey(MonkeyBase):
    def eat_peach(self):
        print('猴子喜欢吃桃子。。。')

class MonkeyKing(Monkey,ShenXian):
    """美猴王"""
    def play_golden_stick(self):
        print('孙悟空玩金箍棒')

m = MonkeyKing()
m.fight()
"""return: MonkeyBase fight"""

"""当我添加了一个MonkeyBase的父类，然后取消MonkeyBase的fight方法，将这个方法放到AnimalBase中。
此时，虽然ShenXianBase比AnimalBase先一级，且他也有fight，但是MonkeyKing也只会调用AnimalBase的fight方法"""


class AnimalBase1:
    def fight(self):
        print("Animal Fight!")

class ShenXianBase1:
    def fight(self):
        print("ShenXianBase fight")

class MonkeyBase1(AnimalBase1):
    pass

class ShenXian1(ShenXianBase1):
    """神仙类"""
    def fly(self):
        print('神仙都会飞')

class Monkey1(MonkeyBase1):
    def eat_peach(self):
        print('猴子喜欢吃桃子。。。')

class MonkeyKing1(Monkey1,ShenXian1):
    """美猴王"""
    def play_golden_stick(self):
        print('孙悟空玩金箍棒')

n = MonkeyKing1()
n.fight()
"""return: Animal Fight!"""



"""
所有类的祖师爷：：object类
所有类都是继承object类的。。也就是python中的一切皆对象
所以，，我们写的类class也是个对象，，叫类对象
"""
"""
class A:
    这种写法叫经典类
class A(obj):
    这种写法叫新式类
"""



"""
python3中的不完全广度优先
园艺师python3用了C3算法


比如现在MonkeyBase与ShenXianBase都继承于Base这个父类
class MonkeyKing(Monkey,ShenXian)
猴王先继承了Monkey，
注意，现在我们设定：只有ShenXian和Base有fight这个方法
若果python3真的是深度优先，MonkeyKing会按照这个顺序查找：Monkey---MonkeyBase---Base

但事实上，在这种有交汇的继承关系中，MonkeyKing的查找顺序是这样的
Monkey---MonkeyBase---ShenXian---ShenXianBase


                                           ___________________MonkeyBase(超类)__________________
                                          |                                                     |
                _________Monkey___________|                                                     |
               |        （父类）                                                                |
               |                                                                                Base        
MonkeyKing-----                                                                                 |    
   (子类)      |                                                                                | 
               |________ShenXian___________                                                     |
                        （父类）            |                                                    |       
                                            |____________________ShenXianBase(超类）_____________| 


"""



class Base:
    def fight(self):
        print("Animal Fight!")

class ShenXianBase2(Base):
    pass

class MonkeyBase2(Base):
    pass

class ShenXian2(ShenXianBase2):
    """神仙类"""
    def fly(self):
        print('神仙都会飞')

    def fight(self):
        print('Shenxian Fight')

class Monkey2(MonkeyBase2):
    def eat_peach(self):
        print('猴子喜欢吃桃子。。。')

class MonkeyKing2(Monkey2,ShenXian2):
    """美猴王"""
    def play_golden_stick(self):
        print('孙悟空玩金箍棒')

q = MonkeyKing2()
q.fight()

"""
在复杂的多继承中，如果你搞不清楚继承关系了可以通过print(classname.mro())查看继承顺序。
顺序是按照列表中元素的先后顺序排列的
"""
print (MonkeyKing2.mro())
"""
[<class '__main__.MonkeyKing2'>, <class '__main__.Monkey2'>, <class '__main__.MonkeyBase2'>, <class '__main__.ShenXian2'>, <class '__main__.ShenXianBase2'>, <class '__main__.Base'>, <class 'object'>]

顺序：
MonkeyKing2----Monkey2----MonkeyBase2----ShenXian2----ShenXianBase2----Base----Object
"""