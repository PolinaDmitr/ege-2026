line = open('24_4.txt').readline()
k_max = 1
k = 1
for i in range(len(line) - 1):
    if (line[i] in '124') != (line[i + 1] in '124'):
        k += 1
    else:
        if k > k_max:
            k_max = k
        k = 1
print(k_max)