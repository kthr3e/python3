a = [input() for i in range(2)]
def popcount(n):
    count=0
    while n!=0:
        if n%2==1:
            count+=1
        n=int(n/2)
    return count

def f(n):
    c=0
    while n!=0:
        n=int(n%popcount(n))
        c+=1
    print(c)

b=[]
for i in range(int(a[0])):
    k=0
    b=list(a[1])
    if b[i]=='0':
        b[i]='1'
    else :
        b[i]='0'
    for j in range(int(a[0])):
        k = k*2 + int(b[j])
    f(k)
