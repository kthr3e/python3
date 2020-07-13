def m():
    N=int(input())
    cases=[list(map(int,input().split())) for i in range(N)]
    line=[0]*N
    count=0
    cases.sort()
    others=[]

    for case in cases:
      if case[1]>=case[2]:
        for i in range(1,case[0]+1):
          if line[case[0]-i]==0:
            line[case[0]-i]=1
            count+=case[1]
            break
      else:
        a=[cases.index(case),case[0],case[2] - case[1]]
        others.append(a)
    print("count:",count)
    others.sort(reverse=True,key=lambda x:x[2])
    print("case[0]<case[1]差が大きい奴：",others)

    for other in others:
      for i in range(len(line)):
        if line[i]==0 and i>other[0]:
          line[i]=1
          count+=cases[other[0]][2]
          del others[others.index(other)]
          break

    print("count:",count)
    print("差が大きいものがなくなったやつで入りきらなかったやつ：",others)
   # for other in others:


T=int(input())
for i in range(T):
    m()


#解説を見て作成してみる
#ラクダたちの集合 Sを用意する。 Sははじめ空集合。
#j=1,2,3,....,Nの順に着目する
#Ki=jなる全てのラクダを Sに追加する。
#その後、 |S|>jである限り、ラクダを取り除く
#このとき、 Li-Riが小さいラクダから順に取り除く
#上記の貪欲法は優先度付きキューを用いて O(NlogN)で実行可能で十分高速です。
#できなかった、、これは動画見てやる
def max():
    S=[]
    N=int(input())
    cases=[list(map(int,input().split())) for i in range(N)]
    Li=[]
    Ri=[]
    for case in cases:
        if case[1]>=case[2]:
            Li.append(case)
        else:
            Ri.append(case)
    L=[]
    a=0
    for j in range(1,N+1):
      if j==N:
        for l in Li:
          L.append(l)
      else:
        for l in Li:
          if l[0]<=j:
            L.append(l)
            a+=1
            #print("a:",a)
            #print("j:",j)
            #print("del前のL:",L)
            if len(L)>j:
              while len(L)>j:
                min=L[0][1]-L[0][2]
                k=0
                for i in range(len(L)):
                  if L[i][1]-L[i][2]<min:
                    k=i
                    min=L[i][1]-L[i][2]
                L.remove(L[k])
                a-=1
                #print("a:",a)
                #print("del後のL:",L)
              #print("Li:",len(Li))
      if a!=0:
        for i in range(1,a+1):
          Li.remove(L[-i])
        a=0
        #print("remove後のLi;",Li)
    #print("finish L:",L)

    R=[]
    for j in range(1,N+1):
      if j==N:
        for r in Ri:
          R.append(r)
      else:
        for r in Ri:
          if r[0]<=j:
            R.append(r)
            a+=1
            #print("j:",j)
           # print("del前のR:",R)
            if len(R)>j:
              while len(R)>j:
                min=R[0][2]-R[0][1]
                k=0
                for i in range(len(R)):
                  if R[i][2]-R[i][1]<min:
                    k=i
                    min=R[i][2]-R[i][1]
                R.remove(R[k])
                a-=1
              #print("del後のR:",R)
              #print("Ri:",len(Ri))
          if a==1:
            for i in range(1,a+1):
              Ri.remove(R[-i])
            a=0
            #print("remove後のRi;",Ri)
    #print("finish R:",R)

    sum=0
    S=L+R
    #print("L:",L,"R:",R)
    for j in range(len(S)):
        if S[j][0]>=j+1:
            sum+=S[j][1]

        else:
            sum+=S[j][2]

    print(sum)

T=int(input())
for i in range(T):
    max()

#以下から動画で学んだプログラム
#1 5 10 ->1 0 5 みたいに最低値からどれくらい加算できるかを考える。
#x 0 y とx y 0でグループを分け、それぞれ独立で考える。というのも左に来たらいいやつ、右に来たらいい奴とで固めて考えてくっつけるのが最適に近いかららしい。
#左側さえ溶ければあとは左右反転させたものをやればよい。
#最後から見て割り当てる人をきめる。別にすべての枠を埋める必要はない。
#前から見ると、すべての項を対象としてしまい、すべての項の最大をとって入れてしまうため、最大より劣るやつで、その項までに入らなければいけないものが入らなくなってしまう。
#貪欲法というらしい。
#なんかC言語でやっていたので断念検索してみたらパイソンの人がいた。
    import heapq as hq

    T = int(input())
    for _ in range(T):
        N = int(input())
        camels = [list(map(int, input().split())) for _ in range(N)]
        base = 0
        camels_L = [[] for _ in range(N+1)]
        camels_R = [[] for _ in range(N+1)]
        # 左から詰めるラクダと右から詰めるラクダを仕分ける
        for camel in camels:
            if camel[1] >= camel[2]:
                camels_L[camel[0]].append(camel[1] - camel[2])
                base += camel[2] # LとRの低いほうを加算
            else:
                # Rラクダは右から何列目かを考えるのでN - camel[0]と反転する
                camels_R[N - camel[0]].append(camel[2] - camel[1])
                base += camel[1] # LとRの低いほうを加算

        diff = 0

        # Lラクダについて考える
        heap_camels = []
        hq.heapify(heap_camels)
        """
プライオリティキューは 「最小値(あるいは最大値)を取り出すこと」に特化した配列です。
使う場面は「配列の要素が増える」と「最小値を取り出す」を何度も繰り返す時です。
（配列の要素が増えないのであれば、最初にソートして前から取っていけばいい。
逆に言えば、「配列の要素が増える→ソートする→最小値を取り出す」を繰り返してしまう時は
積極的にプライオリティキューを用いれば良い）
"""
        for i in range(1, N+1):
            # 左からi番目までが限度のラクダをまとめて追加
            for camel in camels_L[i]:
                hq.heappush(heap_camels, camel)
            # 左からi番目までに入りきらない場合に低いものから除外
            while len(heap_camels) > i:
                hq.heappop(heap_camels)
        # heapqに残ったものがすべての条件を満たしうれしさが最大
        diff += sum(heap_camels)

        # Rラクダについても同様
        heap_camels = []
        hq.heapify(heap_camels)
        for i in range(1, N+1):
            for camel in camels_R[i]:
                hq.heappush(heap_camels, camel)
            while len(heap_camels) > i:
                hq.heappop(heap_camels)
        diff += sum(heap_camels)
        print(diff + base)
