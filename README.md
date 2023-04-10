# IPv6_probing
Repository to check existence of IPv6 address and check validity avoiding aliases

# Instructions
to execute the operation, perform the following processes:
1. open a bash terminal in a folder containing this repositorz (locally or via ssh)
2. run chmod +x retrieve_addresses.sh to allow execution of customs bash files
3. execute ./retrieve_addresses.sh that will download weekly list of actives addresses and decode into a local .txt file
    1. ipv6_retrieval will be executed downloading and storing in the working directory ipv6 hitlist
    2. ipv6_aliases_removal will iterate the hitlist and send 16 packets to pseudo-random addresses within IPv6 prefix, using TCP/80 and ICMPv6 enforcing traversal of a subprefix with different nybbles. SUDO permissions required for Linux kernel
4. work in progress

# Zmap Scanner
to install ZMapv6, do:
1. make sure to install all the dependencies of ZMap  
   On Debian-based systems (including Ubuntu), run:  
   ```sudo apt-get install build-essential cmake libgmp3-dev gengetopt libpcap-dev flex byacc libjson-c-dev pkg-config libunistring-dev```
   For other systems, refer to <https://github.com/zmap/zmap/blob/main/INSTALL.md> to install dependencies.  
2. fetch source code  
   Remember to fetch from the **git repo** <https://github.com/tumi8/zmap.git>, and go to **master branch**:  
   ```
   git clone https://github.com/tumi8/zmap.git
   git checkout master
   ```
   **DO NOT** use any version provided by Ubuntu or any release version, none of them support IPv6.  
3. make and install  
   ```
   cmake .
   make -j4
   sudo make install
   ```
   to check whether installed successfully, run:  
   ```
   zmap --version
   zmap --help | grep IPv6
   ```
to scan a list of IPv6 addresses with zmap:  
1. go to sub-dir: ```zmap_scan```
2. get local IPv6 info :IPv6 address and gateway MAC.
3. fill IPv6 address and gateway MAC in zmap_scan_once.sh:  
   ```--ipv6-source-ip=<Your IP> -G <Your MAC> --ipv6-target-file=<Your File>```
   note: gateway MAC maybe not needed.  
4. run the bash script
   ```bash zmap_scan_once.sh```
