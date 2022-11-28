'''
Set() is much more faster.


Suppose you have two lists, a and b. If you would like to combine them into one list, c, without using Set()
'''


a = ['a','b','c']
b = ['b','d','e']
c = a + [i for i in b if i not in a]
print(c)


'''
But this is slow, specially when a and b are contains many elements.
Use Set() is much more faster!!!
'''
a, b = set(a), set(b)
c = list(a | b)
print(c)


'''
operator:
    | --> union, e.g., a | b == a or b 并集
    & --> intersection, e.g., a & b == a and b 交集
    - --> difference, e.g., a - b == remove elemnts that exists in b from a
            a - b would be {'c', 'a'}
'''



'''
Remove duplicates from a list:

'''
l = [1, 2, 4, 2, 1, 4, 5]
l = [*set(l)]
print(l)
