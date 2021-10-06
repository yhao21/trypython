

import pandas as pd
from kfold_template import run_kfold
from sklearn import tree
from sklearn.ensemble import BaggingClassifier



dataset = pd.read_csv('dataset.csv')
#print(dataset.head(5))

target = dataset.iloc[:,30].values
data = dataset.iloc[:,0:30].values

machine = BaggingClassifier(n_estimators=21)

    
acc_score, conf_matrix = run_kfold(4, data, target, machine)
print(acc_score)
for i in conf_matrix:
    print(i)

'''
bagging use the subset of raw dataset to do random forest many times.

[0.92364, 0.92288, 0.9243, 0.92244]
[[  417   271     3     1]
 [   84 32971  1188     2]
 [    0  1614  8438   270]
 [    0     7   378  4356]]
[[  421   288     2     0]
 [  100 33123  1090     3]
 [    0  1692  8278   290]
 [    0     6   385  4322]]
[[  445   254     9     0]
 [   96 33211  1116     3]
 [    1  1672  8338   280]
 [    1     4   349  4221]]
[[  417   279     7     0]
 [   96 33051  1154     2]
 [    0  1694  8371   271]
 [    0     4   371  4283]]
'''
