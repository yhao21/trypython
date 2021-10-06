import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from matplotlib import pyplot as plt

"""
一般线性回归方法：

    1. 使用pandas导入csv
    2. 对数据进行切片，将解释变量和被解释变量分开，分别存放在两个不同的array中
    3. 建立线性回归machine
    4. 通过fit方法训练machine
    5. 提交一组完整的解释变量数据给machine，让其预测被解释变量的值
    6. 可使用R^2，检验拟合优度。
"""
#导入csv
df = pd.read_csv('ols_dataset.csv')
#将df切片，提取解释变量的数据，注意，3:10表示提取3到9列，始终记得：index是第0列，且结尾数字取不到
data = df.iloc[:,3:10].values
#将df切片，提取第2列，y的值
target = df.iloc[:,2].values

machine = linear_model.LinearRegression()
machine.fit(data,target)
#把原始数据中第5行至99行的x作为检验数据，让machine预测他们的y
test_data = df.iloc[5:100,3:10].values
test_target = df.iloc[5:100,2].values
prediction = machine.predict(test_data)
#把第5至99行真实的y和machine预测出来的y对比，计算拟合优度
r2 = metrics.r2_score(test_target,prediction)

print(r2)

#将prediction打印出来，x轴为真实的y值数据，纵轴为预测数据
plt.xlabel('test_target')
plt.ylabel('prediction')
plt.scatter(test_target,prediction)
#将散点图保存在本地
plt.savefig('test_prediction.png')
