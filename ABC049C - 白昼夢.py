import sys
S = input()
T=["dream","dreamer","erase","eraser"]
while S:
    for word in T:
        if S.endswith(word):
            S=S[:-1*len(word)]
            break
    else:
        print("NO")
        sys.exit()
print("YES")


import re
print('YES' if re.fullmatch(r'((dream(er)?)|(eraser?))*', input()) else 'NO')
"""
reで正規表現に対するアプローチ
※正規表現とは・・https://techacademy.jp/magazine/15635#:~:text=Python%E3%81%AE%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE%E3%81%A8,%E8%A1%8C%E3%81%86%E3%81%93%E3%81%A8%E3%81%8C%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%99%E3%80%82
https://qiita.com/hiroyuki_mrp/items/29e87bf5fe46de62983c
match(r'探したい文字列','対象となる文字列')
r'((dream(er)?)|(eraser?))*' -> dreamの語尾にerが0,1回続く、または、eraseの語尾にrが0回か一回続くものが
0回以上続くもの。
まだまだ正規表現があるため頑張ろう
"""
