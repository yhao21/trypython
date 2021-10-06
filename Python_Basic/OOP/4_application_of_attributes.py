import time



class People():
    def __init__(self,name,age,gender,nation):
        self.name = name
        self.age = age
        self.gender = gender
        self.nation = nation

p1 = People('Synferlo',22,'M','CH')
p2= People('Jack',15,'M','CH')
p3 = People('Simon',45,'F','CH')

"""
这里你发现p1-p3他们的nation属性都是CH，如果你有很多个实例对象，则你存入了很多的CH，浪费空间
为了避免这个问题，我们可以将nation定义为类属性
"""


class People1():
    nation = 'CH'
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

p4 = People1('Synferlo',22,'M')
p5= People1('Jack',15,'M')
p6 = People1('Simon',45,'F')

print(p4.nation)
"""return: CH"""

"""如果有一天你想吧数据库中所人的国际都改成US，则只需要将类属性的nation修改即可，无需逐一修改实例对象的属性"""
People1.nation = "US"
print(p4.nation)
"""return：US"""

"""
此时，我想对其中一个实例的nation属性做修改，只需用对象名+属性 = 值即可，此操作不会对类属性产生影响
即，其他人国籍还是US
"""

p6.nation = 'TW'
print(p6.nation)
"""return: TW"""
print(People1.nation)
"""return: US"""

"""
按理说所有实例对象使用的nation都是类属性的，为什么p6修改后与其他人不一样了呢
因为：
    p6.nation = 'TW'这个操作相当于给p6新建了一个实例属性，当你再次调用他的时候，相当于调用的是实例属性，而不是类属性
"""