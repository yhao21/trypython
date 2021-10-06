import sys, os
import time, requests
import json

import urllib.request


if not os.path.exists('json_files'):
    os.mkdir('json_files')

url = 'https://api.themoviedb.org/3/movie/550?api_key=bc2d1819d6e843ced94b1aadacbfe29e'


r = requests.get(url)
r.encoding = r.apparent_encoding
html = r.text

print(html)

#
#api_key = sys.argv[1]
#print(api_key)
#
#
#res = urllib.request.urlopen('https://api.themoviedb.org/3/movie/550?api_key=bc2d1819d6e843ced94b1aadacbfe29e')
#
#json_res = json.load(res)
#print(json_res)
#

"""
 when you run .py in terminal, use:
 python3.8 <file>.py bc2d1819d6e843ced94b1aadacbfe29e   then, you do
 not neet to write api key into your code. hence, others cannot
 get your key.
"""
#
#res = urllib.request.urlopen('https://api.themoviedb.org/3/movie/550?api_key=' + api_key)
#
#json_res = json.load(res)
#print(json_res)
#





