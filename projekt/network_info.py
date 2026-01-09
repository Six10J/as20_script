#!/usr/bin/env python3

#Rubrik av programmet visar vilken version programmet är i 
print ("")
print ("--- network_info v 0.31 ---")
print ("")

#För att fastställa att programmet kan arbeta med nätverks information
import socket

#Skriver ut nätverks infromation
print("Hostname: " + socket.gethostname())

#Lösning för att skriva ut IPv4 address lånat 
#från https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib (2026-01-09)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("IPv4 address: " + s.getsockname()[0])
s.close()

#Gör så att programmet kan köra CLI komandon
import os

#Test av att köra CLI komandon
print ("")
print (os.system("ping -c 4 8.8.8.8"))