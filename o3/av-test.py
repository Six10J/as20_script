#!/usr/bin/env python3

#Modul för OS information
import platform, time

#Skapar en variabel som får värdet av de OS programmet körs på
system = platform.system()

#If sats som ser till att användarn är på en Windows platform
if system == "Windows":
    # Fortsätt med Windows-specifik kod
    print("Windows upptäckt. Scriptet fortsätter..")

elif system == "Linux":
    print("Linux upptäckt. Detta script är avsett för Windows.")
    exit()

elif system == "Darwin":
    print("macOS upptäckt. Detta script är avsett för Windows.")
    exit()

else:
    print(f"Okänt operativsystem ({system}). Detta script är avsett för Windows. Avbryter körning.")
    exit()

# Skriv AV test signaturen baserad på EICAR-testfil, innehållet är helt ofarligt och kommer inte att skada systemet.

eicar_str = "X5O!P%@AP[4\\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"

f = open("C:\\Users\\sixte\\AV-TEST-FILE.txt", "x")
print("Fil skapad på skrivbordet: C:\\Users\\sixte\\AV-TEST-FILE.txt")

with open("C:\\Users\\sixte\\AV-TEST-FILE.txt", "a") as f:
    f.write(eicar_str)

print("Ger AV möjligheten att detektera \"viruset\"")
time.sleep(3)

try:
 with open("C:\\Users\\sixte\\AV-TEST-FILE.txt", "r") as f:
     fil_innehåll = f.read()
     if fil_innehåll == eicar_str:
        print("AV test lyckades")
except Exception as e:
    # Om ett fel uppstår här pga att filen har tagits bort eller flyttats
    print("[!!!] Filen kunde inte läsas!")
    print("[!!!] AV har tagit bort/karantänat filen.")
    print("[---] Din AV/EDR-lösning är helt fungerande och skyddar mot kända virus-signaturer.")
