import hashlib

"""
接下来介绍一个比md5更牛逼的加密算法：SHA-1

SHA-1：Secure Hash Algorithm

主要适用于数字签名标准(Digital Signature Standard DSS)里定义的数字签名算法(Digital Signature Algorithm DSA)
但是2005年被山东大学教授 王小云破解了，
所以后续推出了SHA224,256,384,512四个版本,加密位数越多，耗时越大
目前流行的是256，，https就是基于SHA-256

原本网站是通过ssl，，后来进化到ssl2，就是SHA-256



SHA-1对于长度小于2^64位的消息生成的是160位的 value




"""
s1 = hashlib.sha1()
s1.update(b'hi hash')
print(s1.hexdigest())
"""return: e0602fab293bd62be7c313c045ec383d8c306060
通过16进制返回的40位，我们知道16进制是每四位数转换成一个字符，所以验证：，SHA生成的是160位"""


s2 = hashlib.sha256()
s2.update(b'hi hash')
print(s2.hexdigest())
"""return: 607fc72e456ab42e9a8fc9f14744b01ca1f4792ca1447ea9e569bb180b145b4e"""

s3 = hashlib.sha512()
s3.update(b'hi hash')
print(s3.hexdigest())
"""0eeaa76aa3c3976e1440894667668cb4f4b893e2888520efcb18d039384a8805bc2033e4ab60c5f1ce8c9fdc53968acf27791d63d1f5a779f06da337ed989b0b"""

