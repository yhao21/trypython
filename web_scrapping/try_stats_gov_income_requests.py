import requests
import os
from selenium import webdriver

if not os.path.exists("stats_gov_html_file"):
    os.mkdir("stats_gov_html_file")
f = open("stats_gov_html_file/text.html","w",encoding="utf-8-sig")
browser = webdriver.Chrome()
url = "http://data.stats.gov.cn/easyquery.htm?cn=C01"
browser.get(url)
browser.find_element_by_id("treeZhiBiao_5_span")
browser.find_element_by_id("treeZhiBiao_33_span")

html = browser.page_source

f.write(html)
f.close()