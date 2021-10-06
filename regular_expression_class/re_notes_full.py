import re
"""
###search方法：朝招符合正则表达式的内容

##准备正则表达式,python中使用r方式写
    ## pattern = "baidu"
    # #所以，要写成r模式的正则

pattern = r"baidu"

##准备查找的字符串
url = "http://www.baidu.com"

##匹配操作
    ##匹配不到返回None
result = re.search(pattern,url)
print(result)
    ##返回：<re.Match object; span=(11, 16), match='baidu'>
    ##11,16表示“baidu这个字符串在url中的位置是第11到第16个字符，
    
    
转义字符：
\d  表示0-9中任意一个数字 d for digit
\D  表示除了0-9以外的任意一个字符
\s  表示任意一个空白字符 s for space
\S  表示除了空白字符以外的任意一个字符
\w  表示0-9，a-z,A-Z和_中的任意一个字符
\W  表示除了0-9,a-z,A-Z和_以外的任意一个字符
.   表示除了换行\n以外的任意一个字符
"""

###原子测试：
##准备正则表达式
# pattern = r"\d+"

##准备查找的字符串
# url = "2664564315"

##匹配操作
##search是用来查找符合的第一个字符
# result = re.search(pattern,url)
# print(result)
"""
返回：None，原因，如果用r"\d"在url中查找，他会逐一判断url中的每一个字符是不是0~9的数字，若不是，则返回none
但如果我们在url中加入一个数字2
返回：<re.Match object; span=(14, 15), match='2'>
若pattern=r"\D"即，查找除了0~9以外的字符，则第一个h就被找到
url被改为13254564（全是数字）则用\D返回的就是None，因为url全是数字
但如果在url=13254*564，用\D就能找到*
url = 13254 564,\D可以查找出空格。
\s可以查找到所有不可见字符
url = "15364564\t315"
    <re.Match object; span=(8, 9), match='\t'>
url = "15364564\n315"
    <re.Match object; span=(8, 9), match='\n'>
\w表示找到0~9，a~z,A~Z,_，，，，
url = "15364564315"
    <re.Match object; span=(0, 1), match='1'>
url = "\ 2664564315"
    <re.Match object; span=(2, 3), match='2'>
\W是小w的所有非集
url = "+2664564315"
    <re.Match object; span=(0, 1), match='+'>
. 表示任意字符
拓展：
r"\d+"表示找到第一个数字后，取它本身和后面所有数字
url = "2664564315"
    <re.Match object; span=(0, 10), match='2664564315'>
"""

"""
元字符：(原子修饰符)
需用[]  自定义原子列表

"""
##准备re
# pattern = r'[^ \n\r\t\f\v]'
# ##re查找的字符串
# url = "我喜欢2个姑你娘的2只纤纤玉手"

