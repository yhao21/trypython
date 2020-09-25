import pandas as pd

df = pd.read_excel('new_construction.xlsx')
new_c = df.iloc[:,:].values
print(df)
print(new_c)

data = pd.DataFrame()
order = ['建筑', '金币', '粮食', '木材', '铁矿' , '产出/分钟', '耗时']

for b in range(new_c.shape[0]):
    for lv in range (1, 11):
        name = new_c[b][0] + ' Lv.%d' % lv
        money = new_c[b][1] * (lv ** 3)
        food = new_c[b][2] * (lv ** 3)
        lumber = new_c[b][3] * (lv ** 3)
        ore = new_c[b][4] * (lv ** 3)
        output = new_c[b][5] * (lv ** 3)
        time_count = new_c[b][6] * (lv ** 3)

        data = data.append({
            '建筑': name,
            '金币': money,
            '粮食': food,
            '木材': lumber,
            '铁矿': ore,
            '产出/分钟': output,
            '耗时': time_count
        }, ignore_index = True)

data = data[order]
data.to_csv('upgrade_construction.csv', encoding = 'utf-8-sig')
print(data)
