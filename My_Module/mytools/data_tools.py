import pandas as pd
import numpy as np
from dateutil import relativedelta
import matplotlib.pyplot as plt
import os
import matplotlib.dates as mdates


def get_QoQ(df):
    '''
    This function will compute quarterly average using monthly raw data


         YYYYMM  Inflation                   YYYYMM  Inflation
0    1872-01-01   1.524880              0    1872Q1  -0.471015
1    1872-02-01  -1.479751              1    1872Q2   6.470473
2    1872-03-01  -1.458173      ==>     2    1872Q3   7.366998
3    1872-04-01   4.538217              3    1872Q4   3.836112
4    1872-05-01   7.008965              4    1873Q1   3.304951

    '''

    mapping = {
            "1":"01",
            "2":"04",
            "3":"07",
            "4":"10",
            }
    df['YYYYMM'] = df['YYYYMM'].astype('datetime64[ns]')
    # Convert 2020-01-01 to 2020Q1.
    df['YYYYMM'] = pd.PeriodIndex(pd.to_datetime(df.YYYYMM), freq = 'Q')
    df['YYYYMM'] = df['YYYYMM'].apply(lambda x: f'{x.year}-{mapping[str(x.quarter)]}-01')



    # Compute quarterly average.
    df = df.groupby(['YYYYMM'], as_index = False).mean()


    return df

def moving_average(window_size, arr):
    '''
    arr: a list of data.
    '''

    # Program to calculate moving average
    #arr = [1, 2, 3, 7, 9]
    #window_size = 3
    
    i = 0
    # Initialize an empty list to store moving averages
    moving_averages = []
    
    # Loop through the array to consider
    # every window of size 3
    while i < len(arr) - window_size + 1:
    
    	# Store elements from i to i+window_size
    	# in list to get the current window
    	window = arr[i : i + window_size]
    
    	# Calculate the average of current window
    	window_average = round(sum(window) / window_size, 6)
    	
    	# Store the average of current
    	# window in moving average list
    	moving_averages.append(window_average)
    	
    	# Shift window to right by one position
    	i += 1
    
    return moving_averages


def plot_trend_init(fig_spec = {"unit":'year',"fontsize":20,"figsize":(12,8),"month_interval":[1,6],"year_interval":5,"sharex":True,"sharey":True,}, xlabel = '', ylabel = ''):

    
    '''
    This function set up a general format for all charts you would like to plot.
    fig_spec = {
            "unit":'year',
            "fontsize":10,
            "figsize":(6,4),
            "month_interval":[1,6],     months in showed up. In this case, Jan and Jun.
            "year_interval":5,          Mark ticks every <year_interval> years.
            "sharex":True,
            "sharey":True,
            }

    '''

    fig, ax = plt.subplots(figsize = fig_spec['figsize'], sharex = fig_spec['sharex'], sharey = fig_spec['sharey'])
    fig.autofmt_xdate(rotation = 30)


    if fig_spec['unit'] == 'month':
        ###------If you want to use month interval for horizontal axis------###
        #fmt_half_year = mdates.MonthLocator(interval=6)
        fmt_half_year = mdates.MonthLocator(fig_spec['month_interval'])
        ax.xaxis.set_major_locator(fmt_half_year)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    elif fig_spec['unit'] == 'year':
        ###------If you want to use month interval for horizontal axis------###
        year_axis = mdates.YearLocator(base = fig_spec['year_interval'])
        ax.xaxis.set_major_locator(year_axis)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    ###------Set labels------###
    ax.set_ylabel(ylabel, fontsize = fig_spec['fontsize'])
    ax.set_xlabel(xlabel, fontsize = fig_spec['fontsize'])

    ###------set fontsize for ticks on the horizontal and vertical axis------###
    ax.tick_params(axis = 'x', labelsize = fig_spec['fontsize'])
    ax.tick_params(axis = 'y', labelsize = fig_spec['fontsize'])



def save_test_df_tracking_id():
    '''
    This test df is used to track individual respondents. 
    It only includes four cols: YYYYMM, ID, IDPREV, DATEPR
    ID: Interview ID
    IDPREV: Interview ID for respondents who was being interviewed in the past. 
            We can track Interview IDs for a same respondent in the past by using IDPREV.
    DATEPR: Previous date being interviewed. Usually, a respondent will be re-interviewed
            every six months.
    '''
    #df = pd.read_csv('./complete_data_full_variables.csv', low_memory=False)
    df = pd.read_csv('./full_dataset.csv', low_memory=False) # this is an updated dataset.
    test_df = df[['YYYYMM', 'ID', 'IDPREV', 'DATEPR']]
    test_df.to_csv('./test_df_assign_individual_id.csv', index = False)
    print('Test df is being created.')


