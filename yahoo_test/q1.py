"""
# sysのほうが標準入力受け取りの動作速度が速い
T = list(map(int,input().split()))
#print(T)
max = abs(T[0]-T[len(T)-1])
#print("max:",max)
for i in range(0,len(T)-1):
    if max < abs(T[i] - T[i+1]):
        max = abs(T[i] - T[i+1])

print(max)
"""
import sys
for line in sys.stdin:
    T = [int(s) for s in line.split()]
#print(T)

max = abs(T[0]-T[len(T)-1])
for i in range(0,len(T)-1):
    if max < abs(T[i] - T[i+1]):
        max = abs(T[i] - T[i+1])

print(max)
