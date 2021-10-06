import pandas as pd
import numpy as np


df = pd.read_csv('dataset_ps_4.csv')

df = df['ability'].values.reshape(len(df),1)
print(df.shape)