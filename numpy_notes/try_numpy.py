import numpy as np

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. ndarray

运行数组之间的运算
a = np.array([1,2,3,4,5,6])
b = np.array([1,2,3,4,5,6])
c = a**2 + b**3
print(c)

    [  2  12  36  80 150 252]
    
    
ndarray是一个多维数组对象，有两部分组成：
1.实际数据
2.描述数据的元数据（维度，类型等）

五个运算数形：
.ndim       秩，即轴的数量或维度的数量
.shape      对象尺度，多少行m列n
.size       元素的个数，相当于n*m的值
.dytpe      对象的元素类型
.itemsize   对象中每个元素的大小，以字节为单位

a = np.array([[0,1,2,3,4],
             [5,4,3,2,1]])
print(a.ndim)
    return: 2
    
a = np.array([[0,1,2,3,4],
             [5,4,3,2,1]])
print(a.shape)
    return: (2,5)

a = np.array([[0,1,2,3,4],
             [5,4,3,2,1]])
print(a.size)
    return: 10

a = np.array([[0,1,2,3,4],
             [5,4,3,2,1]])
print(a.itemsize)
    return: 4
每个元素由四个字节组成

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ndarray 支持非同质对象：
a = np.array([[0,1,2,3,4],
              [5,4,3,2]])
a中，一个为5个数的列表，一个为4个数的列表，这叫非同质，

a = np.array([[0,1,2,3,4],
             [5,4,3,2]])
print(a.shape)
    return: (2,)

a = np.array([[0,1,2,3,4],
             [5,4,3,2]])
print(a.dtype)
    return: object
    
当a为非同质时，np会把他分类为object类别，多个object碰在一起又可以相互运算了
!!!!注意，np在处理非同质时候，无法发挥其优势，所以在大规模数据处理时，尽量避免非同质
！！！

a = np.array([[0,1,2,3,4],
             [5,4,3,2]])
print(a.size)
    return: 2

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ndarray数组创建：

$$$ 1. 从python中的列表、元组等类型创建
    x = np.array(list/tuple)
    x = np.array(list/tuple,dtype=np.float)
    当不指定dtype时，np将自动识别
    
    元组与列表只要组成部分的数量相同就可以混合使用：
    a = np.array([[1,2],(3,4),[5,1]])
    print(a)
    
        [[1 2]
         [3 4]
         [5 1]]
    
    可以设置数据类型：如，float
    a = np.array([[1,2],(3,4),[5,1]],dtype=float)
    print(a)

        [[1. 2.]
         [3. 4.]
         [5. 1.]]
         
$$$ 2. 使用创建函数：
    np.arange(n)：       创建从0-n-1个数字
    np.ones(shape)：     根据shape生成全1数组，默认为float除非设置dtype
    np.zeros(shpae)：    根据shape生成全0数组，默认为float除非设置dtype
    np.full(shape,val)： 根据shape生成一个数组，每个元素值都是val
    np.eye(n)：          创建正方形的n*n单位矩阵，对角线为1，其余为0,默认float
    np.identity(n_row)          create an identity matrix
    

### 2.1 np.arange(n)

a = np.arange(10).reshape(2,5)
print(a)
    [[0 1 2 3 4]
     [5 6 7 8 9]]
     
### 2.2 np.ones(shape)

