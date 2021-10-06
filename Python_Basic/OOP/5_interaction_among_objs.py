
class Dog:
    role = 'dog'

    def __init__(self,name,breed,attack_val):
        self.name = name
        self.breed = breed
        self.attack_val = attack_val
        self.life_val = 100

    def bite(self,person):
        person.life_val -= self.attack_val
        print('dog [%s] attack human [%s], human [%s] lose [%s] HP, remaining HP is [%s]...' % (self.name,person.name,person.name,self.attack_val,person.life_val))

class Person:
    role = 'person'
    def __init__(self,name,gender,attack_val):
        self.name = name
        self.gender = gender
        self.attack_val = attack_val
        self.life_val = 100

    def attack(self,dog):
        dog.life_val -= self.attack_val
        print('human [%s] attack dog [%s], dog [%s] lose [%s] HP, remaining HP is [%s]...' % (self.name,dog.name,dog.name,self.attack_val,dog.life_val))

d1 = Dog('Mjj','jin mao',30)
d2 = Dog('HH','er ha',40)


p1 = Person('Synfer','M',50)

p1.attack(d1)
"""return: human [Synfer] attack dog [Mjj], dog [Mjj] lose [50] HP, remaining HP is [50]..."""

d1.bite(p1)
"""dog [Mjj] attack human [Synfer], human [Synfer] lose [30] HP, remaining HP is [70]..."""