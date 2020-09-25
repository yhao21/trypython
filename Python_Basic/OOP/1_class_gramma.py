import time

"""
1. 类名使用驼峰体
2. d_type 是类属性，say_hi是类方法
3. 在类内部调用类属性要用self.+属性名
4. 在类外部调用类方法：对象名+类方法，如d.say_hi

"""

class Dog():
    d_type = '京巴' #类属性，即公共属性，是大家共享的，只有大家共有的属性才可以放在这里

    def say_hi(self):
        print('hi, my type is ',self.d_type)

d = Dog()
d2 = Dog()


d.say_hi()      #hi, my type is  京巴
d2.say_hi()     #hi, my type is  京巴

Dog.d_type = '金毛'
d.say_hi()      #hi, my type is  金毛
d2.say_hi()     #hi, my type is  金毛


"""
修改类属性后，修改之前的对象打印的还是原来的属性
我们将type改为金毛后，第一次打印d.sayhi()还是京巴，因为此时还没有修改type属性
"""