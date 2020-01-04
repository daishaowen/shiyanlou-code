for i in range(1,101):
    if i%7==0:
        continue
    elif (i%10)%7==0 and i%10!=0:
        continue
    elif (i//10%10)%7==0 and (i//10%10)%10!=0:
        continue
    else:
        print(i)

