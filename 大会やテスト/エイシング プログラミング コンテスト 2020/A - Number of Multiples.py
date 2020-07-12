L,R,d = map(int,input().split())
print(sum(1 for i in range(L,R+1) if i%d == 0))

"""
l, r, d = map(int, input().split())
print(r//d - (l-1)//d)
今回の場合に限りdの倍数のため、いくつあるのかは最高数字がdの何倍かから、最小値の一つ下の数字がdの何倍であるかをひけばよい。
これだとO(1)で済むのでより高速。
"""
