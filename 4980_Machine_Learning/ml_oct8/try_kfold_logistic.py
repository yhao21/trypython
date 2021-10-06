

import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
#from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import KFold

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix





dataset = pd.read_csv('regression_dataset.csv')
#print(dataset)


# y1 is continuous Y, y2 is binomial. here we use y1

#target = dataset.iloc[:,1].values
target = dataset.iloc[:,2].values
data = dataset.iloc[:,3:].values


kfold_object = KFold(n_splits=4)
kfold_object.get_n_splits(data)

'''
training_index [2500 2501 2502 ... 9997 9998 9999]
test_index [   0    1    2 ... 2497 2498 2499]
training_index [   0    1    2 ... 9997 9998 9999]
test_index [2500 2501 2502 ... 4997 4998 4999]
training_index [   0    1    2 ... 9997 9998 9999]
test_index [5000 5001 5002 ... 7497 7498 7499]
training_index [   0    1    2 ... 7497 7498 7499]
test_index [7500 7501 7502 ... 9997 9998 9999]
'''

for training_index, test_index in kfold_object.split(data):
    print('training_index', training_index)
    print('test_index', test_index)

    data_training, data_test = data[training_index], data[test_index]
    target_training, target_test = target[training_index], target[test_index]

    machine = linear_model.LogisticRegression()
    machine.fit(data_training, target_training)
    results = machine.predict(data_test)

    # r2 doesn't make sense in binary case
    r2 = metrics.r2_score(target_test, results)

    # 0.912, means 91% you are right
    score = accuracy_score(target_test, results)
    print(score)
    conf_matrix = confusion_matrix(target_test, results)
    print(conf_matrix)
'''

    [[398  63   2   0   0]
    [ 51 262 106   0   0]
    [  2  89 344 117   2]
    [  0   1 111 294  89]
    [  0   0   3  83 483]]

 The number on the diagonal is how many of correct guess
'''


























