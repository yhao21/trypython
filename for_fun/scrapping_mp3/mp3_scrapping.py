import requests

# url = 'http://94.191.88.231/mp3/2017/02/Five.mp3'
# headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
#
# r = requests.get(url, headers = headers)
# html = r.content
#
# with open('my_music.mp3', 'wb') as f:
#     f.write(html)





url = 'https://www.youtube.com/b09ab19b-e87c-4d85-b48f-54f5a33bcbc2'
headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

r = requests.get(url, headers = headers)
html = r.content

with open('my_music.mp4', 'wb') as f:
    f.write(html)