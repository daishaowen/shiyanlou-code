#!/usr/bin/env python3
def fibo3(num):
    mylist = []
    a = 1
    b = 1
    for i in range(num):
        mylist.append(a)
        a,b = b,a+b
    return mylist

print(fibo3(6))
    
