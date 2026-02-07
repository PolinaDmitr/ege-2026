line = open('24_9.txt').readline()
k = 1
k_max = 1
for i in range(len(line) - 1):
    if line[i] in 'ABC' and line[i] == line[i + 1]:
        k += 1
    else:
        k_max = max(k, k_max)
        k = 1
print(k_max)