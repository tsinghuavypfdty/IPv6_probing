# python3 gen_ip_list.py 2001:1201:10::/48 2048 > ips_to_scan.txt
sudo zmap -M icmp6_echoscan --ipv6-source-ip=2402:f000:2:801:4dd0:4ec9:e35b:e38a -B 100K -G F8:89:D2:80:78:D1 --output-module=csv -o "output.csv" --ipv6-target-file=ips_to_scan.txt 
sudo zmap -M icmp6_echoscan --ipv6-source-ip=2402:f000:2:801:4dd0:4ec9:e35b:e38a -B 100K -G F8:89:D2:80:78:D1 --output-module=csv -o "output.csv" --ipv6-target-file=ips_to_scan.txt 
