import os
import requests
import lzma

url = 'https://alcatraz.net.in.tum.de/ipv6-hitlist-service/open/responsive-addresses.txt.xz'
filename = 'weekly_responsive_ipv6_addresses.txt.xz'

response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

with lzma.open(filename) as f:
    uncompressed_content = f.read().decode('utf-8')

with open('weekly_responsive_ipv6_addresses.txt', 'w') as f:
    f.write(uncompressed_content)



response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)