import re
"""
regular expression 基础知识：


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

re组成部分：
1. 原子
2.元字符
3.模式修正符

匹配方式：
拿着re表达式在目标字符串中从头到尾依次比对直到找到符合要求的字符串


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.原子

ID：每一个字符，都是原子

字符分为两种：
1.可见字符
2.不可见字符：\t \n \f \r..

特殊定义的原子：转义字符
1.\d 表示0-9中任意一个数字，d for digit
2.\D 表示除了0-9以外的任意一个字符
3.\s 表示一个空白字符 s for space
4.\S 表示除了空白字符以外的任意一个字符
5.\w 表示0-9,a-z,A-Z,"_"中任意一个字符
6.\W 表示除了0-9,a-z,A-Z,"_"以外任意一个字符
7."." 表示除了换行\n以外的任意一个字符
8.“\” 表示取消转义字符的意义，只取其字符含义
    如：\[google]表示被搜索的google外面必须被[]包裹，而不是google中任意一个字母都可以满足匹配
    如：\. 表示取消“.”的转义字符含义，单纯只取一个.    如r"www\."表示www.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2.元字符（原子修饰符）

2.1 自定义原子列表 []

[]表示满足方括号中任意一个即匹配成功
比如：
    1.\d = [0123456789]
    2.\w = [a-zA-Z0-9]

另外可以通过[]自己设置想要取得内容：
比如：我想要取10以内的任意一个奇数：
    odd number = [13579]

### []中^的使用：
他表示方括号内的非集，比如：
    1.\d = [0123456789]
    2.\D = [^0123456789]
    表示除了0-9以外的任意一个字符

2.2 表示数量的元字符

+       表示一个或者无限个被修饰的原子
?       表示一个或零个被修饰的原子
*       表示任意个（+与?的功能组合）
{m}     表示m个被修饰的原子
{m,n}   表示m到n个被修饰的原子，区间内任意数量都可以
{m,}    表示从m到无穷多个被修饰的原子
{,n}    表示最多n个被修饰的原子

2.3 限定开头结尾的元字符

\A：表示限定内容必须在字符串的开头部位
\Z：表示限定内容必须在字符串的结尾
^   可识别换行符，并将换行符识别为新的开头（功能与\A一样）
$   可识别换行符，将换行符前一个字符视为结尾（功能与\Z一样）
注意：使用^ 与 $ 时，必须使用多行模式：re.M

2.4 词边界
\b：表示需要查找的内容前or后or both 必须是一个单词分隔符号，即，只要该单词前面不是紧密相连的数字或者字母即可。
比如：
pattern = r"\bgood"
pattern = r"good\b"
pattern = r"\bgood\b"

\B：表示需要查找的内容前or后or both需与数字或字母紧密相连
比如：
pattern = r"\Bgood"
    internetgood

2.5 “|” 左右内容二选一

比如：
pattern = r"ab|cd"
    表示要么取ab要么取cd
pattern = r"a(b|c)d"
    表示要么abd，要么acd

2.6 （）的作用

2.6.1 这里出现了（）的第一个作用：表示运算优先级

pattern = r"a(b|c)d"

2.6.2 （）第二个作用：将括号中内容视为一个整体

pattern = r"(go)+"
    表示go重复多次

2.6.3 （）第三个作用：表示存储模式单元



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3. 模式修正符：

re.A：表示re.ascii，在ascii模式下进行re匹配，这是只支持英文和数字
re.U：表示re.unicode，在万国码模式下匹配，这是默认模式，可识别他国语言
re.S：表示无视回车换行符号\n，“.”可以匹配到任何字符包括\n
re.M：表示re.multline 多行模式
re.X：表示忽略字符串中的空格进行匹配
re.I：表示忽略大小写进行匹配

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4. 正则扩展语法

4.1 (?imuaxs) 在pattern中使用模式修正符的方法
        pattern = r"(?i)baidu"
        无需再查找函数中声明模式修正符也可以通过忽视大小写的方法查找，括号内可用多个模式修正符
        pattern = r"(?ims)baidu"
        
4.2 (?:) 取消对该模式单元的存储
        pattern = r"(?:baidu)+"
        查找时加括号会自动存储括号中的模式单元。但如果加上?:就只发挥将括号内当做整体的功能，不进行模式单元存储
        
4.3 (?P<name>) 自定义模式单元的名称
        str = "<title>百度</title><body>www.baidu.com</body>"
        pattern = r"<(?P<biaoqian>)[a-z]+>.*</(?P=biaoqian)>
        将第一个符合的标签名（title）以“biaoqian”为名保存为模式单元，后面进行调用，表示只取title标签中间的内容
        
4.4 (?#) 在pattern中加入注释


各类断言：
正向 代表 有
负向 代表 没有
先行 代表 从左到右查找
负向 代表 从右到左查找

4.5 (?=) 正向先行断言
    pattern = r"lmonkey(?=\.com)"
    找到右侧有.com的lmonkey
         
4.6 (?!) 负向先行断言
    pattern = r"lmonkey(?!\.com)"
    找到右侧没有.com的lmonkey
    
4.7 (?<=) 正向后行断言
    pattern = r"(?<=www\.)lmonkey"
    找到左侧有www.的lmonkey
    
4.8 (?<!) 负向后行断言
    pattern = r"(?<!www\.)lmonkey"
    找到左侧没有www.的lmonkey
    
注意：
使用0宽断言是，不可以使用+等不确定重复次数的元字符
需使用{m}来规定确切的重复次数

4.9 ((id/name)?Y|N) 表示根据问号前的模式单元是否存在来执行命令，如果存在执行Y，否则执行N
    pattern = r"(www)?(?(1).*|\w+\.)"
    str = "www.baidu.com"
    表示判断www是否存在，如果存在，返回www和整个网址
    否则，返回替代www.的内容
    
    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

5. re 模块

compile() 
escape()
findall()
finditer()
match()
search()
split()
sub()
subn()


5.1 compile()

将re表达式和模式修正符写在compile中，避免单独设置pattern函数
result = re.compile(r"w{3}\.baidu\.com", re.I)
表示忽略大小写查找“www.baidu.com”

如果我想从第10开始一直到字符串末尾进行匹配呢
rx = re.compile(r"lmonkey").findall(str,10)
    ['lmonkey']

5.2 escape()

对字符串进行转义处理，即取消所有所有转义字符含义，只取字符含义
str = "how old are you? I'm 25 years old."
result = re.escape(str)
    how\ old\ are\ you\?\ I'm\ 25\ years\ old\.
    
5.3 findall()

和BeautifulSoup中的find_all()一样
result = re.compile(r"w{3}\.baidu\.com", re.I).findall(str)

5.4 finditer()

以迭代器形式返回搜索内容个，需用for循环解析查看

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

5.5 match()

只能找到段落开头且符合内容的字符串，且无法识别\n 换行符号

5.6 search()

与BeautifulSoup 中的find一样

5.7 split()

使用re切割字符串
pattern = r"\d+"
str = "10世9贪，凑得8两7钱6分5毫4厘，况且3心2意，1等下流"
格式：re.split(pattern,string,要切几刀（数字值）切割次数)
    ['', '世', '贪，凑得', '两', '钱', '分', '毫', '厘，况且', '心', '意，', '等下流']
    ['', '世', '贪，凑得', '两7钱6分5毫4厘，况且3心2意，1等下流']

5.8 sub()

替换
pattern = r"蜡笔小新"
str = "蜡笔小新的爸爸是野原广志，蜡笔小新的妈妈是野原美伢，蜡笔小新的妹妹是野原葵"
replace_s = "野原新之助"
result = re.sub(pattern, replace_s, str)
    野原新之助的爸爸是野原广志，野原新之助的妈妈是野原美伢，野原新之助的妹妹是野原葵
result = re.sub(pattern, replace_s, str,2)
    野原新之助的爸爸是野原广志，野原新之助的妈妈是野原美伢，蜡笔小新的妹妹是野原葵

5.9 subn()
 
与sub（）一样，只是返回结果最后面会告诉你替换了几个

返回值：由替换后的字符串和资环此处组成的元组

pattern = r"蜡笔小新"
str = "蜡笔小新的爸爸是野原广志，蜡笔小新的妈妈是野原美伢，蜡笔小新的妹妹是野原葵"
replace_s = "野原新之助"
result = re.subn(pattern, replace_s, str, 3)
    ('野原新之助的爸爸是野原广志，野原新之助的妈妈是野原美伢，野原新之助的妹妹是野原葵', 3)


6. 属性查看

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