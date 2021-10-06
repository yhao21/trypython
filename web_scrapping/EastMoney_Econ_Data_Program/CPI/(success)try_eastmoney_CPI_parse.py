import glob
import pandas as pd
from bs4 import BeautifulSoup

df = pd.DataFrame()

for one_file in glob.glob("eastmoney_cpi_html_file/pages/*.html"):
    f = open(one_file, "r",encoding="utf-8")
    soup = BeautifulSoup (f.read(), "html.parser")
    for items in soup.find("div",class_="Content").find_next_sibling().find_all("tr"):
        try:
############当用tds变量定义td时，这些td就变成了列表形式，就可以按照顺序查找了，注意，这是处理表格数据的一个有效方法
            tds = items.find_all("td", style="width:;")
            ##全国数据
            ##月份
            month_count = tds[0].get_text().strip()
            ##当月值
            monthly_country = tds[1].get_text().strip()
            ##当月同比
            mon_YoY_country = tds[2].get_text().strip()
            ##当月环比
            mon_MoM_country = tds[3].get_text().strip()
            ##累计增长
            mon_cumulative_growth_country = tds[4].get_text().strip()
            ###城市数据开始
            ##当月值
            monthly_city = tds[5].get_text().strip()
            ##当月同比
            mon_YoY_city = tds[6].get_text().strip()
            ##当月环比
            mon_MoM_city = tds[7].get_text().strip()
            ##累计增长
            mon_cumulative_growth_city = tds[8].get_text().strip()
            ##农村数据开始
            ##当月值
            monthly_rural = tds[9].get_text().strip()
            ##当月同比
            mon_YoY_rural = tds[10].get_text().strip()
            ##当月环比
            mon_MoM_rural = tds[11].get_text().strip()
            ##累计增长
            mon_cumulative_growth_rural = tds[12].get_text().strip()
            df = df.append({
                "Month":month_count,
                "Monthly CPI(country)" : monthly_country,
                "Monthly CPI YoY(country)" : mon_YoY_country,
                "Monthly CPI MoM(country)" : mon_MoM_country,
                "Monthly CPI Cumulative Growth(country)" : mon_cumulative_growth_country,
                "Monthly CPI(city)" : monthly_city,
                "Monthly CPI YoY(city)" : mon_YoY_city,
                "Monthly CPI MoM(city)" : mon_MoM_city,
                "Monthly CPI Cumulative Growth(city)" : mon_cumulative_growth_city,
                "Monthly CPI(rural)" : monthly_rural,
                "Monthly CPI YoY(rural)" : mon_YoY_rural,
                "Monthly CPI MoM(rural)" : mon_MoM_rural,
                "Monthly CPI Cumulative Growth(rural)" : mon_cumulative_growth_rural
            },ignore_index=True)

        except:
            pass
print(df)
df.to_csv("eastmoney_cpi_html_file/China_CPI_Data.csv",encoding="utf-8-sig")
