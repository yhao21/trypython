import numpy as np
import time


n = 1000000
"""
如何测算numpy和python自带list元算时间呢？
"""
#生成一个1000000个数字的列表
'''
n = 1000000
l = [i for i in range(n)]
print(l)'''

#若想对列表每个数字乘以2，则需要用到循环
'''
st = time.time()
A = []
for j in l:
    A.append(j*2)
et = time.time()
print(A)
print('total time  ',et - st)

"""total time   0.10371851921081543"""
'''

#若使用列表生成式，时间会变快么？快了将近一倍
'''
st = time.time()
A = [i*2 for i in range(n)]
et = time.time()
print(A)
print('total time  ',et - st)

"""total time   0.0608365535736084"""
'''


#numpy简直神速啊！！
'''
st = time.time()
a = np.arange(0,n)*2
et = time.time()
print(a)
print('total time  ',et - st)
"""total time   0.0019910335540771484"""
'''