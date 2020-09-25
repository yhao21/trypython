import kfold_module
import pandas as pd
from sklearn import tree




dataset = pd.read_csv('dataset.csv')

target = dataset.iloc[:,30].values
data = dataset.iloc[:,0:30].values
print(dataset)

##  max_depth is how many lay you want
machine = tree.DecisionTreeClassifier(criterion = 'gini',max_depth = 10)
r2, confusion_matrix, accu_rate = kfold_module.run_kfold(3,data,target,machine,1,1)
print(r2, accu_rate)
for i in confusion_matrix:
    print(i)
"""
[0.7683555716221614, 0.7675739200153362, 0.7700765946970509] [0.8970105149474252, 0.8976555117224414, 0.8987039870398704]
[[  393   518    10     1]
 [  172 43837  1695     3]
 [    0  3304  9984   440]
 [    0    27   696  5587]]
[[  461   484    14     0]
 [  195 44117  1480     7]
 [    0  3532  9835   373]
 [    0    22   716  5431]]
[[  431   490    12     0]
 [  176 44027  1579     2]
 [    1  3341  9955   444]
 [    2    25   681  5500]]
"""
""""""