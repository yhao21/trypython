import time
from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets
import pandas as pd
from sklearn.model_selection import KFold
from sklearn import metrics,linear_model

"""
KNN  K nearest neighbor


优点：思想简单，数学少，效果好
缺点：


时间    
    |
    |
    |
    |
    |
    |                               *
    |                            ——   
    |                   ——  ——
    |   +                     ——  
    |    +   +          ——      ——
    |   +
    |      + +
    |______________________________________________________
                                                        肿瘤大小


假设：
+ 代表良性肿瘤
— 代表恶性肿瘤


那么当我们新出现一个肿瘤 * 时，我们如何判断他是良性还是恶性肿瘤呢


根据经验，我们领  K = 3，表示，取离新加入的点 * 最近的3个点，以他们自己的特征(肿瘤大小，时间)判断这个新的点 * 是良性还是恶性肿瘤

我们可以发现，* 很有可能是恶性肿瘤




时间    
    |
    |
    |
    |
    |
    |                               
    |                            ——   
    |                   ——  ——
    |   +    +   O   ——           ——  
    |    +   +          ——      ——
    |   +
    |      + +
    |______________________________________________________
                                                        肿瘤大小


比如现在又有一个新的点 'O'，我们发现距离这个点 'O' 最近的三个obs是两个 '+' 和一个 '——'，
对着三个点来说，+ 和 —— 的数量比是2:1，那么K nearest neighbor会告诉我们这个新的点 'O' 很可能和 + 属于同一类，是良性肿瘤





这就是K nearest neighbor 解决分类问题，
当然也可以解决回归问题，，以后再讲
"""
"""

我们使iris数据集
    iris = datasets.load_iris()
    data_source = pd.DataFrame(iris.data)
    target_source = pd.DataFrame(iris.target)
    data = data_source.iloc[:,2:].values
    target = target_source.iloc[:,:].values
    
将target和data合并起来
    data = np.hstack((target,data))
      target   x1  x2
        [[0.  1.4 0.2]
         [0.  1.4 0.2]
         [0.  1.4 0.2]
         ...
         [1.  4.7 1.4]
         [1.  4.5 1.5]
         [1.  4.9 1.5]
         ...
         [2.  5.  1.9]
         [2.  5.2 2. ]
         [2.  5.4 2.3]
         [2.  5.1 1.8]]
   
将target = 1 的所有行提取出来，命名为set1
将target = 2 的所有行提取出来，命名为set2
    set1 = data[data[:,0] == 1]
        [[1.  4.7 1.4]
         [1.  4.5 1.5]
         [1.  4.9 1.5]
         [1.  4.  1.3]
         [1.  4.6 1.5]
         ....
    set2 = data[data[:,0] == 2]
        [[2.  6.  2.5]
         [2.  5.1 1.9]
         [2.  5.9 2.1]
         [2.  5.6 1.8]
         ....

将set1，set2中的x部分，也就是后两列提取出来（这个数组一共3列）
注意：
sub1是所有target = 1 所对应的x的值
sub2是所有target = 2 所对应的x的值

我们令target = 1 表示良性肿瘤，target = 2 表示恶性肿瘤
那么，sub1对应的就是良性肿瘤所具备的两种特征，sub2是恶性肿瘤所对应的两种特征
    sub1 = set1[:,1:]
        [[4.7 1.4]
         [4.5 1.5]
         [4.9 1.5]
         [4.  1.3]
         ....
    sub2 = set2[:,1:]
        [[6.  2.5]
         [5.1 1.9]
         [5.9 2.1]
         [5.6 1.8]
         ....
将提取出来的sub1和sub2合并成一个打的X数组，这是一个100*2的矩阵
    X = np.vstack((sub1,sub2))

同样逻辑我们把这些x对应的y也提出来，然后合并成一个100*1的矩阵
    Y = np.vstack((set1[:,0].reshape(len(set1),1),set2[:,0].reshape(len(set2),1)))
        [[1.]
         [1.]
         [1.]
         [1.]
        ....
         [2.]
         [2.]
         [2.]
         [2.]]




我们知道：

target = 1 表示良性肿瘤，target = 2 表示恶性肿瘤
sub1表示良性肿瘤所具备的两种特征(x1,x2)，sub2是恶性肿瘤所对应的两种特征(x1,x2)


我们想做的是，用这些数据训练机器，
未来当我们给出一个具备(x1,x2)特征的新的肿瘤sample1，比如[5.6  2]
我们希望机器能够判断他是良性还是恶性肿瘤
    
    sample = np.array([5.6,2])
    plt.scatter(sample[0],sample[1],color = 'green',marker = '+')
    
直观来看这个新的点sample是在恶性肿瘤这个点集群中的
    
    sample = np.array([5.6,2])
    plt.scatter(sub1[:,0],sub1[:,1],color = 'red')
    plt.scatter(sub2[:,0],sub2[:,1],color = 'blue')
    plt.scatter(sample[0],sample[1],color = 'green',marker = '+')
    plt.savefig('sample.png')
    
    
    
如何判断这个点属于哪个集群呢？

方法一：笨办法，计算两点之间的距离，用for循环计算这个点与所有点之间的距离
    
    距离公式：
    二维平面中distance = [(x1 - x2)^2 + (y1 - y2)^2]^(1/2)
    三位平面中distance = [(x1 - x2)^2 + (y1 - y2)^2 + (z1 - z2)^2]^(1/2)
        
        distance = []
        for i in range(len(x_train)):
            d = np.sqrt((sample[0] - x_train[i,0])**2 + (sample[1] - x_train[i,1])**2)
                distance.append(d)
                
    这段代码是在计算sample点和X（包含sub1和sub2，即良性和恶性肿瘤）内每一个点之间的距离，然后保存到一个列表distance里面
    我们也可以使用更简洁的列表生成式写这段for循环
    
        distance1 = [np.sqrt((sample[0] - x_train[i,0])**2 + (sample[1] - x_train[i,1])**2) for i in range(len(x_train))]
    
    我们想知道的是距离这个sample点最近的三个点属于哪个集合（良性还是恶性）
    那么此时我们就要用到np.argsort()这个方法了，他会在告诉你从小到大排序后当前列表内的值会在什么位置上
    比如一个数组a = [5 8 9 5 0]，np.argsort(a)的结果为[4 0 3 1 2]
    np.argsort(a)结果中的第一个数字4表示，a中最小的数字在列表a中的第四列，也就是最后一个。我们发现，a中最后一个就是数字0
    所以下面order中的第一个数字78表示，distance中最小的那个数在第78列，
    
    
        order = np.argsort(distance)
        print(order)
            [78 62 74 53 82 89 66 87 58 54 61 70 52 98 97 90 86 65 93 79 75 95 60 80
             51 92 94 99 85 91 63 84 96 33 64 50 27 71 59 83 73 77 57 69 81 76 20 88
             22  2  6 26 55 36  0 13 72  4 67 56 41 35 23 16 18 34 28  1  8  5 68 15
             25 37 40 24 47 11 46 44 45 49 38  3 21 39 42  9 17 32 12 19 30 14 31 29
             10 43  7 48]
    
    
    现在比如我想找距离sample最近的k个点，比如我们找最近的6个点，即，k = 6
    也就是说，我们只需要在y_train中找到第78,62,74,53,82,和89列对应的值即可

        k = 6
        nearest_6_y_value = [list(y_train[i]) for i in order[:k]]
            [[2.0], [2.0], [2.0], [2.0], [2.0], [2.0]]
        nearest_6_y_value = [j for i in nearest_6_y_value for j in i]
        print(nearest_6_y_value)
            [2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
            

        from collections import Counter
        print(Counter(nearest_6_y_value))
            Counter({2.0: 6})
            
    注意，这里要把y_train[i]之间加上list把他变成列表模式，不然他前面就会带着array字样
    然后再把两层列表整理成一层
    无法用collections 模块中的counter 方法计数
    经过counter计数，发现6个值都是2.0,
    你会发现返回的结果中y值都是2，所以他是一个恶性肿瘤
    
    如果我们Counter中有多个元素，比如2.0有6个，1.0有2个，那么我们可以通过.most_common(n)来显示counter中票数最多的n个值
        print(Counter(nearest_6_y_value).most_common(1))
            [(2.0, 6)]
            
    显示的就是，最多票数的是2.0这个值，一共有6票
    然后我们可以取出2.0这个值：
        print(Counter(nearest_6_y_value).most_common(1)[0][0])
            return: 2.0



方法二：使用sklearn中的KNN算法，from sklearn.neighbors import KNeighborsClassifier

    方法在3_KNN_sklearn文件中查看
    
    
    
注意，KNN也可以用来做回归，sklearn把它封装在KneighborsRegression




KNN缺点：
1. 效率低下
    如果训练集有m个样本n个特征，那么预测一个新的样本就需要m*n的时间
    
    我们可以通过一些优化来提高他的效率：树结构（KD-Tree，Ball-Tree）

2. 高度数据相关
    对outlier很敏感，在样本中哪怕只有两个outlier也很可能导致预测错误
    
3. 预测结果具有不可解释性
    只能预测它属于哪一类，但是不知道为什么属于这一类。比如线性回归可以考estimator beta来解释，但是KNN不行
    
4. 维数灾难
    随着维度增加，‘看似相近的两个点之间的距离会越来越大’
    例子：
        1维          0到1的距离是                 1
        2维          (0,0)到(1,1)的距离           1.414
        3维          (0,0,0)(1,1,1)               1.73
        64维         (0,0,...,0)(1,1,...,1)       8
        10000维      (0,0,...,0)(1,1,...,1)       100
    
    后面会学习降维方法PCA
    
    
"""

"""完整代码"""
iris = datasets.load_iris()

data_source = pd.DataFrame(iris.data)
target_source = pd.DataFrame(iris.target)
data = data_source.iloc[:,2:].values
target = target_source.iloc[:,:].values
data = np.hstack((target,data))


set1 = data[data[:,0] == 1]
set2 = data[data[:,0] == 2]

sub1 = set1[:,1:]
sub2 = set2[:,1:]
X = np.vstack((sub1,sub2))
Y = np.vstack((set1[:,0].reshape(len(set1),1),set2[:,0].reshape(len(set2),1)))

x_train = np.array(X)
y_train = np.array(Y)


sample = np.array([5.6,2])

distance = []
for i in range(len(x_train)):
    d = np.sqrt((sample[0] - x_train[i,0])**2 + (sample[1] - x_train[i,1])**2)
    distance.append(d)

order = np.argsort(distance)

k = 6
nearest_6_y_value = [list(y_train[i]) for i in order[:k]]
nearest_6_y_value = [j for i in nearest_6_y_value for j in i]
print(nearest_6_y_value)

from collections import Counter
print(Counter(nearest_6_y_value))
print(Counter(nearest_6_y_value).most_common(1)[0][0])