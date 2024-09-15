import pandas as pd
import numpy as np



'''
Please always check if there is na or infinite in your
dataset before you run regression.

To check na:
    df.isna().sum()
To check inf:
    np.isinf(df).sum()

Once you find the na info, you can print that row using
    a = df[df[col_name].isna()]
    print(a)



'''
