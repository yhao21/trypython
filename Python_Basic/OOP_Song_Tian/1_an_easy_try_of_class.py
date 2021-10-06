

##创建一个名字为product的类，里面存放着三个商品的信息：商品名，标签价格，和实际价格
class Product():
    ##初始化这个类
    def __init__(self,name):
        self.name = name
        self.label_price = 0
        self.real_price = 0

##定义三个商品名称，并传送到product类当中
c = Product("computer")
d = Product("printer")
e = Product("projector")

##设定商品的标签价格和实际价格，注意，同一个商品信息可以并排写
c.label_price, c.real_price = 10000, 8000
d.label_price, d.real_price = 2000, 1000
e.label_price, e.real_price = 1500, 900

##定义s1，s2分别为三个商品的标签价格之和与实际价格之和
s1,s2 = 0,0

##运用for循环进行价格加总
for i in [c,d,e]:
    s1 += i.label_price
    s2 += i.real_price
print(s1,s2)