import glob
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()

for one_file in glob.glob("eastmoney_ppi_html_file/pages/*.html"):
    f = open (one_file, "r", encoding = "utf-8")
    soup = BeautifulSoup (f.read(),"html.parser")
    for items in soup.find_all("tr"):
        try:
            tds = items.find_all("td",style="width:;")
            ##全国数据
            ##月份
            month_count = tds[0].get_text().strip()
            ##当月值
            monthly_ppi = tds[1].get_text().strip()
            ##当月同比
            mon_YoY = tds[2].get_text().strip()
            ##当月累计
            mon_cumulative_growth = tds[3].get_text().strip()
            df = df.append({
                "Month":month_count,
                "Monthly PPI":monthly_ppi,
                "Monthly PPI YoY":mon_YoY,
                "Monthly PPI Cumulative Growth":mon_cumulative_growth
            },ignore_index=True)
        except:
            pass

print(df)
df.to_csv("eastmoney_ppi_html_file/China_PPI_Data.csv",encoding = "utf-8-sig")
