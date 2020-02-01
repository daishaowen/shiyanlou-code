#!/usr/bin/env python3
import sys
def Hours(m):
    h = m // 60
    m = m % 60
    return h,m

def main():
    try:
        if (sys.argv[1].isdigit()) and (int(sys.argv[1]) >=0):
            hours,minutes=Hours(int(sys.argv[1]))
            print("{} H, {} M".format(hours,minutes))
        else:
            raise ValueError("a value error happend")
    except ValueError:
        print("Parameter Error")

if __name__ == '__main__':
    main()
