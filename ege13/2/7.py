# Для узла с IP-адресом 195.154.162.96 адрес сети
# равен 195.154.162.0.
from ipaddress import *

print(bin(231), bin(252))

ip_add = ip_address('195.154.162.96')
for n in range(31, 0, -1):
    net = ip_network(f'195.154.162.0/{n}', False)
    if ip_add in net:
        print(n)
        break

