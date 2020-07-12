a = [input() for i in range(2)]
def popcount(n):
    count=0
    while n!=0:
        if n%2==1:
            count+=1
        n=int(n/2)
    return count

def f(n):
    c=0
    while n!=0:
        n=int(n%popcount(n))
        c+=1
    print(c)

b=[]
for i in range(int(a[0])):
    k=0
    b=list(a[1])
    if b[i]=='0':
        b[i]='1'
    else :
        b[i]='0'
    for j in range(int(a[0])):
        k = k*2 + int(b[j])
    f(k)

"""
def popcount(x):
    return bin(x).count("1")
#binはxを二進数の文字列に変換する関数。今回は問題の趣旨から、1をカウントした。

N, X = open(0).read().split()
N = int(N)
XS = list(X)
X = int(X, 2)
#int関数はint("a",b)でaという文字列をb進数表記で読み取り10進数の整数に変換してくれる

p = popcount(X)
xi = X % (p + 1)
if p == 1:
    xd = 0
else:
    xd = X % (p - 1)
#xiとxdはxの一の個数±1の値で割った数を保持している。なぜ？
#二進数だからどこかの桁が一つ入れかわったら1の個数は一個ずつの増減しかないため。
#x increase, x decrease の意味の変数だなこれ
#割った値の保持についても理解したい。
#つぎに考えるのが、1の増減によってその数に2の何乗かが加減する。
#そのあまりを1が増えた場合はそのくらいの数のあまりをxiに足す。
#1が0になった場合は数が減少してるので、xdからその数のあまりを引く。
for i in range(N):
    #i桁目が1の時
    if XS[i] == "1":
        #1の数が一つのとき、分母が1のためあまりはゼロ、この語の処理関係なく飛ばす。
        if p == 1:
            print(0)
            continue
        #1の数が複数個あるとき
        else:
            k = pow(2, N - 1 - i, p - 1)
            #pow(a,b,c) aのb乗を計算する。さらにcを付け加えることで、cの剰余つまりcで割った余りがでてくる。
            #ここではもともとの数が1の時、つまり1->0その桁が変化したときなので、2のN-1-i乗文の値が減ったということ
            x = (xd - k) % (p - 1)
            #上のあまりを求めた後xdから引き、その値を1の個数で割った余りを出す
            #今回kを考慮しているがあまりでひいたときにマイナスになる可能性が出てくるため、ここでもう一回余りを求めなおす。
    else:
        k = pow(2, N - 1 - i, p + 1)
        x = (xi + k) % (p + 1)
    ans = 1
    #後の動作は説明通り。
    while x != 0:
        x %= popcount(x)
        ans += 1
    print(ans)
"""

def popcount(n):
    return bin(n).count('1')

N=int(input())
X=input()
xl=list(X)
X=int(X,2)
a=popcount(X)
#1が減った時
if a==1:
    xd=0
else:
    xd=X%(a-1)
#1が増えたとき
xi=X%(a+1)

for i in range(N):
    if xl[i]=='1':
        if a==1:
            print(0)
            continue
        else:
            k=pow(2,N-1-i,a-1)
            x=(xd-k)%(a-1)
    else:
        k=pow(2,N-1-i,a+1)
        x=(xi+k)%(a+1)
    count=1
    while x!=0:
        x%=popcount(x)
        count+=1
    print(count)
