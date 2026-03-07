line = open('24_hard_3.txt').readline()
# print(line[:100])
# count_lnd = 0
# left = 0
# lnd_max = 0
# for right in range(2, len(line) - 2):
#     if line[right - 2 : right + 1] == 'LND':
#         count_lnd += 1
#     while count_lnd > 1000:
#         if line[left : left + 3] == 'LND':
#             count_lnd -= 1
#             left += 1
#         if count_lnd <= 1000:
#             for l1 in range(left, right):
#                 if line[l1] == line[right]:
#                     lnd_max = max(lnd_max, right - l1 + 1)
#                     break
# print(lnd_max)

#очень долго, надо поиграть с индексами
ind = [-1]
for i in range(len(line) - 2):
    if line[i : i + 3] == 'LND':
        ind.append(i)
ind.append(len(line))

k_max = 0
for i in range(1, len(ind) - 10002):
    st = ind[i - 1] + 1
    end = ind[i + 10_000] + 1
    for a in range(st, ind[i]):
        for b in range(ind[i + 9_999], end + 1):
            if line[a] != line[b]:
                k_max = max(k_max, b - a + 1)
print(k_max)



