import requests
import time
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}

def xssfunc():
  print(Fore.GREEN + """
     _  ____________
    | |/ / ___/ ___/
    |   /\__ \\__ \ 
   /   |___/ ___/ / 
  /_/|_/____/____/\n"""+ Style.RESET_ALL)

  attack_type = raw_input("Type attack POST OR GET ? (p/g) : ")

  # GET REQUEST
  if attack_type == "g":
    try:
      site = raw_input("Site URL : ")
      req = requests.get(site);
      print(Fore.GREEN + "url is alive" + Style.RESET_ALL+"\n")
    except:
      print(Fore.RED + "url does't respond ")
      
      sys.exit(0)
    try:
        payload_file = raw_input("wordlist.txt directory : ")
        payload_open = open(payload_file, "r")
    except FileNotFoundError:
      print("your file " + Fore.RED + payload_file + Style.RESET_ALL + " is not found, try again !"+Style.RESET_ALL)
      sys.exit(0)
    print(Fore.YELLOW + "Attacking is in process\n"+ Style.RESET_ALL)
    time.sleep(1)
    
    payload_open = open(payload_file,"r")
    for payload in payload_open:
      if payload in requests.get(site + payload, headers=header).text:
        print(Fore.GREEN + "XSS  DETECTED: " + Style.RESET_ALL + requests.get(site + payload, headers=header).url)
      else:
        print("no results for " + payload)

  # POST REQUEST
  elif attack_type == "p":
    try:
      site = raw_input("Site URL :")

      data = raw_input("Post DATA : ")
      
      req = requests.post(site, headers=header, data=data)
      
      print(Fore.GREEN + "url is alive" + Style.RESET_ALL)
    except:

      print(Fore.RED + "url does't respond ")
      sys.exit(0)
    try:
      payload_file = raw_input("payload file directory: ")
      
      reper = open(payload_file, "r")
    except FileNotFoundError:
      print("your file " + Fore.RED + payload_file + Style.RESET_ALL + " is not found, try again !")
      sys.exit(0)
    print(Fore.GREEN + "Test in process...\n")
    payload_open = open(payload_file,"r")
    for payload in payload_open:
      req = requests.post(site+payload, headers=header, params=data).text;
      if payload in req:
        print(Fore.GREEN + "XSS  DETECTED: " + Style.RESET_ALL + requests.get(site + payload, headers=header, data=data.url + " Post DATA = " + data + "\n"))
      else:
        print("no results for " + payload)
  else:
    print("Unknown answer please enter g or p")
    sys.exit(0)
