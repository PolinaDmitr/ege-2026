file = open('24_6.txt')
line = file.readline()

left = 0
count = 0
max_len = 0

# левый указатель на самую левую крайнюю цифру, правый указатель - на первый арифметический знак после правой крайней цифры

for right in range(1, len(line)):
    if line[right - 1] in '+*' and line[right] in '+*':
        left = right + 1    # сразу на следующее для правого указателя значение
        count = 0
        continue
    if line[right] in '*+':
        count += 1
    # для ситуаций, когда изначально левый указатель встал на *+
    while line[left] in '*+' and left < right:
        left += 1
        count -= 1
    while count > 80 and left < right:
        if line[left] in '*+':
            count -= 1
        left += 1

    if count <= 80 and line[right] in '*+':
        max_len = max(max_len, (right - 1) - left + 1)
        print(line[left - 1: right + 2], right - left)

print(max_len)
