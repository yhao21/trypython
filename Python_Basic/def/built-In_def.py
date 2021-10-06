import time

'''"""
https://docs.python.org/3/library/functions.html?highlight=built#ascii

abs # 求绝对值 

all #Return True if bool(x) is True for all values x in the iterable.If the iterable is empty, return True.

any #Return True if bool(x) is True for any x in the iterable.If the iterable is empty, return False.

ascii #Return an ASCII-only representation of an object,ascii(“中国”) 返回”‘\u4e2d\u56fd’”

bin #返回整数的2进制格式 

bool # 判断一个数据结构是True or False, bool({}) 返回就是False, 因为是空dict

bytearray # 把byte变成 bytearray, 可修改的数组

bytes # bytes(“中国”,”gbk”) 

callable # 判断一个对象是否可调用 

chr # 返回一个数字对应的ascii字符 ， 比如chr(90)返回ascii里的’Z’
classmethod #面向对象时用，现在忽略

compile #py解释器自己用的东西，忽略

complex #求复数，一般人用不到

copyright #没用

credits #没用

delattr #面向对象时用，现在忽略

dict #生成一个空dict

dir #返回对象的可调用属性

divmod #返回除法的商和余数 ，比如divmod(4,2)，结果(2, 0) 

enumerate #返回列表的索引和元素，比如 d = [“alex”,”jack”]，enumerate(d)后，得到(0, ‘alex’) (1, ‘jack’)

eval #可以把字符串形式的list,dict,set,tuple,再转换成其原有的数据类型。 

exec #把字符串格式的代码，进行解义并执行，比如exec(“print(‘hellworld’)”)，会解义里面的字符串并执行

exit #退出程序

filter #对list、dict、set、tuple等可迭代对象进行过滤， filter(lambda x:x>10,[0,1,23,3,4,4,5,6,67,7])过滤出所有大于10的值

float #转成浮点

format #没用

frozenset #把一个集合变成不可修改的

getattr #面向对象时用，现在忽略

globals #打印全局作用域里的值 

hasattr #面向对象时用，现在忽略

hash #hash函数

help 

hex #返回一个10进制的16进制表示形式,hex(10) 返回’0xa’

id #查看对象内存地址

input 

int

isinstance #判断一个数据结构的类型，比如判断a是不是fronzenset, isinstance(a,frozenset) 返回 True or False

issubclass #面向对象时用，现在忽略

iter #把一个数据结构变成迭代器，讲了迭代器就明白了

len

list

locals

map # map(lambda x:x**2,[1,2,3,43,45,5,6,]) 输出 [1, 4, 9, 1849, 2025, 25, 36]

max # 求最大值 

memoryview # 一般人不用，忽略 

min # 求最小值 

next # 生成器会用到，现在忽略 

object #面向对象时用，现在忽略

oct # 返回10进制数的8进制表示

open 

ord # 返回ascii的字符对应的10进制数 ord(‘a’) 返回97，

print

property #面向对象时用，现在忽略

quit

range 

repr #没什么用

reversed # 可以把一个列表反转

round #可以把小数4舍5入成整数 ，round(10.15,1) 得10.2

set

setattr #面向对象时用，现在忽略

slice # 没用

sorted 

staticmethod #面向对象时用，现在忽略

str

sum #求和,a=[1, 4, 9, 1849, 2025, 25, 36],sum(a) 得3949

super #面向对象时用，现在忽略

tuple 

type 

vars #返回一个对象的属性，面向对象时就明白了

zip #可以把2个或多个列表拼成一个， a=[1, 4, 9, 1849, 2025, 25, 36]，b = [“a”,”b”,”c”,”d”]， """'''