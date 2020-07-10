N,Y = map(int,input().split())
#print(10000*x+5000*y+1000*z == Y for x in range(N+1) for y in range(N+1-x) for z in range(N+1-x-y))
for x in range(N+1):
    for y in range(N+1-x):
        z = N-x-y
        if 10000*x+5000*y+1000*z == Y and 0<=z<=2000:
            print(x,y,z)
            exit()
print(-1,-1,-1)

"""
n,y = map(int,input().split())
for i in range(n+1):
  for j in range(n-i+1):
    if 10*i + 5*j + (n-i-j) == y//1000:
      print(i,j,n-i-j)
      exit()
print(-1,-1,-1)
あんま変わらん
"""
