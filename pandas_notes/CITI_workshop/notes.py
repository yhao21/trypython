import time
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


def fibo1(upper_bound):
    
    res = []

    for i in range (upper_bound):
        if i <= 1:
            res.append(i)
        elif i > 1:
            last_one = res[-1]
            last_two = res[-2]
            new = last_one + last_two
            res.append(new)

#    print(res)

st = time.time()
fibo1(50000)
print(time.time() - st)



def fibo2(upper_bound):

    res = []
    n1 = 0
    n2 = 0

    for i in range(1,upper_bound):
        if i == 1:
            n1 = 0
            n2 = 1
            res.append(n1)
            res.append(n2)

        elif i > 1:
            temp_record = n1
            n1 = n2
            n2 = temp_record + n1
            res.append(n2)

#    print(res)


st = time.time()
fibo2(50000)
print(time.time() - st)


def fibo3(upper_bound):
    n1 = 0
    n2 = 1
    res = [0,1]
    count = 0
    while count < upper_bound - 2:
        old_n = n1
        n1 = n2
        n2 = old_n + n1
        res.append(n2)
        count += 1

#    print(res)


st = time.time()
fibo3(50000)
print(time.time() - st)




