import time
"""
作为专业的程序员，
在修改或开发新程序时，需要之到一个基本守则：开放-封闭守则

封闭：别人已经写好并正常运行的代码禁止修改（包括已经写好的函数调用方式也不可以修改）

开放：可以扩展引用已经写好的程序

"""

"""
-----------------例子-------------------------
一个视频网站，分为四个模块：
    1. 首页
    2. 欧美专区
    3. 日韩专区
    4. 国内专区

现在需要给欧美和日韩区添加一个账号登录系统，只有付费会员才能有账号
不登录只能看首页和国内专区，只有登录的人才能看欧美+日韩
"""
"""
源代码（无登录系统）
"""
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
US_EU()
JP_KO()
domestic()




