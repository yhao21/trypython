import kfold_module
import pandas as pd
from sklearn import linear_model




dataset = pd.read_csv('historical_data.csv')
target = dataset.iloc[:,0].values
data = dataset.iloc[:,1:].values

result = kfold_module.run_kfold(4, data, target, linear_model.LinearRegression())
print(result)


machine = linear_model.LinearRegression()
machine.fit(data, target)



#new_data = pd.read_csv('new_data.csv')
#print(machine.predict(new_data))
