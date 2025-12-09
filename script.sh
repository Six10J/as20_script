#!/bin/bash
#
# Detta script samlar in systeminformation - RECON
#
# Kan användas för följande attacker:
# [Skriv möjliga attacker]
#
# Author: Frans Schartau
# Last Update: 2025-01-01


echo "Välkommen till RECON script för att kontrollera en Linux-miljö"

echo
echo "=== SYSTEMINFO ==="
uname -a
echo
env | grep -e "NAME" -e "LANG" -e "as20" 

echo
echo "=== AKTUELL ANVÄNDARE ==="
echo $USER

echo
echo "=== ANVÄNDARE MED SHELL ==="
grep "sh$" /etc/passwd

echo
echo "=== NÄTVERK ==="
ip a | grep inet
echo
curl https://ipapi.co/json/ | grep -e ip -e network  

echo
echo "=== Hårdvara  ==="
lscpu | grep -A3 Architecture
echo
free -h

echo
echo "=== Test ==="
# skriv in dina egna kommandon för tester

