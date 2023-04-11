# IPv6_probing
Repository to check existence of IPv6 address and check validity avoiding aliases

# Prerequisites
* local installation of python 3.8+ and Linux terminal (bash, zsh also via WSL) with valid connetivity and SUDO option available
* install via packet manager (pip or conda) the following python packages:
    * for hitlist retrieval: os, requests, lzma
    * for de-aliasing: scapy, random, concurrent.futures
* ...

# Instructions
to execute the operation, perform the following processes:
1. open a bash terminal in a folder containing this repository (locally or via ssh)
2. run chmod +x retrieve_addresses.sh to allow execution of customs bash files
3. execute ./retrieve_addresses.sh that will download weekly list of actives addresses and decode into a local .txt file
    1. ipv6_retrieval will be executed downloading and storing in the working directory ipv6 hitlist
    2. ipv6_aliases_removal will iterate the hitlist and send 16 packets to pseudo-random addresses within IPv6 prefix, using TCP/80 and ICMPv6 enforcing traversal of a subprefix with different nybbles. SUDO permissions required for Linux kernel
4. ...
