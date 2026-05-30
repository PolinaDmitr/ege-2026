file = open('24_28799.txt')
line = file.readline()

max_len = 0

l_len = 0
l_sum = 0


for i in range(len(line)):
    l_len = 0
    l_sum = 0
    for j in range(i, len(line)):
        if line[j] in '0123456789':
            l_sum += int(line[j])
            if l_sum <= 200:
                l_len += 1
                max_len = max(l_len, max_len)
            else:
                break
        else:
            break
print(max_len)