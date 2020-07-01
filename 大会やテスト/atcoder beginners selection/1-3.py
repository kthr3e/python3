count = 0
kai = input()
num = input().split(" ")
flag = False
while True:
    for i in range(int(kai)):
        if int(num[i]) % 2 != 0:
            flag = True
            break
        num[i] = int(num[i]) / 2
    if flag:
        break
    count += 1

print(count)
