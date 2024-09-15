import pandas as pd
import numpy as np




def form_regression_result(model, round_digit = 4, if_return = False, if_print = False, print_all = False, reg_model = 'OLS', t_name = None, hide_t = False):
    var_name = model.params.index.to_list()
    b = model.params.values                            # a pd series
    se = model.bse.values                              # a pd series
    obs = int(model.nobs)                       # a float number
    r2 = ''
    f = ''
    rmse = ''
    llr = ''                                    # likelihood ratio test chi2 statistics
    llr_pvalue = ''                             #likelihood ratio test pvalue
    if reg_model == 'OLS':
        r2 = round(model.rsquared_adj, round_digit) # a float number
        f = round(model.fvalue, round_digit)        # a float number
        rmse = round(np.sqrt(model.ssr/model.nobs), round_digit)
    elif reg_model == 'logit':
        r2 = round(model.prsquared, round_digit)
        llr = round(model.llr, round_digit)
        llr_pvalue = round(model.llr_pvalue, round_digit)
    p= round(model.pvalues, round_digit).values



    if hide_t:
        var_name = [i for i in var_name if i not in t_name]
        b = [model.params[i] for i in var_name]


    result = []
    result_col = []
    p_values = []
    for i in range(len(b)):


        p_star = p_to_star(p[i])
        result.append(f'{round(b[i], round_digit)}{p_star}&')
        result.append(f'({round(se[i],round_digit)})&')
        #result_col.append(b.index.to_list()[i])
        result_col.append(var_name[i])
        result_col.append('')


    #result += ['','',obs, r2, f]
    if reg_model == 'OLS':
        result += ['&','&',f'{obs}&', f'{r2}&', f'{f}&', f'{rmse}&']
        result_col += ['','','No. of Obs.', 'Adj. R squared', 'F-statistics', 'RMSE']
        p_values += ['']*5
    elif reg_model == 'logit':
        result += ['&','&',f'{obs}&', f'{r2}&', f'{llr}&', f'{llr_pvalue}&']
        result_col += ['','','No. of Obs.', 'Pseudo-R-squared', 'LR', 'LR-pvalue']

    df_result = pd.DataFrame()
    df_result['key'] = result_col
    df_result['value'] = result

    if if_print == True:
        if print_all:
            pd.set_option('display.max_rows', None)
        print(df_result)
    if if_return == True:
        return df_result



def init_result_df(reg_model = 'OLS', xs = ['const','tau','PX1_Not_weighted','exp_gap','AGE','EDUC2','EDUC3','EDUC4','EDUC5','EDUC6','SEX2','YTL52','YTL53','YTL54','YTL55','REGION2','REGION3','REGION4','PAGO1','PAGO2','INEXQ11','INEXQ12','PEXP1','PEXP2','BUS51','BUS52','RATEX1','RATEX2']):
    '''
    You need to use this function in together with function <form_result_to_df>
    This function initiate an empty df needed by function <form_result_to_df> to store regression result.
    reg_model: 'logit' or 'OLS'
    '''
    result = []
    
    for i in xs:
        result += [f'{i}&', f'{i}_se&']

    if reg_model == 'OLS':
        result += ['&', '&', 'No. of Obs.&', 'Adj. R squared&', 'F-statistics&', 'RMSE&']
    elif reg_model == 'logit':
        result += ['&', '&', 'No. of Obs.&', 'Pseudo-R-squared&', 'LR&', 'LR-pvalue&']
    
    df = pd.DataFrame(index = result)
    df['x'] = ['&' if '_se' in i else i for i in result]
    return df



