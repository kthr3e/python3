s = '1.23,2.4,3.123'
split = s.split(',')
split_f = [float(s) for s in split]
sum=0
for s in split_f:
    sum+=s
print(sum)
