import re
import glob
import requests

kv = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

for one_file in glob.glob("tieba_pubg_html_file/*.html"):
    f = open(one_file, "r",encoding="utf-8")
    #re找到最后一页的url页码
    result = re.compile(r'pn=(.*?)" class="last pagination-item " >尾页</a>').findall(f.read())
    #将页码从列表中取出
    total_page = int(result[0])
    #计算一共多少页
    x = int((total_page/50) + 1)
    #取每一页的url并requests  html页面文本
    for page in range (1, 10+1):
        full_url = "https://tieba.baidu.com/f?kw=pubg&ie=utf-8&pn=" + str((page-1)*50)
        f = open("tieba_pubg_html_file/pages/page #" + str(page) + ".html", "w", encoding="utf-8")
        r = requests.get(full_url,headers = kv)
        html = r.text
        f.write(html)
        f.close()
        print("finish downloading page # " + str(page) + "...")