import say_hi_module
"""
每一个.py文件都是一个module，每个module里面的函数就是一个功能，包含着多个.py文件的文件夹是一个package

比如requests模块就是个文件夹，里面有很多py文件，
导入模块的某个功能的方式：
import <package name>.<.py file name>.<def name>
或者
from <package name>.<.py file name> import <def name>


创建一个自己的模块并导入，其实就是写一个py文件，然后导入他，
之所以上面导入say_hi会有红线是因为我们没有把它存在python的package包，pycharm检测不到。
不过不影响我们使用


我们在say hi模块中写一个可以打印名字的函数，然后在现在这个文件里调用它
"""
my_name = 'John'
say_hi_module.hello(my_name)
"""return:  Hello John, welcome to SynFerLo's module!!"""
