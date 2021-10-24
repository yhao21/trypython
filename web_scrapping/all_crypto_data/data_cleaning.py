import pandas as pd
import numpy as np
import os, glob, re
import matplotlib.pyplot as plt
import toolkits as tk
from sklearn.neighbors import KernelDensity
import seaborn as sns
from datetime import date
import datetime
import matplotlib.pyplot as plt



def plot_period_qualified_cryptos():
    file_folder = 'history_csv'
    file_path = os.path.join(file_folder,'*.csv')
    
    
    
    time_period = [i*50 for i in range(50)]
    qualified_crypto_num = []
    
    
    round_index = 1
    for periods in time_period:
        print(f'[{round_index}/{len(time_period)}]')
    
        count = 0
        for one_file in glob.glob(file_path):
            name = re.compile(r'history_csv/(.*).csv').findall(one_file)[0]
            df = pd.read_csv(one_file)
            if len(df) > periods - 1:
                count += 1
    
        qualified_crypto_num.append(count)
        round_index += 1
    
    plt.plot(time_period, qualified_crypto_num)
    plt.xlabel('num_of_days')
    plt.ylabel('num_of_qualified_cryptos')
    plt.savefig('figures/periods_qualified_cryptos.png')
    plt.clf()







def merge_dfs():
    df1 = pd.read_csv('csv_folder/each_crypto.csv')
    df2 = pd.read_csv('csv_folder/homepage_crypto_href.csv')
    print(df1)
    print(df2)
    df1_crypto_name = list(df1['name'].values)
    df2_crypto_name = list(df2['name'].values)

    remove_list = []
    for crypto in df2_crypto_name:
        if crypto not in df1_crypto_name:
            remove_list.append((crypto, df2_crypto_name.index(crypto)))

    remove_index = remove_list[0][1]
    df = df2.drop(df2.index[remove_index], axis = 0)
    df = df.drop(['href'], axis = 1)
    df = df.sort_values('name').reset_index(drop = True)
    df1 = df1.sort_values('name').reset_index(drop = True)
    # df is the merged dataframe
    df['max_supply'] = df1['max_supply']


    print(df)


def risk_sd_return():
    file_path = os.path.join('history_csv', '*.csv')
    for crypto_csv in glob.glob(file_path):
        name = re.compile(r'history_csv/(.*).csv').findall(crypto_csv)[0]
        print(name)
        crypto_df = pd.read_csv(crypto_csv)
        open_price = crypto_df['open_price'].values
        price_sd = np.std(open_price)
        print(price_sd)
    
def return_of_different_cryptos():
    crypto_list = ['bitcoin','ethereum','dogecoin','shiba-inu','polygon','fm-gallery']
    for crypto in crypto_list:
        df = pd.read_csv(f'history_csv/{crypto}.csv')
        price = df['open_price'].values.astype('float32')
        return_rate = tk.compute_n_lag_return(price,my_lags = 14, change_rate = True)
        scale = [0.05 * i for i in range(-30, 30)]


            #plt.hist(return_rate, bins = scale, rwidth = 0.8)
            #plt.savefig(f'figures/{crypto}_return_distribution.png')
            #plt.clf()


        sns.distplot(return_rate, kde = True, hist = False, bins = scale,\
                    label = f'{crypto}')
    plt.legend()
    plt.xlabel('rate of returns')
    plt.savefig(f'return_rate/return_diff_cryptos.png')
    plt.clf()


def return_different_periods():
    crypto_list = ['bitcoin','ethereum','dogecoin','shiba-inu','polygon','fm-gallery']
    for crypto in crypto_list:
        df = pd.read_csv(f'history_csv/{crypto}.csv')
        price = df['open_price'].values.astype('float32')

        # different return periods: daily, weekly, half-monthly, monthly
        periods = [1,7,14,30]
        for period in periods:
            return_rate = tk.compute_n_lag_return(price,my_lags = period, change_rate = True)
            scale = [0.05 * i for i in range(-30, 30)]

            sns.distplot(return_rate, kde = True, hist = False, bins = scale,\
                    label = f'Return periods:{period}')
        plt.legend()
        plt.xlabel('rate of returns')
        plt.savefig(f'return_rate/{crypto}.png')
        plt.clf()




