line = open('24_9.txt').readline()
line = line.replace('G', ' G')
m = line.split()
k_max = 0
for l in m:
    k = 0
    for i in range(len(l)):
        if l[i] in '13579':
            k += 1
            if k > 45:
                k_max = max(k_max, i)
                break
    if k == 45:
        k_max = max(len(l), k_max)
print(k_max)
