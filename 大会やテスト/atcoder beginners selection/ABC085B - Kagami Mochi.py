N = int(input())
#d = map(int,open(0).read().split())
d = sorted([int(input()) for i in range(N)])
print(1 + sum(1 for i in range(N-1) if d[i] < d[i+1]))

"""

a,*b=open(0);print(len(set(b)))
setは重複しない要素のコレクションである。
"""
