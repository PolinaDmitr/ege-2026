l = '3' * 900 + '1' * 100
l = list(l)

for i in range(999, -1, -1):
    if l[i] == '3':
        l[i] = '0'
    elif l[i] == '0':
        l[i] = '3'
print(sum(int(x) for x in l))