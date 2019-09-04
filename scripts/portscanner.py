#!/usr/bin/env python
import socket
import subprocess
import sys
import colorama
from datetime import datetime
from colorama import Fore, Back, Style

def portfunc():
    # Clear the screen
    subprocess.call('clear', shell=True)

    # Ask for input
    remoteServer    = raw_input("Enter a remote host to scan: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)

    # Green Nice Banner :)
    print Fore.GREEN +"#" * 60+Style.RESET_ALL
    print "Please wait, scanning your IP", remoteServerIP
    print Fore.GREEN +"#" * 60+Style.RESET_ALL

    starttime = datetime.now()

    try:
        for port in range(1,300):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port {}: 	 Open".format(port)
            sock.close()

    except KeyboardInterrupt:
        print Fore.RED + "Good Bye" + Style.RESET_ALL;
        sys.exit()

    except socket.gaierror:
        print Fore.RED+'Hostname error. Exiting'+Style.RESET_ALL;
        sys.exit()

    except socket.error:
        print "Couldn't connect to IP"
        sys.exit()

    # get ending time
    endtime = datetime.now()

    #calculate the total time
    total =  endtime - starttime

    # Printing total time
    print 'Scanning Completed in: ', total
