K=int(input())
n=['7']*10**6
if K%2==0 or K%5==0:
    print(-1)

elif K%7==0:
    c=len(str(K/7))
    while int(''.join(n[0:c]))%K!=0:
        c+=1
    print(c)

else:
    c=K
    while int(''.join(n[0:c]))%K!=0:
        c+=1
    print(c)
