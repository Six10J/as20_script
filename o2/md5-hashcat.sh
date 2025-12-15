#!/bin/bash

if ! command -v hashcat &> /dev/null; then
    echo "ERROR: hashcat är inte installerat!"
    echo "Installera med: sudo apt install hashcat"
    exit 1
fi

echo "=== Hashcat MD5 Cracker ==="
hashcat --version | head -n 1
echo "==========================="

HASH_FILE="${1:-mina_hashar.txt}"
MASK="${2:-?d?d?d?d?d?d?d?d?d?d}"  		
HASH_TYPE="0"    				
ATTACK_MODE="3"  				

echo "Startar hashcat ..."
echo "=================="

hashcat -m "$HASH_TYPE" -a "$ATTACK_MODE" "$HASH_FILE" "$MASK" -O -w 3 --force

echo ""
echo "=================="
echo "Hashcat körning slutförd! Allt OK!"

