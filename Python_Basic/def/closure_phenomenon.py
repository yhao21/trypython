

def outer():
    name = 'adam'

    def inner():
        print('his name is ',name)
    return inner

outer()

"""
函数在执行完后会释放里面所有变量，即全部删除
所以直接调用outer()没有任何反馈

但如果我们把outer赋值给一个变量，通过这个变量调用，则可以：
相当于把inner函数赋值给了外部变量fun，只要fun存在，则可以在outer函数外调用inner函数
这就是闭包现象（enclosure phenomenon）
"""

def outer():
    name = 'adam'

    def inner():
        print('his name is ',name)
    return inner

outer()
fun = outer()
fun()
"""
return:
    his name is  adam
"""