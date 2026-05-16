file = open('24_5.txt')
line = file.readline()

word_x = []

word = ''
for i in range(len(line)):
    if line[i] == '.':
        if word == '' or word == '.':
            word = '.'
        else:
            word += line[i]
            if word[-2] == 'X':
                word_x.append((i - len(word) + 1, i))
                print(word)
            word = '.'
    elif word != '':
        word += line[i]

min_x = 10 ** 10
min_l = ''

for i in range(len(word_x) - 1500):
    start = word_x[i][0]
    end = word_x[i + 1500 - 1][1]
    # c = line[start : end + 1].count('X.X.')
    # if i + 1500 - 1 + c < len(word_x):
    #     end = word_x[i + 1500 - 1 + c][1]
    if end - start + 1 < min_x:
        min_x = end - start + 1
        min_l = line[start : end + 1]

print(min_x)


word_x = []

word = ''
for i in range(len(min_l)):
    if min_l[i] == '.':
        if word == '' or word == '.':
            word = '.'
        else:
            word += min_l[i]
            if word[-2] == 'X':
                word_x.append((i - len(word) + 1, i))
                word = ''
            else:
                word = '.'
    elif word != '':
        word += min_l[i]

print(len(word_x))


