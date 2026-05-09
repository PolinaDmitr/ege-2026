file = open('17_11.txt')
line = file.readline()

digit_count = [0] * 10
a_count = 0
left = 0
min_len = 10 ** 10

for right in range(len(line)):
    if line[right] in '0123456789':
        digit_count[int(line[right])] += 1
    if line[right] in 'ABCDEF':
        a_count += 1

    while (a_count > 3
           or (line[left] in '0123456789' and digit_count[int(line[left])] > 1)
           or (line[left] not in '0123456789ABCDEF')):
        if line[left] in 'ABCDEF':
            a_count -= 1
        if line[left] in '0123456789':
            digit_count[int(line[left])] -= 1
        left += 1

    if all(x > 0 for x in digit_count) and a_count == 3:
        print(line[left : right + 1], digit_count, right - left + 1)
        min_len = min(min_len, right - left + 1)

print(min_len)
