import time

"""
选择最优超参数（hyperparameter）的方法：网格搜索

当我们有多个超参数时，我们一般先固定一个超参数，然后使用for循环搜索另一超参数的最优值
然后再循环那个之前固定的超参数，例如我们在8_hyperparameter中寻找method和k的方法一样

for method in []:
    for k in range(1,50):
        .......
        
        
我们可以用表格列出每次循环的结果(中间结果是拟合优度，即，准确率）：
        k   |    1   2   3   4   5   6   ... 49  50
-------------------------------------------------------
method      |   .96 .97 。。。。。。。。。。。。。
uniform     |
distance    |
            

这种形式，每一个（method，k）对应一个点，非常近似于网格结构。

我们称之为 “网格搜索”

网格搜索是寻找最优超参的一般方法


sklearn中的grid search模块就为我们编译了这种搜索方法

这个算法被封装在sklearn.model_selection中的GridSearchCV模块  CV是cross validation的缩写，交叉验证
使用这个方法获得的最优参数和我们之前自己写的程序返回的最优参数会有所不同，就是因为这里是通过交叉验证的方式选择最优值的
交叉验证的准确度是比我们直接train_test_split更准确的


GridSearchCV(estimator,para_grid,n_jobs,verbose)

使用verbose，边计算边返回结果：
verbose = 1时：
Fitting 5 folds for each of 60 candidates, totalling 300 fits
[Parallel(n_jobs=-1)]: Using backend LokyBackend with 8 concurrent workers.
[Parallel(n_jobs=-1)]: Done  34 tasks      | elapsed:    0.8s
[Parallel(n_jobs=-1)]: Done 285 out of 300 | elapsed:    7.0s remaining:    0.3s
[Parallel(n_jobs=-1)]: Done 300 out of 300 | elapsed:    7.8s finished


5 folds就是交叉验证的数量
candidates的数量是由我们传入的parameter列表决定的，

para_grid = [
    {
        'weights':['uniform'],
        'n_neighbors':[i for i in range(1,11)]
    },
    {
        'weights':['distance'],
        'n_neighbors':[i for i in range(1,11)],
        'p':[i for i in range(1,6)]
    }
]

当weights = uniform的时候，我们有10个neighbors需要验证，一共10个candidate
当weights = distance的时候，除了这10个neighbors，还有5个p值需要验证，一共有10*5中组合情况
所以两个加在一起一共是60中情况


verbose = 4时：

Fitting 5 folds for each of 60 candidates, totalling 300 fits
[Parallel(n_jobs=-1)]: Using backend LokyBackend with 8 concurrent workers.
[CV] n_neighbors=1, weights=uniform ..................................
[CV] n_neighbors=1, weights=uniform ..................................
[CV] n_neighbors=1, weights=uniform ..................................
[CV] n_neighbors=1, weights=uniform ..................................
[CV] n_neighbors=1, weights=uniform ..................................
[CV] n_neighbors=2, weights=uniform ..................................
[CV] n_neighbors=2, weights=uniform ..................................
[CV] n_neighbors=2, weights=uniform ..................................
[CV] ...... n_neighbors=1, weights=uniform, score=0.986, total=   0.0s
[CV] ...... n_neighbors=1, weights=uniform, score=0.990, total=   0.0s
[CV] ...... n_neighbors=1, weights=uniform, score=0.990, total=   0.0s
[CV] n_neighbors=2, weights=uniform ..................................
[CV] ...... n_neighbors=1, weights=uniform, score=0.972, total=   0.0s
[CV] ...... n_neighbors=1, weights=uniform, score=0.993, total=   0.0s
[CV] ...... n_neighbors=2, weights=uniform, score=0.979, total=   0.0s
[CV] ...... n_neighbors=2, weights=uniform, score=0.986, total=   0.0s
。。。。。。。
[CV] n_neighbors=10, p=4, weights=distance ...........................
[CV]  n_neighbors=10, p=4, weights=distance, score=0.976, total=   0.3s
[CV] n_neighbors=10, p=5, weights=distance ...........................
[CV]  n_neighbors=10, p=5, weights=distance, score=0.983, total=   0.3s
[CV]  n_neighbors=10, p=4, weights=distance, score=0.983, total=   0.3s
[Parallel(n_jobs=-1)]: Done 300 out of 300 | elapsed:    7.9s finished



首先我们需要将超参按照不同情况，分组写入一个列表中，
每种情况以字典的形式封装，即，一个列表中有几个字典，就有集中情况



para_grid = [
    {
        'weights':['uniform'],
        'n_neighbors':[i for i in range(1,11)]
    },
    {
        'weights':['distance'],
        'n_neighbors':[i for i in range(1,11)],
        'p':[i for i in range(1,6)]
    }
]


注意，在编写字典的key值是，必须与sklearn中KNN算法的参数名相同

"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV,train_test_split
from sklearn import datasets
import numpy as np




dig = datasets.load_digits()
data = dig.data
target = dig.target


data_training,data_test,target_training,target_test = train_test_split(data,target,test_size = 0.2)


para_grid = [
    {
        'weights':['uniform'],
        'n_neighbors':[i for i in range(1,11)]
    },
    {
        'weights':['distance'],
        'n_neighbors':[i for i in range(1,11)],
        'p':[i for i in range(1,6)]
    }
]

machine = KNeighborsClassifier()
#在这个方法中传入两个参数，第一个是我们的machine，第二个是要搜索的超参列表,第三个是使用都少个核心计算，-1表示全部的核
#verbose表示边计算边显示结果。未来我们在优化参数的时候很可能一个测试就几个小时，这时候我们需要计算机边计算边返回结果
#verbose的值越大，返回信息越详细
grid_search = GridSearchCV(machine,param_grid = para_grid,n_jobs = -1,verbose = 1)
#根据我们的训练集来筛选，这个过程会比较慢，我们来计时看看，用了将近一分钟的时间
s_t = time.time()
grid_search.fit(data_training,target_training)
e_t = time.time()
print('fit time ',e_t - s_t)
#然后调用best_estimator_返回最佳参数
best_para = grid_search.best_estimator_
print(best_para)
"""
fit time  52.726829290390015
当我们使用全部核心计算的时候：
fit time  7.776644229888916
计算机快了很多
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                     metric_params=None, n_jobs=None, n_neighbors=3, p=4,
                     weights='distance')

"""
#查看拟合准确度
best_score = grid_search.best_score_
print(best_score)
"""
0.9874709639953544

"""
#查看最佳参数
print(grid_search.best_params_)
"""{'n_neighbors': 3, 'weights': 'uniform'}"""

