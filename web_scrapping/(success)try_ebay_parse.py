import glob
from bs4 import BeautifulSoup
import pandas as pd


#"item name", "price", "shipping price", "item condition"
df = pd.DataFrame()

##在html_files_taobao文件夹中查找文件
for one_file_name_taobao in glob.glob ("html_files_taobao/*.html"):
    ##以只读方式打开文件夹中文件，转码为utf-8模式，注意，一定要转码！
    f = open(one_file_name_taobao, "r", encoding="utf-8")
    soup = BeautifulSoup(f.read(), "html.parser")
    ##解析完成后一定要关闭文档再进行下一步操作
    f.close()

    ##从标签中获取文本
    items_row = soup.find_all("div", class_="s-item__info clearfix")
    for item in items_row:
        item_name = item.find("a", class_="s-item__link").get_text()
        item_price = item.find("span", class_="s-item__price").get_text()
        item_condition = item.find ("span", class_="SECONDARY_INFO").get_text()
        df = df.append({
                "Product Name":item_name,
                "Product Price":item_price,
                "Product Condition":item_condition
        }, ignore_index=True)

print (df)
df.to_csv("html_files_taobao/ebay_video_card_data.csv")