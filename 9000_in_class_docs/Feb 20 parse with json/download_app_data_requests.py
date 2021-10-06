import requests
from selenium import webdriver


driver = webdriver.Chrome()
url = 'https://sensortower.com/ios/rankings/top/iphone/us/all-categories?data=2020-02-01&date=2020-02-01'
driver.get(url)
html = driver.page_source

f = open('test_tower.html','w',encoding = 'utf-8')
f.write(html)
f.close()

driver.close()



"""url = https://sensortower.com/"""

"""Tom's Method

find XHR, and copy url = "https://sensortower.com/api/ios/rankings/get_category_rankings?category=0&country=US&date=2020-02-01T00%3A00%3A00.000Z&device=IPHONE&limit=50&offset=0"

"""


url = 'https://sensortower.com/api/ios/rankings/get_category_rankings?category=0&country=US&date=2020-02-01T00%3A00%3A00.000Z&device=IPHONE&limit=50&offset=0'
r = requests.get(url)
f = open('tower.json','w',encoding='utf-8')
f.write(r.text)
r.close()