def form_result_to_df(df, model, model_name, reg_model = 'OLS', round_digit = 4, hide_t = False, t_name = None):
    '''
    This function store formatted regression result in a df.

    Parameters:
                df: a df to store regression result. If you do not have one, you need to create an empty df from function <init_result_df>
                model: a fitted regression model from statsmodels, e.g., model = sm.Logit(y, x).fit()
                model_name (col name): a name (string) to name the column that store regression result.
                reg_model: 'OLS' or 'logit'. It determines the layout of df.
                hide_t: If True, df will not save coef for time dummies.
                t_name: Specify all column name of time dummies to drop if <hide_t> is being set True



    model: regression model
    df: df store regression results
    '''

    # set up result df
    
    df[model_name] = ['&' for i in range(len(df))]
    new_variable_added = False
    var_name = model.params.index.to_list()

    if hide_t:
        var_name = [i for i in var_name if i not in t_name]
    
    
    #for coef in model.params.index:
    for coef in var_name:
        stars = p_to_star(model.pvalues[coef])
        df.loc[f'{coef}&',model_name] = f'{round(model.params[coef], round_digit)}{stars}&'
        df.loc[f'{coef}_se&',model_name] = f'({round(model.bse[coef], round_digit)})&'

        # if explanatory variable is not in predifined result df, replace NaN in x column by &
        if f'{coef}&' not in df.index.to_list():
            new_variable_added = True
            df.loc[f'{coef}&','x'] = '&'
            df.loc[f'{coef}_se&','x'] = '&'


    if reg_model == 'OLS':
        df.loc['No. of Obs.&', model_name] = f'{int(model.nobs)}&'
        df.loc['Adj. R squared&', model_name] = f'{round(model.rsquared_adj, round_digit)}&'
        df.loc['F-statistics&', model_name] = f'{round(model.fvalue, round_digit)}&'
        df.loc['RMSE&', model_name] = f'{round(np.sqrt(model.ssr/model.nobs), round_digit)}&'
        # if new explanatory variable is added, move info rows to the end of df
        if new_variable_added:
            info_rows = ['&', 'No. of Obs.&', 'Adj. R squared&', 'F-statistics&', 'RMSE&']
            df_info = df.loc[info_rows, :]
            df = df.drop(info_rows)
            df = pd.concat([df, df_info])
        

    elif reg_model == 'logit':
        df.loc['No. of Obs.&', model_name] = f'{int(model.nobs)}&'
        df.loc['Pseudo-R-squared&', model_name] = f'{round(model.prsquared, round_digit)}&'
        df.loc['LR&', model_name] = f'{round(model.llr, round_digit)}&'
        df.loc['LR-pvalue&', model_name] = f'{round(model.llr_pvalue, round_digit)}&'

        if new_variable_added:
            info_rows = ['&', 'No. of Obs.&', 'Pseudo-R-squared&', 'LR&', 'LR-pvalue&']
            df_info = df.loc[info_rows, :]
            df = df.drop(info_rows)
            df = pd.concat([df, df_info])
    
    return df










def p_to_star(pvalue):
    p = None
    if pvalue <= 0.001:
        p = '***'
    elif pvalue >0.001 and pvalue <= 0.01:
        p = '**'
    elif pvalue > 0.01 and pvalue <= 0.05:
        p = '*'
    elif pvalue > 0.05 and pvalue <= 0.1:
        p = '.'
    else:
        p = ''
    return p





def add_time_dummies(df, every_n_year = 2):
    '''
    df is a df of time periods

    This function return a dataframe of time dummies.


    ever_n_year specify how you want to form time dummies.
    if ever_n_year=0, manual
    if ever_n_year=1, annual
    if ever_n_year=2, biennial (every two year)

    Start from ever_n_year = 1, check how the results are different from ever_n_year = 0. Check if results are robust.
    '''


    df['YYYYMM'] = df['YYYYMM'].astype('datetime64')
    df_dummy = pd.DataFrame()
    if every_n_year == 0:
        df_dummy['D'] = np.select([
            (df['YYYYMM'].dt.year < 1984),
            (df['YYYYMM'].dt.year < 1987),
            (df['YYYYMM'].dt.year < 1991),
            (df['YYYYMM'].dt.year < 1998),
            (df['YYYYMM'].dt.year < 2001),
            (df['YYYYMM'].dt.year < 2002),
            (df['YYYYMM'].dt.year < 2008),
            (df['YYYYMM'].dt.year < 2010),
            (df['YYYYMM'].dt.year < 2012),
            (df['YYYYMM'].dt.year < 2015),
            (df['YYYYMM'].dt.year < 2020),
            (df['YYYYMM'].dt.year < 2023),
            (df['YYYYMM'].dt.year < 2025)
            ],[0,1,2,3,4,5,6,7,8,9,10,11,12])
    else:

        y0 = df['YYYYMM'].dt.year[0]
        dummy = 0
        dummy_list = []
        for one_row in df['YYYYMM'].dt.year:
            if one_row - y0 == every_n_year:
                dummy += 1
                y0 = one_row

            dummy_list.append(dummy)

        df_dummy['D'] = dummy_list


    return df_dummy[['D']]

