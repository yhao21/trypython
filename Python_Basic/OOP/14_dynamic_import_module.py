import time

"""
动态加载模块：

想要达到的目的：
    正常我们导入模块使用的是 import + <module name>
    现在我想通过一个import后加入字符串，然后这个字符串映射一个module名字的方式达成动态加载模块的方式

"""

"""方法一：通过__import__("<module name>")的方式，即系统自带方法完成模块导入"""
__import__("reflection_target_module")
"""return: This is reflection_targe_module"""


"""方法二：官方推荐： importlib 模块"""
import importlib


importlib.import_module('reflection_target_module')
"""return: This is reflection_targe_module"""

"""如果我想调用其他文件夹（包）中的某个模块的办呢？比如我想导入list文件夹下的create_a_list"""
"""需要先把对应文件的路径找出来，然后在找对应的包"""
importlib.import_module('D:\Yan\PHD PROGRAM\Class\Spring 2020\Econ 9000 Machine learning\Try_pycharm_\Python_Basic\list.create_a_list')


import os

b = os.path.abspath('d')
print(b)


"""
a #文件夹
	│a.py
	│__init__.py
b #文件夹
	│b.py
	│__init__.py
	├─c#文件夹
		│c.py
		│__init__.py

# c.py 中内容
args = {'a':1}

class C:
    
    def c(self):
        pass
————————————————
版权声明：本文为CSDN博主「edward_zcl」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/edward_zcl/article/details/88809212



import importlib

params = importlib.import_module('b.c.c') #绝对导入
params_ = importlib.import_module('.c.c',package='b') #相对导入

# 对象中取出需要的对象
params.args #取出变量
params.C  #取出class C
params.C.c  #取出class C 中的c 方法
————————————————
版权声明：本文为CSDN博主「edward_zcl」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/edward_zcl/article/details/88809212

"""