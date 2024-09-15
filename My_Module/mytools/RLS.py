import os
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#from pandas_datareader.data import DataReader



df = sm.datasets.copper.load_pandas().data
df.index = pd.date_range('1951-01-01', '1975-01-01', freq = 'AS')
y = df['WORLDCONSUMPTION']
x = sm.add_constant(df[['COPPERPRICE','INCOMEINDEX','ALUMPRICE', 'INVENTORYINDEX']])
#mod = sm.RecursiveLS(y,x)
#result = mod.fit()
#print(result.summary())        # It is same as OLS estimator.



#const          -6562.3719   2378.939     -2.759      0.006   -1.12e+04   -1899.737
#COPPERPRICE      -13.8132     15.041     -0.918      0.358     -43.292      15.666
#INCOMEINDEX      1.21e+04    763.401     15.853      0.000    1.06e+04    1.36e+04
#ALUMPRICE         70.4146     32.678      2.155      0.031       6.367     134.462
#INVENTORYINDEX   311.7330   2130.084      0.146      0.884   -3863.155    4486.621
#===================================================================================
#Ljung-Box (L1) (Q):                   2.17   Jarque-Bera (JB):                 1.70
#Prob(Q):                              0.14   Prob(JB):                         0.43
#Heteroskedasticity (H):               3.38   Skew:                            -0.67
#Prob(H) (two-sided):                  0.13   Kurtosis:                         2.53



#mod_OLS = sm.OLS(y,x)
#result_OLS = mod_OLS.fit()
#print(result_OLS.summary())


# In RLS model: gamma(t) = 1/t, i.e., lambda = (t-1)/t. alpha = 1, 
#===================================================================================




class fit():
    '''
    fit().k         return num. of period being use to form the initial X'X matrix.
    fit().b         return lasted estimate of beta.
    fit().series_b  return all historical beta hat. The first col is "Time".
    fit().series_ee return all historical error
    '''
    def __init__(self, t, X, Y, lamb, a=1, c=100,P0_guess = False, print_result = False, not_return_y_hat = False):
        self.t = t          # time column, a df
        self.X = X          # a df
        self.Y = Y          # a df
        self.lamb = lamb
        self.a = a
        self.c = c
        self.k = 0
        self.SSR = 0
        self.P0_guess = P0_guess
        self.series_b = []       # return a dataframe
        self.series_ee = []      # return a dataframe
        self.series_e = []       # return a dataframe
        self.series_y_hat = []       # return a dataframe
        self.setup_figure_dir()
        self.print_result = print_result
        self.run()


    def setup_figure_dir(self):
        if not os.path.exists('./figures'):
            os.mkdir('./figures')
    def run(self):
        '''
        '''
        start_row = 0

        if self.P0_guess:
            self.P = self.c * np.identity(self.k)
            self.b = np.zeros((self.k,1))    #initial b_hat is a column of zeros.
            I = np.identity(self.k)
        else:
            self.k = self.X.shape[1] # get num. of explanatory variables. It determines
            # pass first k rows to fit the off-line identification.
            x = self.X.iloc[:self.k,:].values
            y = np.array(self.Y[:self.k]).reshape(self.k,1)
            self.P = np.linalg.inv(self.a * np.dot(x.T,x))
            self.b = np.dot(self.P, self.a * np.dot(x.T, y))    # a column vector
            start_row = self.k
            e = y - np.dot(x,self.b)
            #self.ee = np.dot(e.T,e)[0][0]
            self.ee = np.dot(e,e.T)
            self.SSR = np.diag(self.ee).sum()
            #print(self.ee[0][0])


        # Note, the new x and y should start from the k+1 row since you use the first
        # k row to compute initial P and b_hat

        self.series_b = self.b.T
        #self.series_ee = [self.ee]
        self.series_ee = [self.SSR]

        self.series_y_hat = list(np.dot(x,self.b).T[0])


        '''
        The initial e is not a scalar, it is a k * 1 matrix since we are using the
        first k columns to form the covariance matrix. Hence, we need to convert it
        into a list of scalars.
        '''
        self.series_e = [list(e.flatten())[1]]

        for i in range(start_row, len(self.Y)):

            x = self.X.iloc[i,:].values
            y = self.Y.iloc[i].values
            x = x.reshape(len(x),1)
            self.L = np.dot(self.P, x)/(self.lamb/self.a + np.dot(np.dot(x.T,self.P),x))
            e = y - np.dot(x.T,self.b)

            # update b_hat and P
            self.b = self.b + self.L*e
            self.P = 1/self.lamb * (self.P - np.dot(np.dot(self.L,x.T),self.P))
            #self.ee = np.dot(e.T,e)[0][0]
            self.ee = np.dot(e,e.T)
            self.SSR = np.diag(self.ee).sum()


            # store values
            self.series_b = np.vstack((self.series_b, self.b.T))
            #self.series_ee.append(self.ee)
            self.series_ee.append(self.SSR)
            self.series_e.append(e[0][0])
            self.series_y_hat.append(np.dot(x.T,self.b)[0][0])


            if self.print_result:
                print(f'b:{self.b}')
                print(f'P:{self.P}')
                print(f'e:{e}')
                print(f'L:{self.L}')
            

        


        #print(self.series_e)
        time_col = self.t[self.k-1:].reset_index(drop = True)
        self.series_b = pd.DataFrame(self.series_b, columns = self.X.columns.to_list())
        self.series_b = pd.concat([time_col, self.series_b], axis = 1)
        self.series_ee = pd.concat([time_col, pd.DataFrame(self.series_ee)], axis = 1)
        self.series_ee.columns = ['Time', 'SSR']

        self.series_e = pd.concat([time_col, pd.DataFrame(self.series_e)], axis = 1)
        self.series_e.columns = ['Time', 'Error']

        self.series_y_hat = pd.DataFrame(self.series_y_hat, columns = self.Y.columns.to_list())
        self.series_y_hat = pd.concat([self.t, self.series_y_hat], axis = 1)



