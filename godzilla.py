#!/usr/bin/python

from scripts.openman import openfunc
from scripts.portscanner import portfunc
from scripts.subnet_scanner import subnet
from scripts.http_sniffer   import snifffunc
from scripts.Arp_Spoofing   import arpfunc
from scripts.xss import xssfunc
from scripts.sqlinj import sqlfunc
import colorama
from colorama import Fore, Back, Style
colorama.init()


print Fore.BLUE +"""
                      ^\    ^                  
                      / \\  / \                 
                     /.  \\/   \      |\___/|   
  *----*           / / |  \\    \  __/  O  O\   
  |   /          /  /  |   \\    \_\/  \     \     
 / /\/         /   /   |    \\   _\/    '@___@      
/  /         /    /    |     \\ _\/       |U
|  |       /     /     |      \\\/        |
\  |     /_     /      |       \\  )   \ _|_
\   \       ~-./_ _    |    .- ; (  \_ _ _,\'
~    ~.           .-~-.|.-*      _        {-,
 \      ~-. _ .-~                 \      /\'
  \                   }            {   .*
   ~.                 '-/        /.-~----.
     ~- _             /        >..----.\\\"""+
         ~ - - - - ^}_ _ _ _ _ _ _.-\\\"""+

\n"""+Style.RESET_ALL


print Fore.YELLOW +"[#][1] "+Style.RESET_ALL+"Port Scanner"
print Fore.YELLOW +"[#][2] "+Style.RESET_ALL+"XSS Scanner"
print Fore.YELLOW +"[#][3] "+Style.RESET_ALL+"Open Redirect Scanner"
print Fore.YELLOW +"[#][4] "+Style.RESET_ALL+"HTTP Sniffer "
print Fore.YELLOW +"[#][5] "+Style.RESET_ALL+"Arp Poisner "
print Fore.YELLOW +"[#][6] "+Style.RESET_ALL+"Subnet Scanner"
print Fore.YELLOW +"[#][7] "+Style.RESET_ALL+"Sql Injection Scanner\n"


attack = raw_input("enter your atack number: ");

if attack == "3":
	openfunc()
elif attack == "1":
	portfunc()
elif attack == "2":
	xssfunc()
elif attack == "4":
	snifffunc()
elif attack == "6":
	subnet()
elif attack == "5":
	arpfunc()
elif attack == "7":
	sqlfunc()
