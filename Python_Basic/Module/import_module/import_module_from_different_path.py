import sys

print(sys.path)

"""
['D:\\Yan\\PHD PROGRAM\\Class\\Spring 2020\\Econ 9000 Machine learning\\Try_pycharm_\\Python_Basic\\Module', 
'D:\\Yan\\PHD PROGRAM\\Class\\Spring 2020\\Econ 9000 Machine learning\\Try_pycharm_', 
'D:\\Python\\python38.zip', 
'D:\\Python\\DLLs', 
'D:\\Python\\lib', 
'D:\\Python', 
'D:\\Yan\\PHD PROGRAM\\Class\\Spring 2020\\Econ 9000 Machine learning\\Try_pycharm_\\venv', 
'D:\\Yan\\PHD PROGRAM\\Class\\Spring 2020\\Econ 9000 Machine learning\\Try_pycharm_\\venv\\lib\\site-packages', 
'D:\\Python\\lib\\site-packages', 
'D:\\Python\\lib\\site-packages\\win32', 
'D:\\Python\\lib\\site-packages\\win32\\lib', 
'D:\\Python\\lib\\site-packages\\Pythonwin']

"""
"""
通过sys.path打印出来的这些路径是运行python时，当你想调用模块时，系统会去查找的路径。如果你调用的模块在其中任何一个模块下，都可以成功导入

但是注意了：

如果不用pycharm，你会发现打印出来的第一个路径是''，即，空路径
['', 
'D:\\Yan\\PHD PROGRAM\\Class\\Spring 2020\\Econ 9000 Machine learning\\Try_pycharm_', 
'D:\\Python\\python38.zip', 。。。。


之所以pycharm里显示除了当前文件的路径，
因为pycharm自己程序会帮助你把你当前文件所在的目录自动添加到这个sys.path

但是当你是用其他python编辑器的时候，不一定会把你的路径放到sys.path里面，

所以，
为了在任何时候都能够调用自己写的模块，你可以吧自己写的模块放到：
site-packages这个目录下，
这个目录是专门用来存放你下载的第三方库的
"""