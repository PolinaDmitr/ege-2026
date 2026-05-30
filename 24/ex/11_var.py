file = open('24.txt')
line = file.readline()

numb = ''
numb_over_7 = 0
k_min = 10 ** 10
over7 = '89ABCDEF'
alphabet = '123456789ABCDEF'

for i in range(len(line)):
    numb = ''
    numb_over_7 = 0
    for j in range(i, len(line)):
        if line[j] in alphabet:
            numb += line[j]
            if line[j] in over7:
                numb_over_7 += 1
            if numb_over_7 >= 12:
                k_min = min(k_min, len(numb))
                print(numb)
                break
        else:
            break

print(k_min)