##匹配操作
# result = re.search(pattern,url)
# print(result)
"""
###需要0-9中奇数组成的原子：1,3,5,7,9
url = "我喜欢21个姑娘的2只纤纤玉手"
如果只用\d的话，就只能取到2
我们用pattern = r"[13579]"表示取一个1或者一个3或者一个5或者一个7.。。
[]只能取一个
如：
url = "我喜欢2个姑你娘的2只纤纤玉手"
pattern = r'[135你79]'
    <re.Match object; span=(6, 7), match='你'>
所以通过[]自定义原子列表可以翻译表示转义字符，比如：
\d = [0123456789]
\s = [\n\r\t\v\f]
\w = [a-zA-Z0-9_]
注意，如果多个字符在ascii码中是连续的，可以进行缩写，比如：
a-z表示从a到z，0-9表示从0到9
pattern = r'[123456789]'
url = "我喜欢2个姑你娘的2只纤纤玉手"
    <re.Match object; span=(3, 4), match='2'>
如果我们把pattern改成这样：
pattern = r'[1-9]'
    <re.Match object; span=(3, 4), match='2'>
结果一样的

\D如何改写为自定义[]呢：
###[^]自定义排除列表:
    表示原子列表之外任意的一个字符
比如：
r'[^ \n\r\t\f\v]'=\S表示取空白以外的所有字符中的一个
\s = \n\r\t\f\v
pattern = r'[^ \n\r\t\f\v]'
url = "我喜欢2个姑你娘的2只纤纤玉手"
    <re.Match object; span=(0, 1), match='我'>
    
    

google的网址可以写成：
www.google.com
www.gogle.com
www.gooogle.com

如何通过正则匹配以上三种网址：
需要用到：与数量相关的元字符：

固定数量：
+：表示一个或者无限个被修饰的原子
?：表示一个或者零个被修饰的原子
*：表示任意个修饰的原子（就是+与?功能的组合）
不固定数量：(自定义数量）
{m}，
{m,n}
{m,}
{,n}

~~~ ?的含义：表示?前面的字符出现一次或不出现均可匹配到（即，问号前面的字符有没有都不会影响匹配）
例子：
pattern = r"go?gle"
url = "www.ggle.com"
    <re.Match object; span=(4, 8), match='ggle'>
url = "www.gogle.com"
    <re.Match object; span=(4, 9), match='gogle'>
即，用r"go?gle"可以匹配到gogle和ggle


~~~ +的含义：表示+前面的字符可以连续出现无数个
例子：
pattern = r"go+gle"
url = "www.gooooogle.com
    <re.Match object; span=(4, 13), match='gooooogle'>
"www.google.com"
    <re.Match object; span=(4, 10), match='google'>

~~~ *的含义:加号前面的字符不论有没有，或者有多少个，都能匹配到
例子：
pattern = r"go*gle"
url = "www.goooooooogle.com"
    <re.Match object; span=(4, 16), match='goooooooogle'>
url = "www.ggle.com"
    <re.Match object; span=(4, 8), match='ggle'>


~~~{m,n}表示被修饰的原子只能出现m~n次
例子：
pattern = r"go{2,5}gle"  表示“o”出现2~5次的这类字符串均可被匹配到
url = "www.gooogle.com"
    <re.Match object; span=(4, 11), match='gooogle'>
url = "www.google.com"
    <re.Match object; span=(4, 10), match='google'>
~~~{m}表示被修饰的只能出现m次才能被匹配到
例子：
pattern = r"go{2}gle"
url = "www.google.com"
    <re.Match object; span=(4, 10), match='google'>
url = "www.gogle.com"
    None

~~~{m,}表示被修饰的原子出现的次数大于等于m均可被匹配到
pattern = r"go{2,}gle
url = "www.goooooogle.com"
    <re.Match object; span=(4, 14), match='goooooogle'>

~~~{,n}表示被修饰的原子出现的次数小于等于n次时可以被匹配到
pattern = r"go{,3}gle"
url = "www.ggle.com"
    <re.Match object; span=(4, 8), match='ggle'>
url = "www.gooogle.com"
    <re.Match object; span=(4, 11), match='gooogle'>
url = "www.goooogle.com"
    None




####限定开头结尾的元字符：(都只能找到第一个符合要求的字符串）
\A:表示限定内容必须在整个字符串的开头部位
\Z:表示限定内容个必须在整个字符串的结束为止
^:与\A的功能相同
$:与\Z的功能相同
^和$ 与\A and \Z不同的是，在result=re.search(pattern,url,re.M)中，加入re.M
则$与^可以在一行字符串中识别换行符号并认为换行符号后的内容是新的一行。
此时，即便在一行字符串的开头没有找到对象，但如果字符串中出现换行符，且换行符后出现要查找的字符串，则该字符串可被找到


\A 修饰的字符串必须在要搜索的字符串的开头
例子：
pattern = r"\Ahttp"
url = "http://www.google.com"
    <re.Match object; span=(0, 4), match='http'>
pattern = r"\Ahttp"
url = "://www.http.google.com"
    None
即使是http前面有空格也不可能匹配到

\Z
例子：
pattern = r"http\Z"
url = "www..google.com.http"
    <re.Match object; span=(16, 20), match='http'>
pattern = r"http\Z"
url = "www..google.com.httpdfa"
    None
    
$
例子：
pattern = r"http$"
url = "www..google.com.http"
    <re.Match object; span=(16, 20), match='http'>
    
^
例子：
pattern = r"^http"
url = "www..google.com.http"
    None
    
^和$ 与\A and \Z不同的是，在result=re.search(pattern,url,re.M)中，加入re.M
则$与^可以在一行字符串中识别换行符号并认为换行符号后的内容是新的一行。
此时，即便在一行字符串的开头没有找到对象，但如果字符串中出现换行符，且换行符后出现要查找的字符串，则该字符串可被找到
但A与Z无法完成

这就是多行模式中的查找：
多行模式：如果字符串中包含\n字符，则可以使用多行匹配模式，
就是将每一行当做独立的字符串匹配
^ 与 $支持多行匹配
但是A与Z不存在多行匹配

￥￥￥￥注意，多行模式必须使用模式修正符

pattern = r"^http"
url = "ww\nhttpw..google.com."
    <re.Match object; span=(3, 7), match='http'>
pattern = r"ww$"
url = "ww\nht123tpw..google.com."
    <re.Match object; span=(0, 2), match='ww'>
    
$$$模式修正符：
词边界
\b：表示需要查找的内容前面必须是一个单词分割符号：所有可以将单词分开的符号都可以，这包含了各种标点符号
    即，除了要搜索的词条前面不可以有字母、汉字（re中汉字作为字母处理）和数字与其连接
    
例子:
pattern = r"\bgood"
url = "python is a dfadf'good tool"
    <re.Match object; span=(18, 22), match='good'>
url = "python is a dfadf.good tool"
    <re.Match object; span=(18, 22), match='good'>
url = "python is a df123good tool"
    None
url = "python is a df123我good adfad,goodtool"
    这时找到的就是第二个good
    <re.Match object; span=(29, 33), match='good'>

若只想找到good这个单词，而不是以good作为一部分的单词的话，就在good前后都加上\b
pattern = r"\bgood\b"
url = "python is a df123我good adfad,goodtool good sdfadf"
    <re.Match object; span=(38, 42), match='good'>


\B: \b的非集，表示以不能当做英文单词分割的字符查找目标字符串，
比如，目标字符串紧跟在一串连续的英文字母或者数字后
例子：
\B可以查找在某一个单词或数字串中的一段字母, 即，隐藏在一串连续单词或数字中的字符串
pattern = r"\Binter"
url = " kjinternet is a df123我good adfad,goodtool inter sdfadf"
    <re.Match object; span=(3, 8), match='inter'>
url = "1564internet is a df123我good adfad,goodtool inter sdfadf"
    <re.Match object; span=(4, 9), match='inter'>
pattern = r"inter\B"
url = "1564internet is a df123我good adfad,goodtool inter sdfadf"
    <re.Match object; span=(4, 9), match='inter'>


%%%%   “|” 表示选择关系，|左右完整内容二选一，
如果|前后的内容是相连的，先找前面的，
如果先出现了|后面的内容紧接着出现了|前面的内容，则会匹配到|后面的内容
pattern = r"ab|cd"
url = "我喜欢的字母是abcd"
    <re.Match object; span=(7, 9), match='ab'>
url = "我喜欢的字母是cd"
    <re.Match object; span=(7, 9), match='cd'>
url = "我喜欢的字母是cdab"
    <re.Match object; span=(7, 9), match='cd'>
    
    
￥￥￥￥   "()" 第一个作用表示：改变正则表达式中的优先级关系
表示先完成括号里边的二选一


pattern = r"b|cd"
url = "我喜欢的字母是abcd"
    <re.Match object; span=(8, 9), match='b'>
pattern = r"(b|c)d"
url = "我喜欢的字母是abcd"
    <re.Match object; span=(9, 11), match='cd'>
pattern = r"a(b|c)"
url = url = "我喜欢的字母是abcd"
    <re.Match object; span=(7, 9), match='ab'>
下面之所以找不到是因为，系统会找abd或者acd，
pattern = r"a(b|c)d"
url = "我喜欢的字母是abcd"
    None
pattern = r"a(b|c)d"
url = "我喜欢的字母是acd"
    <re.Match object; span=(7, 10), match='acd'>


$$$  ()的第二个作用：将括号内内容看做一个整体

比如：
想要查找go无限重复：
若用go+gle，则只能找到goooooogle类似的字符
若想找到：gogogogogogle这种go重复的，就需要使用（）

pattern = r"(go)+"
url = "gogogogle.com"
    <re.Match object; span=(0, 6), match='gogogo'>
pattern = r"(go)?"
url = "gle.com"
    <re.Match object; span=(0, 0), match=''>



￥￥￥ ()的第三个作用：将匹配的内容当做模式单元进行存储




###模式修整符
设定匹配的一些额外规则，用在re.search()之类的函数中，作为参数

常用的
re.A：表示re.ASCII，在ascii模式下进行re匹配，注意ascii只支持数字字母和符号，无中文日文之类的
re.U：默认值，输不输都一样，表示re.UNICODE，在unicode模式下进行re匹配
re.S：是“.”可以匹配任何字符，包含\n
re.M或写成re.MULTLINE
re.X: 表示要搜索的re中的字符串的空格可以被忽略
re.I：表示忽略re中要查找字符串的大小写

re.A
例子：
pattern = r"\w+"
url = "我你sdfa哈打的费difan"
result = re.findall(pattern,url,re.A)
    ['sdfa', 'difan']
&&&&注意，用findall返回的是一个列表

re.U
例子：
result = re.findall(pattern,url,re.U)
    ['我你sdfa哈打的费difan']
result = re.findall(pattern,url)
    ['我你sdfa哈打的费difan']
    
re.S
注意“.”是可以找到任何原子的，除了\n
加入re.S后，\n被视为一个字符
例子：
pattern = r"."
url = "我\n你sdfa哈打的费difan"
result = re.findall(pattern,url,re.S)
    ['我', '\n', '你', 's', 'd', 'f', 'a', '哈', '打', '的', '费', 'd', 'i', 'f', 'a', 'n']
result = re.findall(pattern,url)
    ['我', '你', 's', 'd', 'f', 'a', '哈', '打', '的', '费', 'd', 'i', 'f', 'a', 'n']
    
re.M
表示支持多行搜索
例子：
pattern = r"good"
url = "good\ngood dfafd \ngood nadsfa"
result = re.findall(pattern,url,re.M)
    ['good', 'good', 'good']
    
pattern = r"^good"
url = "good\ngood dfafd \ngood nadsfagood"
result = re.findall(pattern,url,re.M)
    ['good', 'good', 'good']
    
    
re.X
例子：
pattern = r"good good"
表示，字符串中的good good或者goodgood都可以被找到
url = "goodgood dfafd good nadsfagood"
result = re.findall(pattern,url,re.X)
    ['goodgood']
result = re.findall(pattern,url)
    若不加re.X则找不到good good
    []


re.I
表示忽略re中要查找字符串的大小写
例子：
pattern = r"Good"
若不加re.I则匹配不到任何内容
url = "goodgood dfafd good nadsfagood"
result = re.findall(pattern,url)
    []
result = re.findall(pattern,url, re.I)
    ['good', 'good', 'good', 'good']
    
    
    
@@@@转义字符的应用和python扩展正则语法
@@@@转移字符的应用
\n换行
\r回车
\t缩进
等等


如何去掉转义字符的含义呢，比如我只想找到\n而不是让他表示换行
又或者，我只想找到.而不是.在正则中的含义（表示任何字符除了\n)

例子：
pattern = r"www.google.com"
url = "wwwlgooglepcom"
    ['wwwlgooglepcom']
如果在re中，将.前面加上\则去掉了.在re中所代表的的含义
也就是说，我只找www.google.com这个字符串，任何将.替换为其他字符的字符串都不可能被找到
pattern = r"www\.google\.com"
url = "wwwlgooglepcom"
    []
url = "www.google.com"
    ['www.google.com']



\取消中括号的意义
[]表示取[]中的任意一个
如果在re中[]前面不加\：
pattern = r"[google]"
url = "www.google.com[google]"
    ['g', 'o', 'o', 'g', 'l', 'e', 'o', 'g', 'o', 'o', 'g', 'l', 'e']
    匹配到google中的每一个字母
但如果我们只想匹配包括[]在内的这个字符串：“[google]”
则需要在re中在[]前面加上\

pattern = r"\[google]"
url = "www.google.com[google]"
    ['[google]']



{{{}}}}}  正则的扩展语法；：：只在python中存在的re语法

1. (?limsux) 模式修正符的应用：即，在括号中加入模式修饰符之类的，
    注意模式修正符除了在re.search中作为参数，也可以直接使用
    
2. (?:) 取消对该模式单元的存储，只启用括号的前两个作用
3. (?P<name>)命名并存储模式单元
4. (?P=name) 注意是大写P，，，，调用模式单元
5. (?#)re注释
6. (?=) 正向先行断言 （0宽断言）
7. (?!) 负向先行断言 （0宽断言）
8 (?<=) 正向后行断言 （0宽断言)
9. (?<!) 负向后行断言 （0宽断言
10. (?(id/内容)Y|N)



####  1.(?limsux) 多种模式修正符的同时应用！！！！！！
pattern = r"baidu"
url = "www.baidu.com"
    ['baidu']
    
但如果我把url中的百度按大小写书写呢？
url = "BaiDu.com"
    则匹配不到

那么，除了在findall函数中将re.I作为参数，来达到忽视大小写外，如何在pattern进行此类操作呢，如下
pattern = r"(?i)baidu"
url = "www.BaiDu.com"
    ['BaiDu']
    
注意，可以将多个模式修正符放在括号中
如：忽视大小写与多行模式并行
pattern = r"(?im)baidu"
url = "www.BaiDu.\nbaiDucom"
    ['BaiDu', 'baiDu']

如：忽略大小写与空格
pattern = r"(?ix)bai du
url = "www.BaiDu.\nbaiDucom"
    ['BaiDu', 'baiDu']
    


#####   2. (?:)  ： 取消单元存储功能
涉及到()的第三个作用：将匹配的内容当做模式单元进行存储

我们将result定义为代表匹配结果的变量（结果对象）
我们现在打印一下这个结果对象中的存储模式单元
pattern = r"baidu"
url = www.baidu.com"
result = re.search(pattern,url)
print (result)
print (result.groups())
    <re.Match object; span=(4, 9), match='baidu'>
    ()
返回()表示没有任何东西被存储下来，

如果我们在du上加入括号:表示将括号中的内容当做模式单元处理，就是：把他存起来
pattern = r"bai(du)
url = "www.baidu.com"
print (result.groups())
    ('du',)
此时，du被python存储起来了
pattern = r"(bai)(du)"
    ('bai', 'du')
    
然而，当我们在搜索字符串时想把某一段字符串当做一个整体进行搜索时，()在进行定义整体的同时，也顺便把这段字符串存储起来了
虽然并无大碍，但是会占用空间资源
比如：我们想将du看做整体，找到du无限循环的字符串
那么我们会在pattern中的du外边加上括号和加号：
pattern = r"(du)+"
url = "www.baidudududududu.com"
然而，我们发现，python在找到我们要的字符串同时，还把du给存储起来了
    <re.Match object; span=(7, 19), match='dudududududu'>
    ('du',)

我们并不希望存储du，那么，只需要在括号内加上?:
pattern = r"(?:du)+"
url = "www.baidudududududu.com"
print(result)
print (result.groups())
    <re.Match object; span=(7, 19), match='dudududududu'>
    ()
    
此时，re就不会存储了




##### 3. (?P<name>)  自定义模式单元的名称
recall，在pattern 的搜索此外加上()即可存储该模式单元：pattern = r"bai(du)"

正常模式单元的使用：
html文件中各种标签中间有字符串，如果我们直接尝试将html中的标签和字符串以re的方式表达出来进行查找，：
比如我们想匹配str中的“<title>百度</title>”，
str = "<title>百度</title><body>www.baidu.com</body>"
直观来想，我们需要下面的re表达式：
pattern = r"<[a-z]+>.*</[a-z]+>"
但返回的是：<re.Match object; span=(0, 43), match='<title>百度</title><body>www.baidu.com</body>'>
连body都被返回了，，那么如何只取前边的title部分呢：
需要时用模式单元的存储功能：
pattern = r"(<[a-z]+>).*</\1>
    <re.Match object; span=(0, 17), match='<title>百度</title>'>
(<[a-z]+>)表示将<[a-z]+>存储到模式单元中，因为按照顺序<[a-z]+>先匹配的是<title>，所以title就会被存到模式单元中
后面\1表示调取模式单元中的第一个存储对象，
通过这种方式，我们就保证了查找对象的前后标签名都是title
注意，索引时候\1是第一个，而不是\0


但是当我们在爬取数据过程中存储了大量的模式单元，我们在用数字索引模式单元位置是，难免会出现数错位置的情况，
那么为了避免这种情况出现，我们可以使用字典模式单元

example:
pattern = r"<(?P<biaoti>[a-z]+)>.*"
str = "<title>百度</title><body>www.baidu.com</body>"
print(result)
print (result.groupdict())
    <re.Match object; span=(0, 43), match='<title>百度</title><body>www.baidu.com</body>'>
    {'biaoti': 'title'}
通过这中方式，我们将通过<[a-z]+>找到的内容明明为biaoti并存储在模式单元内
这样，要想表示前后标签名一样，只需要：
pattern = r"<(?P<biao>[a-z]+)>.*</(?P=biao)>"
    <re.Match object; span=(0, 17), match='<title>百度</title>'>
    {'biao': 'title'}
注意：在引用的时候格式与明明时候不同。
命名时：(?P<name>)
引用时：(?P=name)即可



###### 5. (?#) 正则注释内容

通过在pattern 中添加(?#内容) 来为这个正则表达式添加注释，这个注释可以再re中任何位置，包括re搜索内容的中间
但是不要在存储单元的命名里写入，因为会被识别为单元名字（会报错）
pattern = r"<(?P<biaoti>[a-z]+)>.*</(?P=biaoti)>"
pattern = r"<(?P<biaoti>[a-z]+)>.*<(?P=biaoti)(?#)>
pattern = r"(?#注释)<(?#注释)(?P<biaoti>[a-z]+)>.(?#注释)*</(?P=biaoti)>(?#注释)"
    <re.Match object; span=(0, 17), match='<title>百度</title>'>
    {'biaoti': 'title'}




##### 6. (?=) 正向先行断言（0宽）
正向 代表 有
负向 代表 没有
先行 = 向右进行查找
后行 = 向左进行查找


(?=)例子：
查找右边有.com的lmonkey
pattern = r"lmonkey(?=\.com)"
str = "www.lmonkey.comlmonkey"
result = re.findall(pattern,str)
    ['lmonkey']
    
注意：pattern 中：
要搜索的字符串是lmonkey,在他后面加入正向先行断言，查找他后面有没有.com
这里要注意，因为" . "是转义字符，所以要使用" \ " 去掉其转义含义，只取字符串含义
(?=\.com)

但是(?=\.com)放到前面就不管用了
pattern = r"(?=\.com)lmonkey"
str = "www.lmonkey.comlmonkey"
    []
    


#### 7. 负向先行断言 (?!)
正向 代表 有
负向 代表 没有
先行 = 向右进行查找
后行 = 向左进行查找

例子：
pattern = r"lmonkey(?!\.com)"
str = "www.lmonkey.comlmonkey"
    <re.Match object; span=(15, 22), match='lmonkey'>
此时查找的时候后面没有.com的lmonkey，那么，后面的lmonkey就被找出来了
为了清楚看到在多个lmonkey下如何操作，我们组合运用一下(?!\.com)与\d

pattern = r"lmonkey\d(?!\.com)"
str = "www.lmonkey1.comlmonkey2.cn.lmonkey3.\nlmonkey.com"
result = re.findall(pattern,str)
    ['lmonkey2', 'lmonkey3']
返回的只有2和3，他们后面是没有.com的


##### 8. 正向后行断言 (?<=)  查找左边有
正向 代表 有
负向 代表 没有
先行 = 向右进行查找
后行 = 向左进行查找

例子：
pattern = r"(?<=www\.)lmonkey\d"
str = "www.lmonkey1.comlmonkey2.cn.lmonkey3.\nlmonkey.com"
    ['lmonkey1']

    
    
##### 9.负向后行断言 (?<!) 查找左边没有

例子：
pattern = r"(?<!www\.)lmonkey\d"
str = "www.lmonkey1.comlmonkey2.cn.lmonkey3.\nlmonkey.com"
    ['lmonkey2', 'lmonkey3']
    


0宽断言注意事项：
recall：
(?=)
(?!)
(?<=)
(?<!)

注意：后行断言查找时，不可以用+表示重复数量，因为+不能限制出现几次：
pattern = r"(?<=w+\.)lmonkey\d(?=\.com)"
str = "www.lmonkey1.comlmonkey2.cn.lmonkey3.\nwww.lmonkey4.com"
    re.error: look-behind requires fixed-width pattern

此时我们可以通过{}来规定重复次数：但是只能用{m}而不是区间{m,n}，即，必须是不可变的
pattern = r"(?<=w{3}\.)lmonkey\d(?=\.com)"
str = "www.lmonkey1.com,lmonkey2.cn.lmonkey3.\nwww.lmonkey4.com"
    ['lmonkey1', 'lmonkey4']



###### 10. ((id/name)?Y|N）根据模式单元是否存在决定使用Y（存在）或N（不存在）的规则
注意，这里？后面的id/name所指的是存储的模式单元的名字或位置

目标：如果（www）这个模式单元出现则获取整个网址，如果没有www，则获取"."前面的内容个，看看是什么替换了www
注意：因为是要查找模式单元是否存在，所以，需要在要查找的对象外加上()

pattern = r"(www)?(?(1).*|\w+\.)"
str = "www.baidu.com"
    <re.Match object; span=(0, 13), match='www.baidu.com'>
str = "wdd.baidu.com"
    <re.Match object; span=(0, 4), match='wdd.'>
    




############ 正则表达式的书写规则（实例：验证）

步骤：
1.设定规则（几个字母，几个数字，几个汉子，能不能用符号之类的）
    邮箱实例 （得有字母，至少三个字符以上，可以使用个数字，不区分大小写，不能使用特殊符号，可以使用下划线）
2.写出符合规则的实例（具体邮箱）
    yhao
    yhao618
    yan_hao618
    Yan_Hao99_i
3.书写正则
    最开始写成这样就可以匹配：
    pattern = r"(?i)\w{3,}"
    str = "Yhao21"
        <re.Match object; span=(0, 6), match='Yhao21'>
    ！！但其实是不准确的，因为我们的re验证过程是拿着re pattern从头到尾依次比对，只要符合就能返回。
    所以，当我们str前面或者后面出现特殊符号时，也可以被匹配到，
    比如：
    pattern = r"(?i)\w{3,}"
    str = "+++Yhao21+++"
        <re.Match object; span=(3, 9), match='Yhao21'>
    然而！我们的邮箱名字 "从头至尾" 是不允许有特殊符号的
    所以，我们需要在pattern中加入^$或者\A\Z
    pattern = r"^(?i)\w{3,}$"
    str = "+++Yhao21+++"
        None
4.验证错误的用户名


!!!!实例1：用户名验证（简易版）

要求：
得有字母，至少三个字符以上，可以使用个数字，不区分大小写，不能使用特殊符号，可以使用下划线
pattern = r"^(?i)\w{3,}$"
str = "yhao618"


!!!!实例2：ip地址验证

要求：
分为4个数字段
每个数字段以“.”分隔
只能是数字
数字取值范围不能大于255

ip例子：
192.168.0.1
127.0.0.1
0.0.0.0
255.255.255.255

将例子改写正则思路：
直接复制一个例子，然后修改第一段数字，因为后面都是重复第一段数字，所以只需改写第一段然后让其重复多次即可
但是要注意，第四个数字段后面没有“.”
因为上限255，我们需要拆分成多个取值范围，范围之间用 | 分隔，表示满足其中任意一个模式即可
一位数的情况：“\d\.”   表示0-9
两位数的情况（错误）：“\d{2}\.” 表示00-99
    但我们要求的是从10-99
    所以
两位数的情况：“[1-9]\d\.”
三位数的第一种情况：“1\d{2}” 从100-199
三位数的第二种情况：“2[0-4]\d” 从200-249
三位数的第三种情况："25[0-5]" 从250-255
注意把所有情况组合后要用括号把整体括起来，然后再加\.
pattern = r"^(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\."
此时如果加上$则无法匹配到整个ip，str = "192.168.0.1"
除非把str改为str = "192."

但是这个re太复杂了，需要缩写
缩写的思路就是合并 | 之间的相同内容
先把前两个合并：
pattern = r"^(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\."
在[1-9]后面加?表示[1-9]可有可无，，这是？的基本功能，注意回顾最开始的基础知识！
pattern = r"^([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])\."
两位和三位如何合并呢？
首先\d{2}可以改写为\d\d,
[1-9]?\d|1\d\d|2[0-4]\d|25[0-5]
这表示要么[1-9]?后面加上\d,
要么1\d后面加上\d,
那么，[1-9]?与1\d就可以进行合并了，对吧
([1-9]?|1\d)\d|2[0-4]\d|25[0-5]
然后用([1-9]?|1\d)\d
与后面2[0-4]\d再合并
发现共同的还是最后一位
([1-9]?|1\d|2[0-4])\d|25[0-5]
后面255部分与前面没有公因式了，，所以就化简到这里把。。
而后用正确、错误的例子检验re是否书写正确。

后面添加重复项，
将前面的整体复制3遍，
((([1-9]?|1\d|2[0-4])\d|25[0-5])\.){3}
然后最后一段数字后不加“ . ”
(([1-9]?|1\d|2[0-4])\d|25[0-5])
最后限制好前后 ^ $
pattern = r"^((([1-9]?|1\d|2[0-4])\d|25[0-5])\.){3}(([1-9]?|1\d|2[0-4])\d|25[0-5])$"
str = "169.168.255.255"
    <re.Match object; span=(0, 15), match='169.168.255.255'>

学好正则必须要：
勤学苦练，多加练习！！！
不要贪图网上的简单正则，
一定要写：
严谨的re！
避免bug





!!!!实例3：电话号码
规则：
纯数字，11位数，第一位必须是1，第2,3,位号码有限制138,137，不可以110,199，即从130-139,,147,150-159,170+,180+,190+
电话号码例子：
13012346587
13701304462
13901310261
14701310261
15001310261
15901310261
17001310261
17901310261
18001310261
19001304462

书写re：
只有前三位有限制，后面8位随便写
所以后面写\d{8}
前三位：
13\d|147|15\d|17\d|18\d|19\d
发现前面选择项中第一位都是1
1(3\d|47|5\d|7\d|8\d|9\d)
其中3578可以提取
1(47|[35789]\d)
pattern = r"^1(47|[35789]\d)\d{8}$"



!!!! 实例4：身份证
规则：
18位，数字和字母X（x只能最后一位），
分为
110108，，，1993，，，06       18，，，005         2或者x
地区         年       月       日      顺序码      校验码

假设前6位是随机数字，
假设从1800年开始

例子
110345199912140510
110108199305180751
12023418511009123x

re 过程：
pattern = r"\d{6}     (18|19|[2-9]\d)\d{2}       (0[1-9]|1[0-2])        ([012]\d|3[01])          \d{3}         (\d|x)"
            地区              年                        月                      日                 顺序码         校验码
            
pattern = r"^\d{6}(18|19|[2-9]\d)\d{2}(0[1-9]|1[0-2])([012]\d|3[01])\d{3}(\d|x)$"
str = "12023418511009123x"
    <re.Match object; span=(0, 18), match='12023418511009123x'>
str = "12023419511309123x"
    None
    没有13月
    
    
    
    
@@@@@   re模块
1. re模块的方法
    compile()
    escape()
    findall()
    finditer()
    match()
    search()
    split()
    sub()
    subn()
    
2. re对象的方法:(借助compile()方法获取）
3. 匹配结果对象的方法



^^^^^^  re模块的方法：

1. compile() ：

作用1：编译re，获取re对象
作用2：可以循环利用，提高程序效率

compile的参数：re.compile(正则字符串，模式修正符）
返回值：正则对象


引言案例：
打印pattern的属性
pattern = r"\d{13}"
print(pattern,type(pattern))
    \d{13} <class 'str'>
    
compile()格式：compile(pattern, 模式修正符如re.I re.U....)
pattern = r"\d{13}"
pattern_obj = re.compile(pattern,re.I)
print(pattern_obj,type(pattern_obj))   
    re.compile('\\d{13}', re.IGNORECASE) <class 're.Pattern'>
    
    
2. escape() ：对字符串进行转义处理    

作用：在除了字母和数字以外的字符前面加上\进行转义，避免有些字母被识别为转义字符。

例子：
pattern = r"\d{13}"
str = "how old are you? I'm 25 years old."
result = re.escape(str)
    how\ old\ are\ you\?\ I'm\ 25\ years\ old\.

格式：re.escape(string)
返回值：字符串


3. findall() 通过re匹配，获得所有匹配的内容

格式：re.findall(re表达式，要匹配的字符串，模式修正符(flags))
返回值：列表

例子

pattern = r"baidu"
str = "www.baidu.com.baidu.net-BAIDU.CN.www.BaiDu.com"
result = re.findall(pattern,str,re.I)
    ['baidu', 'baidu', 'BAIDU', 'BaiDu']



4. finditer() 与findall相似，获取所有匹配的结果对象，以迭代器格式代码返回


pattern = r"baidu"
str = "www.baidu.com.baidu.net-BAIDU.CN.www.BaiDu.com"
result = re.finditer(pattern,str,re.I)
    <callable_iterator object at 0x000001EC0AB4DB20>
    这是什么东西呢？通过for循环来查看：
for i in result:
    print(i)
    <re.Match object; span=(4, 9), match='baidu'>
    <re.Match object; span=(14, 19), match='baidu'>
    <re.Match object; span=(24, 29), match='BAIDU'>
    <re.Match object; span=(37, 42), match='BaiDu'>
    
    
5. match()  对字符串进行re匹配。匹配对象必须在字符串开头才能被匹配到，换行\n，空格什么的都无法识别，必须在最开始。

例子：
pattern = r"baidu"
str = "www.baidu.com"
    None

pattern = r"baidu"
str = "baidu.com"  
    <re.Match object; span=(0, 5), match='baidu'>


6.search() 对字符串进行re匹配，当匹配到第一个结果时就停止了

7. split() 使用re切割字符串

格式：re.split(pattern,string,要切几刀（数字值）切割次数)

把搜索对象（pattern）左右内容分割，并保存在列表中
pattern = r"baidu"
str = "www. baidu.com,adfa ,df"
    ['www. ', '.com,adfa ,df']


pattern = r"\d+"
str = "10世9贪，凑得8两7钱6分5毫4厘，况且3心2意，1等下流"
    ['', '世', '贪，凑得', '两', '钱', '分', '毫', '厘，况且', '心', '意，', '等下流']
    
比如我只想切前三个数字，后面的数字保留，则，
pattern = r"\d+"
str = "10世9贪，凑得8两7钱6分5毫4厘，况且3心2意，1等下流"
result = re.split(pattern,str,3)
        ['', '世', '贪，凑得', '两7钱6分5毫4厘，况且3心2意，1等下流']



8. sub() 正则替换

格式：
re.sub(pattern, replace_s, string, 替换的最大次数(填写数字)如果不写，则全替换)

我希望把蜡笔小新找出来替换成另一个名字：
str = "蜡笔小新的爸爸是野原广志，蜡笔小新的妈妈是野原美伢，蜡笔小新的妹妹是野原葵"
pattern = r"蜡笔小新"
替换成:
replace_s = “野原新之助”

pattern = r"蜡笔小新"
str = "蜡笔小新的爸爸是野原广志，蜡笔小新的妈妈是野原美伢，蜡笔小新的妹妹是野原葵"
replace_s = "野原新之助"
result = re.sub(pattern, replace_s, str)
    野原新之助的爸爸是野原广志，野原新之助的妈妈是野原美伢，野原新之助的妹妹是野原葵
    
    
pattern = r"蜡笔小新"
str = "蜡笔小新的爸爸是野原广志，蜡笔小新的妈妈是野原美伢，蜡笔小新的妹妹是野原葵"
replace_s = "野原新之助"
result = re.sub(pattern, replace_s, str,2)
    野原新之助的爸爸是野原广志，野原新之助的妈妈是野原美伢，蜡笔小新的妹妹是野原葵


9. subn() 与sub（）一样，只是返回结果最后面会告诉你替换了几个

返回值：由替换后的字符串和资环此处组成的元组

pattern = r"蜡笔小新"
str = "蜡笔小新的爸爸是野原广志，蜡笔小新的妈妈是野原美伢，蜡笔小新的妹妹是野原葵"
replace_s = "野原新之助"
result = re.subn(pattern, replace_s, str, 3)
    ('野原新之助的爸爸是野原广志，野原新之助的妈妈是野原美伢，野原新之助的妹妹是野原葵', 3)



^^^^^ 正则对象的方法（借助compile（））

rx代表正则对象

可用方法：
findall() ： rx.findall()
finditer()： 
match()
split()
sub()
subn()

提供了属性：
flages: 模式修正符
pattern:
groups:
groupindex:


1. findall()
借助compile，无需单独列出pattern，直接在代码中写入re表达式和模式修正符
例子：
str = "www.baidu.com;mp4.BaiDU.cn=image.BaiDu.com"
rx = re.compile(r"baidu",re.I).findall(str)
    ['baidu', 'BaiDU', 'BaiDu']
    
    
    
2. finditer()
str = "www.baidu.com;mp4.BaiDU.cn=image.BaiDu.com"
rx = re.compile(r"baidu",re.I).finditer(str)
    <callable_iterator object at 0x000002571901DB20>
for i in rx:
    print(i)
<re.Match object; span=(4, 9), match='baidu'>
<re.Match object; span=(18, 23), match='BaiDU'>
<re.Match object; span=(33, 38), match='BaiDu'>


3. match() 记住，只能匹配到开头的

str = "baidu.com;mp4.BaiDU.cn=image.BaiDu.com"
rx = re.compile(r"baidu",re.I).match(str)
    <re.Match object; span=(0, 5), match='baidu'>
    
4.search()

str = "www.baidu.com;mp4.BaiDU.cn=image.BaiDu.com"
rx = re.compile(r"baidu",re.I).search(str)
    <re.Match object; span=(4, 9), match='baidu'>
    
    
5.split()

str = "www.baidu.com;mp4.BaiDU.cn=image.BaiDu.com"
rx = re.compile(r"baidu",re.I).split(str)
    ['www.', '.com;mp4.', '.cn=image.', '.com']
    
    
6.sub() 

str = "www.baidu.com;mp4.BaiDU.cn=image.BaiDu.com"
replace_s = "google"
rx = re.compile(r"baidu",re.I).sub(replace_s, str,后面可加替换次数)
    www.google.com;mp4.google.cn=image.google.com

rx = re.compile(r"baidu",re.I).sub(replace_s,str,2)
    www.google.com;mp4.google.cn=image.BaiDu.com


7.subn()

str = "www.baidu.com;mp4.BaiDU.cn=image.BaiDu.com"
replace_s = "taobao"
rx = re.compile(r"baidu",re.I).subn(replace_s,str)
    ('www.taobao.com;mp4.taobao.cn=image.taobao.com', 3)
    


查看属性：

1.pattern, 查看查找的re表达式
rx = re.compile(r"baidu",re.I).pattern
    baidu
    
2.flags, 查看使用了那些模式修正符
rx = re.compile(r"baidu",re.I).flags
    34

3. groups, 查看索引模式单元的个数
rx = re.compile(r"(baidu)",re.I).groups
    1 表示有一个模式单元
rx = re.compile(r"(baidu)(com)",re.I).groups
    2
rx = re.compile(r"(?P<name>)",re.I).groups
    1 命名方式的模式单元也可以搜索到
    
    
4. groupindex()
只查找通过命名方式的储存的模式单元，并返回该模式单元的位置编号：
rx = re.compile(r"(?P<b>)(baidfu)(?P<name>)",re.I).groupindex
    {'b': 1, 'name': 3}
    表示：b是第一个模式单元，name是第三个模式单元



^^^^^ 正则对象的扩展用法

findall()
finditer()
match()
search()

一般都是对字符串整体进行查找，
如何进行前10个字符查找，或者在字符串中的某个部分进行查找呢？

一般查找

pattern = r"lmonkey"
str = "https://www.lmonkey.com"
rx = re.compile(pattern).findall(str)
    ['lmonkey']
    
如果我只想在前十个字符中查找有没有lmonkey呢？
rx = re.compile(r"lmonkey").findall(str,0,10)
    []
如果我想从第10开始一直到字符串末尾进行匹配呢
rx = re.compile(r"lmonkey").findall(str,10)
    ['lmonkey']

findall()格式新探索：

findall(string,开始位置，结束位置)



爬取内容时，
<div>
    <div class= lalala>
        <span>...</span>
    </div>
</div>

如果我想获得第二个div时，
要使用：
<div class=lalala>(.*?)</div>
加问号表示非贪婪模式，他会在第一个</div>结束查找，
如果不加问号，则会匹配到最后一个</div>
"""
pattern = r"lmonkey"
str = "https://www.lmonkey.com"
rx = re.compile(pattern).findall(str,10)
print(rx)
