input()
a = list(map(int,input().split()))
b= a[0::2]
print(sum(1 for i in b if i%2==1))
