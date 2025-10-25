l = '1' * 100 + '3' * 900
l1 = []
for i in l:
    if i == '3':
        l1.append('0')
    else:
        l1.append('1')
print(l)
print(l1)
print(sum(int(x) for x in l1))