import time
"""

数据归一化



引例：

还是以肿瘤为例


            肿瘤大小（厘米）            发现时间（天）
样本1             1                        100
样本2             5                        200


我们计算欧拉距离的话   distance = ((1-5)**2 + (100-200)**2)**(1/2)
你会发现，虽然肿瘤2比肿瘤1的大小打了5倍，但是因为发现时间的数值太大了，他们的距离被发现时间所主导，无法反映出肿瘤大小的信息


那我如果我们把发现时间的单位调整为年呢？


            肿瘤大小（厘米）            发现时间（年）
样本1             1                        0.27
样本2             5                        0.55

此时，我们计算欧拉距离的话   distance = ((1-5)**2 + (0.27-0.55)**2)**(1/2)

这时候距离的大小被肿瘤大小主导，，

显然，使用这两种距离进行KNN判断的结果是有很大偏差的


这就是为什么我们需要将数据归一，即，将所有数据映射到同一尺度中，，，


    常用方法为：
    
    1. 最值归一化(normalization)
    
        把所有数据映射到0-1之间
    
        公式：
    
        X(scale) = [ x - x(min) ] / [ x(max) - x (min)]
    
        这种方法适用于分布有明显边界的情况，比如像素的分布是从0到255。但是这种方法会受到outlier的影响
        对于没有明显边界的情况（如人们的收入），这种方法欠佳，因为他会受到outlier影响
    
    
    2. 均值方差归一化(standardization)
    
        把所有数据归到均值为0方差为1的分布中
        
        这个方法是为了修正normalization的缺陷，它适用于没有明显边界的情况，也适用于有边界的情况
    
    公式：
    
    X(scale) = [ x - x(mean) ] / SD
    
    

"""

import numpy as np
import matplotlib.pyplot as plt

"""normalization"""
#一维数组例子
x = np.random.randint(0,100,size = 100)
normalization_numerator = x - np.min(x)
normalization_denominator = np.max(x) - np.min(x)
normalization = normalization_numerator / normalization_denominator
print(normalization)

#矩阵例子
y = np.random.randint(0,100,(50,2))
#randint中的值都是整数，但是归一化后是浮点数，所以我们必须改变y中的数据类型为浮点数
y = np.array(y,dtype = float)
#矩阵的归一化需要对每一列进行归一,这里我们用for循环完成
for col in range(y.shape[1]):
    y[:,col] = (y[:,col] - np.min(y[:,col])) / np.max(y[:,col])
print(y)
plt.scatter(y[:,0],y[:,1])
plt.show()



"""standardization"""


x1 = np.random.randint(0,100,(50,2))
x1 = np.array(x1,dtype = float)
for col in range(x1.shape[1]):
    x1[:,col] = (x1[:,col] - np.mean(x1[:,col])) / np.std(x1[:,col])
print(x1,'\n\n--------x1---------')
plt.scatter(x1[:,0],x1[:,1])
plt.show()

