file = open('17_6.txt')
line = file.readline()

k = 0
left = 0
max_len = 0

last_right = ''


for right in range(1, len(line)):
    if line[right] in '*+' and last_right in '*+':
        left = right
        last_right = line[right]
        k = 0
        continue
    if line[right] in '*+':
        k += 1
    while line[left] in '*+' and left < right:
        left += 1
        # k -= 1
    while k > 80 and left < right:
        if line[left] in '*+':
            k -= 1
        left += 1
    if k <= 80 and line[right] in '*+':
        max_len = max(max_len, right - 1 - left + 1)
        print(line[left : right], line[left], line[right], right - left + 1)
    last_right = line[right]

print(max_len)



