import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import KFold

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix



def run_kfold(n, data, target, machine):
    '''
    arg: machine gives what kind of regression you want to do
    '''
    # you can customize n
    kfold_object = KFold(n_splits = n)
    kfold_object.get_n_splits(data)

    results_accuracy = []
    results_confusion = []
    for training_index, test_index in kfold_object.split(data):

        data_training, data_test = data[training_index], data[test_index]
        target_training, target_test = target[training_index], target[test_index]

        machine.fit(data_training, target_training)
        results = machine.predict(data_test)

        # r2 doesn't make sense in binary case
        r2 = metrics.r2_score(target_test, results)

        # 0.912, means 91% you are right
        score = accuracy_score(target_test, results)
        conf_matrix = confusion_matrix(target_test, results)
        #print(conf_matrix)
        #print(score)

        results_accuracy.append(score)
        results_confusion.append(conf_matrix)

    return results_accuracy, results_confusion


























