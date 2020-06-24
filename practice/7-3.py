# 九九の表を作成してみよう

def multiply(x, y):
    return x * y

for num in range(1, 10):
    for num2 in range(1,10):
        print(multiply(num2, num), end="")
        if num2 < 9:
            print(", ", end="")
    print()
