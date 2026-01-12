#!/usr/bin/env python3

#För att fastställa att programmet kan arbeta med nätverks information
import socket
#Impoterar maskinvara info
import re, uuid
#Gör så att programmet kan köra CLI komandon
import os, subprocess
os_value = (os.name)

#Rubrik av programmet visar vilken version programmet är i 
print ("")
print ("--- network_info v 0.5 ---")
print ("")

#Skriver ut nätverks infromation
print("Hostname: " + socket.gethostname())

#Lösning för att skriva ut IPv4 address lånat 
#från https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib (2026-01-09)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("IPv4 address: " + s.getsockname()[0])
s.close()

#Hämtar mac addressen och skriver ut den lånat från https://www.geeksforgeeks.org/python/extracting-mac-address-using-python/ (2026-01-09)
mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
print("MAC address: " + mac)

#Usel lösning för att skriva ut netmask och broadcast address kunde inte hitta något bättre
if os_value == "posix":
 ifconfig_var = str(subprocess.run("ifconfig | grep ""netmask""", shell=True, capture_output=True, text=True))
 ifconfig_var_list = ifconfig_var.split()
 # för testing av kod print (ifconfig_var_list)
 print ("Subnet mask: " + ifconfig_var_list[9])
 broadcast_address = ifconfig_var_list[11]
 broadcast_address = broadcast_address.replace("\\n", "")
 print ("Brodcast address: " + broadcast_address)

else:
 print("This program can currently only print Subnet mask and Broadcast address in a Linux enviorment")

#Pingar googles publika DNS server, olika kod beroende på operativ system
if os_value == "posix":
 print ("")
 print (os.system("ping -c 4 8.8.8.8"))

elif os_value == "nt":
 print ("")
 print (os.system("ping 8.8.8.8"))

else:
 print("Unkown operating system detected") 

# Feature for code:
# The Ping dosent work in windows platform and Linux good to go.
# Cant run ./network_info.py and i chmod 777 and rerun it.
# Use try-except to catch network bug and so on 
# // Rob