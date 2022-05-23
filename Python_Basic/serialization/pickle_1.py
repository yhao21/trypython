import time

"""
序列化是讲字典里的信息转换成16进制的字符串，然后可以被存入文件中


import pickle

序列化需要用：pickle.dumps()执行
反序列化(即，从文件中提取字符串并重新整理成字典模式）：pickle.loads()

"""
import pickle

d = {
    'player':'synferlo',
    'hp':100,
    'weapon':"mk-47"
}

d_dump = pickle.dumps(d)
print(d_dump)
"""b'\x80\x04\x951\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x06player\x94\x8c\x08synferlo\x94\x8c\x02hp\x94Kd\x8c\x06weapon\x94\x8c\x05mk-47\x94u.'"""
a = pickle.loads(d_dump)
print(a)
"""{'player': 'synferlo', 'hp': 100, 'weapon': 'mk-47'}"""



"""保存序列化结果到文档  .pkl文档"""
f = open('text.pkl','wb')
pickle.dump(d,f)
"""也可以用 f.write()都可以，只不过用pickle.dump写一行就够了"""
"""注意保存时候使用'wb' 格式，即，二进制格式"""





"""保存于提取"""

d = {
    'player':'synferlo',
    'hp':100,
    'weapon':"mk-47"
}

e = {
    'synferlo','culiu','sanxian'
}

f = open('info.pkl','wb')
f.write(pickle.dumps(d))
f.write(pickle.dumps(e))
f.close()
##为什么用pickle.dump写入文件虽然写成功过了但是无法通过load加载
# pickle.dump(d,f)
# pickle.dump(e,f)


"""注意我这里dump了两次，分别把两个字典存入文件中"""
g = open('info.pkl','rb')
print(pickle.load(g))
print(pickle.load(g))

"""
如果你在写入文件的时候dumps了两次，则在加载文件时候也需要load两次，
如果只load一次，则只显示第一次dumps进去的内容
当然，如果你只dumps两次但是你load次数大于二，程序会报错
"""


"""扩展内容：pickle对datetime的保存"""
import datetime
a = pickle.dumps(datetime.datetime.now())
print(a)
#"""""b"\x80\x04\x95*\x00\x00\x00\x00\x00\x00\x00\x8c\x08datetime\x94\x8c\x08datetime\x94\x93\x94C\n\x07\xe4\x02\x11\x13'\x1b\x00,\xc1\x94\x85\x94R\x94.""""""
print(pickle.loads(a))
"""2020-02-17 19:41:49.452139"""
