file = open('17_10.txt')
line = file.readline()

left = 0
k = 0
min_len = 10 ** 10

for right in range(len(line)):
    if line[right] == 'Z':
        k += 1
    while k > 270:
        if line[left] == 'Z':
            k -= 1
        left += 1
    while line[left] != 'Z':
        left += 1
    if k == 270:
        min_len = min(min_len, right - left + 1)
        print(line[left : right + 1], right - left + 1)

print(min_len)