#!/usr/bin/env python3
def fibo1(num):
    if num == 1:
        return 1
    elif num == 2:
        return 1
    elif num > 2:
        return fibo1(num-1)+fibo1(num-2)
    else:
        print("False")

def main():
    mylist = []
    for i in range(1,9):
        mylist.append(fibo1(i))
    print(mylist)

if __name__ == '__main__':
    main()
         
