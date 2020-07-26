N,K=map(int,input().split())
A=list(map(int,input().split()))

for i in range(K,N):
    if A[i]>A[i-K]:
        print("Yes")
    else:
        print("No")

n,k=map(int,input().split())
A=list(map(int,input().split()))
for i in range(n-k):
    print("NYoe s"[A[i]<A[k+i]::2])
#ほぼ全門と同じ。
