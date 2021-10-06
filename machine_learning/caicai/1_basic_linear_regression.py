from sklearn import linear_model
from sklearn.datasets import fetch_california_housing as cal_house
from sklearn.model_selection import KFold
from sklearn import metrics
import pandas as pd


"""
完整代码如下：
后面是每一步的解释
"""

x_data = pd.DataFrame(cal_house().data)
y_target = pd.DataFrame(cal_house().target)
x_data.columns = cal_house().feature_names

x_for_reg = x_data.iloc[:,:].values
y_for_reg = y_target.iloc[:,:].values

kfold_obj = KFold(n_splits = 5)


r2_result = []
for training_ind,test_ind in kfold_obj.split(x_for_reg):
    x_for_reg_training,y_for_reg_training = x_for_reg[training_ind],y_for_reg[training_ind]
    x_for_reg_test,y_for_reg_test = x_for_reg[test_ind],y_for_reg[test_ind]
    machine = linear_model.LinearRegression()
    machine.fit(x_for_reg_training,y_for_reg_training)
    prediction_OLS = machine.predict(x_for_reg_test)
    r2 = metrics.r2_score(y_for_reg_test,prediction_OLS)
    r2_result.append(r2)
print('-----------------------------r2_result--------------------------\n\n')
print(r2_result,'\n\n\n')

#打印estimators
print(machine.coef_)
"""
[[ 4.47847084e-01  9.40820722e-03 -1.20960919e-01  7.10267788e-01
  -1.47053238e-06 -8.81496820e-03 -4.21714509e-01 -4.29775301e-01]]

"""
#查看beta 0 （即第一个常数项）
print(machine.intercept_)
'''
[-36.39051025]
'''

"""
通过匹配函数zip，将解释变量名称和其对应的estimator对应起来
"""

estimators_val = []
for i in machine.coef_:
    for j in i:
        estimators_val.append(j)

"""
上面操作是为了把machine.coef_中的每一个值取出来放入一个列表中，因为machine.coef_本身是一个列表中存了一个以列表
所以相当于最外层列表中只有一个元素，这个元素就是存储着8个coef的一个列表。
所以我们要用两次循环把内层列表中的每一个值取出来，放入新的列表中，这样才能和feature_names进行匹配。
因为feature_names是单层列表。
如果不提取coef直接匹配，只能匹配到一项
"""
estimators = [*zip(cal_house().feature_names,estimators_val)]
print(estimators)
'''
[
('MedInc', 0.44784708400334505), 
('HouseAge', 0.009408207215585412), 
('AveRooms', -0.1209609188599623), 
('AveBedrms', 0.7102677881409649), 
('Population', -1.4705323836683437e-06), 
('AveOccup', -0.008814968196347306), 
('Latitude', -0.4217145086670072), 
('Longitude', -0.4297753011634542)
]
'''








#
#
# #下载sklearn数据库中的加州房屋信息数据
# housevalue = cal_house()
# #使用.data是将所有的x（解释变量）保存到一个dataframe中，即Tom的data
# x = pd.DataFrame(housevalue.data)
#
# #打印该数据库的表头信息，即
# #print(housevalue.feature_names)
# """['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']"""
#
# #查看当前dataframe的表头
# #print(x.head())
# '''
#         0     1         2         3       4         5      6       7
# 0  8.3252  41.0  6.984127  1.023810   322.0  2.555556  37.88 -122.23
# 1  8.3014  21.0  6.238137  0.971880  2401.0  2.109842  37.86 -122.22
#
# 发现表头是数字，而不是项目名称，所以我们接下来要把列名添加进去
#
# '''
# #将每一列对应的名字放到数据库中
# x.columns = housevalue.feature_names
# #print(x)
# #打印所有的y（被解释变量）
# #print(housevalue.target)
# y = pd.DataFrame(housevalue.target)
#
# #查看此数据库的信息
# print(housevalue.DESCR)
# '''
# California Housing dataset
# --------------------------
#
# **Data Set Characteristics:**
#
#     :Number of Instances: 20640
#
#     :Number of Attributes: 8 numeric, predictive attributes and the target
#
#     :Attribute Information:
#         - MedInc        median income in block
#         - HouseAge      median house age in block
#         - AveRooms      average number of rooms
#         - AveBedrms     average number of bedrooms
#         - Population    block population
#         - AveOccup      average house occupancy
#         - Latitude      house block latitude
#         - Longitude     house block longitude
#
#     :Missing Attribute Values: None
#
# This dataset was obtained from the StatLib repository.
# http://lib.stat.cmu.edu/datasets/
#
# The target variable is the median house value for California districts.
#
# This dataset was derived from the 1990 U.S. census, using one row per census
# block group. A block group is the smallest geographical unit for which the U.S.
# Census Bureau publishes sample data (a block group typically has a population
# of 600 to 3,000 people).
#
# It can be downloaded/loaded using the
# :func:`sklearn.datasets.fetch_california_housing` function.
#
# .. topic:: References
#
#     - Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions,
#       Statistics and Probability Letters, 33 (1997) 291-297
# '''
#
#
# data = x.iloc[:,:].values
#
# #The target variable is the median house value for California districts.
# target = y.iloc[:,:].values
#
#
#
# kfold_object = KFold(n_splits = 5)
#
# r2_result = []
#
# for training_index,test_index in kfold_object.split(x):
#     training_data,training_target = data[training_index],target[training_index]
#     test_data,test_target = data[test_index],target[test_index]
#     # print(training_index,'\n\n\n',test_index,'\n\n\n')
#     machine = linear_model.LinearRegression()
#     machine.fit(training_data,training_target)
#     prediction = machine.predict(test_data)
#     r_2 = metrics.r2_score(test_target,prediction)
#     r2_result.append(r_2)
# print(r2_result)
#
#
#
