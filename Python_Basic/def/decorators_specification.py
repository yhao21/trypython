import time



"""
首先说一下闭包，

闭包需要满足三个条件：
1. 函数内嵌套一个内部函数
2. 内部函数调用了外部函数的变量
3. 外部函数返回内部函数的结果

def outter():
    name = 'Harry'

    def inner():
        print('hello' + name)

    return inner


a = outter()
a()



注意, a = outter()，这里是吧outter返回的值赋值给了a，也就是把inner函数赋值给了a

所以如果没有后面的a()去调用，系统是不会执行inner函数的，终端不会打印任何东西 （因为没有调用函数）


"""


# def name(fun):
#     def greeting():
#         fun()
#         print('harry')
#     return greeting
#
# @ name
# def hello():
#     print('hello')
#
# hello()
#


"""
装饰器：
比如我们有两个函数，一个负责打印hello，一个负责打印good bye
现在我想让他们两个在打印内容后面加上我的名字： hello harry, good bye harry

有两种方法，
一种是直接在原来的hello和good_bye函数上修改打印内容
另一种就是通过写一个装饰器函数，然后每次执行hello和good_bye的时候都通过装饰器函数把我的名字加上


如何做到这一点呢？

首先需要写一个装饰器函数，这个函数需要传入一个参数，这个参数就是我们要进行修饰加工的目标函数，即hello和good_bye

然后在这个装饰器函数name内部， 我们要嵌套一个加工函数，他负责把我的名字添加到两个输入函数所输出的结果后面

最后，装饰器函数name返回这个内部的加工函数


def name(function):
    def add_my_name():
        input_fun_string = function()
        my_name = 'Harry'
        greeting = input_fun_string + my_name

        print(greeting)

    return add_my_name

@ name
def hello():
    content = 'hello '
    return content

@ name
def good_bye():
    content = 'good bye '
    return content


hello()
good_bye()



当你调用hello()的时候，程序会将hello传入@后的装饰器函数中，
然后他们会执行name函数，name返回的是add_my_name，所以当你执行hello的时候相当于执行的是add_my_name()

也就是将hello的返回值'hello'赋值给input_fun_string,
而后将input_fun_string 和 my_name拼接，并赋值给greeting

最后打印greeting

所以，最后调用hello()输出的是： hello Harry

同理，调用good_bye()输出的是： good bye Harry


"""


# def name(function):
#     def add_my_name():
#         input_fun_string = function()
#         my_name = 'Harry'
#         greeting = input_fun_string + my_name
#
#         print(greeting)
#
#     return add_my_name
#
# @ name
# def hello():
#     content = 'hello '
#     return content
#
# @ name
# def good_bye():
#     content = 'good bye '
#     return content
#
#
# hello()
# good_bye()






"""

再举个例子，
比如我想计算一下一个函数的运行时间

需要计算时间的函数是wtf()

装饰器函数是time_count，他会计算wtf这个函数运行了多久


这次我们不把时间直接打印出来，而是通过返回值得方式把它赋值给变量a
然后我们通过打印变量a来查看wtf这个函数运行的时间


def time_count(function):
    def time_what():
        st = time.time()
        function()
        et = time.time()
        total_time = et - st
        return total_time

    return time_what

@time_count
def wtf():
    b = 0
    for i in range(100000):
        b += 1

    print(b)


a = wtf()
print(a)




注意，因为我们装饰器里的函数time_what这次不再是打印total_time，而是直接返回total_time这个变量
所以，我们必须要现将wtf赋值给一个变量a，然后再打印这个变量a才能看到total_time的值
如果我们不print(a)，
即，只有 a = wtf()
程序是这样执行的：
1. 将wtf传入time_count
2. 执行time_what, 
    2.1 记录开始时间st
    2.2 function()调用了传入的函数wtf，此时wtf被执行，输出100000
    2.3 记录wtf运行的时间
    2.4 计算et - st并赋值给total_time
    2.5 返回total_time
3. 将返回的total_time赋值给变量a
程序执行完毕

所以，如果我们不print(a), 其实我们所做的只是给a赋值了，
要想查看a的值，也就是total_time，必须要打印他才可以




"""















