from matplotlib import pyplot as plt
import numpy as np
from sklearn import datasets
import pandas


'''

鸢尾花数据集


使用.keys()查看这个sklearn自带数据集内包含的内容
    
    iris = datasets.load_iris()
    print(iris.keys())
    ''dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])''


查看X(i)的名字（特征名称）
    
    iris = datasets.load_iris()
    iris.feature_names
        ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
        
    将X(i)的名称放到dataframe中：
    
        df = pd.DataFrame(iris.data)
        df.columns = iris.feature_names
        print(df.head())
                  sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
        0                5.1               3.5                1.4               0.2
        1                4.9               3.0                1.4               0.2
        2                4.7               3.2                1.3               0.2
        3                4.6               3.1                1.5               0.2
        4                5.0               3.6                1.4               0.2




使用scatter简单的画一些图像
    
    #取所有行，但是只取前两列
    #横轴是X的第0列，纵轴是X的第1列
        X = iris.data[:,:2]
        plt.scatter(X[:,0],X[:,1])
        plt.show()
    

    #观察一下Y的值,发现Y可以为0,1,2
    
    #我们将数组X前两列中Y值为0的值取出，标记为红色
    #我们将数组X前两列中Y值为1的值取出，标记为蓝色
    #我们将数组X前两列中Y值为2的值取出，标记为绿色
    
        X = iris.data[:,:2]
        Y = iris.target
        print(Y)
        plt.scatter(X[Y == 0,0],X[Y == 0,1],color = 'red')
        plt.scatter(X[Y == 1,0],X[Y == 1,1],color = 'blue')
        plt.scatter(X[Y == 2,0],X[Y == 2,1],color = 'green')
        plt.show()
    也可以使用for循环来写这个语句
    
        C = ['red','blue','green']
        M = ['o','+', 0]
        for y in range (3):
            plt.scatter(X[Y == y,0],X[Y == y,1],color = C[y],marker = M[y])
        plt.show()




'''