from ipaddress import *
for mask in range(31, 1, -1):
    c = 0
    net = ip_network(f'156.38.155.174/{mask}',0)
    for ip in net:
        l = f'{int(ip):032b}'
        if l.count('1') == 12:
            c += 1
    if c == 45:
        print(net.netmask, mask)