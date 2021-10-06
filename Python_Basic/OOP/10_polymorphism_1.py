import time
"""
类的多态：polymorphism

举个简单例子说明什么是多态：

比如：猪，狗，猫，蛇都继承了Animal这个父类，这个父类下有一个方法叫eat

虽然这四种动物都会Eat，但是他们四个吃的方法却不一样：蛇是靠吞的，狗是靠啃的

这就是一个接口，多种形态


再比如，，同样都是button，调用方法都是onClick()
但是按钮可以使方形、圆形

这两个对象都是用同一个接口onClick()
这就叫多态 polymorphism
"""
"""
代码例子：

猫和狗都会叫（sound），但一个是汪汪汪，一个是喵喵喵，
我们通过同一个接口(make_sound)调用它们 
"""


class Dog:
    def sound(self):
        print('汪汪汪')

class Cat:
    def sound(self):
        print('喵喵喵')

def make_sound(animal_type):
    animal_type.sound()

d1 = Dog()
c1 = Cat()

make_sound(d1)
"""汪汪汪"""
make_sound(c1)
"""喵喵喵"""

"""
recall:
之所以make_sound可以调用sound方法，是因为你生成实例d1时候，d1可以调用Dog下的sound
所以你调用的时候：
make_sound(d1) == d1.sound
即通过实例自己调用实例所属类的方法
"""


"""
不过一般我们不通过函数来完成多态，，一般是通过：  抽象类完成！
"""