#201.92.0.20 и 201.92.0.49
from ipaddress import *

ip_add_2 = ip_address('201.92.0.49')
for n in range(31, 0, -1):
    net = ip_network(f'201.92.0.20/{n}', False)
    if ip_add_2 in net:
        count = net.num_addresses - 4
        print(count)
        break