line = open('24_7.txt').readline()
k_max = 1
k = 1
# for i in range(len(line) - 1):
#     if line[i] in '0123456789' and line[i + 1] in '0123456789':
#         if int(line[i]) % 2 != int(line[i + 1]) % 2:
#             k_max = max(k, k_max)
#             k = 1
#         else:
#             k += 1
#     else:
#         k += 1
for i in range(len(line) - 1):
    if line[i] in '02468' and line[i + 1] in '02468':
        k_max = max(k, k_max)
        k = 1
    else:
        k += 1
print(k_max)