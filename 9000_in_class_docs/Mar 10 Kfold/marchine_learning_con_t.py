import pandas as pd
from sklearn import linear_model


df = pd.read_csv('ols_dataset.csv')
#target is your y
target = df.iloc[:,2].values
#data is your explanatory variables
data = df.iloc[:,3:10].values

# print(df)
# print(target)
# print(data)

machine = linear_model.LinearRegression()

machine.fit(data,target)

"""after training machine with target, you can train it without target(with only data)"""

X = [
    [24,55,31,3,0,7,20],
    [ 5,25,39,3,1,4,30],
    [5,25,39,3,1,4,30]]
#given three obs, predict their y
result = machine.predict(X)

print(result)
"""
[3326.43968971 2067.48105899 2067.48105899]

true y:
[2904.5 1706.7 3083.5]
"""


"""
如何检验我们的machine是否准确呢：

把原始数据分成两个dataset，dataset1，和dataset2

我们用dataset1去训练machine，然后让machine使用dataset2的data（x）预测y，然后把预测出来的y和dataset2的y对比，比较我们的machine是否优秀

Notice，当dataset2与dataaset1的差异 与 你手中个的dataset和真实世界的数据的差异不同时，误差会出现

                 data            target
-----------------------------------------------
dataset          known           known         
-----------------------------------------------
realworld        known           unknown
application


                data            target
--------------------------------------------------
dataset 1       known            known 
--------------------------------------------------
dataset 2       known            known



we can use sklearn's module to separate your dataset into two parts: training(dataset 1), testing(dataset 2)

you have to balance your loads of training and testing dataset

if you have very little training dataset and large testing dataset, your machine might not be accurate
if you have many training dataset and very little testing dataset, then your test might be weak

"""