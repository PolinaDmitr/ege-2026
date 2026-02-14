line = open('24_12.txt').readline()

line = line.replace('HALLOWEEN', 'h').replace('TRICK', 'i').replace('TREAT', 'e')

h_counter = 0
i_counter = 0
e_counter = 0
left = 0
counter = 0

for right in range(len(line)):
    if line[right] == 'h':
        h_counter += 1
    if line[right] == 'i':
        i_counter += 1
    if line[right] == 'e':
        e_counter += 1

    while h_counter > 5 or i_counter > 5 or e_counter > 5:
        if line[left] == 'h':
            h_counter -= 1
            if h_counter == 5 and i_counter == 5 and e_counter == 5:
                counter += 8
        if line[left] == 'i':
            i_counter -= 1
            if h_counter == 5 and i_counter == 5 and e_counter == 5:
                counter += 4
        if line[left] == 'e':
            e_counter -= 1
            if h_counter == 5 and i_counter == 5 and e_counter == 5:
                counter += 4
        left += 1

    if h_counter == 5 and i_counter == 5 and e_counter == 5:
        counter += 1
print(counter)
