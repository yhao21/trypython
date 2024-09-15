import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
#import RLS

class fit():

    def __init__(self, t, X, Y, lamb = 1, a=1, c=100,P0_guess = False, print_result = False, not_return_y_hat = False, gamma = 0.00000001, is_constant_gamma = True, gamma_series = []):
        self.t = t          # time column, a df
        self.X = X          # a df
        self.Y = Y          # a df
        self.lamb = lamb
        self.gamma = gamma
        self.constant_gamma = is_constant_gamma
        self.gamma_series = gamma_series    # a ndarray
        self.a = a
        self.c = c
        self.k = 0
        self.SSR = 0
        self.P0_guess = P0_guess
        self.b = []       # return a dataframe
        self.ee = []      # return a dataframe
        self.resid = []       # return a dataframe
        self.series_y_hat = []       # return a dataframe
        #self.setup_figure_dir()
        self.print_result = print_result
        self.run()

    def run(self):
        '''
        This function will etimate coefs 
        '''
        #print(self.X.iloc[:,:].values)
        #print(self.Y.iloc[:,:].values)
        #print('X:',self.X.iloc[:,:].values.shape)
        #print('Y:',self.Y.iloc[:,:].values.shape)

        ###------B based on lamba------##
        #B = np.diag([self.lamb**i for i in range(self.X.shape[0])])

        ##------B based on gamma------##
        if self.constant_gamma:
            B = np.diag([self.gamma * (1 - self.gamma) ** i for i in range(self.X.shape[0])])
        else:
            B = np.diag(self.gamma_series)

        XTB = np.dot(self.X.T, B)
        XTBY = np.dot(XTB, self.Y)
        XTBX = np.dot(XTB, self.X)

        #print('XTB', XTB)
        #print('XTBY', XTBY)
        #print('XTBX', XTBX)
        #print('B', B)
        #print('X', self.X)
        #print('Y', self.Y)


        self.b = np.dot(np.linalg.inv(XTBX), XTBY)
        self.resid = self.Y.iloc[:,:].values - np.dot(self.X, self.b)
        self.ee = np.dot(self.resid.T, self.resid)[0][0]
        #print('Coefs\n', self.b)







if __name__ == '__main__':

    df = pd.read_csv('../dataset/raw_dataset/Annual_inflation.csv')
    df['YYYYMM'] = df['YYYYMM'].astype('datetime64')
    years = df['YYYYMM'].dt.year.unique()
    year_range = years.max() - years.min() # =46



    df['Inflation_lag1'] = df['Annual_inflation'].shift(1)
    df = df.drop([0])

    lamb = 0.97
    gamma = 0.000000000001
    gamma = 1
    t = df[['YYYYMM']]
    x = sm.add_constant(df[['Inflation_lag1']])
    y = df[['Annual_inflation']]

    #model = RLS.fit(df[['YYYYMM']], x, y, lamb = lamb)
    #bs = model.series_b
    ##          YYYYMM     const  Inflation_lag1
    ##  551 2024-02-01  0.036481        0.988086
    print(df)

    fit(t,x,y,lamb = lamb, gamma = gamma)




