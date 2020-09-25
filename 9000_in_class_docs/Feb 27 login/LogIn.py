import os
import pandas as pd

import requests

if not os.path.exists("Login_html"):
    os.mkdir('Login_html')


"""
chrome选中preserve log

然后登陆密码随便输入：输入一个错误的，然后提交，在Network里面找到Basic

在General下找到：
Request URL: https://accounts.douban.com/j/mobile/login/basic

在requests header下面找到这个；
Referer: https://accounts.douban.com/passport/login_popup?login_source=anony
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36


在form data下面找到你的username和password对应的标题
ck: 
name: 156465
password: 561
remember: false

豆瓣用的是name和password
我们需要用这个去建立登陆信息的字典
"""

referer = 'https://accounts.douban.com/passport/login_popup?login_source=anony'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
headers = {'User-Agent':user_agent,
           'referer':referer}

#通过post上传信息需要session
session_douban = requests.session()

def log_in(usr_name, password):
    print('in process')
    url = 'https://accounts.douban.com/j/mobile/login/basic'
    #这里填入真实的用户名密码
    post_data = {
        'name':usr_name,
        'password':password
    }
    #通过post发送请求
    r = session_douban.post(url,post_data,headers = headers)
    print(r.status_code)
    #print(f'status_code = {r.status_code'})
    print(r.text)

#log_in('harry.yanhao@gmail.com','harry618')


df = pd.read_csv('douban_user_website_1000.csv')

for link in df['user_website']:
    #print (link)
    filename = link.replace('https://www.douban.com/people/','').replace('/','')
    print(filename)
    if not os.path.exists("user_information_html"):
        os.mkdir("user_information_html")
    if not os.path.exists('user_information_html/' + filename + '.html'):

        f = open('user_information_html/' + filename + '.html','w',encoding = 'utf-8')
        r = session_douban.get(link,headers = {'User-Agent':user_agent})
        print(r.status_code)
        r.encoding = r.apparent_encoding
        html = r.text
        print('downloading ' + filename)
        f.write(html)
        f.close()
