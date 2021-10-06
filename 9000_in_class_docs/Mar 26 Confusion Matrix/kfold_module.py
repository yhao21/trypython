import pandas as pd
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix,accuracy_score


def run_kfold(split_number, data, target, machine, confusion=0,use_accuracy = 0):
    kfold_object = KFold(n_splits=split_number)
    kfold_object.get_n_splits(data)

    result_r2 = []
    result_confusion_matrix = []
    result_accu_rate = []
    for training_index, test_index in kfold_object.split(data):
        # print('\n------------------training_index----------------\n\n',training_index)
        # print('\n------------------test_index--------------------\n\n',test_index)
        ##将使用的那一部分data复制给这俩个变量
        data_training, data_test = data[training_index], data[test_index]
        target_training, target_test = target[training_index], target[test_index]
        # machine = linear_model.LinearRegression()
        machine.fit(data_training, target_training)
        prediction = machine.predict(data_test)
        # print('\n------------------------R2------------------\n\n',metrics.r2_score(target_test,prediction))
        # print('\n\n\n\n\n')
        if use_accuracy == 1:
            result_accu_rate.append(accuracy_score(target_test,prediction))


        if confusion == 1:
            result_confusion_matrix.append(confusion_matrix(target_test, prediction))

        result_r2.append(metrics.r2_score(target_test, prediction))

    return result_r2,result_confusion_matrix,result_accu_rate


if __name__ == "__main__":
    df = pd.read_csv('ols_dataset.csv')

    target = df.iloc[:, 2].values

    data = df.iloc[:, 3:10].values

    r2_score = run_kfold(3, data, target)

    print(r2_score)
