 license = """         GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007
 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed."""
  
 # Don't edit the file, don't delete the license. if you will, idc i cant find u, im just having a bad day so im going harsh with the licenses

import zipfile
import colorama
import time
from colorama import Fore
import os.path
import urllib.request


colorama.init()

print(Fore.LIGHTYELLOW_EX+"""
███╗   ███╗███████╗ ██████╗ ██╗    ██╗███████╗    ███████╗██╗██████╗      ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
████╗ ████║██╔════╝██╔═══██╗██║    ██║██╔════╝    ╚══███╔╝██║██╔══██╗    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██╔████╔██║█████╗  ██║   ██║██║ █╗ ██║███████╗      ███╔╝ ██║██████╔╝    ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║╚██╔╝██║██╔══╝  ██║   ██║██║███╗██║╚════██║     ███╔╝  ██║██╔═══╝     ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║███████╗╚██████╔╝╚███╔███╔╝███████║    ███████╗██║██║         ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝     ╚═╝╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝    ╚══════╝╚═╝╚═╝          ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                 
""")
zip_file = input("[?] File to crack: ")
if ".zip" not in zip_file:
    zip_file = zip_file+".zip"
else:
    pass


def crack_password(password_list, obj):

    idx = 0


    print(Fore.MAGENTA+"[*] Starting bruteforce in 2 seconds, action will be timed.")
    time.sleep(2)
    with open(password_list, 'rb') as file:
        t0 = time.time()
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    print(Fore.GREEN+f"[{idx}] Trying password: {word.decode()}")
                    obj.extractall(pwd=word)

                    print(Fore.MAGENTA+"[+] Password found: ", word.decode())
                    print(Fore.MAGENTA+"[+] Zipfile extracted.")
                    t1 = time.time()
                    total = t1 - t0
                    print(Fore.MAGENTA+"[*] Time taken: ", total, "seconds.")

                    return True
                except:
                    continue

    return False

downld = input("Would you like to download rockyou.txt (133 mb), a password list. (Y/N): ")

if downld == "y" or downld == "Y" or downld == "yes" or downld == "YES":
  urllib.request.urlretrieve("https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt", "rockyou.txt")

else:
  password_list = input("[?] input your custom file with passwords: ")
if ".txt" not in password_list:
    password_list = password_list+".txt"


try:
# ZipFile object initialised
    obj = zipfile.ZipFile(zip_file)
except:
    input(Fore.RED+"[-] Invalid File.")
    exit()

# count of number of words present in file
try:
    cnt = len(list(open(password_list, "rb")))
except:
    input(Fore.RED + "[-] Invalid File.")
    exit()


print(Fore.GREEN+"[+] ", cnt,
      "number of passwords detected, starting bruteforce...")

if crack_password(password_list, obj) == False:
    input(Fore.RED+"[-] Password not found in this file.")
    exit()
