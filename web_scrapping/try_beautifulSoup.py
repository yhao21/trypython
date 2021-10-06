# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.bilibili.com/video/av28951415?from=search&seid=12506065350425881349"
#
# r = requests.get(url)
# r_text = r.text
#
# soup = BeautifulSoup(r_text, "html.parser")
# ##查看第一个a标签
# a = soup.a
# print (a)


##查询a标签在bs4中的对象种类（tag，navigable string, beautifulsoup, comment)
# a_tage = soup.a
# print (type (a_tage))

##查询a标签下的href属性信息
# a_href = soup.a.attrs["href"]
# print (a_href)

##查看a标签的字符内容
# a_string = soup.a.string
# print (a_string)


##获取class为title所有a标签的title
# for string_content in soup.find_all ("a", class_="title"):
#     print (string_content.get("title"))

##获取class为title所有a标签的href属性
# for link in soup.find_all ("a", class_="title"):
#     print (link.get("href"))

##获取class为title所有a标签文本

# for string_content in soup.find_all ("a", class_="title"):
#     print (string_content.get_text())



page = "50"

print('downloading page #   '+page)


