#!/usr/bin/env python3
def intersection(f,start1,start2):
    x_n = start1
    x_n1 = start2
    while True:
        x_n2 = x_n1 - f(x_n1)/((f(x_n1)-f(x_n))/(x_n1-x_n))
        if abs(x_n2-x_n1) < 10**-5:
            return x_n2
        x_n = x_n1
        x_n1 = x_n2

def function(x):
    return (x**3)-2*x-5

if __name__ == '__main__':
    print(intersection(function,3,3.5))
