from itertools import *

# count = 0
# for i in product('0123456', repeat=5):
#     if i[0] != '0':
#         s = "".join(i)
#         s = s.replace('0', 'a').replace('2', 'a').replace('4', 'a').replace('6', 'a')
#         s = s.replace('1', 'b').replace('3', 'b').replace('5', 'b')
#         if s.count('aa') >= 2 and s.count('aaa') == 0:
#             print(i)
#             count += 1
# print(count)

# count = 0
# for i in permutations('0123456789', r=6):
#     if i[0] != '0':
#         s = ''.join(i)
#         s_numb = int(s)
#         if s_numb % 4 == 0:
#             s = s.replace('0', 'a').replace('2', 'a')\
#             .replace('4', 'a').replace('6', 'a').replace('8', 'a')
#             if s.count('aa') == 0:
#                 print(s_numb)
#                 count += 1
# print(count)

# result = set()
# for i in permutations('parijanka'):
#     s = ''.join(i)
#     s1 = s.replace('i', 'a')
#     if s1.count('aa') == 1 and 'aaa' not in s1:
#         result.add(s)
# print(len(result))

count = 0
# for i in product(range(0, 25), repeat=4):
#     if i[0] != 0:
#         sum_k = 0
#         sum_m = 0
#         for j in i:
#             if j % 2 == 0:
#                 sum_k += 1
#             if j > 15:
#                 sum_m += 1
#         if sum_k == 1 and sum_m <= 2:
#             count += 1
# print(count)

for i in product('ДИОНСЙ', repeat=6):
    s = ''.join(i)
    k = int('Д' in s) + int('Н' in s)
    if ('Д' in s) != ('Н' in s) and 'ИИ' not in s and 'OO'not in s and 'ЙЙ'not in s \
            and 'СС' not in s and 'ДД'not in s and 'НН' not in s:
        count += 1
print(count)

