

class Person():

    def __init__(self,name,):
        self.name = name
        self.hp_val = 100
        self.attack_val = 100

    def attack(self,obj):
        obj.hp_val -= self.attack_val
        print("human %s attack robot %s, robot's HP [%s] ....." % (self.name,obj.name,obj.hp_val))


class Robot():
    def __init__(self,name):
        self.name = name
        self.hp_val = 1000
        self.attack_val = 5



p1 = Person('Adam')
p2 = Robot('Harry')

p1.attack(p2)

