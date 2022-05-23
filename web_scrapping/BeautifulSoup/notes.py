from bs4 import BeautifulSoup



'''
使用.contents可以找到一个标签下的所有子节点（不包含任何孙子节点）。返回值是一个list



with open('film_search_dir/捉妖记.html', 'r') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
data = soup.find('div',{'id':'root'}).contents[0]

这是找到<div id="root"> 标签下面的所有子节点，但不包含子节点下的孙子节点。所以返回的是一个list，里面有一个div







'''
