file = open('27_6_b.txt')
cl1 = []
cl2 = []
cl3 = []
cl4 = []
cl5 = []
cl6 = []
cl7 = []
file.readline()


for i in file.readlines():
    x, y = map(float, i.split())
    if y > 20:
        cl1.append((x, y))
    elif x < 0 and y < 0:
        cl2.append((x, y))
    elif x < 0:
        cl3.append((x, y))
    elif y > 14:
        cl4.append((x, y))
    elif x < 7:
        cl5.append((x, y))
    elif y > 4:
        cl6.append((x, y))
    else:
        cl7.append((x, y))