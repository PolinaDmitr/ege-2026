from itertools import *

count = 0
for i in product('0123456', repeat=5):
    if i[0] != '0':
        count_6 = i.count('6')
        # flag = True
        # for j in range(len(i) - 1):
        #     if i[j] == i[j + 1]:
        #         flag = False
        #         break
        flag = all(i[j] != i[j + 1] for j in range(len(i) - 1))
        if count_6 == 1 and flag:
            count += 1
print(count)