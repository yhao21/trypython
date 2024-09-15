import numpy as np
import pandas as pd
import statsmodels.api as sm



def RLS_LFE(t_list, X, Y, ageqtr, theta, is_OLS = False):
    '''
    '''

    ###------Initialization------###
    nx = X.shape[1]     # num of explanatory variables including constant terms
    b = np.ones((nx, 1))
    R = np.ones((nx, nx))

    for t in range(len(t_list)):

        if is_OLS:
            gamma = 1/(t+1)
        else:
            gamma = theta/ageqtr[t]

        x = X.values[t].reshape(nx, 1)
        xx =  np.dot(x, x.T)
        y = Y.values[t][0]
        err = y - np.dot(b.T, x)[0][0]

        R = R + gamma * (xx - R)
        b = b + gamma * np.dot(np.linalg.inv(R), x) * err

    '''
        [[0.01510205]
         [0.26191154]]
    '''
    return b




if __name__ == '__main__':
    df = pd.read_csv('../dataset/age_cohorts/inflation_nagel.csv')[['YYYYMM', 'Inflation']]
    df['YYYYMM'] = df['YYYYMM'].astype('datetime64[ns]')
    print(df)

    df['Inflation_lag1'] = df['Inflation'].shift(1)
    df = df.drop([0]).reset_index(drop = True)
    df['ageqtr'] = (df['YYYYMM'].dt.year - 1800) * 4 + df['YYYYMM'].dt.quarter

    t = df[['YYYYMM']]
    x = sm.add_constant(df[['Inflation_lag1']])
    y = df[['Inflation']]
    ageqtr = df['ageqtr']

    theta = 1


    RLS_LFE(t, x, y, ageqtr, theta)

    #model = sm.OLS(y, x).fit()
