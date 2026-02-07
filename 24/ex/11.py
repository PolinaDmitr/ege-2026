line = open('24_11.txt').readline()
l1 = line.replace('A', ' A').replace('D', 'D ')
l = l1.split()
k_max = 0
for i in l:
    if i[-1] == 'D' and i[0] == 'A':
        print(i)
        k_max = max(k_max, len(i))
l2 = line.replace('A', 'A ').replace('D', ' D')
l = l2.split()
for i in l:
    if i[-1] == 'A' and i[0] == 'D':
        print(i)
        k_max = max(k_max, len(i))
print(k_max)
