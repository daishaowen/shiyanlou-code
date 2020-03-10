#!/usr/bin/env python3
def newton(f,f1,start):
    x_n = start
    while True:
        x_n1 = x_n-f(x_n)/f1(x_n)
        if abs(x_n1-x_n) < 10**-5:
            return x_n1
        x_n = x_n1

def function(x):
    return (x**3)-2*x-5

def function1(x):
    return 3*(x**2)-2

if __name__ == '__main__':
    print(newton(function,function1,3))
