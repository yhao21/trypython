

"""
=========================
if statement
=========================

=======
======= good code
=======

    x = 1 if condition else 0
    print(x)


=======
======= bad code
=======

    condition = True
    if condition:
        x = 1
    else:
        x = 0
    print('hello', x)



=========================
format large number
=========================

=======
======= good code
=======

    a = 10_000_000_000
    b = 100_000
    total = a + b

    print(f'{total:,}')


    return:10,000,100,000

    ### 
    '_' will not show up when you print the variable.
    use f'' to format your print function.
    ###


=======
======= bad code
=======

    a = 10000000000
    b = 100000
    total = a + b

    print(total)



=========================
context manager
=========================

=======
======= good code
=======

    with open('one_file.txt', 'r') as f:
        content = f.read()


=======
======= bad code
=======

    f = open('one_file.html')
    content = f.read()
    f.close()



=========================
pairing
=========================

=======
======= good code
=======

    
    names = ['synferlo', 'xie', 'wanzf']
    
    for index, name in enumerate(names):
        print(index, name)
    
    return:
        0 synferlo
        1 xie
        2 wanzf

    ###
    enumerate will print both index and content.
    add arguement 'start = n' to start your index from real number n, n = 1, 2, 3, ...
        names = ['synferlo', 'xie', 'wanzf']
        
        for index, name in enumerate(names, start = 3):
            print(index, name)

        return:
            3 synferlo
            4 xie
            5 wanzf
    ###


=======
======= good code
=======

    
    names = ['synferlo', 'xie', 'wanzf']
    ages = [15, 20, 50]
    
    for name, age in zip(names, ages):
        print(f'{name} is {age} years old.')


    return:
        synferlo is 15 years old.
        xie is 20 years old.
        wanzf is 50 years old.

    ###
    zip function wil pair each element in lists
    i.e.,

        a = zip(names, ages)
        for i in a:
            print(i)
        
        return:
            ('synferlo', 15)
            ('xie', 20)
            ('wanzf', 50)
    ###



=========================
Unpacking
=========================

=======
======= good code
=======


    a, b, *c, d = (1, 2, 3, 4, 5, 6, 7, 8)
    
    print(a)
    print(b)
    print(c)
    print(d)


    return:
        1
        2
        [3, 4, 5, 6, 7]
        8
    
    ###
    the sign * let c equals to everyting, other than a and b, up to the last value.
    ###




"""















