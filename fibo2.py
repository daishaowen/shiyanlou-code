#!/usr/bin/env python3
def fibo2(num):
    if num == 1:
        return [1]
    elif num == 2:
        return [1,1]
    l = [1,1]
    for i in range(2,num):
        l.append(l[-1]+l[-2])
    return l
    

print(fibo2(5))
