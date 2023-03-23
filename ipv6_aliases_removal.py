from scapy.all import *
import random
from scapy.layers.inet6 import IPv6, TCP, ICMPv6EchoRequest

# Define function to generate pseudo-random addresses within a given prefix
def generate_random_addresses(prefix, num_addresses):
    addresses = []
    for i in range(num_addresses):
        random_suffix = ''.join(random.choices('0123456789abcdef', k=16))
        address = prefix[:-1] + ':' + random_suffix + ':' + '0'*(39-len(prefix+random_suffix))
        addresses.append(IPv6(address))
    return addresses

# Read in the list of responsive IPv6 addresses
with open("responsive_ipv6_addresses.txt", "r") as f:
    # Skip the first line
    f.readline()
    # Read in the remaining lines and format as IPv6 addresses
    responsive_addresses = []
    for addr in f.readlines():
        addr = addr.strip()
        print(addr)
        # convert IPv6 address to bytes
        ipv6_bytes = socket.inet_pton(socket.AF_INET6, addr)
        print(ipv6_bytes)
        ipv6_pkt = IPv6(ipv6_bytes) #error!!!!
        print(ipv6_pkt.summary())
        responsive_addresses.append(ipv6_pkt)

# Define TCP and ICMPv6 packets
tcp_packet = IPv6()/TCP(dport=80)
icmp_packet = IPv6()/ICMPv6EchoRequest()

# Create file to store unresponsive IPv6 addresses
non_aliased_addresses_file = open("non_aliased_ipv6_addresses.txt.xz", "w")

# Send packets to pseudo-random addresses within each responsive prefix
for address in responsive_addresses:
    #print(responsive_addresses)
    for prefix_length in range(64, 124, 4):
        prefix = str(address)[:prefix_length] + ':'
        random_addresses = generate_random_addresses(prefix, 32)
        for random_address in random_addresses:
            tcp_packet.dst = random_address
            icmp_packet.dst = random_address
            response_tcp = sr1(tcp_packet, timeout=2, verbose=False)
            response_icmp = sr1(icmp_packet, timeout=2, verbose=False)
            if response_tcp is None and response_icmp is None:
                non_aliased_addresses_file.write(f"{str(address)}\n")
    print(f"Packets sent to {str(address)}")

# Close the file containing unresponsive IPv6 addresses
non_aliased_addresses_file.close()