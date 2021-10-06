import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time_series import diff_lags as nlag
from sklearn.ensemble import RandomForestRegressor
from sklearn import linear_model
#from My_Module.kfold_module import run_kfold
from sklearn.model_selection import KFold
from sklearn import metrics



def run_kfold(split_number,data,target,machine):

    kfold_object = KFold(n_splits=split_number)
    kfold_object.get_n_splits(data)
    result = []
    for training_index,test_index in kfold_object.split(data):
        data_training,data_test = data[training_index],data[test_index]
        target_training,target_test =target[training_index],target[test_index]
        machine.fit(data_training,target_training)
        prediction = machine.predict(data_test)

        result.append(metrics.r2_score(target_test,prediction))
    with open('saved_machine.pickle','wb') as f:
        pickle.dump(machine, f)


    return result




def make_lag(input_series, lag_num):
    '''
    create lag terms

    Suppose you have a price series [2,3,1,4,5], the last element stands for the current price
    the first element stands for the oldest price.

    if lag_num = 1, this fn will generate a lag1 list for you:
        [0,2,3,1,4]
    if lag_num = 2, this fn will generate a lag2 list for you:
        [0,0,2,3,1]
    Hence, you can form a dataframe below by your self:
    index   price   lag1    lag2
      0      2       0       0
      1      3       2       0
      2      1       3       2
      3      4       1       3
      4      5       4       1


    '''
    return [0]*lag_num + list(input_series[:-lag_num])




df = pd.read_csv('NewCleanData.csv')
df = df[['Open_price','Volume','cir_supply']]
df['lnprice'] = np.log(df['Open_price'])
df['lnvolume'] = np.log(df['Volume'])
df['lncir'] = np.log(df['cir_supply'])
df = df.drop(['Open_price','Volume','cir_supply'],axis = 1)


df['price_lag1'] = make_lag(df['lnprice'],1)
df['price_lag2'] = make_lag(df['lnprice'],2)
df['volume_lag1'] = make_lag(df['lnvolume'],1)
df['volume_lag2'] = make_lag(df['lnvolume'],2)
df['cir_lag1'] = make_lag(df['lncir'],1)
df['cir_lag2'] = make_lag(df['lncir'],2)

# drop the first two rows.
df = df.drop(df.index[:2])


print(df)

#-------------------#
# train machine with first 2000 obs
target = df.iloc[:2000,0].values
data = df.iloc[:2000,1:].values
# RF works supper bad
#machine = RandomForestRegressor(n_estimators=201, max_depth=30, n_jobs=-1)
# LR works supper good
machine = linear_model.LinearRegression()
r2_score = run_kfold(4,data,target,machine)
print(r2_score)





#-------------------#
# test machine with the rest of data
with open('saved_machine.pickle','rb') as g:
    machine = pickle.load(g)

data_input = df.iloc[2000:,1:].values
target_true = df.iloc[2000:,0].values
prediction = machine.predict(data_input)
r2_score = metrics.r2_score(target_true,prediction)
print(r2_score)

#col = df.columns.values[1:]
#coef_list = [(item,item_value) for item, item_value in zip(col,machine.coef_)]
#print('\n\n')
#[print('{:13} {}'.format(*i)) for i in coef_list]




#-------------------#
# test if the performance by comparing the first diff
pre_diff = nlag(prediction,1)
true_diff = nlag(target_true,1)
r2_diff = metrics.r2_score(true_diff,pre_diff)
print('\n\n')
print(r2_diff)
x = list(range(len(pre_diff)))
plt.plot(x, pre_diff, c='red')
plt.plot(x, true_diff, c='blue')
plt.show()





