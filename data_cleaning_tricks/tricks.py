import pandas as pd
import numpy as np
'''
1. Suppose we have 4 by 4 var-cov matrix below
[
    [1,  0.2, 0.4, 0.5],
    [0.2, 1,  0.3, 0.6],
    [0.4,0.3,  1,  0.7],
    [0.5,0.6, 0.7,  1]
]

Use the following mechanism to go through the upper triangle of the matrix
'''

var_cov = [
        [1,0.2,0.4,0.5],
        [0.2, 1,0.3,0.6],
        [0.4,0.3,1,0.7],
        [0.5,0.6,0.7,1]
        ]

var_cov = pd.DataFrame(var_cov, columns = ['x1','x2','x3','x4'])
matrix = var_cov.iloc[:,:].values
index_list = []
for col in range(len(var_cov.columns)):
    for row in range(col):
        index_list.append((row,col))

#[(0, 1), (0, 2), (1, 2), (0, 3), (1, 3), (2, 3)]
print(index_list)

