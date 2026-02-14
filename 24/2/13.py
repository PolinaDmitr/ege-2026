line = open('24_13.txt').readline()

line = 'Y' + line + 'Y'
y_ind = [x for x in range(len(line)) if line[x] == 'Y']
k_max = 0

for i in range(1, len(y_ind) - 81):
    l = line[y_ind[i - 1] + 1 : y_ind[i + 80]]
    if l.count('2025') >= 90:
        k_max = max(k_max, len(l))
print(k_max)

