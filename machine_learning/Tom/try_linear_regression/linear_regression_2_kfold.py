import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import KFold


def run_kfold(data,target,split_number):

    kfold_object = KFold(n_splits = split_number)
    #get_n_splits命令用来查看‘将数据切片成几份’，因为我们传入的是4，所以，程序将数据切片成4份。这一行代码可以不写
    a = kfold_object.get_n_splits(data)
    print(a)
    """return：a = 4"""


    result = []

    for training_index,test_index in kfold_object.split(data):
        '''通过打印training和test index查看系统是如何切片的。程序将数据分为四等分，共循环四次，每次将25%的数据作为test，剩下75%作为training'''
        # print('\n-----------------------training_index-----------------\n\n',training_index)
        # print('\n-----------------------test_index---------------------\n\n',test_index)
        # print('\n\n\n')
        '''将对应training和test两种编号的data数据提取出来'''
        data_training,data_test = data[training_index],data[test_index]
        #print(data_training,'\n\n\n',data_test,'\n\n\n')
        target_training,target_test = target[training_index],target[test_index]
        machine = linear_model.LinearRegression()
        machine.fit(data_training,target_training)
        prediction = machine.predict(data_test)
        r_2 = metrics.r2_score(target_test,prediction)
        result.append(r_2)
    return result



if __name__ == '__main__':
    df = pd.read_csv('ols_dataset.csv')
    target = df.iloc[:,2].values
    data = df.iloc[:,3:10].values
    r2 = run_kfold(data,target,split_number = 4)

    print(r2)