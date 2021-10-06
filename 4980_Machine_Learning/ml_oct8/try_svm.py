
import kfold_template
import pandas as pd
from sklearn import svm


dataset = pd.read_csv('regression_dataset.csv')


# y1 is continuous Y, y2 is binomial. here we use y1
#target = dataset.iloc[:,1].values
target = dataset.iloc[:,2].values
data = dataset.iloc[:,3:].values
machine = svm.SVC(kernel = 'linear')
#acc_score, conf_matr = kfold_template.run_kfold(4, data, target, machine)
acc_score, conf_matr = kfold_template.run_kfold(5, data, target, machine)

print(acc_score, conf_matr)


# print readable results
for item in conf_matr:
    print(item)





