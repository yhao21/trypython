import pandas as pd
import numpy as np
import re
import statsmodels.api as sm




class Dummies():

    def __init__(self, dataset, dummy_object, drop = True, show_delete = False):
        self.dataset = dataset
        self.dummy_object = dummy_object
        self.drop = drop
        self.show = show_delete


    def get_dummies(self):
        dummies = []
        for val in self.dataset[self.dummy_object]:
            if val not in dummies:
                dummies.append(val)
        dummies.sort()

        return dummies


    def dummies(self):
        dummies = self.get_dummies()
        df_copy = np.array(self.dataset.copy().iloc[:,:].values)
        dum_name_list = [self.dummy_object + str(i) for i in dummies]
        dum_col_name = list(self.dataset.columns.values) + dum_name_list

        for dum_val in dummies:
            dum_col = []
            for row in range(df_copy.shape[0]):
                if df_copy[row,2] == dum_val:
                    dum_col.append(1)
                else:
                    dum_col.append(0)
            df_copy = np.hstack((df_copy,np.array(dum_col).reshape(len(dum_col),1)))
        dummy_output = pd.DataFrame(df_copy, columns = dum_col_name)
        dummy_output.pop(self.dummy_object)
        if self.drop == True:
            dummy_output.pop(dum_name_list[0])

        if self.show == False:
            return dummy_output
        elif self.show == True:
            return dummy_output, dum_name_list[0]


class Polynominal():

    def __init__(self, dataset, term, power):
        self.dataset = dataset
        self.term = term
        self.power = power


    def poly(self):
        data_col = list(self.dataset.columns.values)
        term_index = data_col.index(self.term)
        data_col.insert(term_index + 1, self.term + str(self.power))
        term_value = self.dataset.iloc[:,term_index].values
        term_with_power = np.array(term_value ** self.power).reshape(len(term_value),1)
        df_before = self.dataset.iloc[:,0:term_index + 1].values
        df_after = self.dataset.iloc[:,term_index + 1:].values
        data = pd.DataFrame(np.hstack((df_before,term_with_power,df_after)), columns = data_col)

        return data


class Regression():

    def __init__(self, data, target):
        self.data = data
        self.target = target


    def OLS(self):
        data = sm.add_constant(self.data)
        machine = sm.OLS(self.target, data).fit()
        result = machine.summary()

        return result


def prepare(dataset, target_range, data_range):
    data_s = data_range[0]
    data_e = data_range[1]
    col_name = list(dataset.columns.values)
    target_name = col_name[target_range:target_range + 1]
    data_name = col_name[data_s:data_e]

    target = pd.DataFrame(dataset.iloc[:, target_range].values, columns=target_name)
    data = pd.DataFrame(dataset.iloc[:, data_s:data_e].values, columns=data_name)

    return data, target


if __name__ == '__main__':

    df = pd.read_csv('dataset_ps_4.csv')
    print(df.head())

    data,target = prepare(df,1,(2,9))
    data = Polynominal(data,'exp',2).poly()
    data.pop('occ')
    data = Dummies(data,'region').dummies()
    result = Regression(data,target).OLS()

    print(data)
    print(result)


