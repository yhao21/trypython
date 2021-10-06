import time

"""
反射，，reflection

可以通过字符串操作对象的属性或者方法（主要是在你不清楚这个对象是否有某一个属性时，检查这个属性是不是有这个属性，便于后面修改）

"""

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print('walking')


def talk(self):
    print(self.name,' is talking.....')

p = Person('Synferlo',11)
"""
这个时候比如我不知道这个p有没有一个叫hobbie的属性，如果我直接用if p.hobbie: print('...')的话，相当于直接调用这个属性，系统会报错
那我们就通过反射完成：

if hasattr(p,'hobbie'):
    print('l.....')

"""
if hasattr(p,'hobbie'):
    print('yes')
"""没有返回任何值，表示，没有这个属性"""

if hasattr(p,'name'):
    print('yes,name')
"""return: yes,name"""
"""表示有这个属性"""



"""
反射、映射、自省的四种方法：增删改查

getattr()
hasattr()
setattr()
delattr()

"""

a = getattr(p,'name')
print(a)
"""
return: Synferlo
getattr是用来获取对象的属性的
"""


"""设计一个获得对象属性的小程序"""
# user_command = input('>>:').strip()
# if hasattr(p,user_command):
#     func = getattr(p,user_command)
#     func()
# else:
#     print('no such method')
"""
    >>:walk
    walking
"""


"""通过setattr()添加一个属性"""
setattr(p,'gender','female')
print(p.gender)
"""return: female"""


"""添加一个方法,把talk方法添加到Person中。必须要自己把p传入进去，这是和类方法的区别"""
setattr(p,'speak',talk)
p.speak(p)
"""Synferlo  is talking....."""


"""不光可以对实例绑定，还可以对类绑定.  给类绑定方法后，无需手动把实例对象传入方法中"""

setattr(Person,'speak2',talk)
p.speak2()
"""Synferlo  is talking....."""


"""delattr()"""
delattr(p,'age')
p.age
"""AttributeError: 'Person' object has no attribute 'age'
成功删除

这种方法和
del p.age的效果是一样的
"""