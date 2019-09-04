#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()


# merge payload with target host
def merge(s,b) :
  global a
  a = requests.get(s+b)


def openfunc():
      print"""\x1b[31;1m                                      
         ____                    _____ _    _ _   _ 
        / __ \                  / ____| |  | | \ | |
       | |  | |_ __   ___ _ __ | |  __| |  | |  \| |
       | |  | | '_ \ / _ \ '_ \| | |_ | |  | | . ` |
       | |__| | |_) |  __/ | | | |__| | |__| | |\  |
        \____/| .__/ \___|_| |_|\_____|\____/|_| \_|
              | |                                   
              |_|                                   \x1b[0m
      \x1b[32;1m
                 _________
               /'        /|
              /         / |_
             /         /  //|
            /_________/  ////|
           |   _ _    | 8o////|
           | /'// )_  |   8///|
           |/ // // ) |   8o///|
           / // // //,|  /  8//|
          / // // /// | /   8//|
         / // // ///__|/    8//|
        /.(_)// /// |       8///|
       (_)' `(_)//| |       8////|___________
      (_) /_\ (_)'| |        8///////////////
      (_) \"/ (_)'|_|         8/////////////
       (_)._.(_) d' Hb         8oooooooopb'
         `(_)'  d'  H`b
               d'   `b`b
              d'     H `b
             d'      `b `b
            d'           `b
           d'             `b


             
           
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
                        print '\x1b[32m                 ___  \x1b[0m' 
                        print '\x1b[32m Trying for : ~~|___) \x1b[0m' + str(clean_target+payload)
                        print 'Response Code:'+str(a.history)+'\n'
                        print 'Final Result: ' +  str(a.url)     + '\n'
      except KeyboardInterrupt:
          print "\n"+Fore.GREEN+"Good Bye ;)"
          sys.exit()



