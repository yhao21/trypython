import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix





dataset = pd.read_csv('dataset.csv')


target = dataset.iloc[:,30].values
data = dataset.iloc[:,0:30].values



data_training,data_test,target_training,target_test = train_test_split(data,target,test_size = 0.25, random_state = 0)

machine = RandomForestClassifier(n_estimators=21, criterion='gini', max_depth=10)
machine.fit(data_training,target_training)
prediction = machine.predict(data_test)

print(confusion_matrix(target_test,prediction))


#with open('serialized_machine.pickle','wb') as f:
#    pickle.dump(machine, f)


