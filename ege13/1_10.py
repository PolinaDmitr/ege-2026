from ipaddress import *

for n in range(31, 0, -1):
    count = 0
    net = ip_network(f'143.131.211.37/{n}', False)
    for i in net:
        if bin(int(i)).count('1') == 10:
            count += 1
    if count == 15:
        print(n)
        break