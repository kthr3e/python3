import math
N = int(input())
for i in range(1,N+1):
    print(sum(1 for x in range(1,int(math.sqrt(i))) for y in range(1,int(math.sqrt(i))) for z in range(1,int(math.sqrt(i))) if x*x+y*y+z*z+x*y+y*z+z*x==i))
