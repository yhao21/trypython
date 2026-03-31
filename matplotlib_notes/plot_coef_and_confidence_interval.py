import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



"""
Method 1: errorbar
    You will receive a chart like this:
                ___
                 |
                 *
                _|_
                
"""
df = pd.DataFrame()
np.random.seed(10)
n = 10
# Generate coef and 95% confidence interval
df['coef'] = np.random.normal(4,1, n) - np.random.normal(0, 0.5, n)
df['se'] = abs(np.random.normal(0.5, 0.5, n))   # SE must be positive.
df['ci_high'] = df['coef'] + 1.96 * df['se']
df['ci_low'] = df['coef'] - 1.96 * df['se']

print(df)
#       coef        se   ci_high    ci_low
#   5.115073  0.488864  6.073247  4.156900
#   4.113760  0.371686  4.842265  3.385255
#   2.937133  0.633035  4.177881  1.696384
#   3.477479  1.692484  6.794747  0.160211
#   4.507021  1.061846  6.588238  2.425803
#   3.057346  1.336311  5.676515  0.438176
#   4.833813  0.549575  5.910979  3.756646
#   4.040980  1.198998  6.391017  1.690944
#   3.262023  0.364376  3.976200  2.547846
#   4.365302  0.806602  5.946242  2.784362

plt.errorbar(
        df.index,    # X
        df['coef'],
        # distance from the estimated mean to the lower or higher bound, i.e., 1.96*se.
        df['coef'] - df['ci_low'],
        fmt = 'o',  # The marker for the mean, "o" for dot.
        markersize = 3,     # size of the marker (dot)
        color = 'black',    # color of marker.
        ecolor = 'black',   # color of the CI candle.
        elinewidth = 1,     # line width of the CI candle.
        capsize = 3,
        capthick = 1,
        label = '95% Conf. Interval'
        )
plt.savefig('./figures/errorbar_confidence_interval.png')
plt.close()





