import time
import numpy as np
from matplotlib import pyplot as plt
import random
import pandas as pd



"""
=========================
Operations
=========================

    % --> the remainder
    the remainder of 8/4 is 0
    the remainder of 8/3 is 2, 8-(3*2) = 2
    



    //Quotient --> 整除， 只显示整数部分（四舍五入）



=========================
Functions
=========================

1. assign default value to an argument

    def cheerup(name = "Tigers"):
        print('hello' + name)
    
    cheerup()



=========================
Lists
=========================

1. add variables in to the list

    a = 8
    b = 4.3
    a_add = a + b
    a_sub = a - b
    a_mul = a * b
    a_div = a / b
    
    a_list = [a_add, a_sub, a_mul, a_div]
    print(a_list)



2. Slicing --> access multi values
    print(a_list[1:3])



3. "remove" in list
    remove first occurence of value
    a_list.remove(value, /)



    a = 8
    b = 4.3
    a_add = a + b
    a_sub = a - b
    a_mul = a * b
    a_div = a / b
    a_quo = a // b
    
    a_list = [a_add, a_sub, a_mul, a_div]
    
    a_list.append(a_quo)
    print(a_list)
    
    
    a_list.remove(a_quo)
    print(a_list)



4. operation for each elements in the list
    i.e., multiply all elements by 2


    a_list = [i*2 for i in a_list]
    print(a_list)

"""


def mulby3(num):
    result = num * 3

    return result


a = 8
b = 4.3
a_add = a + b
a_sub = a - b
a_mul = a * b
a_div = a / b
a_quo = a // b
a_rem = a % b
a_pow = a ** b

a_list = [a_add, a_sub, a_mul, a_div]

a_list.append(a_quo)
a_list.append(a_rem)
a_list.append(a_pow)
#print(a_list)
#print(a_list[1:4])




mulby2_list = [i*2 for i in a_list]


mulby3_list = [mulby3(i) for i in a_list]
#print(mulby3_list)

test_list = [1,2,3,4]
test_list = [i*4 for i in test_list]
#print(test_list)





word_list = ['cat', 'dog', 'rabbit', 'otter', 'tiger', 'seal']


#for word in word_list:
    #print(word)
    #print(word.upper())
    #print(word.capitalize())



#def compare(num):
#    if num == 4:
#        print(str(num) + ' is equal to 4')
#    
#    elif num > 4:
#        print(str(num) + ' is greater than 4')
#    
#    else:
#        print(str(num) + ' is less than 4')
#
#
#n_list = [i for i in range (1,10)]
#print(n_list)
#
#
#for item in n_list:
#    compare(item)



"""
Fibonacci sequence:
    0,1,1,2,3,5,8,....
"""


#def fibo1(upper_bound):
#    
#    res = []
#
#    for i in range (upper_bound):
#        if i <= 1:
#            res.append(i)
#        elif i > 1:
#            last_one = res[-1]
#            last_two = res[-2]
#            new = last_one + last_two
#            res.append(new)
#
#    print(res)
#
#st = time.time()
#fibo1(10)
#print(time.time() - st)
#
#
#
#def fibo2(upper_bound):
#
#    res = []
#    n1 = 0
#    n2 = 0
#
#    for i in range(1,upper_bound):
#        if i == 1:
#            n1 = 0
#            n2 = 1
#            res.append(n1)
#            res.append(n2)
#
#        elif i > 1:
#            temp_record = n1
#            n1 = n2
#            n2 = temp_record + n1
#            res.append(n2)
#
#    print(res)
#
#
#st = time.time()
#fibo2(10)
#print(time.time() - st)
#
#
#def fibo3(upper_bound):
#    n1 = 0
#    n2 = 1
#    res = [0,1]
#    count = 0
#    while count < upper_bound - 2:
#        old_n = n1
#        n1 = n2
#        n2 = old_n + n1
#        res.append(n2)
#        count += 1
#
#    print(res)
#
#
#st = time.time()
#fibo3(10)
#print(time.time() - st)
#



a = [
    [1,2,3,4],
    [2,3,4],
    [5,6,7],
    [3,3,4]
]

#print(a)


