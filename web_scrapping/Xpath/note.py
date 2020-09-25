import lxml
"""
模块导入：
from lxml import etree

html = etree.HTML(f.read())




基本语法：
/       从根节点开始找tag
//      直接从子孙节点开始找
.       选取当前节点
..      选取当前节点的父亲节点
@       选取属性
text()  选取文本

*       匹配任何元素节点
@*      匹配任何属性节点
node()  匹配任何类型的节点
/div/*  选取div所有子元素
//*     选取文档所有元素
//title[@*] 选取所有带属性的title元素


xpath 神器： 模糊查询

//div[contains(tag/attrs,"string that you want")]
example:
//div[contains(id,"qiushi")]

注意：
xpath返回的是一个list
所以：
通过模糊查询找到所有行，作为根节点，然后用for 循环取每一个

"""