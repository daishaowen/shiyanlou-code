#!/usr/bin/env python3
def gcd(a,b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def lcm(a,b):
    return (a*b) // gcd(a,b)

def three_gcd(a,b,c):
    return gcd(a, gcd(b,c))

def three_lcm(a,b,c):
    return lcm(a, lcm(b,c))

if __name__ == '__main__':
    a, b, c = 2, 7, 6
    print("gcd",three_gcd(a,b,c))
    print("lcm",three_lcm(a,b,c))
