
import sys, os
import time, requests
import json

import urllib.request


#if not os.path.exists('json_files'):
#    os.mkdir('json_files')
#
#url = 'https://api.themoviedb.org/3/movie/550?api_key=bc2d1819d6e843ced94b1aadacbfe29e'
#
#
#r = requests.get(url)
#r.encoding = r.apparent_encoding
#html = r.text
#
#print(html)
#
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



#url = 'https://api.themoviedb.org/3/movie/550?api_key=bc2d1819d6e843ced94b1aadacbfe29e'
#res = urllib.request.urlopen(url)
#json_res = json.load(res)
#print(json_res['id'])


"""
api key
bc2d1819d6e843ced94b1aadacbfe29e

when you run the program, use command:
    python3.8 sep22.py bc2d1819d6e843ced94b1aadacbfe29e

place your api key after the file name!!
"""



#
#
#movie_id = '550'
#res = urllib.request.urlopen("https://api.themoviedb.org/3/movie/"+ movie_id+"?api_key=" + api_key)
#json_res = json.load(res)
#print(json_res)
#
#"""
#save <json_res> into a json file
#"""
#
#f = open("json_files/tmdb" + movie_id + ".json", "w")
#f.write(json.dumps(json_res))
#f.close()
#

api_key = sys.argv[1]


if not os.path.exists('json_files'):
    os.mkdir('json_files')


for i in range(550,555):
    
    movie_id = str(i)
    res = urllib.request.urlopen("https://api.themoviedb.org/3/movie/"+ movie_id+"?api_key=" + api_key)
    json_res = json.load(res)
    #print(json_res)
    
    f = open("json_files/tmdb" + movie_id + ".json", "w")
    f.write(json.dumps(json_res))
    f.close()
    


