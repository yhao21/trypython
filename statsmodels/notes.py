
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf





'''
###------Run regression like in R------###


model = smf.ols(formula = 'PX1_Not_weighted ~ tau + C(YYYYMM)', data = df).fit()

    use C() to mark catecorical data, such as EDU, SEX, ...


###------Clustered standard error------###
Consider a df have
    yyyymm  income  age  edu  expr

If you would like to cluster SE at yyyymm and age,
    
    df['yyyymm_id'] = df['yyyymm'].astype('category').cat.codes
    df['age_id'] = df['age'].astype('category').cat.codes
    model = smf.ols(formula = 'income~age+C(edu)+expr)')..fit(cov_type = 'cluster', cov_kwds={'groups': df[['yyyymm_id', 'age_id']]})




NOTICE: You can clustered at a level that is even not in your regression equation!
For example, I can only regress income on edu, then cluster at yyyymm and age,

    model = smf.ols(formula = 'income ~ C(edu))')..fit(cov_type = 'cluster', cov_kwds={'groups': df[['yyyymm_id', 'age_id']]})




'''

