file = open('24_28799 (1).txt')
line = file.readline()


len_max = 0

for i in range(len(line)):
    sum_current = 0
    len_current = 0
    if line[i] in '0123456789':
        for j in range(i, len(line)):
            if line[j] in '0123456789':
                sum_current += int(line[j])
                if sum_current <= 200:
                    len_current += 1
                else:
                    len_max = max(len_current, len_max)
                    break
            else:
                len_max = max(len_current, len_max)
                break
print(len_max)