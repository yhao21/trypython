from selenium import webdriver
import glob



f = open("tieba_pubg_html_file/selenium_pubg_page_number.html","w",encoding="utf-8-sig")

browser = webdriver.Chrome()
browser.get('https://tieba.baidu.com/f?kw=pubg&ie=utf-8&pn=0')
html = browser.page_source
f.write(html)
f.close()


for one_file in glob.glob("tieba_pubg_html_file/selenium_pubg_page_number.html"):
    f = open(one_file,"r",encoding="utf-8")
    for i in range(1,11):
        newf = open("tieba_pubg_html_file/pages/page # " + str(i) + ".html","w",encoding = "utf-8-sig")
        browser.get('https://tieba.baidu.com/f?kw=pubg&ie=utf-8&pn=' + str((i-1)*50))
        new_html = browser.page_source
        newf.write(new_html)
        newf.close()
        print('finishi downloading page #' + str(i))
    f.close()
    ##注意，一定要在结束后再关闭浏览器，否则会报错：invalid session id
    browser.close()
