#!/usr/bin/env python3
i=1
print("-" * 50)
while i<10:
    j=1
    while j<=i:
        term=i*j
        print("{}*{}={}".format(i,j,term),end=' ')
        j+=1
    i+=1
    print()
print("-" * 50)
