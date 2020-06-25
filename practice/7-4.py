# coding: utf-8
# Your code here!

# スコープを理解する
a = 10
b = 20
message ="paiza"

def sum(x,y):
    a = 3
    global message
    message += "paiza"
    print(message)
    print(str(a))
    return x + y

num = sum(a,b)
print(num)
