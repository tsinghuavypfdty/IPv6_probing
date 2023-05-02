from scapy.all import *
import random
from scapy.layers.inet6 import IPv6, TCP, ICMPv6EchoRequest
import concurrent.futures

# Define function to generate pseudo-random addresses within a given prefix
def generate_random_addresses(prefix, num_addresses):
    addresses = []
    for i in range(num_addresses):
        random_suffix = ''.join(random.choices('0123456789abcdef', k=16))
        address = prefix[:-1] + ':' + random_suffix + ':' + '0'*(39-len(prefix+random_suffix))
        addresses.append(IPv6(address))
    return addresses

def send_requests(ipv6, output_file):
    # Define TCP and ICMPv6 packets
    tcp_packet = IPv6()/TCP(dport=80, flags='S')
    icmp_packet = IPv6()/ICMPv6EchoRequest()
    # initialize counter to check responses
    resp = 0
    # take prefixes from /64 to /124 -> not sure of this process to select random addresses for aliases validation
    for prefix_length in range(64, 124, 4):
        prefix = str(addr)[:prefix_length] + ':'
    # generate 1 address for each 4-bit subprefix
        for i in range(16):
            nybble = hex(i)[2:]
            subprefix = prefix + nybble + '000:'
            random_address = generate_random_addresses(subprefix, 1)[0]
            #print(f"random address: {str(random_address)}")
            # send request to pseudo-random address
            tcp_packet.dst = random_address
            icmp_packet.dst = random_address
            response_tcp = sr1(tcp_packet, timeout=2, verbose=False)
            response_icmp = sr1(icmp_packet, timeout=2, verbose=False)
            print(f"Packets sent to {str(random_address)} generated from {str(addr)}")
            if response_tcp or response_icmp:
                resp += 1
                print(f"Response received from {str(random_address)} generated from {str(addr)}")
            # check if 16 responses were collected for IPv6 prefixes
            if resp < 16:        
                output_file.write(f"{str(addr)}")

# Create file to store unresponsive IPv6 addresses
non_aliased_addresses_file = open("non_aliased_ipv6_addresses.txt", "w")

def process_address(ipv6):
    output =  non_aliased_addresses_file
    send_requests(ipv6, output)

# Read in the list of responsive IPv6 addresses
with open("responsive_ipv6_addresses.txt", "r") as f:
    # Skip the first line
    f.readline()
    # Create a list of IPv6 addresses with the new line special char removed
    addresses = []
    for a in range(10):
        addresses.append(f.readline().strip())
    print(f"Addresses: {addresses}")

# Create a ThreadPoolExecutor with nß worker threads
with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:
    print(f"Addresses: {addresses}")
    # Submit a send_requests task for each IPv6 address
    future_to_addr = {executor.submit(process_address, addr): addr for addr in addresses}

    # Wait for all tasks to complete and check for exceptions -> review parallelization process
    for future in concurrent.futures.as_completed(future_to_addr):
        addr = future_to_addr[future]
        try:
            _ = future.result()
        except Exception as e:
            print(f"Error processing address {addr}: {e}")

# Close the file containing non-aliased IPv6 addresses
non_aliased_addresses_file.close()