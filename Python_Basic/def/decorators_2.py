import time

''"""
添加会员，我们要先模拟一个会员库，比如有一个会员名字叫synferlo，密码是harry618
如果不通过装饰器，为了避免大规模修改源代码的函数，我们只能通过修改函数调用方式（即高阶函数）的方法达到效果。
也就是说，我们将一个函数作为参数传入到另一个函数中
"""''
"""
方法：
在log_in_system()函数中嵌套一个inner函数，然后return inner，这样整个log_in_system不会返回US，JP函数的结果，而是把inner函数执行后的内存地址返回
然后我们把它赋值给一个变量，在通过这个变量名+()的方式调用inner函数，通过闭包完成不修改源代码和调用方式的完成代码扩展
我们把一个函数的名字赋给一个变量，然后再调用这个变量就相当于调用这个函数：


在不改变源代码和调用方式前提下，把函数名赋值给新变量，然后再调用，这就是“函数装饰器”

又或者，你不想在后面添加：
US_EU = log_in_system(US_EU)
JP_KO = log_in_system(JP_KO)

则可以再想要装饰的函数上面添加   @log_in_system   来达到相同的效果，这就是装饰器的语法。
"""




data_base = {'is_log_in':False,
             'user name':'synferlo',
             'password':'harry618'}

def log_in_system(func):
        ##对字典内变量值得判断用方括号，后面加is或者==
    def inner():
        if data_base['is_log_in'] == False:
            user_name = input('user name: ')
            pass_word = input('password: ')
            if user_name == data_base['user name'] and pass_word == data_base['password']:
                print('Success! Welcome to Membership Section')
                data_base['is_log_in'] = True
                func()
            else:
                print('User name or password is not matched. Please try again')
        else:
            print('log in request has been approved')
            func()
    return inner
"""
添加了return inner后，后面US_EU = log_in_system(US_EU)返回的是inner的内存地址，而不是执行inner，即之前学的闭包现象
当我们真正想要调用inner的时候，需要执行US_EU() （即，代码原本的调用方式
这样我们在不修改原本调用方式和源代码的情况下完成了扩展代码的任务！！"""

def home_page():
    print("""
    --------------------Home Page------------------
        this is the home page of this website

        End


        """)


def US_EU():
    print("""
    -----------------US and EU Section--------------
            welcome to US and EU Membership section

        End


        """)


def JP_KO():
    print("""
     -----------------JP and KO Section--------------
             welcome to JP and KO Membership section

         End


         """)


def domestic():
    print("""
     -----------------Domestic Section--------------
             welcome to Domestic section

         End


         """)


home_page()
domestic()
"""##注意这里一定不能载US_EU和JP_KO后面加括号，加括号表示要启动这个函数，而我们这里是以索引，只是用他们的名字赋值"""
US_EU = log_in_system(US_EU)
JP_KO = log_in_system(JP_KO)

US_EU()
JP_KO()



"""
通过 @log_in_system 达成装饰器效果：
装饰器可以添加多个：执行时候从上到下执行：
@pay_money
@vip_level
@log_in_system
....
"""
data_base = {'is_log_in':False,
             'user name':'synferlo',
             'password':'harry618'}

def log_in_system(func):
        ##对字典内变量值得判断用方括号，后面加is或者==
    def inner():
        if data_base['is_log_in'] == False:
            user_name = input('user name: ')
            pass_word = input('password: ')
            if user_name == data_base['user name'] and pass_word == data_base['password']:
                print('Success! Welcome to Membership Section')
                data_base['is_log_in'] = True
                func()
            else:
                print('User name or password is not matched. Please try again')
        else:
            print('log in request has been approved')
            func()
    return inner
"""
添加了return inner后，后面US_EU = log_in_system(US_EU)返回的是inner的内存地址，而不是执行inner，即之前学的闭包现象
当我们真正想要调用inner的时候，需要执行US_EU() （即，代码原本的调用方式
这样我们在不修改原本调用方式和源代码的情况下完成了扩展代码的任务！！"""

def home_page():
    print("""
    --------------------Home Page------------------
        this is the home page of this website

        End


        """)

@log_in_system
def US_EU():
    print("""
    -----------------US and EU Section--------------
            welcome to US and EU Membership section

        End


        """)

@log_in_system
def JP_KO():
    print("""
     -----------------JP and KO Section--------------
             welcome to JP and KO Membership section

         End


         """)


def domestic():
    print("""
     -----------------Domestic Section--------------
             welcome to Domestic section

         End


         """)


home_page()
domestic()
US_EU()
JP_KO()