def multiple_lambda(t, X, Y, lam_list, a, c, variable, P0_guess = True):
    '''
    You need to specify a list of lambdas.

    You need to specify which variable you are looking at. By default, it will
    run for all variables.
    '''
    df_b = pd.DataFrame()   # a df store b_hat under different lambda.
    df_e = pd.DataFrame()   # a df store e under different lambda.
    for lam in lam_list:
        model = fit(t,X,Y,lam,a,c,P0_guess = False)
        series_b = model.series_b[variable]
        df_b[f'lambda={lam}'] = series_b
    
        series_e = model.series_e['Error']
        df_e[f'lambda={lam}'] = series_e


                
    df_b = pd.concat([model.series_b.iloc[:,0], df_b], axis = 1)
    df_e = pd.concat([model.series_b.iloc[:,0], df_e], axis = 1)


    return df_b, df_e

                
def multiple_lambda_multi_variables(t,x,y,lam_list,a,c,one_vr,P0_guess=False):
    df_lams = pd.DataFrame()

    for lam in lam_list:
        model = fit(t,x,y,lam,a,c,P0_guess = False)
        series_b = model.series_b
        series_e = model.series_e[['Error']]
        col_b = series_b.columns.to_list()
        col_b[1] = f'const_{one_vr}'
        col_b = [col_b[0]]+[f'{i}_lambda={lam}' for i in col_b[1:]]
        series_b.columns = col_b
        series_e.columns = [f'Error_{one_vr}_lambda={lam}']

        df_lams = pd.concat([df_lams, series_b[col_b[1:]], series_e], axis = 1)
    
    return df_lams



