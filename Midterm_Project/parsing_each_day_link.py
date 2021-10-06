import pandas as pd
from bs4 import BeautifulSoup
import glob,os


def parsing_each_day_link():

    assert str(os.listdir('box_office_pages')) != '[]', \
        "You should download each year's page first!\n\nCheck if you have run [ web_scrapping.py ]"

    link_data = pd.DataFrame()

    for one_file in glob.glob('box_office_pages/*.html'):
        f = open(one_file,'r',encoding = 'utf-8')
        html = f.read()
        soup = BeautifulSoup(html,'html.parser')
        tds = soup.find_all('td', class_='a-text-left mojo-header-column mojo-truncate mojo-field-type-date_interval mojo-sort-column')
        for item in tds:
            date_link = item.find('a').get('href')
            full_link = 'https://www.boxofficemojo.com/' + date_link
            date = item.find('a').get_text()
            link_data = link_data.append({
                'Dates':date,
                'Links':full_link
            },ignore_index = True)

    order = ['Dates','Links']
    link_data = link_data[order]
    print(link_data)
    link_data.to_csv('date_links.csv')


if __name__ == "__main__":

    parsing_each_day_link()