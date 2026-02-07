line = open('24_2.txt').readline()
print(line[:100])
k = 1
k_max = 1
for i in range(len(line) - 1):
    if (line[i] in '124') == (line[i + 1] in '124'):
        k_max = max(k_max, k)
        k = 1
    else:
        k += 1
print(k_max)