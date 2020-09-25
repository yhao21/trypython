import requests
from bs4 import BeautifulSoup

url = "http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=pubg&step_word=&hs=0&pn=1&spn=0&di=158290&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=3752152307%2C1004735981&os=1589180208%2C130798169&simid=3261407827%2C2941143625&adpicid=0&lpn=0&ln=1422&fr=&fmq=1579736531251_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fp0.ifengimg.com%2Fpmop%2F2018%2F0620%2F23009D6D98137604B6275D9BD9146D5980C18543_size67_w600_h368.jpeg&fromurl=ippr_z2C%24qAzdH3FAzdH3Foj4j1tw_z%26e3Btujg2_z%26e3Bv54AzdH3Fmc0bl0baAzdH3Foj4j1tw_z%26e3Bfip4s&gsm=&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"

def get_html_text (url):
    try:
        r = requests.get (url)
        r.raise_for_status ()
        r.encoding = r.apparent_encoding
        return (r.text)
    except:
        print ("there is an error.")


def download_pic (pic, html)
    soup = BeautifulSoup (r.text, html."parser")
    







