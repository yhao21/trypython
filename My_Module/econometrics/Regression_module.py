import pandas as pd
import numpy as np
import re
import statsmodels.api as sm





class Dummies():
    '''
    This module converts a column data to dummy variables.
    Call Dummies(df_array, dummy_name, convert_df = True).make_dummy() to run this module

    Parameters:

        df_array:   a ndarray converted by your dataframe. You should convert your pandas 
                    dataframe to ndarray by df.iloc[].values

        dummy_name: the name of dummy variable, return col names are based on this dummy_name.

        convert_df: Default True. Convert the output dummy variable columns to pandas dataframe.
                    If convert_df = False, program will return a ndarray, rather dataframe.
                    If you need to convert multiply dummies, you should set convert_df = False,
                    so that you can write this module in a for loop and merge all output ndarray
                    manually.

    Return items:
        
        This module return two items, converted dataframe (or ndarray), and column names (list)

    Example:

        df = pd.read_csv('sample_data_not_city.csv')
        stars = df.iloc[:,1].values
        dummy_df, dummy_col = Dummies(stars, 'stars', convert_df = True).make_dummy()

    '''


    def __init__(self, df_array, dummy_name, convert_df = True):
        self.array = df_array
        self.name_base = dummy_name
        self.convert = convert_df
        self.dummy_values = []          # verify categories in df_array, cate = ['1', '2'] in df = [1,1,2,1]
        self.col = []                   # final dummy_df col name list
        self.main_array = []            # store all converted dummy columns


    def make_dummy(self):

        self.count_categories()
        ## values in value list are floats
        #print('categories:', self.dummy_values)


        if len(self.dummy_values) == 2:         # if count is 2, then it is binary, no need to make more cols
            self.col = [self.name_base + str(self.dummy_values[0])]
            self.binary_dummy()
            self.main_array = pd.DataFrame(self.main_array)
            self.main_array.columns = self.col
            print(df.head(3))
            print(self.main_array)
            print('columns:',self.col)

        else:
            self.convert_binary()

            self.make_col_name()

            if self.convert:        # convert to dataframe if self.convert = True
                self.main_array = pd.DataFrame(self.main_array)
                self.main_array.columns = self.col

            print(df.head(3))
            print(self.main_array)
            print('columns:',self.col)
        
        return self.main_array, self.col
        
                

    def make_col_name(self):
        '''
        Make col name list. Names are in form of <dummy name base><dummy value>
        '''

        for item in self.dummy_values:
            name = self.name_base + str(item)
            self.col.append(name)
        print(self.col)



    def convert_binary(self):
        '''
        Convert to 0, 1
        '''

        for dummy_value in self.dummy_values:   # dummy_value: one category in list. i.e., 1 in [1, 2]
            new_array = []                      # save convert dummy for one dummy_value in self.dummy_values
            for item in self.array:             # item: values in df (raw dataset)
                if item == dummy_value:         # convert dummy_value in df to binary data (1 if equal)
                    new_array.append(1)
                else:
                    new_array.append(0)

            if len(self.main_array) == 0:            # if self.main_array is empty, assign new to main
                self.main_array = np.array(new_array).reshape(len(new_array), 1)
            else:
                new_array = np.array(new_array).reshape(len(new_array), 1)
                self.main_array = np.hstack((self.main_array, new_array))



    def binary_dummy(self):
        new_array = []
        for item in self.array:
            if item == self.dummy_values[0]:
                new_array.append(1)
            else:
                new_array.append(0)
        self.main_array = np.array(new_array).reshape(len(new_array), 1)



    def count_categories(self):

        for i in self.array:
            if i not in self.dummy_values:
                self.dummy_values.append(i)

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
    result = Regression(data,target).OLS()

    print(data)
    print(result)

    #####################
    ### Dummies Usage ###
    #####################

    ## multi class
    df = pd.read_csv('sample_data_not_city.csv')
    print(df.head(3))
    stars = df.iloc[:,1].values
    dummy_df, dummy_col = Dummies(stars, 'stars', convert_df = False).make_dummy()

    ## single class
    #a = [1,2,2,1,1]
    #df = pd.DataFrame(a)
    #df.columns = ['item']
    #df = df.iloc[:,:].values
    #dummy_df, dummy_col = Dummies(df, 'item', convert_df=True).make_dummy()

