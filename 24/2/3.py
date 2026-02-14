line = open('24_3.txt').readline()
print(line[:100])
left = 0
f_counter = 0
k_max = 0

for right in range(3, len(line)):
    if line[right - 3 : right + 1] == 'FSRQ':
        f_counter += 1

    while f_counter > 80:
        if line[left : left + 4] == 'FSRQ':
            f_counter -= 1
        left += 1

    if f_counter == 80:
        k_max = max(k_max, right - left + 1)
print(k_max)
