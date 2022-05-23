
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS



options = webdriver.ChromeOptions()
#url = 'https://account.dianping.com/pclogin'
ua = 'Mozilla/5.0 (Windows NT 10.0 WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
options.add_argument(f'user-agent={ua}')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)

########################################################################
# 去掉window.navigator.webdriver字段，防止被检测出是使用selenium       
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {      
  "source": """                                                        
    Object.defineProperty(navigator, 'webdriver', {                    
      get: () => undefined                                             
    })                                                                 
  """                                                                  
})                                                                     
########################################################################

def login():
    """
    登录函数
    """
    login_url = 'https://account.dianping.com/login?redir=http%3A%2F%2Fwww.dianping.com%2F'
    driver.get(login_url)   # 打开登录页面，手动扫码登录

    while True:
        try:
            #driver.find_element_by_class_name('login-container')  # 还能找到"请登录"
            driver.find_element_by_class_name('login-box')  # 还能找到"请登录"

            sleep(2)
        except:
            #driver.find_element_by_class_name('countDown')  # 登录成功
            break

    print('登录成功')


def fetch_shoplist(page_num=1):
    """
    获取美食分区下的店铺信息
    """
    city = 'guangzhou'
    food_shop_url = f'http://www.dianping.com/{city}/ch10'  # /p1~
    shop_info = []
    for i in range(1, page_num+1):
        driver.get(food_shop_url+f'/p{i}')
        soup = BS(driver.page_source, 'lxml')
        page_shop = soup.find_all('div', class_='txt')
        for shop in page_shop:
            shop_info.append({
                'shopid': shop.a['data-shopid'],
                'name': shop.a.text.strip(),
                'score': shop.find('div', class_='nebula_star').text.strip()
            })
    return shop_info


def fetch_comment(shopid='H7fXoNAkafmesfFG', page=1):
    """
    爬取指定店铺下的用户评论
    :param shopid: 店铺ID
    :param page: 页码
    :return: 解析后的评论信息
    """
    url = f'http://www.dianping.com/shop/{shopid}/review_all'
    if page != 1:
        url += f'/p{page}'
    driver.get(url)
    soup = BS(driver.page_source, 'lxml')
    comments = soup.find_all('div', class_='main-review')
    comment_list = []
    for item in comments:   # 遍历所有评论
        username = item.find('div', class_='dper-info').text.strip()
        items = item.find_all('span', class_='item')     # 各项评分
        detail_score = []
        for _item in items:
            detail_score.append(_item.text.strip())
        content = item.find('div', class_='review-words').text.strip()  # 获取到的评论不全，做了CSS加密
        comment_list.append({'username': username, 'item': detail_score, 'content': content})
    return comment_list


if __name__ == '__main__':
    login()
    shop_info = fetch_shoplist()
    print(shop_info)
    for _ in shop_info:
        print(_)
    shopid = shop_info[2]['shopid']     # 这里也可以用for来遍历，但要适当加延时
    comment_list = fetch_comment(shopid=shopid, page=1)
    # print(comment_list)
    for _ in comment_list:
        print(_)
    driver.quit()