b = [
    [1,2,3,4],
    [5,6,7,8],
    [9, 10, 11, 12]
]

#print(len(b))

def matrixmul(A,B):
    rows = len(A)
    cols = len(B[0])
    out = [[0 for col in range(cols)] for row in range(rows)]

    for i in range(rows):
        for j in range(cols):
            for k in range(len(B)):
                #out[i][j] = out[i][j] + A[i][k] * B[k][j]
                out[i][j] += A[i][k] * B[k][j]

    
    return out


x = matrixmul(a,b)
#print(x)



def random_matrix(m,n):
     out = [[random.random() for col in range(n)] for row in range(m)]

     return out


rand_a = random_matrix(400,300)
rand_b = random_matrix(300,400)


#st = time.time()
#y = matrixmul(rand_a,rand_b)
#print(y)
#
#print(time.time() - st)
#
#


#a_list = [2,3,4,5]
#b_list = [6,7,8,9]


#a_np = np.array(a_list)
#b_np = np.array(b_list)
#c_np = a_np + b_np
#d_np = a_np * 3.14
#e_np = b_np *2
#f_np = a_np * b_np



#a = np.array(random_matrix(400,300))
#b = np.array(random_matrix(400,300))
#st = time.time()
#c = a*b
#print(time.time() - st)

x_np = np.arange(100)
y_np = x_np**2
z_np = x_np**0.5
#print(y_np)
#print('\n\n')
#print(z_np)

#n_parr = np.arange(10)
#n_parr = n_parr.reshape(2,5)
#print(n_parr)
## transpose matrix
#n_parr = n_parr.T
#print(n_parr)
#
#
#
#a_zeros = np.zeros((3,3))
#print(a_zeros)
#
#
#a_identity = np.eye(5,5)
#print(a_identity)
#
### look for what functions does np have, type name in ""
##print(np.lookfor("array"))
#
## matrix multiplication in numpy
#x2 = np.matmul(rand_a, rand_b)
#print(x2)
#
#
## create matrix by random function
#m1 = np.random.randint(0,10,(3,3))
#print(m1)

#rand_npa = np.random.randint(0,10,(400,300))
#rand_npb = np.random.randint(0,10,(300,400))
#st = time.time()
#x21 = np.matmul(rand_npa,rand_npb)
#print(time.time() - st)
#



#t_mat = np.arange(20).reshape(4,5)
#
##rand_npc = np.random.randint(0,5,120000).reshape(400,300)
#
#print(t_mat)
#print(t_mat[1])
#particular value
#v = t_mat[1,3]
#print(v)
## particular col
#co = t_mat[:,3]
#print(co)
##particular block
#blo = t_mat[:3, :2]
#print(blo)

#=========================
# boolean
#=========================

# find even number
#print((t_mat % 2) == 0)
"""
[[ True False  True False  True]
 [False  True False  True False]
 [ True False  True False  True]
 [False  True False  True False]]
"""


#print((t_mat**2) <= 25)
"""
[[ True  True  True  True  True]
 [ True False False False False]
 [False False False False False]
 [False False False False False]]
"""


#y_np = x_np ** 0.3
#plt.plot(x_np,y_np, 'r--')
#plt.plot(x_np,z_np, 'g')
#plt.savefig('test.png')



#plt.bar([1,2,3,4], [1,3,6,2])
#plt.savefig('bar.png')


"""
=========================
Subplots
=========================
"""
#names = ['results1', 'results2', 'results3']
#values = [1,10,20]
## you can cange any size
#plt.figure(figsize = (9,3))
#plt.subplot(131)
#plt.bar(names, values)
#plt.subplot(132)
#plt.scatter(names,values)
#plt.subplot(133)
#plt.plot(names, values)
#plt.suptitle('different subplots')
#plt.savefig('subplot.png')



def height(v0):
    g = 9.81
    t = (2*v0)/g
    #create evenly space np array
    x_range = np.linspace(0,t,100)
    h = []
    for i in x_range:
        #PEMDAS
        h.append(v0*i - 0.5*g*(i**2))
    plt.plot(x_range,h)
    plt.savefig('height.png')

#height(100)


for v in range(100):
    height(v)








