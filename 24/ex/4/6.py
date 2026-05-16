file = open('24_6.txt')
line = file.readline()

a_word = []
word = ''
start_word = 0
for i in range(len(line)):
    if line[i] == '.':
        if word == '' or word == '.':
            word = line[i]
        else:
            word += line[i]
            if len(word) >= 2 and word[1] == 'A':
                a_word.append((i - len(word) + 1, i))
                print(word)
                word = ''
            else:
                word = '.'
    elif len(word) > 0:
        word += line[i]

min_a = []

for i in range(len(a_word) - 600):
    start = a_word[i]
    end = a_word[i + 600 - 1]
    min_a.append((start, end, end[1] - start[0] + 1))

min_word = min(min_a, key=lambda x: x[2])
print(min_word)
# print(line[min_word[0][0]: min_word[1][1] + 1])
print(len(a_word))



# говно-решение
w = [x for x in range(1, len(line)) if line[x-1] == '.' and line[x] == 'A']
K = 600
print(len(w))

l = []
ml = float('inf')
for x, y in zip(w, w[K - 1:]):
    end = line.find('.', y)
    if end != -1:
        ml = min(ml, end - x + 2)
        l.append(line[x - 1 : end + 1])
print(ml)
l_min = min(l, key=len)

a_word = []
word = ''
start_word = 0
for i in range(len(l_min)):
    if l_min[i] == '.':
        if word == '' or word == '.':
            word = l_min[i]
        else:
            word += l_min[i]
            if len(word) >= 2 and word[1] == 'A':
                a_word.append((i - len(word) + 1, i))
                # print(word)
                word = ''
            else:
                word = '.'
    elif len(word) > 0:
        word += l_min[i]
print(len(a_word)) # тут оказалось 431 слово
print(l_min.count('.A.A'))

