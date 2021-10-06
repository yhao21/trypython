import requests
from bs4 import BeautifulSoup
import bs4

def get_html_text(url):
    try:
        r = requests.get (url)
        r.raise_for_status ()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fill_univlist (ulist, html):
    soup = BeautifulSoup (html, "html.parser")
    for tr in soup.fin ("tbody"):
        if isinstance (tr,bs4.element.Tag):
            tds = tr ("td")
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])

def print_univ_list (ulist, num):
    print ("{:^10}\t{:^10}\t{:^10}\t{:^10}".format ("Rank", "Univ. Name", "Regime","Score"))
    for i in range (num):
        u = ulist [i]
        print ("{:^10}\t{:^10}\t{:^10}\t{:^10}".format (u[0],u[1],u[2],u[3]))

def main ():
    uinfo = []
    url = "www.zuihaodaxue.com/Greater_China_Ranking2019_0.html"
    html = get_html_text(url)
    fill_univlist(uinfo, html)
    print_univ_list(uinfo,5000)







