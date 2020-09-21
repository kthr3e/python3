num = int(input())
pwr=2
root=2
count = 0
while root ** 2 <= num:

    if pwr >= 6:
        pwr = 1
        root +=1

    if root ** pwr == num:
        print('root:',root,'pwr:',pwr)
        count+=1

    pwr += 1
if count == 0:
    print('Not pair root and pwr')
