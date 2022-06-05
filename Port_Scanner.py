import os
from colorama import Fore
import time

green = Fore.LIGHTGREEN_EX
red = Fore.RED

print(Fore.MAGENTA + "'  ..____............_.....____..................................")
print(Fore.MAGENTA + "'  .|.._.\.___.._.__|.|_../.___|..___.__._._.__.._.__...___._.__.")
print(Fore.MAGENTA + "'  .|.|_)./._.\|.'__|.__|.\___.\./.__/._`.|.'_.\|.'_.\./._.\.'__|")
print(Fore.MAGENTA + "'  .|..__/.(_).|.|..|.|_...___).|.(_|.(_|.|.|.|.|.|.|.|..__/.|...")
print(Fore.MAGENTA + "'  .|_|...\___/|_|...\__|.|____/.\___\__,_|_|.|_|_|.|_|\___|_|...")
print(Fore.MAGENTA + "'  ..............................................................")
print(Fore.YELLOW + "                                           By 𝖂𝖍𝖔𝖆𝖒𝖎#0001")
print(" ")
print("[1] Scan Ports")
print("[2] Exit")
print(" ")

option = int(input(f"{green}[+]Choose an option (1-2): "))

if option == 1:
    ip = input(f"{green}[+]Writte target's ip: ")
    ports = input(f"{green}[+]Writte the port range of your scanning process, example 0-80: ") 
    print(f"{red}")
    os.system(f"nmap -p {ports} -T5 -v -Pn {ip}")
else:
    print("Exiting...")
    time.sleep(2)




