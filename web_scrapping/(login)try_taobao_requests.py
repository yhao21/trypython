from selenium import webdriver
import os

driver = webdriver.Chrome()
driver.get ("https://login.taobao.com/member/login.jhtml?spm=a21wu.241046-us.754894437.1.cc7bb6cb0KRhxv&f=top&redirectURL=https%3A%2F%2Fworld.taobao.com%2F%3Fspm%3Da2107.1.1000340.1.23c811d98YiqIQ")
driver.find_element_by_id("TPL_username_1").send_keys("synferlo")
driver.find_element_by_id("TPL_password_1").send_keys("harry618")



####！！！出现下载html问题：即使手动登录后仍无法获取全部html，必须模拟登陆####
# import os
# import requests
#
# if not os.path.exists("html_files_req_taobao"):
#     os.mkdir("html_files_req_taobao")
#
# url = "https://s.taobao.com/search?q=iphone&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306"
# f = open ("html_files_req_taobao/taobao" + ".html", "w", encoding="utf-8")
# r = requests.get (url)
# r.encoding = r.apparent_encoding
# html = r.text
# f.write(html)
# f.close()