def check_obs_each_month(obs_each_month, path_png_dir):
    t = obs_each_month.index.values
    plot_trend_init()

    plt.plot(t, obs_each_month.values)
    plt.title('No. of observations', fontsize = 20)
    plt.savefig(os.path.join(path_png_dir, 'no_obs.png'))
    plt.close()
    print('Plot obs each month!')

    # 01/1978 to 02/1980
    #print(obs_each_month[:26])
    # 03/1980 to 09/1987
    #print(obs_each_month[26:117])


def check_re_interview(re_interview_df, obs_each_month, path_png_dir):

    num_re_interviewed = re_interview_df['YYYYMM'].value_counts(sort = False) # re-interview starts in 01/1981
    start_month = num_re_interviewed.index[0]
    start_index = np.where(obs_each_month.index.values == start_month)[0][0]
    print(f'Re-interview sample starts in [{start_month}]')


    share_of_re_interviewed = np.around((num_re_interviewed/obs_each_month[start_index:]).values, 4) # obs_each_month[36:] starts from 01/1981


    t = num_re_interviewed.index.values

    plot_trend_init()
    plt.plot(t, share_of_re_interviewed)
    plt.title('Ratio of re-inerview sample', fontsize = 20)
    plt.savefig(os.path.join(path_png_dir, 'data_summary_share_of_re_interviewed.png'))
    plt.close()
    print('Plot ratio of re-interview sample!')

    #print(share_of_re_interviewed)

    num_fresh = (obs_each_month[start_index:] - num_re_interviewed).values

    ##------Line plot------##
    plot_trend_init()
    plt.plot(t, num_fresh, label = 'fresh sample')
    plt.plot(t, num_re_interviewed.values, label = 're-interview sample')
    plt.plot(t, obs_each_month[start_index:].values, label = 'Total')
    plt.legend(fontsize = 20)
    plt.title('No. of observations', fontsize = 20)
    plt.savefig(os.path.join(path_png_dir, 'data_summary_num_of_obs_samples_groups.png'))
    plt.close()
    print('Plot fresh and re-interview samples (lines)!')


    ##------Stackplot------##
    plot_trend_init()
    a = np.vstack([num_re_interviewed.values, num_fresh])
    labels = ['re-interview sample', 'fresh sample']
    #plt.stackplot([i for i in range(len(num_fresh))], a, labels = labels)
    plt.stackplot(t, a, labels = labels)
    plt.title('No. of observations', fontsize = 20)
    plt.legend(fontsize = 20)
    plt.savefig(os.path.join(path_png_dir, 'data_summary_sample_groups_stack.png'))
    plt.close()
    print('Plot fresh and re-interview samples (stacked)!')


def frequency_re_interview(re_interview_df):
    #print(re_interview_df)
    re_interview_df['YYYYMM'] = pd.to_datetime(re_interview_df['YYYYMM'], format = "%Y%m")

    re_interview_df['DATEPR'] = pd.to_datetime(re_interview_df['DATEPR'], format = "%Y%m")
    #print(re_interview_df.head(1))
    arow = re_interview_df
    #print(((arow['YYYYMM'] - arow['DATEPR'])/np.timedelta64(1,'M')).value_counts())

    # months      counts
    # 6.045299    38292
    # 5.946734    30161
    # 5.979589    24599
    # 6.012444    22913
    # 6.965235        7











def data_summary(path_png_dir, path_raw_df):
    '''
    Return the following characteristics over time:
        num. of obs
        num. of fresh and re-interview samples
        Ratio of re-investment sample
        Duration of re-interview: 6 months

    '''
    #df = pd.read_csv('./test_df_assign_individual_id.csv')
    df = pd.read_csv(path_raw_df)

    df['YYYYMM'] = pd.to_datetime(df['YYYYMM'], format = '%Y%m')
    #df['YYYYMM'] = df['YYYYMM'].astype('datetime64[ns]')

    unique_month = df['YYYYMM'].unique() # a list of unique month
    obs_each_month = df['YYYYMM'].value_counts(sort = False)
    '''
    I do not use DATEPR to track re-interview since all obs. in 1989-11 are marked
    as re-interview regarding DATEPR, however, only 233 of them have IDPREV.
    I believe this is an error made by the Michigan survey.
    '''
    #re_interview_df = df[df['DATEPR'] != df['DATEPR'][0]]
    re_interview_df = df[df['IDPREV'] != df['IDPREV'][0]]



    #plot_trend_init()

    ####------check obs. in each month------### 
    check_obs_each_month(obs_each_month, path_png_dir)


    ###------Check how many obs are re-interviewed------###
    ## Note: re-interview sample start in 01/1981
    check_re_interview(re_interview_df, obs_each_month, path_png_dir)
    

    ###------Frequency of being re-interviewed (How often?)------###
    frequency_re_interview(re_interview_df)

    


