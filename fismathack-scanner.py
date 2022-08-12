import scapy.all as scapy
import argparse
parse = argparse.ArgumentParser()
parse.add_argument("--IP",help="IP of the gateway")
parse.add_argument("--SM",help="subnet mask(without /)")
args = parse.parse_args()
def scan(ip):
    
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0] 
    print("IP\t\tMAC")
    print("=======================================")
    for element in answered:
        print(element[1].psrc,"\t\t",element[1].hwsrc)
try:        
  scan(args.IP+"/"+args.SM)    
except:
     print("Error")
     
