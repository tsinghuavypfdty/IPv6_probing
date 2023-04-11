# python3 gen_ip_list.py 2001:1201:10::/48 2048 > ips_to_scan.txt
sudo zmap -M ipv6_tcp_synopt -p "80" --ipv6-source-ip=2402:f000:4:1001:809:ba4f:f163:1925 -B 100M --max-runtime=3600 --output-module=csv -o "output.csv" --ipv6-target-file=responsive-addresses.txt
# sudo zmap -M icmp6_echoscan --ipv6-source-ip=2402:f000:4:1001:809:ba4f:f163:1925 -B 100M -G fc:34:97:e2:07:52 --output-module=csv -o "output.csv" --ipv6-target-file=responsive-addresses.txt
