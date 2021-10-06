
import pandas as pd
from kfold_template import run_kfold
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier



dataset = pd.read_csv('dataset.csv')
#print(dataset.head(5))

target = dataset.iloc[:,30].values
data = dataset.iloc[:,0:30].values

#print(target)
#print(data)

#machine = RandomForestClassifier(criterion = 'gini', max_depth=80, n_estimators = 11)

depth = [10, 20, 30, 50, 60]
for dep in depth:
    machine = RandomForestClassifier(criterion = 'gini', max_depth=dep, n_estimators = 11)
    
    acc_score, conf_matrix = run_kfold(4, data, target, machine)
    print('\n\n')
    print('depth = ', str(dep))
    print(acc_score)
    for i in conf_matrix:
        print(i)

'''
depth = 80
accuracy_score:
[0.90474, 0.9046, 0.90586, 0.90568]

confusion_matrix:
[[  258   429     5     0]
 [   39 33098  1105     3]
 [    1  2342  7749   230]
 [    0     8   601  4132]]
[[  254   448     8     1]
 [   47 33204  1061     4]
 [    0  2341  7663   256]
 [    0    15   589  4109]]
[[  278   421     9     0]
 [   38 33328  1057     3]
 [    0  2374  7677   240]
 [    0     9   556  4010]]
[[  273   426     4     0]
 [   47 33199  1057     0]
 [    0  2326  7792   218]
 [    0    16   622  4020]]

 在反对角的三个值， 0,0,16,一般都非常小，因为这个dataset中y = 0123是ordered的
 如果他们没有排序关系，比如不同交通工具，那么在反对角的数字会和靠近对角线的
 数值差不多。
                 预测值

真实值  confusion_matrix


注意，depth增加，提升acc score提升的幅度会下降
但是n_estimators树的数量增加，只会更好， 但是计算速度会下降

max_depth表示对数据切几次，注意，每切一次都会用到一个x variable。
我们有30个x，但是max depth=10,意味着可能有20个x没被切过。
这个问题可以通过bagging解决。
'''


'''
Result under different depth:

depth =  10
[0.81248, 0.8358, 0.79266, 0.83174]

depth =  20
[0.89784, 0.89854, 0.89902, 0.90016]

depth =  30
[0.90322, 0.90366, 0.90416, 0.90436]

depth =  50
[0.90284, 0.90434, 0.90114, 0.90456]

depth =  60
[0.9013, 0.90546, 0.90316, 0.90196]
'''
