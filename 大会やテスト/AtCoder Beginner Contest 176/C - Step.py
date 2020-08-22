input()
A=list(map(int,input().split()))
sum=0
#print(sum(A[i-1] - A[i] for i in range(1,len(A)) if A[i] < A[i-1]))
for i in range(1,len(A)):
     if A[i] < A[i-1]:
         sum+=A[i-1] - A[i]
         A[i]=A[i-1]
print(sum)
