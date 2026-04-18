max_a = 0
for x in range(1, 2222):
    y = (11111 - 5 * x) / 3
    if int(y) == y:
        max_a = max(max_a, 680 * y + 256 * x + 1)
print(max_a)

for x in range(0, 11_111):
    for y in range(0, 11_111):
        if 5 * x + 3 * y <= 11_111:
            max_a = max(max_a, 680 * y + 256 * x + 1)
print(max_a)