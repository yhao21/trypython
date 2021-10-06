import time

"""
组合关系：由一堆组件组成一个完整的实体，组件本身相互独立，但是不能单独运行，必须和宿主结合在一起


比如，人狗大战中的武器，武器自己不能打狗，必须要通过人来操控
"""


class Dog():
    roles = 'dog'

    def __init__(self,name,breed,attack_val):
        self.name  = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = 100

    def bite(self,person):
        person.life_val -= self.attack_val
        print("dog [%s] bite human [%s], human[%s] lose [%s] HP, remaining HP is [%s]" % (self.name,person.name,person.name,self.attack_val,person.life_val))


class Weapon:

    def pan(self, dog):
        """平底锅"""
        self.name = "pan"
        self.attack_val = 40
        dog.life_val -= self.attack_val
        self.attack_info(dog)

    def assault_rifle(self, dog):
        """M4"""
        self.name = "M416"
        self.attack_val = 80
        dog.life_val -= self.attack_val
        self.attack_info(dog)

    def sniper_rifle(self, dog):
        """M24"""
        self.name = "M24"
        self.attack_val = 100
        dog.life_val -= self.attack_val
        self.attack_info(dog)

    def attack_info(self, dog):
        print("[%s] is attacked by [%s], [%s] lose [%s] HP, remaining HP is [%d]" % (
        dog.name, self.name, dog.name, self.attack_val, dog.life_val))


class Person():
    role = 'person'

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
        self.life_val = 100
        self.weapon = Weapon() #在这里对weapon实例化，相当于只要人物被设定，武器同时就被设定好了



d = Dog('Mjj','jin mao',30)
p = Person('Synferlo','M')


d.bite(p)
"""dog [Mjj] bite human [Synferlo], human[Synferlo] lose [30] HP, remaining HP is [70]"""
p.weapon.sniper_rifle(d)
"""[Mjj] is attacked by [M24], [Mjj] lose [100] HP, remaining HP is [0]"""
