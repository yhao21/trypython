import pandas as pd
import numpy as np
import os, glob, re
import matplotlib.pyplot as plt
import toolkits as tk
from sklearn.neighbors import KernelDensity
import seaborn as sns
from datetime import date
import datetime




def check_zero_values(crypto_names, crypto_df):

    zero_value = False
    # crypto is str here
    for crypto in crypto_names:
        price = crypto_df[crypto].values
        if 0 in price:
            zero_value = True
            zero_index = np.where(price == 0)[0]
            print(crypto, zero_index)

            for zero_row in zero_index:
                previous_value = crypto_df.loc[[zero_row-1],crypto].values
                i = 1
                next_value = 0
                while True:
                    # next value
                    if crypto_df.loc[[zero_row+i],crypto].values != 0:
                        next_value = crypto_df.loc[[zero_row+i],crypto].values
                        break
                    i += 1
                crypto_df.at[zero_row, crypto] = (previous_value + next_value)/2
    if zero_value:
        crypto_df.to_csv('csv_folder/qualified_all_cryptos_price_156weeks.csv', index = False)

    return crypto_df




def calculate_sd_expected_return(crypto_names, crypto_df, df, extreme_value = True):
    '''
    This function will merge sd and E to a df
    df: merged dataframe
    '''

    # standard deviation for each crypto return
    sd_crypto = []
    # expected return E(r_i)
    expected_return = []
    
    for crypto in crypto_names:
        daily_return = tk.compute_n_lag_return(crypto_df[crypto], 1, change_rate = True)
        if not extreme_value:
            sd_crypto.append(np.std(daily_return))
            expected_return.append(np.average(daily_return))
        else:
            # take log if there are very large number
            ## log risk vs log return
            sd_crypto.append(np.log(np.std(daily_return)))
            expected_return.append(np.log(np.average(daily_return)))
    
    
    df['sd_price'] = sd_crypto
    df['expected_return_1D'] = expected_return

    return sd_crypto, expected_return, df




def main():

    price_df = pd.read_csv('csv_folder/qualified_all_cryptos_price_156weeks.csv')
    
    crypto_names = list(price_df.columns.values)
    del crypto_names[0]
    del crypto_names[-1]
    
    df = pd.DataFrame(crypto_names, columns = ['crypto'])
    
    
    
    
    # 1
    # check if there are zeros in df
    price_df = check_zero_values(crypto_names, price_df)

    # 2
    # merge SD and expected return
    sd_crypto, expected_return, df = calculate_sd_expected_return(crypto_names, price_df, df, False)
    
    








    # 3
    # plot SD-E() graph
    # note: if sd and expected value is too small, the log of them would be < 0
    '''
    log(SD) and log(E) are positive correlated. It is almost linear!
    '''
    plt.scatter(sd_crypto, expected_return)
    plt.xlabel('log of std. deviation (risk)')
    plt.ylabel('log of expected return')
    #plt.savefig('figures/daily_crypto_log-risk_log-return.png')
    #plt.savefig('crypto_log-risk_log-return.png')
    plt.clf()
    
    
    '''
    Because the SD and E() of crypto: digixdao is extremely large, outlier. 
    Let's see would the risk-return figure look like if we remove digixdao
    '''
    #==============
    #
    #
    #max_index = sd_crypto.index(max(sd_crypto))
    #print(max_index)
    #print(df.loc[[max_index]])
    #
    #price_digixdao = price_df['digixdao'].values
    #plt.plot([i for i in range(len(price_digixdao))], price_digixdao)
    #plt.savefig('a.png')
    #plt.clf()
    
    

    ## Remove outlier
    large_index = []
    # contains all outlier names
    outlier = []
    for i in sd_crypto:
        if i > 50:
            large_index.append(sd_crypto.index(i))
    print(large_index)


    for outlier_crypto in large_index:
        outlier.append(df.loc[[outlier_crypto]]['crypto'].values[0])
    print(outlier)
    price_df = price_df.drop(outlier, axis = 1)




    crypto_names = list(price_df.columns.values)
    del crypto_names[0]
    del crypto_names[-1]

    df = pd.DataFrame(crypto_names, columns = ['crypto'])
    sd_crypto, expected_return, df = calculate_sd_expected_return(crypto_names, price_df, df, False)

    plt.scatter(sd_crypto, expected_return)
    plt.xlabel('std. deviation (risk)')
    plt.ylabel('expected return')
    plt.savefig('figures/daily_crypto_no_outlier_risk_return.png')
    plt.clf()
    

    #==============
    
    
        
    






if __name__ == '__main__':
    #main()
    a = [i for i in range(1,22)]
    print(a)
    daily_diff = tk.compute_n_lag_return(a,1)
    weekly_diff = tk.compute_n_lag_return(a,7)

    print(weekly_diff)








