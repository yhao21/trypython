import kfold_module
import pandas as pd
from sklearn.ensemble import BaggingClassifier




dataset = pd.read_csv('dataset.csv')

target = dataset.iloc[:,30].values
data = dataset.iloc[:,0:30].values
print(dataset)

##  n_estimators is how many trees you want
## Bagging estimator do not use all the features(classification line in gini impurity). it only use some subset of the feature
machine = BaggingClassifier(n_estimators = 21)
r2, confusion_matrix, accu_rate = kfold_module.run_kfold(3,data,target,machine,1,1)
print(r2, accu_rate)
for i in confusion_matrix:
    print(i)

"""
[0.8245609755336845, 0.8309294179398095, 0.8268148424855563] [0.9216253918730406, 0.9245053774731127, 0.9230942309423095]
[[  532   380    10     0]
 [  119 43969  1616     3]
 [    1  2203 11162   362]
 [    0    10   521  5779]]
[[  591   365     3     0]
 [  129 44284  1383     3]
 [    0  2242 11077   421]
 [    0     2   485  5682]]
[[  558   366     9     0]
 [  141 44099  1544     0]
 [    0  2195 11152   394]
 [    1     9   468  5730]]
"""