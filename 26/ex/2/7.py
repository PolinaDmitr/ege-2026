file = open('26_7.txt')
n, k = map(int, file.readline().split())

master = []
count_master = []
for i in range(k + 1):
    master.append(list())
    count_master.append(0)

l = []
for i in range(n):
    t, r, m = map(int, file.readline().split())
    l.append((t, r, m))

l.sort()

util_max = 0

for i in range(len(l)):
    t, r, m = l[i]
    if m != 0:
        if len(master[m]) >= 5:
            current_m = master[m]
            if current_m[0] < t:
                current_m.pop(0)
                current_m.append(r)
                count_master[m] += 1
            else:
                util_max += 1
        else:
            master[m].append(r)
            count_master[m] += 1
    else:
        min_m = min(master[1:],key=len)
        if len(min_m) < 5:
            for j in range(1, k + 1):
                if master[j] == min_m:
                    master[j].append(r)
                    count_master[j] += 1
        else:
            util_max += 1
print(max(count_master), util_max)