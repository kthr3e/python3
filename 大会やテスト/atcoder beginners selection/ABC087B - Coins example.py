a,b,c,x=map(int,open(0))
print(sum(500*i+100*j+50*k==x for i in range(a+1)for j in range(b+1)for k in range(c+1)))

#map関数でint型にして、入力されたものは一文字なので[0]で返している。
#https://qiita.com/kyuna/items/8ee8916c2f4e36321a1c

A, B, C, X = [int(input()) for i in range(4)]
print(sum(500*a+100*b+50*c == X for a in range(A+1) for b in range(B+1) for c in range(C+1)))
#複数の変数に同時に代入して、sum関数によって出力をしている。
