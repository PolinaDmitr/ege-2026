from ipaddress import *

net = ip_network('218.194.82.148/255.255.255.192', False)

#для компьютера! нужны только хосты!
for i in net.hosts():
    print(i)