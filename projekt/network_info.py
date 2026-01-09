#!/usr/bin/env python3

#För att fastställa att programmet kan arbeta med nätverks information
import socket
#Gör så att programmet kan köra CLI komandon
import os
#Impoterar maskinvara info
import re, uuid

#Rubrik av programmet visar vilken version programmet är i 
print ("")
print ("--- network_info v 0.32 ---")
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

#Test av att köra CLI komandon
print ("")
print (os.system("ping -c 4 8.8.8.8"))