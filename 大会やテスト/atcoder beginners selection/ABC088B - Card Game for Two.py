N = int(input())
a = list(map(int,input().split()))
#print(a)
#print(sum(max(a) a.remove(max(a)) for i in range(N)))
sum = 0
for i in range(N):
    if i % 2 == 0:
        sum += max(a)
    else:
        sum -= max(a)
    a.remove(max(a))

print(sum)

"""
コード量が短い人の回答例
input()
この定数はいらないからただ入力しているだけで保持していない。
a = sorted(map(int, input().split()))[::-1]
map関数で標準入力をint型にし、sortedで新たにソートされたリストを作成。-1のステップ数でしている？？
最適な手順だからソートを逆順にして最大値順で並べたかったのだろうか？true,falseはつかえなかったのか？
print(sum(a[::2])-sum(a[1::2]))
[start:stop:step]で今回はステップ数を指定している。2個ごとにみている。
"""
