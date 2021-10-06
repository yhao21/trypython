from selenium import webdriver





driver = webdriver.Chrome()
driver.get('https://coinmarketcap.com/')
html = driver.page_source
with open('coinmarketcap.html','w',encoding = 'utf-8') as f:
    f.write(html)
driver.close()
