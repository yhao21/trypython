from bs4 import BeautifulSoup
import pandas as pd
import glob

df = pd.DataFrame()

for html_file in glob.glob("thriftbooks/*.html"):
    f = open (html_file, "r", encoding="utf-8")
    soup = BeautifulSoup (f.read(), "html.parser")
    books = soup.find_all ("div", class_="AllEditionsItem-tile Recipe-default")
    print (books)