def check_NIF():
    '''
    [uniform-fiscal-object]: Price: 0 Mktcap: 0
    '''

    date_missing_data = []
    df = pd.DataFrame()
    file_path = os.path.join('history_csv','*.csv')
    for crypto_csv in glob.glob(file_path):
        price_NIF_count = 0
        mktcap_NIF_count = 0
        crypto_df = pd.read_csv(crypto_csv)
        name = re.compile(r'history_csv/(.*).csv').findall(crypto_csv)[0]
        for price in crypto_df['open_price']:
            if price == 'NIF':
            #if type(price) != float:
                price_NIF_count += 1
                row_index = list(crypto_df['open_price'].values).index(price)
                print(crypto_df.loc[[row_index]])



        for mktcap in crypto_df['mktcap']:
            if mktcap == 'NIF':
            #if type(mktcap) != float:
                mktcap_NIF_count += 1

        if price_NIF_count != 0:
        #if mktcap_NIF_count != 0:
            print(f'[{name}]: Price: {price_NIF_count} Mktcap: {mktcap_NIF_count}')





def check_if_time_consecutive():
    file_path = os.path.join('history_csv','*.csv')
    qualify_count = 0
    # record unqualified crypto info (name, len(df))
    df = pd.DataFrame()

    for crypto_csv in glob.glob(file_path):
        crypto_df = pd.read_csv(crypto_csv)
        name = re.compile(r'history_csv/(.*).csv').findall(crypto_csv)[0]
        # use dt.date to keep date info only
        crypto_df['date'] = pd.to_datetime(crypto_df['date']).dt.date


        start_date = crypto_df['date'].values[0]
        if start_date == date(2021,10,5):
            qualify_count += 1
            check_consecutive(crypto_df['date'].values, name)
        else:
            df = df.append({
                'name':name,
                'len(df)':len(crypto_df)
                }, ignore_index = True)

        #for date in crypto_df['date']:
    print(qualify_count)
    df.to_csv('csv_folder/time_unqualified_cryptos.csv', index = False)
    print(df)


def check_consecutive(time_series, name):
    start_date = time_series[0]
    count = 0
    for date_index in range(1,len(time_series)):

        # time_series[date_index] is the next day
        if (start_date - time_series[date_index]).days != 1:
            count += 1
        start_date = time_series[date_index]
    if count != 0:
        print(f'{name}: {count} days')





