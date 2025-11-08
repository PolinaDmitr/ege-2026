#167.77.194.47 и 167.77.194.37  из другой – 167.77.200.25
from ipaddress import *

ip_add_1 = ip_address('167.77.194.47')
count = 0
for n in range(31, 0, -1):
    net_1 = ip_network(f'167.77.194.47/{n}', False)
    net_2 = ip_network(f'167.77.200.25/{n}', False)
    if (ip_add_1 in net_1 and ip_add_1 != net_1.network_address
        and ip_add_1 != net_1.broadcast_address) and ip_add_1 not in net_2:
        count += 1
print(count)