def track_individual_id(df, path_df, path_missing):

    '''
    This function identifies individual respondents and assigns unique IndividualID to each respondent.
    Pass full_dataset.csv into the function, it will return:
        1. full_dataset_with_individualID.csv
        2. missing_log.csv which stores past interviews that are not recorded in the original dataset.
    '''

    df['IndividualID'] = ['null' for i in range(len(df))]
    ##------start from the bottom. Backward iteration------##


    IndividualID = 0
    missing_log = []

    index_list = df.index.to_list() # remove a row index when that row is being assigned an individualID.
    index_list.reverse()

    for row_index in index_list:

        one_person = df.loc[row_index] # a row in form of df

        if one_person['IndividualID'] == 'null':

            while True:
                sub_row_index = one_person.name
                if one_person['DATEPR'] != ' ' * 6:
                    df['IndividualID'][sub_row_index] = IndividualID # assign individualID
                    #print(sub_row_index, one_person.values, IndividualID)
                    try: # I use "try" here because the original data does not include ID:282 in 199609
                        one_person = df[(df['YYYYMM'] == int(one_person['DATEPR'])) & (df['ID'] == int(one_person['IDPREV']))].iloc[0] # trace last interview, and update one_person in form of a serie.
                    except:
                        missing_data = missing_log.append([one_person['YYYYMM'], one_person['ID']])
                        IndividualID += 1
                        break
                else:
                    df['IndividualID'][sub_row_index] = IndividualID # assign individualID
                    print(sub_row_index, one_person.values, IndividualID)
                    print(f'Finish assigning person[{IndividualID}]')
                    IndividualID += 1
                    break



    print(df)
    print(missing_log)
    missing_log = pd.DataFrame(missing_log)
    missing_log.columns = ['YYYYMM', 'ID']
    df.to_csv(path_df, index = False)
    missing_log.to_csv(path_missing, index = False)




def get_times_an_individual_being_interviewed(df):
    IDs = df['IndividualID'].unique()
    times_each_individual = df['IndividualID'].value_counts()
    frequency = pd.DataFrame(times_each_individual.values.reshape(len(IDs), 1)).value_counts()

    '''
    Results:
        Times being interviewed        frequency
        1                                88639
        2                               104870
        3                                 5788
    '''


    print(frequency)
    total_HH = frequency.sum()
    print(f'Total respondents: {total_HH}')

    print('Ratio: times being interviewed')
    print(frequency/total_HH)




class DataSummary():
    def __init__(self, df, st, et, time_col):
        self.st = st    # start date
        self.et = et    # end date
        self.time_col = time_col
        self.df = get_df_within_time_interval(st, et, df, self.time_col)
        


    def mean_vs_median(self):
    #def mean_vs_median(df, st, et):
        '''
        This function will 
            1. form a new df including mean and median of HHs 1yr inflation exp,
            2. plot variance of mean and median inflation exp
        '''
    
    
        self.df[self.time_col] = self.df[self.time_col].astype('datetime64')
        df_agg_exp = pd.DataFrame()
        df_agg_exp[self.time_col]= self.df[self.time_col].unique()
        df_agg_exp['inf_1y_mean'] = self.df.groupby(self.time_col).apply(lambda row: ((row.PX1 * row.WT).sum())/row.WT.sum()).values     # compute weighted average of 1yr inflation expectation
        df_agg_exp['inf_1y_median'] = self.df.groupby(self.time_col)['PX1'].median().values
        return df_agg_exp
        
    
        
def get_df_within_time_interval(st, et, df, time_col):
    '''
    Return a df containing data within a certain time interval.
    '''
    return df[(df[time_col] >= st) & (df[time_col] <= et)]
        











if __name__ == '__main__':
    '''
    Note, the original dataset does not include the following case.
            YYYYMM   ID IDPREV  DATEPR
            199609  282
    '''
    #os.mkdir('./figures')

    ###------------### Get a test df to track each individual respondent.
    #save_test_df_tracking_id()



    ####------------### Summary of samples
    #data_summary()


    ###------------### Track individual respondents
    #test_df = pd.read_csv('./test_df_assign_individual_id.csv') # for testing
    #full_df = pd.read_csv('./full_dataset.csv')
    #track_individual_id(full_df)

    ###------------### How many times an invididual is being interviewed?
    #df = pd.read_csv('./full_dataset_with_individualID.csv', low_memory = False)
    #df = df[['YYYYMM', 'ID', 'IDPREV', 'DATEPR', 'IndividualID']]
    #get_times_an_individual_being_interviewed(df)


    df = pd.read_csv('../dataset/age_cohorts/inflation_1872_2024_monthly.csv')
    get_QoQ(df)








