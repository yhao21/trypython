from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
Chrome = webdriver.Chrome()
Chrome.get('https://www.baidu.com/')
"""
##如何命令浏览器按回车：Keys.RETURN
##也可以通过send_keys('coinmarketcap\n')完成按回车的操作
"""
Chrome.find_element_by_id('kw').send_keys('coinmarketcap',Keys.RETURN)
##一定要睡几秒等页面加载好才能拖动滚动条
time.sleep(5)
Chrome.execute_script('var q=document.documentElement.scrollTop=10000')
"""
拖动滚动条的方法：
js = 'var q = document.documentElement.scrollTop = 10000'
Chrome.execute_script(js)
"""