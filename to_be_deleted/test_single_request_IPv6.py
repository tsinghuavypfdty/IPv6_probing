#run the script as SUDO (root) to allow Linux kernel to execute raw sockets
from scapy.all import *
from scapy.layers.inet6 import IPv6, TCP, ICMPv6EchoRequest

addr = '2001:1248:303f:f027:6961:eedd:2757:c10b'
addr2 = '2001:1201:10::1'
print(addr)
print(addr2)
"""
# Create IPv6
ipv6 = IPv6(dst=addr2)
tcp = TCP(dport=80, flags='S')
# Send the packet
send(ipv6/tcp)
"""

# Create and TCP and ICMP headers
tcp_packet = IPv6()/TCP(dport=80, flags='S')
icmp_packet = IPv6()/ICMPv6EchoRequest()

tcp_packet.dst = addr2
icmp_packet.dst = addr2
response_tcp = sr1(tcp_packet, timeout=2, verbose=False)
response_icmp = sr1(icmp_packet, timeout=2, verbose=False)
print(response_tcp.summary())
print(response_icmp.summary())