a = np.ones(10)
print(a)
    [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

a = np.ones(10,dtype=int)
    [1 1 1 1 1 1 1 1 1 1]
    
若要生成矩阵类型：

a = np.ones((3,5),dtype=int)
print(a)
    [[1 1 1 1 1]
     [1 1 1 1 1]
     [1 1 1 1 1]]
     

### identity matrix
a = np.identity(3)

[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]



### 2.3 zeros(shape)

a = np.zeros(4)
print(a)
    [0. 0. 0. 0.]

a = np.zeros((4,5),dtype=int)
    [[0 0 0 0 0]
     [0 0 0 0 0]
     [0 0 0 0 0]
     [0 0 0 0 0]]
     
### 2.4 np.full(shape,val)

a = np.full((2,3),4)
print(a)
    [[4 4 4]
     [4 4 4]]
     
### 2.5 np.eye(n)

a = np.eye(3)
print(a)
    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
     
### 2.6 生成多个矩阵 ###
生成2个3*4的矩阵
a = np.full((2,3,4),1)
print(a)
    [[[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]

     [[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]]
      

生成2组2个3*4的矩阵

a = np.full((2,2,3,4),1)
print(a)
    [[[[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]

     [[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]]


     [[[1 1 1 1]
       [1 1 1 1]
       [1 1 1 1]]

      [[1 1 1 1]
       [1 1 1 1]
       [1 1 1 1]]]]

### 2.7 根据某个数组的样式创建某一个数组：

@@@ 2.7.1 np.ones_like(a)
根据a的样子创建一个全1数组
a = np.full((3,4),5)
b = np.ones_like(a)
print(a)
print(b)
    [[5 5 5 5]
     [5 5 5 5]
     [5 5 5 5]]
 
    [[1 1 1 1]
     [1 1 1 1]
     [1 1 1 1]]
     
@@@ 2.7.2 np.zeros_like(a)

a = np.full((3,4),5)
b = np.zeros_like(a)
print(a)
print(b)
    [[5 5 5 5]
     [5 5 5 5]
     [5 5 5 5]]
     
    [[0 0 0 0]
     [0 0 0 0]
     [0 0 0 0]]

@@@ 2.7.3 np.full_like(a,value)

a = np.full((3,4),5)
b = np.full_like(a,10)
print(a)
print(b)
    [[5 5 5 5]
     [5 5 5 5]
     [5 5 5 5]]
     
    [[10 10 10 10]
     [10 10 10 10]
     [10 10 10 10]]
     
### 2.8 进阶ndarray生成函数：

@@@ 2.8.1 np.linspace()

根据起始和终止值，等间距的生成填充数据，
a = np.linspace(1,10,4)
print(a)
    [ 1.  4.  7. 10.]
    
若不想取终止值：
a = np.linspace(1,10,4,endpoint=False)
    [1.   3.25 5.5  7.75]
    
@@@ 2.8.2 np.concatenate()

将两个或多个数组合并成一个新的数组
a = np.linspace(1,10,4,endpoint=False)
b = np.linspace(2,8,4)
c = np.concatenate((a,b))
print(c)
    [1.   3.25 5.5  7.75 2.   4.   6.   8.  ]
    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
3. ndarray 数组变换

### 3.1 维度变换
1. .reshape(shape)：     新的shape，原数组不变
2. .resize(shape)：      功能与reshape一样，但是它是用来修改原来数组的
3. .swapaxes(ax1,ax2)：  将数组n个维度中的两个维度进行调换
4. .flatten()：          对数组进行降维，返回新数组，原数组不变


reshape:
a = np.ones((2,3,4),dtype=int)
    [[[1 1 1 1]
     [1 1 1 1]
     [1 1 1 1]]

    [[1 1 1 1]
     [1 1 1 1]
     [1 1 1 1]]]
     
b = a.reshape((3,8)) 注意，reshape时候不能改变数组中元素个数，比如原来数组里有2*3*4=24个元素，那么reshape的也必须是24个
b = a.reshape(3,8)
    [[1 1 1 1 1 1 1 1]
     [1 1 1 1 1 1 1 1]
     [1 1 1 1 1 1 1 1]]
     

resize:
会直接改变数组
a = np.ones((2,3,4),dtype=int)
b = a.resize((3,8))
print(a)
    [[1 1 1 1 1 1 1 1]
     [1 1 1 1 1 1 1 1]
     [1 1 1 1 1 1 1 1]]
print(b)
    None
你会发现resize直接在a上做了修改，你是无法打印b的


flatten:
降维处理：
a = np.ones((2,3,4),dtype=int)
    [[[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]

     [[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]]
      
      
b = a.flatten()
    [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
    


astype:

a = np.ones((2,3,4),dtype=int)
    [[[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]

     [[1 1 1 1]
      [1 1 1 1]
      [1 1 1 1]]]

b = a.astype(float)
    [[[1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]]

     [[1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]]]
注意astype一定会创建一个新的数据，即，np拷贝了一份数据，并修改元素类型，再返回给用户
！！！！所以，如果我们想拷贝原来的数组：
只需要使用astype然后输出相同的元素类型即可
！！！很重要


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
4. ndarray可以将数组转换为python中的列表

tolist()函数：
a = np.full((2,3,4),5,dtype=int)
    [[[5 5 5 5]
      [5 5 5 5]
      [5 5 5 5]]

     [[5 5 5 5]
      [5 5 5 5]
      [5 5 5 5]]]
      
b = a.tolist()
    [[[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]], [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]]
    
注意：list的运算速度比np的运算速度低很多，但是有时候为了配合python中其他列表的运算，我们可以将ndarray转为list



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
5. ndarray数组的操作：索引与切片

索引：找到某一个元素的位置
切片：在数组中找到一组数据，即，找到子集


@@找到指定数组中符合条件的元素并把他们提取出来，创建成一个新的数组


a = np.random.randint(10,size = 15)
print(a)
print(a[a<3])
    [1 9 3 6 0 5 1 3 1 7 2 0 0 4 8]
    [1 0 1 1 2 0 0]
把a中所有小于3的数字拿出来创建一个新的数组


多维数组提取：

对一个4*4的多维数组a，取出第3列中能被3整除的那些行

a = np.random.randint(10,size = (4,4))
print(a)
    [[5 0 8 9]
     [7 2 7 4]
     [6 9 1 7]
     [7 0 1 9]]

print(a[a[:,3] % 3 == 0])
    [[5 0 8 9]
     [7 0 1 9]]

不加逗号冒号，默认就是“行”。



也可以这么写：

a = np.random.randint(10,size = (4,4))
print(a)

print(a[a[:,3] % 3 == 0,:])



@@以数组中的某个值为界线，将数组分为前后两部分，前面的元素都比这个数小，后面的都比他大

x = np.arange(15)
np.random.shuffle(x)
print(x)
    [ 5 10  6 14 13 11  2  7  1  0 12  9  8  3  4]
print(np.partition(x,7))
    [ 2  4  3  0  1  5  6  7  8  9 10 11 14 13 12]
生成一个从零到14的数组，然后打乱，使用partition将打乱后的数组以7为界线分为前后两部分
np.partition(array,number)两个参数，一个是要进行排序的数组array，一个是界限值number


！！！！！！！
注意，partition也会存在一些bug
通过生成一个随机数组中如果有两个数字相同，这两个数字在数组的不同位置，且这个数字是你要是用的界限，那么，就会发生下面的情况：

np.random.seed(11)
a = np.random.randint(15,size = (1,10))
print(a)
    [[ 9  0 11  1  7 13 12  1  7  2]]

print(np.partition(a,7))
    [[ 1  2  7  1  0  7  9 11 12 13]]

发现，两个7之前都是小于他们的数，但是第一个7后面并不是比他大的数字，而是比第二个7小的数字。。。。  

当然，，partition也支持argpartition操作


@@ 高级索引

在一个数组中，比如你想取出第3,5,6个值，除了使用x[2],x[4],x[5]的方法，还可以一次性将想要索引的位置放入一个列表ind中
np.random.seed(666)
a = np.random.randint(10,size = 15)
print(a)
    [2 6 9 4 3 1 0 8 7 5 2 5 5 4 8]
ind = [2,4,5]
print (a[ind])
    [9 3 1]


我也可以将这个一维数组a中的某些值取出来然后重新组成一个新的二维数组

np.random.seed(666)
a = np.random.randint(10,size = 15)
print(a)
    [2 6 9 4 3 1 0 8 7 5 2 5 5 4 8]
ind = np.array([
    [0,2],
    [1,3]
])
print (a[ind])
    [[2 9]
     [6 4]]


也可以指定行和列的信息对多维数组进行索引
np.random.seed(666)
a = np.random.randint(10,size = 16).reshape(4,4)
print(a)
    [[2 6 9 4]
     [3 1 0 8]
     [7 5 2 5]
     [5 4 8 4]]

row = [1,3]
col = [0,3]
print(a[row,col])
    [3 4]
表示，取第1行和第3行，第1行取第0列，第3行取第3列，相当于坐标(1,0),(3,3)


可以这样直接输入取前两行中的第0和第3个值
col = np.array([0,3])
print(a[:2,col])
    [[2 4]
     [3 8]]


当然我们也可以通过布尔值来进行索引


np.random.seed(666)
a = np.random.randint(10,size = 16).reshape(4,4)
print(a)
    [[2 6 9 4]
     [3 1 0 8]
     [7 5 2 5]
     [5 4 8 4]]

col = [True,False,False,True]
print(a[:,col])
    [[2 4]
     [3 8]
     [7 5]
     [5 4]]

这里面True表示我要取，False表示不取，
那么这里的意思就是，我要去所有行中的第0和第3列



@@ 一维数组的索引与切片：
a = np.arange(10)
    [0 1 2 3 4 5 6 7 8 9]
找到第二个值：1
print(a[1])
    1
    
@@ 一维数组切片：

格式：a[起始编号 ：终止编号(只会显示终止编号的前一个数) ：步长]
如：我想要1到9每个数之间间隔2：
a = np.arange(10)
    [0 1 2 3 4 5 6 7 8 9]
print(a[1:10:2])
    [1 3 5 7 9]
print(a[0:10:2])
    [0 2 4 6 8]
    
    
@@ 多维数组索引：
a = np.arange(24).reshape((2,3,4))
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]

     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
      
      
索引多维数组，先找最外围位置，然后一层一层的找进去：
比如a中，我想找到22这个数字，
22在第2大组的第3行第3列，
注意，和python其他列表一样，位置序号是从0开始的，所以，
我应该找a[1,2,2]
print(a[1,2,2])
      22
      
负向查询也是和python的列表位置排序相同，
比如我想找19
a[-1,-2,-1]
print(a[-1,-2,-1])
    19
    

逆向排序（从高到低）


L_1 = np.arange(100)
L = []
for i in L_1:
    L.append(i)
L.reverse()
print(L)

python系统自带了一个reverse()方法可以将目标数组逆向排序，但是无法对numpy操作
所以需要把通过numpy创立的数组中的元素提取出来建立一个新的数组，然后再进行逆序


@@ 多维切片：
a = np.arange(24).reshape((2,3,4))
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]

     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
      
比如我想找5和17，
a[:,1,-3]
    [ 5 17]
第一个位置用 : 表示不考虑第一维度，即在两个大组都被考虑进去了
然后1表示两个大组中的第二行
-3表示从右往左数第三个

类似的还可以用：
a[:,-2,1]来找
    [ 5 17]
    

也可以将一维切片运用到多维当中，
比如我想分别取两个大组前两行的所有值，
a[:,0:2,:]
    [[[ 0  1  2  3]
      [ 4  5  6  7]]

     [[12 13 14 15]
      [16 17 18 19]]]
      
0:2表示取第0和第1行，即，列表中的1、2行



使用步长跳跃式获取数据，
比如我想把数组中的偶数拿出来
a = np.arange(24).reshape((2,3,4))
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]

     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
      
print(a[:,:,::2])
    [[[ 0  2]
      [ 4  6]
      [ 8 10]]

     [[12 14]
      [16 18]
      [20 22]]]
      
不关心前两个维度，所以用 :
第三个维度时
回顾一下一维时候a:b:c
c代表步长，如果我不关心起始和终止数，只关心步长，则使用 ::c
这里也是一样，我只要求步长为2，他就会默认从第一个开始取

如果我想取奇数，则只需规定起始是第二个数即可
print(a[:,:,1::2])
    [[[ 1  3]
      [ 5  7]
      [ 9 11]]

     [[13 15]
      [17 19]
      [21 23]]]
这里1代表第二个位置的数字



如何复制原数组：

a = np.random.randint(1,20,(5,7))
[[ 4  3 15 12  6 16 15]
 [ 5 11  3 17 12 16 15]
 [10  1 19 18  9  2  4]
 [ 5  2 11  1  4  9 10]
 [ 1 12 11  5  8 10  9]]
 
此时若直接从a中切片创建子矩阵并修改子矩阵sub_a中的值，则原矩阵对应的值也会被修改
sub_a = a[:2,:3]  取a矩阵中的前两行和前三列
[[ 4  3 15]
 [ 5 11  3]]
 
 sub_a[0,0] = 100   将子矩阵的第一个值“4”修改为100
 [[100   3  15]
 [  5  11   3]]
 
 此时我们再次查看原矩阵a
 print(a) 发现a中的第一个值也被改为100了。这是因为numpy为了快速运算，在你切片时候，他是直接引用原矩阵，而不是重新创建一个新的矩阵。
 
 
 [[ 100  3 15 12  6 16 15]
 [ 5 11  3 17 12 16 15]
 [10  1 19 18  9  2  4]
 [ 5  2 11  1  4  9 10]
 [ 1 12 11  5  8 10  9]]
 
 为了避免切片后对数据的处理影响到原来的矩阵，我们需要将原矩阵a进行复制，创建一个新的矩阵，然后在做切片
 
a = np.random.randint(1,20,(5,7))
print(a)
    [[ 4  3 15 12  6 16 15]
     [ 5 11  3 17 12 16 15]
     [10  1 19 18  9  2  4]
     [ 5  2 11  1  4  9 10]
     [ 1 12 11  5  8 10  9]]
sub_a = a[:2,:3].copy()

print(sub_a)
    [[ 4  3 15]
     [ 5 11  3]]
sub_a[0,0] = 100
print(sub_a)
    [[100   3  15]
     [  5  11   3]]
print(a)
    [[ 4  3 15 12  6 16 15]
     [ 5 11  3 17 12 16 15]
     [10  1 19 18  9  2  4]
     [ 5  2 11  1  4  9 10]
     [ 1 12 11  5  8 10  9]]

此时，修改sub_a就不会影响原矩阵a里面的值了


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
np.array比较运算

比较运算符：
<, <=
>, >=
==
!=
注意，比较运算返回的结果时布尔值


np.random.seed(888)
a = np.random.randint(10,size = 13)
print(a)
    [6 3 7 9 1 0 0 9 3 0 6 3 2]
print(a < 7)
[ True  True False False  True  True  True False  True  True  True  True  True]
发现，所有小于7的元素，返回的都是True


此外我们根据上面的方法，结合数学运算，可以进行更加复杂的判断：


a = np.random.randint(10,size = 15)
print(a)
[4 9 0 4 8 2 8 1 8 0 2 2 3 5 9]

print(2 * a == 3 * a)
[False False  True False False False False False False  True False False False False False]
这个表示，判断数组a乘2后里面哪些值与数组a乘3后相等，我们发现第二个数值，0，满足条件


这种运算也可以用到多维数组


这种判断运用在实际案例中可以表示为：
比如数组中的每一个值是员工工资，1代表月收入1万块，
那么现在我想要统计月收入小于5万的人有几个，


np.random.seed(10)
a = np.random.randint(10,size = 15)
print(a)
[9 4 0 1 9 0 1 8 9 0 8 6 4 3 0]

less_than_5w = np.sum(a<5)
print(less_than_5w)
    return: 9
   
我们通过sum方法计算一共有几个true值，注意，true = 1，false = 0，所以最后的sum就是我们要找的月收入小于5w的员工数量


再比如我们想看看这个数组中有几个偶数：

a = np.random.randint(10,size = 15)
print(a)
even_num = np.sum(a % 2 == 0)
print(even_num)
    [3 2 7 4 7 1 5 6 8 9 1 1 8 6 9]
    6

多维数组中想要看每一行的有几个偶数，就可以np.sum(a % 2 == 0,axis = 1)
多维数组中想要看每一列的有几个偶数，就可以np.sum(a % 2 == 0,axis = 0)
这个方法同样适用于any和all方法


那如果我们想看数组中大于3并且小于5的有几个怎么办呢？

a = np.random.randint(10,size = 15)
print(a)
print(np.sum((a>3) & (a<5)))
    [9 6 3 5 3 7 8 4 4 1 9 6 7 8 4]
    3


那如果我们想看数组中等于3或者小于5的有几个怎么办呢？

a = np.random.randint(10,size = 15)
print(a)
print(np.sum((a==3) | (a<5)))
    [9 7 6 8 4 7 5 7 9 7 1 5 2 9 9]
    3


那么“非”运算怎么办呢？即，概率论中的非
非 a == 3的效果与a != 3是一样的
我们使用“~”表示非


a = np.random.randint(10,size = 15)
print(a)
print(np.sum(~(a>3)))
    [4 8 1 4 3 4 0 5 5 4 9 6 3 6 6]
    4
表示a中不大于3的有几个






当然我们也可以使用numpy中的np.count_nonzero()来实现，效果是一样的

print(np.count_nonzero(a<5))
    return: 9
    
当然我们可以通过这个方法查看我们的矩阵中是否有0元素，因为我们在regression中需要full rank
print(np.sum(a==0))
    [9 4 0 1 9 0 1 8 9 0 8 6 4 3 0]
    return: 4
发现有4个为0的值，

如果我们不想数出几个为零的值，只是想判断是否有0值，则可以使用np.any(a == 0)

np.random.seed(10)
a = np.random.randint(10,size = 15)
print(a)
print(np.any(a == 0))
    [9 4 0 1 9 0 1 8 9 0 8 6 4 3 0]
    True

类似的逻辑判断还有：
all()方法

np.random.seed(10)
a = np.random.randint(10,size = 15)
print(a)
print(np.all(a == 0))
    [9 4 0 1 9 0 1 8 9 0 8 6 4 3 0]
    False




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ndarray数组的运算


数组与标量的运算：
标量是与数组运算的一个元素或者另一个数组，
那么，用一个数组与标量运算，则是让数组内的每一个元素和标量进行相同的运算

获取平均值：
a = np.arange(24).reshape((2,3,4))
print(a.mean())
    11.5
    
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]

     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
      
让a除以a的平均值：
b = a.mean()
print(a/b)
    [[[0.         0.08695652 0.17391304 0.26086957]
      [0.34782609 0.43478261 0.52173913 0.60869565]
      [0.69565217 0.7826087  0.86956522 0.95652174]]

     [[1.04347826 1.13043478 1.2173913  1.30434783]
      [1.39130435 1.47826087 1.56521739 1.65217391]
      [1.73913043 1.82608696 1.91304348 2.        ]]]
      
      
ndarray中的一元函数：
1. np.abs(x)    绝对值
2. np.fabs(x)   绝对值
3. np.sqrt(x)   平方根
4. np.square(x) 平方
5. np.log(x)    对数(以e为底）
6. np.log10(x)  10为底的对数
7. np.log2(x)   2为底的对数
8. np.ceil(x)   取ceiling值，表示不超过元素x的整数值
9. np.floor(x)  取floor值，表示不超过x的最大整数值
10.np.rint(x)   计算数组元素的四舍五入值
11.np.modf(x)   将整数与小数部分以两个独立数组形式返回
12.np.cos(x)    计算普通cos
13.np.cosh(x)   计算双曲cos
14.np.sin(x)    计算普通sin
15.np.sinh(x)   计算双曲sin
16.np.tan(x)    计算普通tan
17.np.tanh(x)   计算双曲tan
18.np.exp(x)    计算指数
19.np.sign(x)   计算各族元素的符号值1(+),0(),-1(-)
20.np.power(base,power) 计算幂次方，计算结果为base^power,比如2的3次方就是 np.power(2,3)



例子：
a = np.arange(24).reshape((2,3,4))
对a内所有元素取平方
b = np.square(a)
    [[[  0   1   4   9]
      [ 16  25  36  49]
      [ 64  81 100 121]]

     [[144 169 196 225]
      [256 289 324 361]
      [400 441 484 529]]]
      
注意，绝大部分一元函数运算后是生成一个新的数组，而不是替换掉a

将a开方后再复制给a，来替换数据
a = np.arange(24).reshape((2,3,4))
a = np.sqrt(a)
    [[[0.         1.         1.41421356 1.73205081]
      [2.         2.23606798 2.44948974 2.64575131]
      [2.82842712 3.         3.16227766 3.31662479]]

     [[3.46410162 3.60555128 3.74165739 3.87298335]
      [4.         4.12310563 4.24264069 4.35889894]
      [4.47213595 4.58257569 4.69041576 4.79583152]]]
      
      
使用modf(x)
将整数和小数部分分开返回
a = np.arange(24).reshape((2,3,4))
a = np.sqrt(a)
b = np.modf(a)
print(b)
    (array([[[0.        , 0.        , 0.41421356, 0.73205081],
             [0.        , 0.23606798, 0.44948974, 0.64575131],
             [0.82842712, 0.        , 0.16227766, 0.31662479]],

            [[0.46410162, 0.60555128, 0.74165739, 0.87298335],
             [0.        , 0.12310563, 0.24264069, 0.35889894],
             [0.47213595, 0.58257569, 0.69041576, 0.79583152]]]), 
     array([[[0., 1., 1., 1.],
             [2., 2., 2., 2.],
             [2., 3., 3., 3.]],

            [[3., 3., 3., 3.],
             [4., 4., 4., 4.],
             [4., 4., 4., 4.]]]))



注意，numpy的核心思想是让用户吧每一个数组当做是一个数字来看待

二元函数，即两个数组之间的运算：

+ - * / **          加减乘除乘方
np.maximum(x,y)     元素级的最大值最小值
np.fmax()           元素级的最大值最小值
np.minimum(x,y)     元素级的最大值最小值
np.fmin()           元素级的最大值最小值
np.mod(x,y)         元素级的模运算
np.copysign(x,y)    将y中个元素的符号拿出来赋值给x中的元素
> < >= <= == !=     大小比较


例子：

a = np.arange(24).reshape((2,3,4))
b = np.sqrt(a)
c = np.maximum(a,b)
print(c)
    [[[ 0.  1.  2.  3.]
      [ 4.  5.  6.  7.]
      [ 8.  9. 10. 11.]]

     [[12. 13. 14. 15.]
      [16. 17. 18. 19.]
      [20. 21. 22. 23.]]]
注意：通过max做运算，只要两个数组type不同，最后生成的就是浮点数


a = np.arange(24).reshape((2,3,4))
b = np.sqrt(a)
c = a>b
print(c)
    [[[False False  True  True]
      [ True  True  True  True]
      [ True  True  True  True]]

     [[ True  True  True  True]
      [ True  True  True  True]
      [ True  True  True  True]]]


矩阵的乘法matrix multiplication

a = np.arange(4).reshape(2,2)
    [[0 1]
     [2 3]]

b = np.full((2,2),10)
    [[10 10]
     [10 10]]
     
若想按照矩阵的乘法规则，不能直接使用a*b命令，而是要：

print(a.dot(b))
    [[10 10]
     [50 50]]
     
注意，dot方法是可以自动判断应该使用行向量还是列向量的，比如：
a是2*2的矩阵，现在有一个1*2的向量v，按照数学规则，a*v是无法计算的，
但是，a.dot(v)方法可以自动识别并将v转置成一个2*1的列向量，然后再与矩阵a相乘


如果直接使用a*b，程序会把两个数组对应的值相乘

print(a*b)
    [[ 0 10]
     [20 30]]

or you can use this function to execute matrix multiplication
np.matmul(matrix_a, matrix_b)


    def random_matrix(m,n):
         out = [[random.random() for col in range(n)] for row in range(m)]
    
         return out
    
    rand_a = random_matrix(400,300)
    rand_b = random_matrix(300,400)
    x2 = np.matmul(rand_a, rand_b)


     
矩阵的转置 matrix transpose

print(a.T)
    [[0 2]
     [1 3]]
     
     
矩阵的逆  inverse of a matrix

需要使用np.linalg.inv() linalg是lineaer algebra的缩写，inv是inverse的缩写
print(np.linalg.inv(a))
    [[-1.5  0.5]
     [ 1.   0. ]]


通过逆矩阵与原矩阵相乘= 1验证是否计算正确：
inv_a = np.linalg.inv(a)
print(inv_a.dot(a))
    [[1. 0.]
     [0. 1.]]
     
     
对于non-squared matrix而言，直接使用inverse命令无法进行逆矩阵的求解，这时候我们就需要使用np.linalg.pinv()

x = np.arange(14).reshape(2,7)
print(x)
    [[ 0  1  2  3  4  5  6]
     [ 7  8  9 10 11 12 13]]

print(np.linalg.pinv(x))
    [[-0.17346939  0.06632653]
     [-0.12244898  0.05102041]
     [-0.07142857  0.03571429]
     [-0.02040816  0.02040816]
     [ 0.03061224  0.00510204]
     [ 0.08163265 -0.01020408]
     [ 0.13265306 -0.0255102 ]]

pinv中的p是pseudo的缩写


向量与矩阵的运算 operation between vector and matrix
a
 [[0 1]
 [2 3]]
 
 创建一个1*2的向量vector：
 vector = np.arange(1,3).reshape(1,2)
    [[1 2]]

我们知道在数学上矩阵运算必须维度相同，如果直接让vector和a相加，数学上是无法计算的，但是numpy会把a中的每一行与vector相加
print(vector + a)
    [[1 3]
     [3 5]]
     
如果我们想把vector变成一个2*2的矩阵怎么办呢：使用vstack方法：

matrix_v = np.vstack([vector] * a.shape[0])
print(matrix_v)
    [[1 2]
     [1 2]]

矩阵a有两行，所以我们要使用a.shape[0]来获取到这个信息（0表示最外层的维度，比如3行的话，shape【0】就是3
vstack中的方括号中放入要改变结构的数组vector，然后乘以a的层数，新的matrix_v就是拥有两行两列的一个matrix了


也可以通过tile()方法进行向量堆叠

new_matrix = np.tile(vector,(2,1))
print(new_matrix)

np.tile()中第一个参数为要堆叠的目标数组（vector），第二个参数选择要堆叠的数量，比如(2,1)表示new_matrix拥有两行vector和一列vector的值
即：
    [[1 2]
     [1 2]]
 
 如果：
 new_matrix = np.tile(vector,(2,2))
     
    [[1 2 1 2]
     [1 2 1 2]]


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
数组的合并：

水平合并数组：np.hstack()    h for horizontal
    
    np.random.seed(1)
    a = np.random.randint(1,10,(4,4))
    print(a)
        [[6 9 6 1]
         [1 2 8 7]
         [3 5 6 3]
         [5 3 5 8]]
    
    np.random.seed(2)
    b = np.random.randint(1,10,(4,1))
    print(b)
        [[9]
         [9]
         [7]
         [3]]
    
    c = np.hstack((b,a))
    print(c)
        [[9 6 9 6 1]
         [9 1 2 8 7]
         [7 3 5 6 3]
         [3 5 3 5 8]]
    
    注意，合并之前，两个数组的dimension必须相同，如：a是4*4的矩阵，b必须是4*n的矩阵才能水平合并，
    合并的时候那个矩阵写在前面，最后的结果里哪个矩阵的元素就在前面



垂直合并数组：np.vstack()

    
    np.random.seed(1)
    a = np.random.randint(1,10,(4,4))
    print(a)
        [[6 9 6 1]
         [1 2 8 7]
         [3 5 6 3]
         [5 3 5 8]]
    
    np.random.seed(2)
    b = np.random.randint(1,10,(1,4))
    print(b)
        [[9 9 7 3]]
    
    c = np.vstack((b,a))
    print(c)
        [[9 9 7 3]
         [6 9 6 1]
         [1 2 8 7]
         [3 5 6 3]
         [5 3 5 8]]

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

numpy数据csv存取

写入csv：
np.savetxt(frame,array,fmt=%.18e,delimiter=None)
frame：文件名，，，，文件、字符串或者产生器，可以使.gz或bz2的压缩文件
array：存入文件的数组
fmt：format默认为$18e，18位科学计数法，也可选择%d用整数体现,%.2f两位浮点数，这是我们主要需要修改的
delimiter：分隔字符串，默认是空格，所以在保存为csv是，我们要将delimiter改为“ , ”

a = np.arange(24).reshape((3,8))
np.savetxt("a.csv",a,fmt="%d",delimiter=",")
用整数保存
np.savetxt("b.csv",a,fmt="%.1f",delimiter=",")
用1位浮点数保存




读取csv
np.loadtxt(frame,dtype=np.float,delimiter=None,unpack=False)

frame:文件名
dtype：默认为浮点数
delimiter：默认为空格，对于csv需要修改为“ , ”
unpack：默认为false表示将读入的数据写入一个数组，若为true则分别写入不同变量

a = np.arange(24).reshape((3,8))
b=np.loadtxt("a.csv",delimiter=",")
print(b)
    [[ 0.  1.  2.  3.  4.  5.  6.  7.]
     [ 8.  9. 10. 11. 12. 13. 14. 15.]
     [16. 17. 18. 19. 20. 21. 22. 23.]]

a = np.arange(24).reshape((3,8))
b=np.loadtxt("a.csv",dtype = int, delimiter=",")
print(b)
    [[ 0  1  2  3  4  5  6  7]
     [ 8  9 10 11 12 13 14 15]
     [16 17 18 19 20 21 22 23]]
     
     
     
注意，csv只能存储和读取一维和二维数组
即savetxt与loadtxt只能存储一维和二维数据存取


多维数据存取：

储存：
a.tofile(frame,sep="",format="%s")

a = np.arange(100).reshape((5,10,2))
b=a.tofile("a.dat",sep=",",format="%d")
存储后，并没有按照任何维度存储，只是单一的按照顺序存储。

如果不该写sep参数，将不以逗号分隔，而是采用二进制存储。这样更节省空间‘
a = np.arange(100).reshape((5,10,2))
b=a.tofile("a.dat",format="%d")

读取：
np.fromfile(frame,dtype=float,count=-1,sep="")
dtype 默认为浮点数
count表示读入元素的个数，-1为整个文件，用户可以按照想读入的个数修改
sep为分隔符，如果是空，则写入为二进制模式

a = np.arange(100).reshape((5,10,2))
b=np.fromfile("a.dat",dtype=int)
    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95
 96 97 98 99]
 
 
注意，存储文件以什么模式分隔，读取时就得按照什么模式读取
比如存的时候是二进制，读取时候也得是二进制。
为了获得和保存前一样的维度，需要重新reshape

a = np.arange(100).reshape((5,10,2))
b=np.fromfile("a.dat",dtype=int).reshape((5,10,2))
    [[[ 0  1]
      [ 2  3]
      [ 4  5]
      [ 6  7]
      [ 8  9]
      [10 11]
      [12 13]
      [14 15]
      [16 17]
      [18 19]]...
      

使用这个方法需要读取时候需要知道原来保存时候的维度
为了明细，一般会写一个文本文件记录，方便查找


还有一个存储方法，可以解决多维存储


保存：

np.save(frame,array)
np.savez(fname,array)压缩版本
frame以.npy为扩展名，压缩扩展名为.npz
array：数组变量

a = np.arange(100).reshape((5,10,2))
np.save("a.npy",a)



读取：

np.load(fname)
frame:文件名

a = np.arange(100).reshape((5,10,2))
b = np.load("a.npy")
print(b)
    [[[ 0  1]
      [ 2  3]
      [ 4  5]
      [ 6  7]
      [ 8  9]
      [10 11]
      [12 13]
      [14 15]
      [16 17]
      [18 19]]....
      
这种保存方式不会打乱维度信息

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
随机数函数：

np.random.normal    生成服从正态分布的随机数组
np.random.rand()    根据维度形状生成0-1的浮点数，均匀分布
np.random.randn()   n维数组，符合标准正态分布
np.random.randint() 根据shape，在low到high的范围内生成随机整数或整数组
np.random.seed(s)    随机数种子，s是给定的种子值



np.random.normal(loc,scale,size)
    loc：均值
    scale：方差
    size：数组结构
    
a = np.random.normal(10,30,(3,4))
print(a)
    生成服从均值为10，方差为30的随机数，并以3*4的矩阵形式呈现
    [[ -5.40455182  33.58608946   0.62650895  47.37406904]
     [ -5.75451958  -3.26541336  19.32308783  72.56708046]
     [-10.8587582  -12.29448777 -25.40316062   9.10698155]]



np.random.rand()    根据维度形状生成0-1的浮点数，均匀分布
a = np.random.rand(2,3,4)
print(a)
    [[[7.61372215e-01 1.46586750e-01 2.99542474e-01 6.07885834e-01]
      [8.14041989e-01 6.37683232e-04 3.66512342e-01 9.64629666e-01]
      [2.29769233e-01 3.12180435e-02 8.20902334e-01 6.34813484e-01]]

     [[7.75669378e-01 5.60232947e-01 9.60492087e-03 3.93161060e-02]
      [1.43558619e-01 1.28975025e-01 4.04538312e-01 7.00540308e-01]
      [8.81168880e-01 1.51341606e-01 7.77822201e-01 5.52614394e-01]]]
      
      
np.random.randn()   n维数组，符合标准正态分布
a = np.random.randn(2,3,4)
print(a)
    [[[-1.38058703  1.38255226 -0.47216249 -0.50449782]
      [-0.31253921  0.02457796 -0.05962786 -0.05775003]
      [ 0.16291162  0.14855361  0.05267478 -0.03414522]]

     [[-0.13412169 -1.89885247  0.67552791  1.38936658]
      [-1.25853178  0.31746718 -0.43811007 -0.25676774]
      [ 0.34726301  1.09429811  0.82878922 -0.81764712]]]


np.random.randint(low,high,shape) 根据shape，在low到high的范围内生成随机整数或整数组

a = np.random.randint(1,10,(3,4))
print(a)
    [[9 4 4 6]
     [2 9 6 1]
     [1 2 5 8]]

最小值为1，最大值为9，shape=3,4

np.random.seed(s)    随机数种子，s是给定的种子值

a = np.random.seed(9)
b = np.random.randint(20,100,(3,4))
c = np.random.seed(9)
d = np.random.randint(20,100,(3,4))
print(b)
print(d)
    [[74 76 42 85]
     [42 72 79 60]
     [53 20 80 79]]
 
    [[74 76 42 85]
     [42 72 79 60]
     [53 20 80 79]]
种子相当于一个命名作用，你使用第九个种子生成b，然后再使用第九个种子生成d，两个是相同的
当你把d的shape改变是，会发现第一行还是一样的

a = np.random.seed(9)
b = np.random.randint(20,100,(3,4))
c = np.random.seed(9)
d = np.random.randint(20,100,(3,10))
print(b)
print(d)
    [[74 76 42 85]
     [42 72 79 60]
     [53 20 80 79]]

    [[74 76 42 85 42 72 79 60 53 20]
     [80 79 94 76 82 32 38 76 21 76]
     [31 57 39 29 76 69 83 33 79 78]]
     
a = np.random.seed(9)
b = np.random.randint(20,100,(3,4))
c = np.random.seed(9)
d = np.random.randint(20,100,(1,10))
print(b)
print(d)   
    [[74 76 42 85]
     [42 72 79 60]
     [53 20 80 79]]

    [[74 76 42 85 42 72 79 60 53 20]]
    
 



高级随机数函数


np.random.shuffle(a)                  根据数组a的第0轴（即第一个维度）进行随机排列，改变数组x，而后a被改变，
np.random.sort(a,axis = 1)           将数组a内的数据按照从小到大的顺序重新排列
np.argsort(a)               返回排序后每个元素在乱序数组a中的索引位置
np.random.permutation(a)              根据数组a的第0轴（即第一个维度）进行乱序排列，但是不改变数组x，而是生成新的数组
np.random.choice(a[,size,replace,p])  从一维数组a中按照概率p抽取元素，形成size形状的新数组，replace表示是否可以重复，默认false，表示可以重复



shuffle(a)

a = np.random.randint(100,200,(3,4))
print(a)
b = np.random.shuffle(a)
print(a)
    [[102 128 153 165]
     [191 154 110 153]
     [178 141 171 177]]
shuffle后    
    [[191 154 110 153]
     [102 128 153 165]
     [178 141 171 177]]
第一轴，即，第一维度是3，也就是列，那么对列进行随机打乱也就是每一列的值相同，但是打乱列的顺序
!!!!
!!!!
注意，超级大坑：
shuffle a之后，虽然赋值给b，但是打印b是打印不出任何东西的，必须要打印a才能看到结果，即，对原数据进行了打乱，所以原数据也被修改了
若不想改变原数组，请用permutation


a = np.random.randint(100,200,(2,3,4))
print(a)
b = np.random.shuffle(a)
print(a)
    [[[177 177 156 140]
      [167 103 119 102]
      [178 124 102 135]]

     [[176 118 178 121]
      [193 120 108 143]
      [172 109 123 191]]]
shuffle后      
    [[[176 118 178 121]
      [193 120 108 143]
      [172 109 123 191]]

     [[177 177 156 140]
      [167 103 119 102]
      [178 124 102 135]]]
      
第一维度是2，所以只是调换了位置，其余内容均相同


np.sort()

a = np.arange(16).reshape(4,4)
    [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]
     [12 13 14 15]]
b = np.random.permutation(a)
    [[ 0  1  2  3]
     [12 13 14 15]
     [ 4  5  6  7]
     [ 8  9 10 11]]
c = np.sort(b)
    [[ 0  1  2  3]
     [12 13 14 15]
     [ 4  5  6  7]
     [ 8  9 10 11]]

！！！！！！！！！！！注意，sort若不设置axis，默认为axis = 1，即只能将每一行进行重新排序，无法对整个矩阵重新排序
若想对其他维度进行排序可以通过修改axis参数的方式调整

np.random.seed(666)
a = np.random.randint(15,size = (3,4))
print(a)
    [[12  2 13 14]
     [14  6  9 14]
     [ 4 13 11 14]]

b = np.random.permutation(a)
print(b)
    [[ 4 13 11 14]
     [14  6  9 14]
     [12  2 13 14]]

c = np.sort(b,axis = 0)
print(c)
    [[ 4  2  9 14]
     [12  6 11 14]
     [14 13 13 14]]

axis = 0表示沿着第0轴也就是每一行对应值进行排序。
这个数组有三行，所以，会先把这三行的第一个值4,14,12取出来，然后进行排序，变成4,12,14，放入新的数组c中，
然后再把这三行的第二个值13,6,2取出来进行排序变成2,6,13.。。。。以此类推
所以我们看到的效果是按照列进行大小排序






注意，sort方法是生成一个重新排好序的数组，不会对原数组进行修改
对于使用shuffle方法将原数组打乱顺序后，想要直接将原数组进行排序的话，需要使用a.sort()，即面向对象的方式调用

a = np.arange(16)
print(a)
    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
b = np.random.shuffle(a)
print(a)
    [ 9  4 15 11  1 10  0  7 14  6 13  5 12  3  8  2]
a.sort()
print(a)
    [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]
    
    
np.argsort(a)

a = np.arange(16)
b = np.random.shuffle(a)
print(a)
[ 6  3 14  2  4  7 11  1 12  9 10 13  8  0 15  5]

c = np.argsort(a)
print(c)    
[13  7  3  1  4 15  0  5 12  9 10  6  8 11  2 14]    

数组c中的数字并不是值，而是将乱序数组a排序后，返回他们在乱序状态下的位置
比如，打乱的数组a中，数字0在第13位，所以，argsort(a)的第一个值是13，
数字1在乱序数组a中的位置是第7位，所以是数字7





  
permutation(a)              根据数组a的第0轴（即第一个维度）进行乱序排列，但是不改变数组x，而是生成新的数组

功能与shuffle()相同，只是不会改变原数组

a = np.random.randint(100,200,(3,4))
print(a)
b = np.random.permutation(a)
print(b)
    [[175 139 175 152]
     [162 157 135 139]
     [154 104 195 164]]
     
    [[154 104 195 164]
     [162 157 135 139]
     [175 139 175 152]]


permutation的另一个用法：

    如果np.random.permutation()中传入的不是一个列表而是一个数字，比如5
    那么，他会自动生成一个0~4的列表，然后对列表里的5个元素进行乱序排列
        a =  np.random.permutation(5)
            [1 3 2 4 0]




choice(a[,size,replace,p])  从一维数组a中按照概率p抽取元素，形成size形状的新数组，replace表示是否可以重复，默认True，表示可以重复

a = np.random.randint(100,200,(10))
print(a)
b = np.random.choice(a,(3,2))
print(b)
    [162 189 138 161 173 120 176 195 102 109]
b:    
    [[176 176]
     [173 102]
     [120 161]]
     
a = np.random.randint(100,200,(10))
print(a)
b = np.random.choice(a,(3,2),replace=False)
print(b)
将repalce设置为false则不会重复
    [165 112 108 196 182 179 132 152 110 161]
    
    [[110 161]
    [179 196]
    [152 108]]


设置概率：
a = np.random.randint(100,200,(10))
print(a)
b = np.random.choice(a,(3,2),p=a/np.sum(a))
表示，a中的值越大，被抽取的概率越高
print(b)
    [188 145 127 116 158 123 159 143 168 176]
    
    [[158 127]
     [176 188]
     [159 176]]
     
     
按照分布函数生成随机数：

uniform(low,high,size)      low起始值，high结束值，size形状
normal(loc,scale,size)      loc均值，scale标准差，size形状
poisson(lam,size)           lam随机事件发生概率，size形状

uniform(low,high,size)

a = np.random.uniform(0,10,(3,4))

[[4.53297702 2.02833113 4.30927178 2.51916885]
 [4.15649038 4.78977995 3.8044613  0.02240229]
 [5.21203576 9.93738236 2.97805628 5.76460852]]


normal(loc,scale,size)

a = np.random.normal(100,10,(3,4))

[[ 85.64914051 109.96524152  96.32842761 103.77608184]
 [ 98.46078518 103.44922325 109.18971026  90.96066979]
 [ 97.3080624   92.98079553 109.61646302 101.32681867]]
 
 

poisson(lam,size)
a = np.random.poisson(20,(3,4))
[[30 17 24 21]
 [25 17 24 17]
 [29 19 29 28]]
 
 
 
 
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 
 
统计函数：

np.sum(a,axis=None)                    求和，axis=none表示对所有轴求和，如果要对特定轴进行计算，可以axis=1，axis=2.。。
np.mean(a,axis=None)                   期望
np.average(a,axis=none,weights=none)   加权平均值
np.std(a,axis=none)                    标准差
np.var(a,axis=none)                    方差


普通sum:

a = np.random.poisson(20,(3,4))
b = sum(a)
print(a)
print(b)

[[14 18 18 19]
 [18 22 16 18]
 [20 22 24 18]]
 求和是每一列相加，52=14=18=20
 [52 62 58 55]

numpy求和np.sum()

a = np.random.poisson(20,(3,4))
b = np.sum(a)
print(a)
print(b)

[[29 25 12 27]
 [17 28 21 18]
 [20 21 16 16]]

250


按维度求和：
生成一个3*4的数组
a = np.random.randint(1,12,(3,4))
    [[ 4 11  5  3]
     [11  5  4  9]
     [ 3  1  7  4]]

summation = np.sum(a,axis = 0)
    [18 17 16 16]

我们设置axis = 0表示按照第一个维度求和。所谓第一个维度就是列表内的第一层数据，我们发现a这个列表中有两层，
第一层是由三个子列表组成的即[ 4 11  5  3]，[11  5  4  9]和[ 3  1  7  4]]，也就是三行
那么，按照第0轴求和也就是每次将每一行中相同位置的数字进行加总，，效果其实就是求这个矩阵每一列的总和
换一种说法：按每个轴求和可以看做是一个压缩的操作：
按照第0轴，也就是行为单位进行压缩，我们有三行，若压缩成一行，就需要从上到下压扁，自然而然三行就变成一行了
三行变一行我们就需要把每一行对应位置的数值加起来。
18 = 4 + 11 + 3
17 = 11 + 5 + 1...

axis = 1表示按照第1轴，其实就是第二个维度，也就是每一行进行求和。
summation = np.sum(a,axis = 1)
    [23 29 15]
23 = 4 + 11 + 5 + 3...
若按照压缩思路解释：
axis = 1表示按照第1轴，也就是以列为单位进行压缩，相当于从左到右挤压，就是把四列变成一列，最终就是一个只有三行的列向量
所以我们要对每一行进行求和



np.prod()表示求数组内所有数字的乘积

np.prod(a)就是把a内所有的数字相乘
np.prod(a+1)就是把a内所有数字先加1再相乘

a = np.random.randint(1,12,(3,4))
    [[ 6 11 10  6]
     [ 9  6  4  8]
     [ 4  9  9  7]]
     
print(np.prod(a))
'''
return:
    -1660217344
'''
有时候乘积会变成负数，这是因为整数溢出问题导致的，默认的int32位不够用，这是需要手动调整dtype为int64
print(np.prod(a,dtype = 'int64')) 



np.mean()
a = np.random.poisson(20,(3,4))
b = np.mean(a)
print(a)
print(b)

[[21 22 24 21]
 [17 17 16 31]
 [19 17 18 20]]
20.25

a = np.random.poisson(20,(3,4))
b = np.mean(a,axis=1)
这里1表示对第二维度求平均数，注意第一维度是0。这里第一维度是行，第二维度是列，那么对列求平均是，其实说的就是每一行求一个平均值。
print(a)
print(b)

[[16 15 21 23]
 [21 20 27 24]
 [17 25 25 20]]
返回了三行每一行的平均值
[18.75 23.   21.75]


对第一维度求平均值：

a = np.random.poisson(20,(3,4))
b = np.mean(a,axis=0)
print(a)
print(b)

[[18 21 26 23]
 [17 18 23 19]
 [16 19 18 17]]
 
[17.         19.33333333 22.33333333 19.66666667]
第一维度是行，对行求平均值就是将每一行的每一列加总求平均值，
17=（18+17+16）/3
19.3333333=（21+18+19）/3



其他统计函数
min(a)      计算数组a中元素的最小值
max(a)      计算数组a中元素的最大值
argmin(a)   计算数组a中最小值后返回这个最小值在一维数组中的位置
argmax(a)   计算数组a中最大值后返回这个最大值在一位数组中的位置
unravel_index(index,shape)  根据shape将一维下标（即位置）转换为多维下标
ptp(a)      计算数组中元素最大值与最小值的差
median(a)   计算数组中元素的中位数
percentile(a,q = percent) 列出数组a中第百分之q位置对应的值（如四分位数）,若无法对应数组中准确数字，则会根据前后两个数字的数学运算求解后显示


a = np.arange(10)
    [0 1 2 3 4 5 6 7 8 9]


result = []
for percentage in [0,25,50,75,100]:
    position = np.percentile(a,q = percentage)
    result.append(position)
print(result)
    [0.0, 2.25, 4.5, 6.75, 9.0]




a = np.arange(15,0,-1)
表示从15开始，1结束，步长为-1，表示倒着走
[15 14 13 12 11 10  9  8  7  6  5  4  3  2  1]
a = np.arange(15,0,-3)
[15 12  9  6  3]

max

a = np.arange(15,0,-1).reshape(3,5)
b = np.max(a)
print(a)
print(b)

[[15 14 13 12 11]
 [10  9  8  7  6]
 [ 5  4  3  2  1]]

15

argmin

a = np.arange(15,0,-1).reshape(3,5)
b = np.argmin(a)
print(a)
print(b)
[[15 14 13 12 11]
 [10  9  8  7  6]
 [ 5  4  3  2  1]]
注意，位置是从0开始的，所以，14表示第15个数字
14


unravel_index()

a = np.arange(15,0,-1).reshape(3,5)
b = np.unravel_index(np.argmin(a),a.shape)
print(a)
print(b)

[[15 14 13 12 11]
 [10  9  8  7  6]
 [ 5  4  3  2  1]]
 2表示第三行，4表示第五列，也就是最后一个数字1
(2, 4)


ptp 

a = np.arange(15,0,-1).reshape(3,5)
b = np.ptp(a)
print(a)
print(b)

[[15 14 13 12 11]
 [10  9  8  7  6]
 [ 5  4  3  2  1]]
最大，最小值的差为14
14


median

a = np.arange(15,0,-1).reshape(3,5)
b = np.median(a)
print(a)
print(b)

[[15 14 13 12 11]
 [10  9  8  7  6]
 [ 5  4  3  2  1]]
中位数，因为是运算，所以结果为浮点数
8.0


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
numpy的梯度函数

np.gradient(f) 计算数组f中的梯度，当f为多维是，返回每个维度的梯度

梯度：连续值之间的变化率，即斜率
比如三个数 a，b，c
b的梯度：（c-a)/2
其中2是a与c之间的距离

例子：
a = np.random.randint(0,20,5)
print(a)
在区间0~20随机取5个整数

a = np.random.randint(0,20,5)
print(a)
b = np.gradient(a)
print(b)

[14  0  1  6 13]
-6.5表示的是第二个元素的梯度，即0的梯度，他等于0后面的数减去前面的数，除以两数之间的距离
-6.5 = (1-14)/2
3 = (6-0)/2
对于最开始和结束的两个值，14与13，他们的梯度等于与他们相邻的数的差，除以距离1
-14 = (0-14)/1
7 = (13-6)/1
[-14.   -6.5   3.    6.    7. ]


对于二维数据梯度值的计算

a = np.random.randint(0,20,(3,5))
print(a)
b = np.gradient(a)
print(b)

[[17  9 10 17 15]
 [ 4 11 10  4  7]
 [ 6  5 15 15 11]]
 
最外层维度的梯度值
[array([[-13. ,   2. ,   0. , -13. ,  -8. ],
       [ -5.5,  -2. ,   2.5,  -1. ,  -2. ],
       [  2. ,  -6. ,   5. ,  11. ,   4. ]]), 
第二层维度的梯度值   
array([[-8. , -3.5,  4. ,  2.5, -2. ],
       [ 7. ,  3. , -3.5, -1.5,  3. ],
       [-1. ,  4.5,  5. , -2. , -4. ]])]









====================
1. find the index of a particular value by using np.where()


    example: find the index of whose value is '.'
    return_list = tbill_df['rate_of_return'].values 
    row_list = np.where(return_list == '.')[0]




====================

np.ravel() 把多维变成一个list



a = np.array([[1,1,1],[2,2,2]])
b = a.ravel()
print(b):   [1 1 1 2 2 2]





====================
Remove a list of items from a ndarray (setdiff1d).
    If you want to remove items in b from a:

    a = np.array([1,2,4,5])
    b = np.array([1,5])
    a = np.setdiff1d(a,b)
    print(a)
    #   result: [2 4]











====================
Split an array/list into multiple sub_lists

    np.array_split(<array>, n_splits)



"""
a = np.array([[1,1,1],[2,2,2]])
b = a.ravel()
print(b)












