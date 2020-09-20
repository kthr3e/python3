#三つの変数の中で奇数で最も大きいものを表示する
x,y,z=map(int,input().split())
nums=x,y,z
mins=[]
for num in nums:
    if num%2==1:
        mins.append(num)
if mins == []:
    print("Not Available")
else:
    print(max(mins))
