
import kfold_module
import pandas as pd
from sklearn import linear_model
import pickle





# Extract machine
with open('machine.pkl', 'rb') as f:
    machine = pickle.load(f)

new_data = pd.read_csv('new_data.csv')
print(machine.predict(new_data))