def period_qualified_cryptos():
    '''
    select cryptos last for a particular time, e.g., 2 years, 3 years
    save their csv to period_qualified_csv
    '''
    file_folder = 'period_qualified_csv'
    if not os.path.exists(file_folder):
        os.mkdir(file_folder)

    # I need weekly return, <periods> convert # of week to days.
    # +2: tile and NIF in the first row.
    periods = (3*365//7) * 7 + 2
    print(periods)

    i = 1
    workload = len(glob.glob('history_csv/*.csv'))
    for crypto_csv in glob.glob('history_csv/*.csv'):

        print(f'[{i}/{workload}]')
        crypto_df = pd.read_csv(crypto_csv)
        crypto_df = crypto_df.drop(['Unnamed: 0'], axis = 1)
        name = re.compile(r'history_csv/(.*).csv').findall(crypto_csv)[0]
        if len(crypto_df) > periods - 1:
            crypto_df.to_csv(f'period_qualified_csv/{name}.csv', index = False)
        i += 1



def price_NIF():

    file_path = 'period_qualified_csv/*.csv'
    for crypto_csv in glob.glob(file_path):
        price_NIF_count = 0
        crypto_df = pd.read_csv(crypto_csv)
        name = re.compile(r'period_qualified_csv/(.*).csv').findall(crypto_csv)[0]
        for price in crypto_df['open_price']:
            if price == 'NIF':
            #if type(price) != float:
                price_NIF_count += 1
                row_index = list(crypto_df['open_price'].values).index(price)
                previous_value = float(crypto_df.loc[[row_index - 1]]['open_price'].values[0])
                next_value = float(crypto_df.loc[[row_index + 1]]['open_price'].values[0])

                crypto_df.at[row_index, 'open_price'] = \
                        (previous_value + next_value)/2

                print(name)
                print(crypto_df.loc[[row_index]])


        crypto_df.to_csv(f'period_qualified_csv/{name}.csv', index = False)

def mktcap_NIF():
    file_path = 'period_qualified_csv/*.csv'
    i = 1
    workload = len(glob.glob(file_path))
    for crypto_csv in glob.glob(file_path):
        print(f'[{i}/{workload}]')
        mktcap_NIF_count = 0
        crypto_df = pd.read_csv(crypto_csv)
        name = re.compile(r'period_qualified_csv/(.*).csv').findall(crypto_csv)[0]

        mktcap_miss = False
        for mktcap in crypto_df['mktcap'].values:
            if mktcap == 'NIF' or mktcap == 0:
                mktcap_NIF_count += 1
                row_index = list(crypto_df['mktcap'].values).index(mktcap)
                previous_cir_supply = float(crypto_df.loc[[row_index - 1]]['mktcap'].values[0])\
                        /float(crypto_df.loc[[row_index - 1]]['open_price'].values[0])
                crypto_df.at[row_index, 'mktcap'] = previous_cir_supply \
                        * float(crypto_df.loc[[row_index]]['open_price'].values[0])



                #crypto_df.at[row_index, 'open_price'] = \
                #        (previous_value + next_value)/2
                mktcap_miss = True
        if mktcap_miss:
            print(f'{name}: {mktcap_NIF_count}')
        i += 1
        crypto_df.to_csv(f'period_qualified_csv/{name}.csv', index = False)



def consecutive_date_data():
    start_date = date(2021,10,1)
    daily_list = [start_date - datetime.timedelta(days = i) for i in range((3*365//7) * 7)]
    weekly_list = [start_date - datetime.timedelta(days = 7*i) for i in range(3*365//7)]
    file_path = 'period_qualified_csv_/*.csv'


    for crypto_csv in glob.glob(file_path):
        daily_count = 0
        weekly_count = 0
        miss_date = False
        miss_week = False
        name = re.compile(r'period_qualified_csv_/(.*).csv').findall(crypto_csv)[0]
        crypto_df = pd.read_csv(crypto_csv)
        crypto_date = crypto_df['date'].values

        # check daily data missing
        for i in daily_list:
            if str(i) not in crypto_date:
                miss_date = True
                daily_count += 1


        if miss_date:
            print(f'{name}: {daily_count}')
            # if data missing > 0 days, remove this crypto
            if daily_count > 0:
                os.remove(f'period_qualified_csv_/{name}.csv')


        # check weekly data missing
        for i in weekly_list:
            if str(i) not in crypto_date:
                miss_week = True
                weekly_count += 1
                print(i)
        if miss_week:
            print(f'{name}: {weekly_count}')



def setup_starting_date(start_date):

    file_path = 'period_qualified_csv_/*.csv'
    for crypto_csv in glob.glob(file_path):
        name = re.compile(r'period_qualified_csv_/(.*).csv').findall(crypto_csv)[0]
        crypto_df = pd.read_csv(crypto_csv)
        crypto_date = list(crypto_df['date'].values)
        row_index = crypto_date.index(start_date)
        remove_rows = [i for i in range(row_index)]
        crypto_df = crypto_df.drop(remove_rows, axis = 0)
        crypto_df.to_csv(f'period_qualified_csv_/{name}.csv', index = False)



def merge_price_mktcap():
    '''
    price df:
    date  BTC_price  ETH_price  Dogecoin_price....

    mktcap df:
    date  BTC_mktcap  ETH_mktcap  Dogecoin_mktcap....

    '''
    start_date = date(2021,10,1)
    daily_list = [start_date - datetime.timedelta(days = i) for i in range((3*365//7 - 1) * 7 + 1)]
    price_df = pd.DataFrame(daily_list, columns = ['date'])
    mktcap_df = pd.DataFrame(daily_list, columns = ['date'])
    name_list = ['date']
    file_path = 'period_qualified_csv_/*.csv'


    i = 1
    workload = len(glob.glob(file_path))
    for crypto_csv in glob.glob(file_path):
        print(f'[{i}/{workload}]')
        name = re.compile(r'period_qualified_csv_/(.*).csv').findall(crypto_csv)[0]
        crypto_df = pd.read_csv(crypto_csv)
        # last day: 2018-10-12
        row_index = [i for i in range(155*7 + 1)]
        sub_df = crypto_df.loc[row_index]
        price_col = sub_df['open_price']
        mktcap_col = sub_df['mktcap']

        # use it to name columns for price_df, mktcap_df
        name_list.append(name)

        price_df[f'{name}'] = price_col
        mktcap_df[f'{name}'] = mktcap_col

        i += 1


    price_df = price_df[name_list]
    mktcap_df = mktcap_df[name_list]
    print(price_df)
    print(mktcap_df)
    #if list(price_df.columns.values) == list(mktcap_df.columns.values):
    #    print('yes')



    price_df.to_csv('csv_folder/qualified_all_cryptos_price_156weeks.csv', index = False)
    mktcap_df.to_csv('csv_folder/qualified_all_cryptos_mktcap_156weeks.csv', index = False)




def merge_qualified_cryptos_with_rf_total_mktcap():
    ## Cleaning and imputation for tbill df
    start_date = date(2021,10,1)
    daily_list = [start_date - datetime.timedelta(days = i) for i in range((3*365//7 - 1) * 7 + 1)]
    tbill_df = pd.read_csv('csv_folder/3month_t-bill_return_rate.csv')
    tbill_df.columns = ['date', 'rate_of_return']
    tbill_df.sort_values('date', inplace = True, ascending = False)
    tbill_df = tbill_df.reset_index(drop = True)
    print(tbill_df)


    # remove rows with '.'
    return_list = tbill_df['rate_of_return'].values 
    row_list = np.where(return_list == '.')[0]
    tbill_df.drop(row_list, axis = 0, inplace = True)
    tbill_df.sort_values('date', inplace = True, ascending = False)
    tbill_df = tbill_df.reset_index(drop = True)

    
    count = 0
    for i in daily_list:
        tbill_dates = tbill_df['date'].values
        if str(i) not in tbill_dates:
            previous_date = i + datetime.timedelta(days = 1)

            row_previous_index_tbill = list(tbill_dates).index(str(previous_date))
            row_next_index_tbill = row_previous_index_tbill + 1

            # missing data = average(previous, next)
            previous_day_return = float(tbill_df.loc[[row_previous_index_tbill]]['rate_of_return'].values[0])
            next_day_return = float(tbill_df.loc[[row_next_index_tbill]]['rate_of_return'].values[0])
            tbill_df = tbill_df.append({
                'date':str(i),
                'rate_of_return':(previous_day_return + next_day_return)/2
                },ignore_index = True)
            tbill_df.sort_values('date', inplace = True, ascending = False)
            tbill_df = tbill_df.reset_index(drop = True)

            #print(f'i: {i}')
            #print(f'previous_date: {previous_date}')
            #print(previous_day_return)
            #print(tbill_df.loc[[row_previous_index_tbill]])


            count += 1
    tbill_df.columns = ['date','risk_free_rate']
    print(tbill_df)

    ## loading cryptos price, mkt df
    price_df = pd.read_csv('csv_folder/qualified_all_cryptos_price_156weeks.csv')
    mktcap_df = pd.read_csv('csv_folder/qualified_all_cryptos_mktcap_156weeks.csv')

    price_df['risk_free_rate'] = tbill_df['risk_free_rate']
    mktcap_df['risk_free_rate'] = tbill_df['risk_free_rate']
    print(price_df)
    print(mktcap_df)

    total_mktcap_df = pd.read_csv('csv_folder/cryptoTOTAL_mktcap_.csv')\
            .sort_values('time', ascending = False)
    total_mktcap_df.reset_index(drop = True, inplace = True)
    total_mktcap_df = pd.DataFrame(total_mktcap_df.iloc[10:1096, :2].values, columns = \
            ['date','total_mktcap'])
    total_mktcap_df['date'] = pd.to_datetime(total_mktcap_df['date']).dt.date
    print(total_mktcap_df)

    mktcap_df['total_mktcap'] = total_mktcap_df['total_mktcap']
    print(mktcap_df)





    price_df.to_csv('csv_folder/qualified_all_cryptos_price_156weeks.csv', index = False)
    mktcap_df.to_csv('csv_folder/qualified_all_cryptos_mktcap_156weeks.csv', index = False)
    # mktcap dominance in my dataframe 0.799026103495852
    # the sum of mktcap for qualified cryptos take 80% of the entire mkt
    mktcap_dominance = np.sum(mktcap_df.iloc[0,1:-2].values)/mktcap_df.iloc[0,-1]






if __name__ == '__main__':



    ## step 1 select cryptos with 3-year data
    #period_qualified_cryptos()


    ## step 2 missing data imputation
    #price_NIF()
    #mktcap_NIF()

    ## remove crypto missing daily date within 3 years
    #consecutive_date_data()   


    ## make all cryptos start from 2021-10-01
    #start_date = date(2021,10,1)
    #setup_starting_date(str(start_date))

    ## last day: 2018-10-12
    #weekly_list = [start_date - datetime.timedelta(days = 7*i) for i in range(3*365//7)]
    #print(weekly_list[-1])
    #print(len(weekly_list))

    ## gather all qualified cryptos' price and mktcap in two different dfs
    #merge_price_mktcap()

    ## merge risk free rate and total mktcap with price_df, mktcap_df
    #merge_qualified_cryptos_with_rf_total_mktcap()













    #merge_dfs()

    ## SD for weekly return
    #risk_sd_return()

    #return_of_different_cryptos()
    #return_different_periods()
    #check_NIF()

    # check if date is consecutive
    #check_if_time_consecutive()













