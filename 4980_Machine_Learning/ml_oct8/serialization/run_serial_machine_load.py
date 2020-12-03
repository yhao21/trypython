
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix



dataset = pd.read_csv('dataset.csv')


target = dataset.iloc[:,30].values
data = dataset.iloc[:,0:30].values

with open('serialized_machine.pickle','rb') as g:
    machine = pickle.load(g)

print(machine)

prediction = machine.predict(data)
print(confusion_matrix(target, prediction))
