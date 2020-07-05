"""
あなたが作成するプログラムは、まず、以下の流れで「二人の相性」を求めます。

1. 相性をチェックする二人の名前を並べた英小文字からなる文字列を入力します。
2. "a" を 1、"b" を 2、...、"z" を 26 として、文字列を数列に変換します。この数列を A とします。
3. 数列 A の隣り合う 2 つの数を足して前から順番に並べた新しい数列 A' を作り、これを新たに A とします。このとき、A の要素の大きさが 101 を超えていた場合、その要素から 101 を引きます。
4. 数列 A の要素数が 1 になるまで 3. の手順を繰り返します。A の要素数が 1 となったとき、残った要素の値を「二人の相性」とします。

名前の並べ方は 2 通りあります。そこで、あなたは相性占いの結果として、 2 通りの方法で計算した「二人の相性」のうち大きい方を出力するようにプログラムを組むことにしました。

たとえば、pa さんと iza さんの名前を "paiza" として並べたとき、「二人の相性」は 78 になります。

iza さんの名前を先に持ってきて "izapa" とすると、「二人の相性」は 83 になります。

相性占いをする二人の人物の名前が与えられたとき、相性占いの結果を出力するプログラムを作成してください。
"""
#https://www.suzu6.net/posts/88-python-max-min/
#https://juppy.hatenablog.com/entry/2018/12/11/python_%E6%96%87%E5%AD%97%E3%82%A2%E3%83%AB%E3%83%95%E3%82%A1%E3%83%99%E3%83%83%E3%83%88%E2%87%86%E6%95%B0%E5%AD%97
names = input().split(" ")
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
