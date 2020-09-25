import json

"""
json与pickle功能相同

但是pickle只能在python用，但是支持所有数据类型，如，class的object对象,def function, datetime,,,,
而json可以在任何语言使用，但是只支持：str,int,dict,set,list,tuple


另外json占用内存空间很小

比如你用python写，但是其他同事用java写，那你们对接工作的时候就用json对接，你写完以后通过json序列化
"""


d = {
    'player':'synferlo',
    'hp':100,
    'weapon':"mk-47"
}

a = json.dumps(d)
print(a)
"""{"player": "synferlo", "hp": 100, "weapon": "mk-47"}"""
"""注意，json.dumps后虽然看起来还是字典形式，其实他是字符串"""
"""而pickle.dumps是转换成16进制模式"""

f = open('json_try.json','w')
json.dump(d,f)
g = open('json_try.json','r')
h = json.load(g)

print(h)
"""{'player': 'synferlo', 'hp': 100, 'weapon': 'mk-47'}"""
"""注意，json只能dump，或者load一次，所以在load之前确保注释掉上面所有dump和load"""

