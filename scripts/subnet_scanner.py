#!/usr/bin/python

import netifaces
import socket
import time


def subnet():
	print """   _____ _    _ ____  _   _ ______ _______    _____  _____          _   _ _   _ ______ _____  
	  / ____| |  | |  _ \| \ | |  ____|__   __|  / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
	 | (___ | |  | | |_) |  \| | |__     | |    | (___ | |       /  \  |  \| |  \| | |__  | |__) |
	  \___ \| |  | |  _ <| . ` |  __|    | |     \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
	  ____) | |__| | |_) | |\  | |____   | |     ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
	 |_____/ \____/|____/|_| \_|______|  |_|    |_____/ \_____/_/    \_\_| \_|_| \_|______|_|  \_\
	                                                                                              
	 """
	time.sleep(5)
	print '\nInterfaces available: ' + str(netifaces.interfaces()) + '\n'


		
	for x in netifaces.interfaces() :

		print x + ' Interface : \n'
		eth0_add       = netifaces.ifaddresses(x)

		interface_info = eth0_add[socket.AF_INET][0]
		
		print interface_info['addr']
		print interface_info['netmask'] + '\n'
