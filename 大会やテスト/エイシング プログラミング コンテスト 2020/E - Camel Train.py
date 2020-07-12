def m():
    N=int(input())
    cases=[list(map(int,input().split())) for i in range(N)]
    cases.sort()
    print(cases)
    p=[0]*N
    ans=0
    for i in range(N):
      for j in range(i):



T=int(input())
for i in range(T):
    m()
