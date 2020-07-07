#https://atcoder.jp/contests/abs/tasks/abc087_b
num_list = []
for i in range(3):
    val = input("")
    if val:
        num_list.append(val)

sum = int(input(""))
count = 0
for i in range(int(num_list[0]) + 1):
    for j in range(int(num_list[1]) + 1):
        for  k in range(int(num_list[2]) + 1):
            x = 500 * i + 100 * j + 50 * k
            if x == sum:
                #print("500: " + str(i) + " 100: " + str(j) + " 50: "+ str(k))
                count += 1
print(count)
