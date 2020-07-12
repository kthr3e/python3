import math
N = int(input())
#for i in range(1,N+1):
    #print(sum(1 for x in range(1,int(math.sqrt(i))) for y in range(1,int(math.sqrt(i))) for z in range(1,int(math.sqrt(i))) if x*(x+y+z)+y*(y+z)+z*z==i))
for i in range(1,N+1):
    count=0
    for x in range(1,int(math.sqrt(i))):
        for y in range(1,int(math.sqrt(i))):
            for z in range(1,int(math.sqrt(i))):
                if x*(x+y+z)+y*(y+z)+z*z>i:
                    break

                if x*(x+y+z)+y*(y+z)+z*z==i:
                    count+=1
    print(count)
    #4銃ループだとどうしても時間がかかりすぎてしまうようだ。

a=[0]*5**7
#**は何乗するか
r=range(1,99)
print(r)
for x in r:
 for y in r:
  for z in r:
      a[x*(x+y+z)+y*(y+z)+z*z-1]+=1
  #制約として1<=n<=10**4であるため0というのはおこりえない、かつ、リストは0から始まるためその結果をいれるためにー1している。
print(*a[:int(input())])
#リストの前に*をつけることで[]をなくして表示している。このことをアンパックというらしい。

a=[0]*int(input())
r=range(1,99)
for x in r:
    for y in r:
        for z in r:
            n=x*(x+y+z)+y*(y+z)+z*z-1
            if n<len(a):
                a[n]+=1
print(*a)
