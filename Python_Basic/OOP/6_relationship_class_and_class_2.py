import time

"""
关联关系：你和你女朋友通过感情关联到一起，你和你老板通过工作关联到一起
"""

class Person:

    def __init__(self,name,age,gender):
        self.name = name
        self.age =  age
        self.gender = gender
        self.partner = None #先生成一个None，传入的而应该是个对象
    def private_behavior(self):
        pass

boy = Person('Synferlo',26,'M')
girl = Person('Zoe',24,'F')

"""如何关联boy和girl呢，在init里创建一个partner"""

boy.partner = girl
girl.partner = boy

"""把girl对象赋值给了boy.partner"""
#print(boy.partner.name,)
#print(girl.partner.name)
"""此时打印boy.partner这个对象的name属性，其实就是打印的girl的name属性"""

boy.partner = None
# print(boy.partner.name)
"""return: AttributeError: 'NoneType' object has no attribute 'name'"""
#print(girl.partner.name)
"""因为没有删除girl的partner关系所以，还可以打印girl的，这相当于单方面“分手”，这不是我们想要的
所以我们需要再把girl的也设置成None才可以"""



"""
上述关联方法若想删除必须输入boy.partner = None, gilr.partner = None
如果你的对象很多，你就要挨个接触，效率很低

那我们可以新建一个类用来存两个人的关系
"""

class Relationship():
    def __init__(self,obj1,obj2):
        self.couple = []

    def make_couple(self,obj1,obj2):
        self.couple = [obj1,obj2] #这样两个人就成了对象
        print('[%s] and [%s] paired successfully' % (obj1.name,obj2.name))



class Person1:
    def __init__(self,name,age,gender):
         self.name = name
         self.age = age
         self.gender = gender
         #self.partner = None


p1 = Person('Mjj',24,'M')
p2 = Person('Lyy',21,'F')
#
# p1.partner = p2
# p2.partner = p1

relation_obj = Relationship(p1,p2)
relation_obj.make_couple(p1,p2)

"""
如果p1和p2分手，你想取消他们两个的pair关系。只需要清空列表就可以，或者当多个人物存在时，还要将p1与p2从列表中移除即可
注意，有了Relationship下的make_couple我们就不需要self.partner了，因为只要调用make_couple就可以知道两个人的关系

但如果我不想通过relationship查找怎么办呢，

需要在Person初始化的时候加一个relation的参数
"""

class Relationship1():

    def __init__(self):
        self.couple = []


    def make_couple(self, obj1, obj2):
        self.couple = [obj1, obj2]  # 这样两个人就成了对象
        print('[%s] and [%s] are soul mates' % (obj1.name, obj2.name))

    def get_partner(self,obj):

        print("looking for [%s]'s partner" % obj.name)
        for p in self.couple:
            if p !=obj:   #即，如果i不是传入的obj本人，那么我们要返回这个人，因为这个人就是传入obj的partner
                return p
        else: #如果self.couple列表为空，表示没有soul mate，name打印下面内容
            print('you do not have soul mate')

    def break_up(self):

        print("[%s] and [%s] are broke up" % (self.couple[0].name,self.couple[1].name))
        self.couple.clear()  #清空couple列表表示两人分手
        #print(self.couple)


class Person2:
    def __init__(self, name, age, gender,relation):
        self.name = name
        self.age = age
        self.gender = gender
        self.relation = relation

relation_obj = Relationship1()
p1 = Person2('Mjj', 24, 'M',relation_obj)
p2 = Person2('Lyy', 21, 'F',relation_obj)
relation_obj.make_couple(p1, p2)

print(p1.relation)
"""<__main__.Relationship1 object at 0x000001687FB80100>
要在Relationship类里写一个get_my_partner,循环出来，
注意，p1和p2都有可能调用这个，所以，p1调用时候传出p2，反之亦然
"""
print(p1.relation.get_partner(p1).name)
"""return: Lyy"""


for i in relation_obj.couple:
    print(i.name)
"""
return:
    Mjj
    Lyy
"""


"""如果想要两个人分手，通过break_up"""
p1.relation.break_up()

p2.relation.get_partner(p2).name