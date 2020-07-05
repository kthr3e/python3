#優秀な回答例1
n=int(input())
a=list(map(int,input().split()))
ans=0

while True:
  b=[i%2 for i in a]
  if b.count(1)==0:
    a=[i/2 for i in a]
    ans+=1
  else:
    break

print(ans)

#！？　異次元中田の回答霊
n=eval([*open(0)][1].replace(*' |'))
print(len(bin(n&-n))-3)
