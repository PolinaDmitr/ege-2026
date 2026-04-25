# 126.115.78.15 и 126.115.84.26
from ipaddress import *

ip1 = ip_address('126.115.78.15')

k = []
for n in range(31, 12, -1):
    net = ip_network(f'126.115.84.26/{n}', False)
    if ip1 not in net:
        continue
    c = 0
    for i in net:
        ip_bin = bin(int(i))[2:]
        if ip_bin.count('1') == 22:
            c += 1
    k.append(c)
    print(n, c)

print(min(k))
