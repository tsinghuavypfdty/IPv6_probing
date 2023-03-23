from scapy.all import *
from scapy.layers.inet6 import IPv6

addr = '2001:1248:303f:f027:6961:eedd:2757:c10b'
print(addr)
ipv6_bytes = socket.inet_pton(socket.AF_INET6, addr)
print(ipv6_bytes)
ipv6_pkt = IPv6(ipv6_bytes)
print(ipv6_pkt.summary())

# define the responsive_addresses list first
responsive_addresses = []
responsive_addresses.append(ipv6_pkt)