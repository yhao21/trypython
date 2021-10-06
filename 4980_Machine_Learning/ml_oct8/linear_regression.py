import pandas as pd
from sklearn import linear_model




dataset = pd.read_csv('regression_dataset.csv')
print(dataset.head(5))

## Continous Y
#target = dataset.iloc[:,0].values
#print(target)
#print('\n\n')
#
#data = dataset.iloc[:,3:].values
#print(data)


#machine = linear_model.LinearRegression()
#machine.fit(data, target)
#
#new_data = [[-0.44087866, -0.29397041, 0.51282394, 0.92839181, -0.01210118,0]]
#result = machine.predict(new_data)
#print(result)
## [3.19788325]




# Discrete Y
target = dataset.iloc[:,1].values
print(target)
print('\n\n')

data = dataset.iloc[:,3:].values
print(data)


machine = linear_model.LinearRegression()
machine.fit(data, target)

new_data = [[-0.44087866, -0.29397041, 0.51282394, 0.92839181, -0.01210118,0]]
result = machine.predict(new_data)
print(result)
"""
this tells us the prob of individual watching movie is [0.26094333]
However, if we set one of the X variable equal to a very large num,
the result can be greater than 1. (note, Prob. < 1)

Hence, LinearRegression is not good for binary data
"""











