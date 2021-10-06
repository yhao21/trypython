import time

"""
效果：

假设：网站中有注册（sign up），登陆（sign in），找回密码（forget my password）三个选项，
你希望通过程序完成：用户输入那个一要求，就进入到哪一个界面
"""

"""通过反射，动态加载完成效果："""

class User:

    def sign_in(self):

        user_name = input('Please input your username: ').strip()
        input('Please input your password: ')
        print('Welcome back, ',user_name)

    def sign_up(self):
        up_name = input('Please input your new username: ').strip()
        first_password = input('Please input your password: ').strip()
        second_password = input('Please input your password: ').strip()
        if first_password == second_password:
            print('Hi %s, welcome to our BWF family!' % up_name)
        else:
            print('your password does not match...so sad....')

    def forget_password(self):
        print('come on.....')


receive = input('Make your choice: sign in/sign up/reset password: ').strip().replace(' ','_')
if hasattr(User,receive):
   command = getattr(User,receive)
   command(1)
else:
    print('command not found')



