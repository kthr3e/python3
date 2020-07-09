
#https://www.suzu6.net/posts/88-python-max-min/
#https://juppy.hatenablog.com/entry/2018/12/11/python_%E6%96%87%E5%AD%97%E3%82%A2%E3%83%AB%E3%83%95%E3%82%A1%E3%83%99%E3%83%83%E3%83%88%E2%87%86%E6%95%B0%E5%AD%97
import itertools
import pandas as pd
names = list(map(str,input().split()))
def matching(p1,p2):
    #print(len(p1))
    num1 = [int(ord(p1[i])) for i in range(len(p1))]
    num2 = [int(ord(p2[i])) for i in range(len(p2))]
    nums1 = num1 + num2
    nums2 = num2 + num1
    return max((sum(nums1[::2]) - sum(nums1[1::2])) % 101,(sum(nums2[::2]) - sum(nums2[1::2])) % 101)
#print(names)
pair = [list(i) for i in itertools.combinations(names,2)]
#print(pair)
#ここで二人のペアの配列リストを作成。
for i in range(len(pair)):
    pair[i].append(matching(*pair[i]))

#print(pair)
df = pd.DataFrame(pair,index = ["一組目","二組目","三組目"],columns = ['一人目','二人目','相性度'])
df
