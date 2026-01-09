#!/usr/bin/env python3

#Rubrik av programmet visar vilken version programmet är i 
print ("")
print ("--- network_info v 0.1 ---")
print ("")

#För att fastställa att programmet kan arbeta med nätverks information
import socket

#Skriver ut nätverks infromation
print("Hostname: " + socket.gethostname())