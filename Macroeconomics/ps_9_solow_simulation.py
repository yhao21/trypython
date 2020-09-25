import time
"""

parameters
    a: Cobb parameter
    A: FTP,     A_t+1 = (1 + g) * A_t
    L: Labor    L_t+1 = (1 + n) * L_t
    d: depreciation rate
    I: Investment I = s * Y_t
    K: Capital  K_t+1 = K_t + I_t - d * K_t
    Y: output   Y_t = (K_t ** a) * (A_t * L_t) ** (1-a) 
    n: growth rate of population
    g: growth rate of A
    
As both A and L are growth, so we should use capital per effective labor to plot solow
k = K/(AL)
y = Y/(AL)

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


year = 100
s = 0.25
d =0.05
n = 0.02
g = 0.01
A = 1
L = 5
K = 10
a = 1/3
Y_0 = (K**a)*((A * L)**(1-a))
I_0 = Y_0 * s

K_result = []
Y_result = []
I_result = []
L_result = []
A_result = []
t_result = []
for t in range(0,year):
    A_1 = ((1+g)**t)*A
    L_1 = ((1+n)**t)*L
    if t == 0:
        K = 10
        Y = (K**a)*((A * L)**(1-a))
        I = Y * s
        K_result.append(K)
        Y_result.append(Y)
        I_result.append(I)

    if t > 0:
        I = Y_result[t-1] * s
        K = (1-d) * K_result[t-1] + I
        Y = (K**a)*((A_1 * L_1)**(1-a))
        K_result.append(K)
        Y_result.append(Y)
        I_result.append(I)

    A_result.append(A_1)
    L_result.append(L_1)
    t_result.append(t)
Y_capita = np.array(Y_result) / np.array(L_result)
K_capita = np.array(K_result) / np.array(L_result)
K_eff_worker = np.array(K_result)/(np.array(A_result) * np.array(L_result))

# print(Y_result)
# print(K_result)
# print(Y_capita)

df = pd.DataFrame()
for i in range(year):
    df = df.append({
        'A':A_result[i],
        'L':L_result[i],
        'K':K_result[i],
        'Y':Y_result[i],
        'I':I_result[i],
        'Y/L':Y_capita[i],
        'K/L':K_capita[i],
        'K_eff = K/AL':K_eff_worker[i]
    },ignore_index = True)
order = ['A','L','K','Y','I','Y/L','K/L','K_eff = K/AL']
df = df[order]

print(df)

K_t_1 = K_eff_worker[1:year]
K_t_0 = K_eff_worker[:year-1]
# print(K_t_1)
# print(K_t_0)
plt.plot(t_result,K_eff_worker)
# plt.plot(K_eff_worker,K_eff_worker)
# plt.plot(K_t_0,K_t_1)
# plt.plot(K_t_0,K_t_0)

plt.xlabel('time')
plt.ylabel('K per effective worker')

plt.show()