#!/usr/bin/env python3
def function(num):
    mylist = [num]
    while True:    
        if num == 1:
            break
        elif num % 2 == 0:
            num = num // 2
            mylist.append(num)
        else:
            num = 3 * num +1
            mylist.append(num)
    return mylist,len(mylist)-1

def function(num):
    mylist = [num]
    while num != 1:
        if num % 2 == 1:
            num = 3*num+1
            mylist.append(num)
        else:
            num = num//2
            mylist.append(num)
    return mylist,len(mylist)-1


print(function(43))
print(function(43))
