import time


"""
如何通过反射，查找  一个.py文件中是否有某一个方法或者变量呢？

如果直接hasattr('xx.py','obj_name'),文件名会被当做一个字符串处理，而不是对应的文件

这里想要达成效果，需要使用 __name__



"""

print(__name__)
"""return: __main__"""

"""
在当前文件下，__name__ == __main__
但是当你在其他文件import这个.py文件时，这个__name__ == 这个文件的文件名

如：你在13_reflection_'__name__'_practice.py 中import 13_reflection_2，这个时候，13_reflection_2中的print(__name__)打印出来的就是“13_reflection_2”

所以，这就是为什么大家在写一些主函数后会加入这个判断条件：
    if __name__ == '__main__':
        main()
        
意思就是，只有当__name__输出的是__main__时候才执行主函数。
也就是说，只有在当前文件夹下才能运行主函数。所以，当你从其他文件调用这个文件时，他是不会运行main函数的，因为当你调用的时候__name__ 等于被调用文件的文件名




所以利用这一点我们可以完成我们当时hasattr想要得到的效果

利用sys先查看我们当前文件（module）的main对应的是什么
"""
import sys

# for k,v in sys.modules.items():
#     print(k,v)

"""
...
encodings.utf_8 <module 'encodings.utf_8' from 'D:\\Python\\lib\\encodings\\utf_8.py'>
_signal <module '_signal' (built-in)>
__main__ <module '__main__' from 'D:/Yan/PHD PROGRAM/Class/Spring 2020/Econ 9000 Machine learning/Try_pycharm_/Python_Basic/OOP/13_reflection_2.py'>
.......


这里返回了一大堆，其中有一个就是：__main__ <module '__main__' from 'D:...">
尖括号中的内容其实就是main代表的module，__main__只是一个代名词。就像self是各个对象名的代名词一样

那这时候我们需要先把main这个名字取出来

"""
print(sys.modules['__main__'])  #这里main以字符串形式出现，是因为，返回的结果中，main是字符串中的一部分
"""<module '__main__' from 'D:/Yan/PHD PROGRAM/Class/Spring 2020/Econ 9000 Machine learning/Try_pycharm_/Python_Basic/OOP/13_reflection_2.py'>"""
print(sys.modules[__name__])  #这里name是个变量，因为在当前文件调用，所以这个变量对应的就是main这个字符串
"""<module '__main__' from 'D:/Yan/PHD PROGRAM/Class/Spring 2020/Econ 9000 Machine learning/Try_pycharm_/Python_Basic/OOP/13_reflection_2.py'>"""

"""这两种方法都可以取出main的值"""




class Person():
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name, " is walking....")

p = Person('Synferlo',29)

mod = sys.modules['__main__']
print(mod.p)
"""<__main__.Person object at 0x00000154F315A790>"""
"""验证成功：可通过mod.p返回对象"""

if hasattr(mod,'p'):
    a = getattr(mod,'p')
    print (a.name)
    """return: Synferlo"""

"""通过反射，拿到了这个文件中的p对象的name"""

"""接下来，，，我们在13_test中尝试一下跨模块获取"""

"""即，动态导入模块"""

#
#
#