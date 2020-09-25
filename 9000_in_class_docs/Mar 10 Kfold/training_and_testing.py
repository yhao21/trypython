import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import metrics


df = pd.read_csv('ols_dataset.csv')
#target is your y
target = df.iloc[:,2].values
#data is your explanatory variables
data = df.iloc[:,3:10].values

"""split your dataset into to two parts"""
data_training,data_test,target_training,target_test = train_test_split(data,target,test_size = 0.25, random_state = 0)

print('-----------------data_training----------------\n')
print(data_training)
print('-----------------data_test----------------\n')
print(data_test)
print('-----------------target_training----------------\n')
print(target_training)
print('-----------------target_test----------------\n')
print(target_test)
# print('data.shape',data.shape)
# print('target.shape',target.shape)

machine = linear_model.LinearRegression()
machine.fit(data_training,target_training)

prediction = machine.predict(data_test)

print('-----------prediction----------\n',prediction)

plt.xlabel('target of test dataset')
plt.ylabel('model prediction')
plt.scatter(target_test,prediction)

plt.savefig('data_test.png')


print('\n-------------------R^2----------------\n',metrics.r2_score(target_test,prediction))

"""
可通过把原始分成不同的四等分，比如testdata在前25%，中25%。。。之类的，这样你就可以检测四次了
"""