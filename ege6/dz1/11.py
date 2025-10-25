
l = ['_'] * 100
j = 50
print(l)

for _ in range(27):
    j += 5
    l[j] = '*' if l[j] == '_' else '_'
    j -= 3
    l[j] = '*' if l[j] == '_' else '_'
    j -= 3
    print(l)
print()
print(l)
count = 0
for i in l:
    if i == '*':
        count += 1
print(count)

l = [-1] * 100
i = 50
print(l)

for _ in range(27):
    i += 5
    l[i] *= -1
    i -= 3
    l[i] *= -1
    i -= 3
print(l)
count = 0
for j in l:
    if j == 1:
        count += 1
print(count)
