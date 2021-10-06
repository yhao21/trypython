




def registration (name,age,education,major,country='CN'):
    data = """
    -------------------info--------------------
    name    : %s
    age     : %s
    edu     : %s
    major   : %s
    country : %s
    """%(name,age,education,major,country)
    print(data)

registration('Adam',25,'PhD','Econ')

"""
def registration (name,age,education,major):
括号里的参数是位置参数，告诉你调用函数的时候，如果不做任何变量声明，第一个传入的是name，第二个是age。。。。

如果在写入参数时候不想按顺序传入，则需要声明对应关系（即，关键参数，形式：name = Adam）

默认参数是函数默认显示的，如果用户不传入该参数，则显示为默认值，上面例子里没有输入country信息，函数会自动显示CN
如果要修改默认参数，可以调用函数时手动传入

另外，参数优先级是：位置参数》关键参数


"""

def registration (name,age,education,major,country='CN'):
    data = """
    -------------------info--------------------
    name    : %s
    age     : %s
    edu     : %s
    major   : %s
    country : %s
    """%(name,age,education,major,country)
    print(data)

registration(education = 'PhD', age = 25, name = 'Adam', major = 'Econ',country = 'JP')
"""
通过使用关键参数，无视位置参数
并通过手动调整country信息，修改默认参数
"""