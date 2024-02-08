from ipaddress import *
ip = '201.92.0.20'
ip2 = '201.92.0.49'
for mask in range(32, -1, -1):
    s1= ip_network(f'{ip}/{mask}', 0)
    s2 = ip_network(f'{ip2}/{mask}' , 0)
    if s1==s2:
        print(s1.netmask)
        print(f'{s1.netmask:b}')
        print(2**(f'{s1.netmask:b}'.count('0'))-4)
        break
