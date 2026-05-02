file = open('17_10.txt')
l = []
l_13 = []
l_25 = []
for i in file.readlines():
    x = int(i)
    l.append(x)
    if x % 13 == 0:
        l_13.append(x)
    if x % 25 == 0:
        l_25.append(x)

digit_13 = sum(int(x) for x in str(l_13[12]))
digit_25 = sum(int(x) for x in str(l_25[24]))

k = []
for i in range(len(l) - 2):
    count_3 = len([x for x in l[i: i + 3] if 100 <= x <= 999])
    if count_3 > 0:
        digit_sum = [sum(int(x) for x in str(j)) for j in l[i : i + 3]]
        if len([x for x in digit_sum if x == digit_13]) <= 1:
            if len([x for x in digit_sum if x == digit_25]) >= 2:
                k.append(sum(l[i : i + 3]))

print(len(k), sum(k) / len(k))