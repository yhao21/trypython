from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
url = "https://login.taobao.com/member/login.jhtml?spm=a21wu.241046-global.754894437.1.41cab6cbFTRIiM&f=top&redirectURL=https%3A%2F%2Fworld.taobao.com%2F"

chrome = webdriver.Chrome()
chrome.get(url)
chrome.find_element_by_id("TPL_username_1").send_keys("synferlo")
chrome.find_element_by_id("TPL_password_1").send_keys("harry618")
chrome.find_element_by_class_name("J_Submit").click()
time.sleep(5)


source = chrome.find_element_by_id("nc_1_n1z")
time.sleep(3)
ActionChains(chrome).drag_and_drop_by_offset(souce,256,2).perform()
time.sleep(2)
###无法拖动滑块

