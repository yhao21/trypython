import pandas as pd


df = pd.DataFrame()


for i in range(1,100):
    a = 'name' + str(i)
    df.append({
        'name':a
    },ignore_index=True)

print(df)