from sklearn import linear_model
import pandas as pd
import numpy as np
import kfold_module
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


data_source = pd.read_csv('logistic_dataset.csv')
# here, y1 is target
target = data_source.iloc[:,2].values
data = data_source.iloc[:,3:9].values
target_for_real = data_source.iloc[:,1].values

r2,confusion_matri,accuracy_score = kfold_module.run_kfold(4,data,target,linear_model.LogisticRegression(),1,1)
"""打印的矩阵很难看，没有对齐"""
print(r2)

for confu_ma in confusion_matri:
    print(confu_ma)
"""此时发现打印出来的矩阵很好看"""

"""对角线数字越大，说明预测的越准"""
print(accuracy_score)
"""[0.6924, 0.7292, 0.7184, 0.7124]"""

"""if you think your model is good, then you create a new machine,
and fit the machine with all of the data and target,
and use real_world_X for prediction"""


real_world_x = [
    [24,55,31,3,0,7],
    [ 5,25,39,3,1,4,],
    [5,25,39,3,1,4]]


machine = linear_model.LogisticRegression()
machine.fit(data,target_for_real)
result_real = machine.predict(real_world_x)
print(result_real)