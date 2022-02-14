'''
login---receive cookie---request url with cookie---download contents

We can do this with "Session", which provides a series of request without lossing cookie. 



'''



import requests








'''
Method one:

inspect--network, then log in, and go to the page you need. For example,

login to coingecko, then click on "portfolio".

Use preview to check if the page is want you want, then

find "portfolio" under Network, click on "Headers"

copy "Request URL" (under General), and "cookie" (under Request Headers)

Form headers below, then use requests.get

'''
# login



headers = {"cookie": "_gid=GA1.2.1785069683.1643398076; __gads=ID=205983994dc3e503:T=1643398077:S=ALNI_MY2Wo5U9EXM8P-yl7lNOUZGa5vU4w; cf_chl_2=75d3b50693e1273; cf_chl_prog=x13; cf_clearance=v8.ZrXA0AjcPM9.7Nkpa8x_bmOqd1F2ucASVzChmeJM-1643398151-0-250; _session_id=baacbd00b05b2b0b3d88e33c2736ed52; _ga=GA1.2.780908369.1643398075; __cf_bm=DL3knOBfpCjCvdUCFiWWXmdRUGzUW030g1tGMGOPYM8-1643400397-0-AXPL3n9xyXe/jJJECoxbPiF65Eqy+gyYVX9GMOfXz68Hlp+hnMGpSbjX9ks9WCeNVzifZpVnuleurP1hq0SOZeU=; _ga_LJR3232ZPB=GS1.1.1643398075.1.1.1643400400.0"}

url = 'https://www.coingecko.com/en/portfolio'
r = requests.get(url, headers = headers)
print(r.status_code)




with open("portfolio_page.html", 'w', encoding = 'utf-8') as f:
    f.write(r.text)







# download contents

