import os
import requests

if not os.path.exists("retry_taobao_html_file"):
    os.mkdir("retry_taobao_html_file")

url = "https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E6%89%8B%E6%9C%BA%E5%A3%B3&suggest=0_1&_input_charset=utf-8&wq=shouji&suggest_query=shouji&source=suggest"
f = open ("retry_taobao_html_file/text" + ".html", "w", encoding="utf-8")
header = {
          "User-Agent":"Mozilla/5.0"
          "cookie": "_m_h5_tk=8e947aaa7e866bbd14603c6cea24d63c_1579855197017; _m_h5_tk_enc=a74849ea28b7429b5b1700958429a4be; t=921e4274a24a764d223d2b8a6fd359cc; _fbp=fb.1.1579845480329.37963207; enc=4B4MLaySYFN%2FVzBYvSVV509QqM6v2OeenfyE9GqUwAIQ%2BpmkUpGmHXAVtuxuK0JuYkCGIwtEglbIyTeTphW5Sg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; cookie2=5c1b2d929e7a4a5acbb381409ee8b725; _tb_token_=555e6df3b3953; alitrackid=www.taobao.com; _samesite_flag_=true; cna=ZHWxFhKgsTACAYlTNjuyYsds; v=0; unb=2207409279637; uc3=lg2=VT5L2FSpMGV7TQ%3D%3D&nk2=EEcL8GUoTXk%3D&vt3=F8dBxdrIENq%2FCXhfyPc%3D&id2=UUphzWMsM6wwH9YBkg%3D%3D; csg=9f7bc8bb; lgc=synferlo; cookie17=UUphzWMsM6wwH9YBkg%3D%3D; dnk=synferlo; skt=527be42a7b7fdf2d; existShop=MTU3OTg5ODM0Nw%3D%3D; uc4=id4=0%40U2grFnyR%2BoyKv7oxxBFsq2R8qzTyxzDy&nk4=0%40Ep546bE2uTdX71dj7zGP5gtgpA%3D%3D; tracknick=synferlo; _cc_=UtASsssmfA%3D%3D; tg=5; _l_g_=Ug%3D%3D; sg=o7b; _nk_=synferlo; cookie1=AC%2FIxoa4tr%2BUN8up2a8%2BEr1uJW8W8s7vA8xatHglhSg%3D; JSESSIONID=2F270ECB3E41A284E524AD51ECFAFE9F; lastalitrackid=login.taobao.com; isg=BA4O1WyS3FJBMGh376O8n--fX-TQj9KJDeO0DThXepHMm671oB8imbRZ19_3mMqh; l=cBgom227QrBPNMSEBOCanurza77OSIRYYuPzaNbMi_5QR6T6KGbOoc4U8F96VAWd978B4Tn8Nrv9-etkZacSYa--g3fP.; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=U%2BGCWk%2F7oPIg&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTblA85bvTYsA%3D%3D&tag=8&lng=zh_CN; mt=ci=0_1
referer: https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fs.taobao.com%2Fsearch%3Finitiative_id%3Dtbindexz_20170306%26ie%3Dutf8%26spm%3Da21bo.2017.201856-taobao-item.2%26sourceId%3Dtb.index%26search_type%3Ditem%26ssid%3Ds5-e%26commend%3Dall%26imgfile%3D%26q%3D%25E6%2589%258B%25E6%259C%25BA%25E5%25A3%25B3%26suggest%3D0_1%26_input_charset%3Dutf-8%26wq%3Dshouji%26suggest_query%3Dshouji%26source%3Dsuggest"
}
r = requests.get(url, headers = header)
r.encoding = r.apparent_encoding
html = r.text
f.write(html)
f.close()