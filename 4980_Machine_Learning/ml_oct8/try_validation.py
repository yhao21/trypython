import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import metrics




dataset = pd.read_csv('regression_dataset.csv')
#print(dataset)


# y1 is continuous Y, y2 is binomial. here we use y1
target = dataset.iloc[:,0].values
#print(target)
#print('\n\n')
data = dataset.iloc[:,3:].values
#print(data)

# test size = 0.25% of the whole dataset
data_training, data_test, target_training, target_test = train_test_split(data, target, test_size = 0.25, random_state = 0)

#print(data.shape)
#print(target.shape)
#
##(7500, 6)
#print(data_training.shape)
##(2500, 6)
#print(data_test.shape)
#
##(7500,)
#print(target_training.shape)
##(2500,)
#print(target_test.shape)



machine = linear_model.LinearRegression()
machine.fit(data_training, target_training)
results = machine.predict(data_test)

print(results)
# compare actual target and our prediction
plt.scatter(target_test, results)
plt.xlabel('target_test')
plt.ylabel('machine_predict')
plt.savefig('scatter_test.png')


r2 = metrics.r2_score(target_test, results)
print(r2)





















