import glob
import pandas as pd
from bs4 import BeautifulSoup


df = pd.DataFrame()
df1 = pd.DataFrame()
df2 = pd.DataFrame()




for one_file in glob.glob("steam_html_file/*.html"):
    f = open(one_file, "r", encoding= "utf-8")
    soup = BeautifulSoup(f.read(),"html.parser")
    items = soup.find("div", id = "search_result_container")
    for item in items.find_all("a"):
        try:
        ###因价格修改统一标签下存在多个子标签，打乱整体标签排列结构。
            price_change = item.find("div",class_="col search_price discounted responsive_secondrow")
            if not price_change:
                ###价格无变动的游戏的价格
                original_price = item.find("div", class_="col search_price_discount_combined responsive_secondrow").get_text().strip()
            else:
                ###注意，如果发现有价格变动时，虽然不去，但是也要输出空值占位置，为后面合并数据做准备！
                original_price = ""
            df1 = df1.append({
                "3.price": original_price
            }, ignore_index=True)

            if price_change:
                ##价格有变动的游戏现在的价格
                changed_price = price_change.get_text().strip()
            else:
                changed_price = ""
            df2 = df2.append({
                "3.price":changed_price
            },ignore_index=True)
                # print(changed_price)
        ###价格信息提取完成
        ######？？？待寻找如何将变动后价格拼接到没有价格变动的那一列中，查寻方向：合并多个df时如何填补同一列中的空缺值

            name = item.find("div", class_="col search_name ellipsis").find("span").get_text().strip()
            release_time = item.find("div", class_="col search_released responsive_secondrow").get_text().strip()
            df = df.append({
                "1.name": name,
                "2.release_time":release_time,
            },ignore_index=True)

        except:
            pass
df = pd.concat()
# df = df.join(df2)
print (df)


####

