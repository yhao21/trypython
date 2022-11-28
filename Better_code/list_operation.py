



'''
###------remove a list of items from another list------###

Given list a and b containing many elements, you would like to remove elements in b from a through set operation, instead of list operation.

    Given:
        a = [i for i in range(30000, 30000+200000)]
        b = [i for i in range(30000, 30000+100000)]
    
        list operation:
        a = [i for i in a if i not in b] # this is super slow.
    
        set operation:
        a, b = set(a), set(b)
        a = list(a - b)         # This is super fast.
    
'''
