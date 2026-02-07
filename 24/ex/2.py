line = open('24_2.txt').readline()
k_max = 0
dig = 0
k_len = 0
for i in range(len(line)):
    if line[i] == 'G' or i == len(line) - 1:
        if dig == 45:
            k_max = max(k_max, k_len)
        dig = 0
        k_len = 0
    elif line[i] in ('1', '3', '5', '7', '9'):
        dig += 1
        if dig > 45:
            k_max = max(k_max, k_len)
            dig = 0
            k_len = 0
    k_len += 1
print(k_max)


# m = line.split('G')[1:]
# k_max = 0
# for l in m:
#     dig = 0
#     for i in range(len(l)):
#         if l[i] in '13579':
#             dig += 1
#         if dig > 45:
#             k_max = max(k_max, i + 1)
#             break
#     if dig == 45:
#         k_max = max(k_max, len(l) + 1)
#
# print(k_max)