from ipaddress import *

ip_add = ip_address('195.154.162.96')

for m in range(31, 22, -1):
    net = ip_network(f'195.154.162.0/{m}')

    if ip_add in net.hosts():
        print(m)
        break

print(bin(231), bin(179))
print(bin(252))
print(231 + 255 + 166 + 225)