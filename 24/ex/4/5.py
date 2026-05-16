file = open('24_5.txt')
line = file.readline()

ind_x = []
word = ''
start_word = 0
for i in range(len(line)):
    if line[i] == '.' and (word == '' or word == '.'):
        word = line[i]
        start_word = i
    elif line[i] == '.' and word != '':
        if word[-1] == 'X':
            ind_x.append((start_word, i))
        word = ''
        start_word = i + 1  #не забыть обнулять
    else:
        word += line[i]
# print(ind_x)
min_line = 10 ** 10

min_m = []
for i in range(0, len(ind_x) - 1500):
    start_i = ind_x[i][0]
    end_i = ind_x[i + 1500 - 1][1]
    # min_line = min(min_line, end_i - start_i + 1)
    min_m.append((start_i, end_i, end_i - start_i + 1))

min_k = min(min_m, key=lambda x: x[2])
print(min_k)
print(line[min_k[0] : min_k[1] + 1])

