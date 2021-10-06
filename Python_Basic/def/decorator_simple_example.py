




'''
Here, we define a function "hello" to print "hello world".

Here we call this function through "hello()"
'''


#def hello():
#    print('hello world')
#
#
#hello()


'''
Now, we want to achieve the following,
1. print "hello world" and "synferlo"
2. do not change function "hello"
3. do not change the way to execute function "hello". Still use "hello()" to
   run this function


Then we can do this
'''

#def outer(func):
#    def inner():
#        func()
#        print('synferlo')
#        
#        return func
#    return inner
#
#
#def hello():
#    print('hello world')
#
#hello = outer(hello)
#
#hello()

'''
Here the process:
    1. define a new variale with the same name as function "hello"
    2. assign the return value of function "outer" to variable "hello".
        2.1 return value of outer is function "inner"
    3. Remember, now, variable "hello" is a function. More precisely, it
       is function "inner".
    4. execute variable "hello" by calling "hello()", it actually call
       the function "inner"
       i.e., hello() is same as inner()
    5. inner function execute func(), which print 'hello world'
    6. inner function then print 'synferlo'

    Done.


Hence, we actually assignt(or save) the function to the variable "hello",
which has the same name as function "hello".
If you change the variable "hello" to any other name, i.e., phi, then call
phi(), it will do the same thing.

We name this variable as "hello" because we DO NOT want to change the way
to call function "hello". We don't want to call "phi". It doesn't satisfy
condition 3.

    def outer(func):
        def inner():
            func()
            print('synferlo')
            
            return func
        return inner
    
    
    def hello():
        print('hello world')
    
    phi = outer(hello)
    
    phi()



To simplify the code, we add "@outer" above function "hello". Hence, 
we do not need to write "hello = outer(hello)" every time.
'''


#def outer(func):
#    def inner():
#        func()
#        print('synferlo')
#        
#        return func
#    return inner
#
#
#@outer
#def hello():
#    print('hello world')
#
## with @outer above, we do not need to write line below.
###hello = outer(hello)
#
#hello()


'''
With 'return func', you can assign this function "inner" to some other 
variable, i.e., a = hello
Then execute function "inner" with "a()"
'''

#def outer(func):
#    def inner():
#        func()
#        print('synferlo')
#
#        return func
#        
#    return inner
#
#
#@outer
#def hello():
#    print('hello world')
#
#a = hello
#a()



'''
Enhance:
    if you don't need to return function "hello" when you call function
    "inner" through "hello()", you don't need to add "return func".
'''

def outer(func):
    def inner():
        func()
        print('synferlo')
        
    return inner


@outer
def hello():
    print('hello world')

hello()









