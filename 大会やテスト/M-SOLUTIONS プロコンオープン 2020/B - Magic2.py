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
