import time

"""
多继承

python和C++支持多继承，
Java不支持

"""
class ShenXian:
    """神仙类"""
    def fly(self):
        print('神仙都会飞')

class Monkey:
    def eat_peach(self):
        print('猴子喜欢吃桃子。。。')

class MonkeyKing(ShenXian,Monkey):
    """美猴王"""
    def play_golden_stick(self):
        print('孙悟空玩金箍棒')

m = MonkeyKing()
m.play_golden_stick()
m.fly()
m.eat_peach()
"""
实例化monkeyking后，发现m可以使用两个父类的方法
"""
"""
    孙悟空玩金箍棒
    神仙都会飞
    猴子喜欢吃桃子。。。
"""
"""
此时ShenXian和Monkey的方法不同，但如果两个父类都有一个名叫fight的方法，则继承ShenXian的方法，因为MonkeyKing(ShenXian,Monkey)中先继承的ShenXian。
多继承的顺序是从左到右依次继承，如果有相同方法的话
"""