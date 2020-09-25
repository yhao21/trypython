from selenium import webdriver
import time
"""
某些网站点击链接后并不是在原来的窗口加载内容，而是新建了一个选项卡进行加载
国内很多网站都是这样子的

那么如果不让selenium切换到新窗口就执行后面的代码，返回的是空值

这就是为什么要学习如何切换新窗口的原因


使用 switch_to.window(handle) 方法
handle是每个标签页独有的属性
如何找到handle呢

通过window_handles查看所有标签页的handles，
依次switch到每一个handles，找到标签页的标题栏里面存在的字符，如“Bing搜索”
找到后跳出循环，执行后面的代码

"""
Chrome = webdriver.Chrome()
Chrome.get('http://www.baidu.com/')
Chrome.find_element_by_id('kw').send_keys('coinmarketcap\n')
Chrome.find_element_by_tag_name('a').click()
for handle in Chrome.window_handles:
    Chrome.switch_to.window(handle)
    if "All Cryptocurrencies" in Chrome.title:
        break
"""
后续代码执行
"""


