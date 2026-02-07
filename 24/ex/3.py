line = open('24.3.txt').readline()
print(line[:100])
print(line[-100:])
ind_xy = []
k_max = 0
for i in range(len(line)):
    if line[i] == 'X' or line[i] == 'Y':
        ind_xy.append(i)
for i in range(len(ind_xy) - 3):
    start = ind_xy[i] + 1
    end = ind_xy[i + 3] - 1
    if line[ind_xy[i + 1]] != line[ind_xy[i + 2]]:
        k_max = max(k_max, end - start + 1)
print(k_max)
