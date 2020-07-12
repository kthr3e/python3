input()
a = list(map(int,input().split()))
b= a[0::2]
print(sum(1 for i in b if i%2==1))

"""
print(sum(int(i)%2 for i in[*open(0)][1].split()[::2]))
[*open(0)][1]がよくわからん
今思うと改行しているからかもしれない、最初の変数が無用だから[0]は読み込まずに次の行から参考にするため？？
input();print(sum(i%2 for i in map(int,input().split()[::2])))
これは上の短くした版
"""
