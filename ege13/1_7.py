#200.154.190.12 и 200.154.184.0
from ipaddress import *


ip_add_2 = ip_address('200.154.184.0')

for n in range(31, 0, -1):
    net = ip_network(f'200.154.190.12/{n}', False)
    if ip_add_2 in net.hosts():
        print(n)
        break