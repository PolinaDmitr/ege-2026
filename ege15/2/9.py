# (680y + 256x < A) ∨ (5x + 3y > 11111)

max_a = 0

for x in range(11_112 // 5 + 1):
    for y in range(11_112 // 3 + 1):
        if 5 * x + 3 * y <= 11_111:
            max_a = max(max_a, 680 * y + 256 * x + 1)

print(max_a)