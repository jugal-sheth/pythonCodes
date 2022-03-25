#!/usr/bin/env python
# coding: utf-8

# In[23]:


import math
def isPerfectSquare(num):
    s =int(math.sqrt(num))
    return s*s == num
 
def isFibonacciNumber(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

def fib(n):
    a = 0
    b = 1
    c = 1
    fib = [0,1]
    if n == 1:
        print(a)
    else:        
        while(c<=n):
            c = a + b
            a = b
            b = c            
            fib.append(c)
        return fib
    
def getanswer(new):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:        
        for i in range(2,new+1):
            c = a + b
            a = b
            b = c
        print(c)      

n = int(input("Enter the first number (fibo) : "))
i = int(input("Enter next num "))

if(isFibonacciNumber(n) == True):
    a = list(fib(n))
    index = a.index(n)
    new = index + i
    #print(a)
    #print(index)
    #print(new)
    getanswer(new)
else:
    print(n  ," is not a fibonacci number")


# In[ ]:




