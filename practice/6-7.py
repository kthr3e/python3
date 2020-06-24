# coding: utf-8
# Your code here!

# 標準入力から2次元リスト

enemy_img = []
while True:
    line = input()
    if line == "_":
        break
    enemy_img.append(line.split(","))

# print(enemy_img)

for line in enemy_img:
    for dot in line:
        if int(dot) == 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()
    
