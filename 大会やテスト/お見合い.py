import itertools
import pandas as pd
names = list(map(str,input().split()))
def matching(p1,p2):
    num1 = [int(ord(p1[i])) for i in range(len(p1))]
    num2 = [int(ord(p2[i])) for i in range(len(p2))]
    nums1 = num1 + num2
    nums2 = num2 + num1
    return max((sum(nums1[::2]) - sum(nums1[1::2])) % 101,(sum(nums2[::2]) - sum(nums2[1::2])) % 101)

pair = [list(i) for i in itertools.combinations(names,2)]
for i in range(len(pair)):
    pair[i].append(matching(*pair[i]))

df = pd.DataFrame(pair,columns = ['一人目','二人目','相性度'])
pd.set_option('display.unicode.east_asian_width', True)
df.style.set_properties(**{'text-align': 'left'})
