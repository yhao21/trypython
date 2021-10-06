import pandas as pd
from kfold_template import run_kfold
from sklearn import tree



dataset = pd.read_csv('dataset.csv')
#print(dataset.head(5))

target = dataset.iloc[:,30].values
data = dataset.iloc[:,0:30].values

print(target)
print(data)

machine = tree.DecisionTreeClassifier(criterion = 'gini',max_depth = 10)

acc_score, conf_matrix = run_kfold(4, data, target, machine)
print(acc_score)
for i in conf_matrix:
    print(i)

'''
accuracy score
[0.89774, 0.89818, 0.89974, 0.8992]

confusion matrix
[[  321   361    10     0]
 [  145 32775  1321     4]
 [    2  2430  7632   258]
 [    0    18   564  4159]]
[[  318   383    10     0]
 [  138 32941  1234     3]
 [    0  2459  7460   341]
 [    0    17   506  4190]]
[[  347   352     9     0]
 [  159 33077  1185     5]
 [    0  2544  7464   283]
 [    1    12   463  4099]]
[[  295   398    10     0]
 [  142 33043  1118     0]
 [    0  2555  7503   278]
 [    0    21   518  4119]]
'''
