
import pandas as pd
from sklearn import linear_model




dataset = pd.read_csv('regression_dataset.csv')
print(dataset.head(5))


# Discrete Y
target = dataset.iloc[:,1].values
print(target)
print('\n\n')

data = dataset.iloc[:,3:].values
print(data)


machine = linear_model.LogisticRegression()
machine.fit(data, target)

new_data = [[-0.44087866, -0.29397041, 0.51282394, 0.92839181, -0.01210118,0]]
result = machine.predict(new_data)
print(result)
"""
Assume 1 for watch movie, 0 for not
# result: [0]

logistic model tells us exactly the value of Y, watch movie or not.
Logistic model works better than linear model for binary data.
"""