def plot_trend(df, plot_all = True, list_x = [], title = 'Results', fig_spec = {"figsize":(10,15),"fontsize":20,"unit":"month","month_interval":[1,4,7,10],"year_interval":5,"png_path":os.path.join("./figures", "result.png")}):

    '''
    You must specify fig_spec:
        fig_spec = {
                "fontsize": int,
                "unit":"month" or "year",
                "month_interval": [1,4,7,10], i.e., a list of months,
                "png_path":"./figures/result.png", i.e., path of png.
                ""
        }
    This function plots the trend of all estimators (beta hat) for a given model.



    The first k row are being used to form the covariance matrix. Do not use y.index.strftime('%Y-%M-%d')[myRLS.k-1:]! Your horizontal axis formatter will not work if times are saved as string. It MUST be datetime64.
    '''
    fig_spec = fig_spec
    x = df.iloc[:,0].values
    variables = df.columns.tolist()[1:]
    fig, axs = plt.subplots(len(variables), sharex = True, figsize = fig_spec['figsize'])


    fsize = 20          # fontsize
    index = 0
    for ax in axs:
        one_variable = variables[index]
        ax.plot(x,df[one_variable])

        index += 1

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
        ax.set_ylabel(one_variable, fontsize = fig_spec['fontsize'])
        ax.set_xlabel('Time', fontsize = fig_spec['fontsize'])

        ###------set fontsize for ticks on the horizontal and vertical axis------###
        ax.tick_params(axis = 'x', labelsize = fig_spec['fontsize'])
        ax.tick_params(axis = 'y', labelsize = fig_spec['fontsize'])

    fig.suptitle(title, fontsize = fig_spec['fontsize'])
    fig.autofmt_xdate()
    plt.savefig(fig_spec['png_path'])







def plot_trend_init(fig_spec = {"unit":'year',"fontsize":20,"figsize":(12,8),"month_interval":[1,6],"year_interval":5,"sharex":True,"sharey":True,}, xlabel = '', ylabel = ''):

    
    '''
    This function set up a general format for all Time Series charts you would like to plot.
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





def plot_init(fig_spec = {"unit":'year',"fontsize":20,"figsize":(12,8),"month_interval":[1,6],"year_interval":5,"sharex":True,"sharey":True,}, xlabel = '', ylabel = ''):

    
    '''
    This function set up a general format for all charts other than time series chart you would like to plot.
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



    ###------Set labels------###
    ax.set_ylabel(ylabel, fontsize = fig_spec['fontsize'])
    ax.set_xlabel(xlabel, fontsize = fig_spec['fontsize'])

    ###------set fontsize for ticks on the horizontal and vertical axis------###
    ax.tick_params(axis = 'x', labelsize = fig_spec['fontsize'])
    ax.tick_params(axis = 'y', labelsize = fig_spec['fontsize'])










if __name__ == '__main__':


    df = sm.datasets.copper.load_pandas().data
    df.index = pd.date_range('1951-01-01', '1975-01-01', freq = 'AS')
    y = df['WORLDCONSUMPTION']
    x = sm.add_constant(df[['COPPERPRICE','INCOMEINDEX','ALUMPRICE', 'INVENTORYINDEX']])


    ###------Run RLS------###
    lamb = 1
    a = 1
    c = 100
    
    t = pd.DataFrame(y.index)
    myRLS = fit(t,x,y,lamb,a,c, False)
    print(myRLS.series_b)
    print(type(x))
    print(type(y))
    print(type(t))


    #path_df = '/home/synferlo/Dropbox/papers/0_code/dataset/demo_groups.csv'
    #time_col = 'YYYYMM'
    #df = pd.read_csv(path_df)

    #pi_t1 = df['exp_1y_mean'].loc[12:]
    #pi_t = df[['exp_1y_mean']].loc[:len(df) - 13]
    #t = df[[time_col]]






    
    ####------Plot trend of each estimator------###
    #time_horizon = pd.DataFrame(y.index[myRLS.k-1:]) # the first k row are being used to form the covariance matrix. Do not use y.index.strftime('%Y-%M-%d')[myRLS.k-1:]! Your horizontal axis formatter will not work if times are saved as string.
    #col_name = ['TIME'] + x.columns.tolist()+['SSR']
    #
    #estimators = pd.concat([time_horizon, myRLS.series_b[1:], myRLS.series_ee[1:]], axis = 1)
    #estimators.columns = col_name
    #
    #fig_spec = {
    #        "unit":'year',
    #        "fontsize":20,
    #        "png_path":'./new.png'
    #        }
    #plot_trend(estimators, fig_spec = fig_spec)
    
    
    
    ###------Use different ------###
    
    
    
    
    
    
    
    
    
    
    
    
