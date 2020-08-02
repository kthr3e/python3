N,D=map(int,input().split())
A=[list(map(int,input().split())) for i in range(N)]
print(sum(A[i][0]**2+A[i][1]**2<=D**2 for i in range(N)))
