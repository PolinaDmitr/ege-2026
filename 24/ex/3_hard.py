line = open('24_hard_3.txt').readline()
print(line[:100])
count_lnd = 0
left = 0
lnd_max = 0
for right in range(2, len(line) - 2):
    if line[right - 2 : right + 1] == 'LND':
        count_lnd += 1
    while count_lnd > 1000:
        if line[left : left + 3] == 'LND':
            count_lnd -= 1
            left += 1
        if count_lnd <= 1000:
            for l1 in range(left, right):
                if line[l1] == line[right]:
                    lnd_max = max(lnd_max, right - l1 + 1)
                    break
print(lnd_max)

#очень долго, надо поиграть с индексами


