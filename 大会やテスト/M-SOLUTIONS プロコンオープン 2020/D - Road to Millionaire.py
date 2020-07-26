input()
A=list(map(int,input().split()))
M=[0,1000]
for i in range(0,len(A)-1):
    if A[i]>A[i+1]:
        M[1]+=A[i]*M[0]
        M[0]=0
    elif A[i]<A[i+1]:
        M[0]+=int(M[1]/A[i])
        M[1]=M[1]%A[i]
M[1]+=A[i+1]*M[0]
M[0]=0
print(M[1])


n=int(input())
A=list(map(int,input().split()))
s=1000
for i in range(n-1):
  if A[i+1]>A[i]:
    s=s//A[i]*A[i+1]+s%A[i]
print(s)
#    s=s//A[i]*A[i+1]+s%A[i] で売買を一気に行っている。売買したお金＋おつり
