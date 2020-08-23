H,W,M=map(int,input().split())
#二次元リストではなく列行を一個のボムで消してくれるためそれぞれのリストを用意。
sumh = [0] * H
sumw = [0] * W
bomb=[]

for i in range(M):
    h,w=map(int,input().split())
    sumh[h-1]+=1
    sumw[w-1]+=1
    bomb.append((h,w))

#爆弾の個数の最大値とその最大値がいくつずつあるか(ch,cw)に保存。最大の列と最大の行のいずれかの組み合わせに置くことで爆破数を最大化できる。
maxh=max(sumh)
maxw=max(sumw)
ch=sumh.count(maxh)
cw=sumw.count(maxw)
#print(maxh,maxw,ch,cw)

#爆弾のある場所がH,Wの座標で両方共で最大個数の場所であった場合その数を加算
count=0
for h,w in bomb:
    if sumh[h-1]==maxh and sumw[w-1]==maxw:
        count+=1
#print(count)

#破壊できる数は、そのマスに爆破対象があるとき一つ減ってしまう。
if count==ch*cw:
    print(maxh+maxw-1)
else:
  print(maxh+maxw)
