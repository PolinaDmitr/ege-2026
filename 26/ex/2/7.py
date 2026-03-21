file = open('26_7.txt')
n, k = map(int, file.readline().split())

master = []
count_master = []
for i in range(k):
    master.append(list())
    count_master.append(0)
#мастерские идут с 0

l = []
for i in range(n):
    t, r, m = map(int, file.readline().split())
    l.append((t, r, m))

l.sort()

util_max = 0

for i in range(len(l)):
    t, r, m = l[i]
    # освободить очереди
    for j in range(k):
        master[j] = [x for x in master[j] if x > t]

    if m != 0:
        if len(master[m - 1]) == 0:
            master[m - 1].append(t + r)
            count_master[m - 1] += 1
        elif len(master[m - 1]) < 5:
            master[m - 1].append(master[m - 1][-1] + r)
            count_master[m - 1] += 1
        else:
            util_max += 1
    else:
        min_m = min(master,key=len)
        if 0 < len(min_m) < 5:
            for j in range(k):
                if master[j] == min_m:
                    master[j].append(master[j][-1] + r)
                    count_master[j] += 1
                    break
        elif len(min_m) == 0:
            for j in range(k):
                if master[j] == min_m:
                    master[j].append(t + r)
                    count_master[j] += 1
                    break
        else:
            util_max += 1
print(max(count_master), util_max)