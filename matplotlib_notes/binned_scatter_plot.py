import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''###------Binned Scatter Plot------###'''

'''
A binned scatter plot is a type of data visualization that displays the relationship between two variables by grouping data points into "bins" along one axis (usually the x-axis), and then plotting a single point for each bin representing an aggregated statistic (like the average) of the data within that bin, providing a cleaner view of trends, especially when dealing with large datasets where a standard scatter plot might appear cluttered. 


Given the following df
d_CAR   d_PX1
 1       3
 0       5
 1       -1
 1       2
 0       -5

Dependent variable d_CAR is a dummy variable, independent variable d_PX1 is a continuous variable.
'''

model = smf.logit(formula = 'd_CAR~d_PX1', data = df).fit()
# Get residuals
resid = model.resid_pearson
df['resid'] = resid


# Number of bins (number of dots in the scatter plot)
n = 50
# Create intervals of bins based on the value of independent variable d_PX1.
px1_bin = np.linspace(df['d_PX1'].min(), df['d_PX1'].max(), n+1)
# Return the indices of the bins to which each value in input array belongs.
x_index = np.digitize(df['d_PX1'].values, px1_bin)
# Values in column x_index refers to the ith bin that d_PX1 belongs to.
df['x_index'] = x_index

result = pd.DataFrame()
# Compute d_PX1 mean for each group
result['d_PX1'] = df.groupby('x_index')[['d_PX1']].mean()
# Compute residual mean for each group
result['resid'] = df.groupby('x_index')[['resid']].mean()

plt.scatter(result['d_PX1'], result['resid'])
plt.savefig('./figures/hi.png')
plt.close()


'''
dataframe: df
       d_CAR  d_PX1     resid  x_index
0          1     -2  2.206012       25
1          1     -4  2.176455       25
3          1      1  2.251103       26
4          0     10 -0.418063       28
5          1     -5  2.161825       24

dataframe: result
            resid       d_PX1
x_index
1        1.146804  -99.000000
3        1.218546  -90.000000
7       -0.741687  -75.000000
8       -0.717092  -70.000000

'''



