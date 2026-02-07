line = open('24_8.txt').readline()
l = line.replace('EA', '2').replace('NPC', '3')
k = 0
k_max = 0
for i in range(len(l)):
    if l[i] not in '23':
        k_max = max(k, k_max)
        k = 0
    else:
        k += int(l[i])
print(k_max)
