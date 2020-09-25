import hashlib


"""#创建md5，并将一个字符串交给md5进行加密"""
#m = hashlib.md5()
#m.update('hi synferlo')

"""调用加密后的字符串"""
#print(m.digest())

"""return: TypeError: Unicode-objects must be encoded before hashing"""
"""因为字符串是unicode，但hash只支持bytes类型，所以要先转码"""

m = hashlib.md5()
m.update(b'hello alex')
print(m.digest())

"""return: b'\xa3\xe3\xbb]v\x11I:j\x12\x00\xafP\x8f\xbc\x0f'
这是个bytes类型不好阅读，所以我们将达转为16进制"""

print(m.hexdigest())

"""return: a3e3bb5d7611493a6a1200af508fbc0f"""
"""注意，md5不管在那台机器上运行，只要输入的字符串是相同的，返回的hash value也一定是相同的！"""


"""那如果我们要对中文进行加密怎么办呢？需要先转码"""
m.update('你好hash'.encode('utf-8'))
print(m.hexdigest())

"""return: 981bada8f9c359d1bfc3361c10691d52"""


"""在同一md5下连续执行多次，其实系统会把他们拼接到一起一次性输出一个hash value"""
#连续多次执行：
m2 = hashlib.md5()
m2.update(b"hello hash")
m2.update("你好 哈希".encode('utf-8'))
print(m2.hexdigest())
"""return: d382ed616cbe6e570555c5c2ed67e89d"""



m3 = hashlib.md5()
m3.update("hello hash你好 哈希".encode('utf-8'))
print(m3.hexdigest())
"""return: d382ed616cbe6e570555c5c2ed67e89d"""

"""注意，在验证这个结论的时候一定要创建两个md5,,i.e. m2 and m3"""
"""如果你同时在m2下验证相当于你把三个字符串拼接到了一起，这就是为什么返回值不同的原因。
一定要注意，，避免这个错误！！"""


