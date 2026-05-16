file = open('26-173.txt')
k = int(file.readline())
n = int(file.readline())

p = []
for i in range(n):
    start, end = map(int, file.readline().split())
    p.append((start, end))

p.sort()

m = [0] * k
count = 0

last_m = 0
last_start_time = 0

for i in p:
    start, end = i

    for j in range(k):
        if m[j] < start:
            m[j] = end
            count += 1
            if start > last_start_time:
                last_m = j
                last_start_time = start
            break

print(m)
print(count)
print(last_m + 1)