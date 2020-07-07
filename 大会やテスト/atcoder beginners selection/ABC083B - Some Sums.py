#N,A,B = map(int,open(0)) hydrogenが対応していない？
N,A,B = map(int,input().split())
#print(sum())の形の書き方がわからなかった
sum = 0
for i in range(1,N+1):
    s = 0
    a = str(i)
    l = len(a)
    for j in range(1,l+1):
        s += int(a[-j])
#    print(s)
    if A <= s <= B:
        sum += i
print(sum)

#回答例
N,A,B=map(int,input().split())
print(sum(i for i in range(N+1) if A<=sum(map(int,str(i)))<=B))
#if A<=sum(map(int,str(i)))<=B) 桁数ごとに、int型に変換して合計したのが条件に収まっているかどうかをみる
