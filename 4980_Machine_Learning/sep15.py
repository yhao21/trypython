import pandas as pd
import numpy as np









df = pd.read_csv('dataset.csv')

df2 = df[df['x1']<0]
#print(df2)


x = df.iloc[:,:30]
print(x)

y = df.iloc[:,30]
print(y)



# if you want to change this DataFrame into array, do this:
x_array = df.iloc[:,:30].values
print(x_array)
