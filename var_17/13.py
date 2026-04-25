from ipaddress import *

for m in range(31, 0, -1):
    net = ip_network(f'156.38.155.174/{m}', False)
    k = 0
    for i in net:
        if bin(int(i))[2:].count('1') == 12:
            k += 1
    if k == 45:
        print(m)
        break