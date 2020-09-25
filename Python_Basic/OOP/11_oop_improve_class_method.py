import time

"""
类方法通过@classmethod装饰器实现，，

类方法与普通方法的区别是：类方法只能访问类变量，不能访问实例变量 self.name = name这些都是实例变量
"""
#
# class Dog:
#
#     def __init__(self,name):
#         self.name = name
#     @classmethod
#     def eat(self):
#         print('dog %s is eating' % self.name)
#
# d = Dog('mjj')
# d.eat()
"""return: AttributeError: type object 'Dog' has no attribute 'name'"""
"""
eat变成类方法后就无法通过实例访问了
只能通过类变量访问
"""


class Dog:
    name = 'stupid_dog'
    def __init__(self,name):
        self.name = name


    # def eat(self):
    #     print(self)
    #     """<__main__.Dog object at 0x00000128C60EA790>"""  #打印出来的self是实例obj
    #     print('dog %s is eating' % self.name)

    @classmethod
    def eat(self):
        print(self)
        """<class '__main__.Dog'>"""  #打印出来的self是类本身，而不是实例对象。所以类方法传入的是类，这也就是为了如果你写先写@classmethod，方法的括号里显示的是cls。class的缩写
        print('dog %s is eating' % self.name)

    @classmethod
    def run(cls):
        print(cls)


d = Dog('mjj')
d.eat()

"""return: dog stupid_dog is eating"""
"""这个时候之所以能找出来是因为我们定义了类变量name = stupid_dog

d.eat找实例变量名字发现不符合要求的时候，他会自己取找类变量下的name"""

d.run()
"""<class '__main__.Dog'>"""




"""
类方法有什么用呢？


感觉没啥用。。。。。。
"""


"""
类方法案例：

比如我们有个student类，
每新建一个学生s(i)，count就加1，最后我们就打印student_number。
我们要的效果是，通过s(i).student_number 就能访问到当前学生总数。
"""

class Student:
    student_number = 0
    def __init__(self,name):
        self.name = name
        Student.student_number += 1
        print('new enroll student [%s],,,current student number [%s]' % (self.name,Student.student_number))
        print('total student number: ', Student.student_number)
s1 = Student('Simon')
s2 = Student('Paul')
s3 = Student('Dougan')
"""
return:
    new enroll student [Simon],,,current student number [1]
    total student number:  1
    new enroll student [Paul],,,current student number [2]
    total student number:  2
    new enroll student [Dougan],,,current student number [3]
    total student number:  3
"""

"""
但这种方法其实是有bud的，我从外部也可以修改student_number的数量：
"""
Student.student_number += 2
print(Student.student_number)
"""return: 5"""
"""但实际上我们只有3个学生。。"""
"""
如何解决这个问题呢

这时候就使用类方法，先把student_number变成私有属性，然后再通过类方法进行修改
"""


class Student1:
    __stu_number = 0
    def __init__(self,name):
        self.name = name
        #Student.stu_number += 1
        # print('new enroll student [%s],,,current student number [%s]' % (self.name,Student.student_number))
        # print('total student number: ', Student.student_number)
        self.add_stu()
    @classmethod
    def add_stu(cls):
        cls.__stu_number +=1
        print('new student enroll, total number:  ',cls.__stu_number)
s11 = Student1('jack')
s22 = Student1('synferlo')
s33 = Student1('adam')
"""
return:
    new student enroll, total number:   1
    new student enroll, total number:   2
    new student enroll, total number:   3
"""
"""现在这样虽然使用了类方法，但还是无法避免从外部修改数据。比如我可以从外部调用add_stu"""
Student1.add_stu()
"""new student enroll, total number:   4"""

"""
为了解决这个问题，我们可以在self.add_stu()中根据有没有生成新实例来判断是否加1
"""




class Student2:
    __stu_number = 0
    def __init__(self,name):
        self.name = name
        self.add_stu(self)


    @classmethod
    def add_stu(cls,obj): #这里的obj就是add_stu(self)中的self，代表实例
        if obj.name: #判断这个obj是否有name属性
            cls.__stu_number +=1
            print('new student enroll, total number:  ',cls.__stu_number)

s111 = Student2('jack')
s222 = Student2('synferlo')
s333 = Student2('adam')

#Student2.add_stu()
"""TypeError: add_stu() missing 1 required positional argument: 'obj'"""
"""这时候如果你再从外面调用，就会报错"""
"""
但其实，，是有bug的，你可以在括号里传s111他同样会计数
Student2.add_stu(s111)
"""