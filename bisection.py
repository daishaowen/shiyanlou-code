#!/usr/bin/env python3
import math
def bisection(f,a,b):
    flex = 10**-7
    if f(a) == 0:
        return a
    elif f(b) == 0:
        return b
    elif f(a)*f(b) > 0:
        print("there are not zero point")
        return
    else:
        c = (a+b)/2
        while abs(a-c) > flex:
            if f(c) == 0:
                return c
            elif f(a)*f(c)<0:
                b = c
            else:
                a = c
            c = (a+b)/2
        return c

def function(x):
    return (x**3)-2*x-5

if __name__ == '__main__':
    print(bisection(function,1,1000))

