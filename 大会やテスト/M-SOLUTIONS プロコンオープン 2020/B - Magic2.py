cards = list(map(int,input().split()))
K = int(input())
for i in range(K):
    if cards[1]<=cards[0]:
        cards[1]*=2
    elif cards[2]<=cards[1]:
        cards[2]*=2
    else:
        break

if cards[0]<cards[1]<cards[2]:
    print('Yes')
else:
    print('No')

a,b,c,k=map(int,open(0).read().split())
while a>=b:b*=2;k-=1
while b>=c:c*=2;k-=1
print('YNeos'[k<0::2])
#試行回数がK回までに収まるか否かで、真偽判別をして、出力のところを調整している。
