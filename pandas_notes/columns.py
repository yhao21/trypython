import pandas as pd



df = pd.read_csv('./data/dataset_ps_4.csv')
df = df.head(10)
###------Rename a column------###
"""
Use df.rename(
    columns = {
        "old_name": "new_name"
    }
)

To rename "age" to "age (yrs)"
"""
df1 = df.rename(columns = {'age':'age (yrs)'})
print(df1)

