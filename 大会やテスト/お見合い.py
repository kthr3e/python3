
#https://www.suzu6.net/posts/88-python-max-min/
#https://juppy.hatenablog.com/entry/2018/12/11/python_%E6%96%87%E5%AD%97%E3%82%A2%E3%83%AB%E3%83%95%E3%82%A1%E3%83%99%E3%83%83%E3%83%88%E2%87%86%E6%95%B0%E5%AD%97
names = input("自分の名前と相手の名前を間に空白を挿入して入力してください: ").split(" ")
#入力とは逆順の名前のリスト
names2 = []
names2.append(names[1])
names2.append(names[0])
#print(names2)
#print(names)
#アルファベットを数字に変換したときに入れるリスト
num_list = []
num_list2 = []

for name in names:
    for i in range(len(name)):
        num_list.append(ord(name[i]) - 96)
#print(num_list)


for name in names2:
    for i in range(len(name)):
        num_list2.append(ord(name[i]) - 96)
#print(num_list2)

# 入力された通りの計算
sum_list = num_list
#print(sum_list)
while len(sum_list) != 1:
    for i in range(len(sum_list) - 1):
        sum_list[i] = sum_list[i] + sum_list[i + 1]
        if sum_list[i] > 101:
            sum_list[i] -= 101
    del sum_list[-1]
    #print(sum_list)

#入力とは名前を逆にして計算
sum_list2 = num_list2
#print(sum_list2)
while len(sum_list2) != 1:
    for i in range(len(sum_list2) - 1):
        sum_list2[i] = sum_list2[i] + sum_list2[i + 1]
        if sum_list2[i] > 101:
            sum_list2[i] -= 101
    del sum_list2[-1]
    #print(sum_list2)

print(max(sum_list[0],sum_list2[0]))
