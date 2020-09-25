import time
"""
高级玩法：

在会员账号上再追加一个vip等级，只有vip等级大于10的用户才能够看到完整的欧美专区，否则只能看基础班欧美专区

"""
data_base = {'is_log_in':False,
             'user name':'synferlo',
             'password':'harry618'}

def log_in_system(func):
    """"
    想达到只有US专区需要上传vip等级，而其他专区不需要的效果，我们需要在inner函数里添加 “非固定参数”
    """
    def inner(*args,**kwarges):
        if data_base['is_log_in'] == False:
            user_name = input('user name: ')
            pass_word = input('password: ')
            if user_name == data_base['user name'] and pass_word == data_base['password']:
                print('Success! Welcome to Membership Section')
                data_base['is_log_in'] = True
                func(*args,**kwarges)
            else:
                print('User name or password is not matched. Please try again')
        else:
            print('log in request has been approved')
            func(*args,**kwarges)
    return inner


def home_page():
    print("""
    --------------------Home Page------------------
        this is the home page of this website

        End


        """)


def US_EU(vip_level):
    if vip_level > 10:
        print("""
    -----------------US and EU Section--------------
            welcome to US and EU PREMIUM section

        End


        """)
    else:
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
US_EU = log_in_system(US_EU)
JP_KO = log_in_system(JP_KO)

US_EU(15)
JP_KO()

"""
user name: synferlo
password: harry618
Success! Welcome to Membership Section

    -----------------US and EU Section--------------
            welcome to US and EU PREMIUM section

        End


        
log in request has been approved

     -----------------JP and KO Section--------------
             welcome to JP and KO Membership section

         End
"""