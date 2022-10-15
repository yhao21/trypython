import time
import matplotlib.pyplot as plt

"""
1. convert Uppercase str to lower case using lower()

    a = 'HELLO'
    print(a.lower())
    

    result: hello



2. convert to Uppercase
    upper()
    
    a = 'hello'
    print(a.upper())

    result: HELLO


3. Uppercase (first letter only)
    capitalize()

    a = 'hello'
    print(a.capitalize())

    result: Hello


4. Extend a list:
    a = [1,2,3]
    b = [4,5,6]
    a.extend(b)
    print(a)
    result: [1, 2, 3, 4, 5, 6]



5. remove all same characters in a string
    If you want to remove all 0s in a1, use .lstrip()
    a1 = '00000000000000000000000084dabb2632bed5637a62524be43f7067237dc920'
    a1 = a1.lstrip('0')

    result: 84dabb2632bed5637a62524be43f7067237dc920

6. check if the elements in a list in contained in another list
    We can use: all(), any()

    Check if all elements in a are in b. If yes, print a

    a = [1,2,3,4]
    b = [1,2,3,4]
    
    
    if all(item in b for item in a):
        print(a)


    You can check if any elements in a are in b by replacing all() by any()
    
"""


a = 'HELLO'
print(a.capitalize())





