# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:10:57 2013

@author: ozdemircili
"""
"""
Install : 

pip install python-nmap

"""
import nmap                         # import nmap.py module
nm = nmap.PortScanner()             # instantiate nmap.PortScanner object
nm.scan('127.0.0.1', '22-443')      # scan host 127.0.0.1, ports from 22 to 443
nm.command_line()                   # get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1
nm.scaninfo()                       # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
nm.all_hosts()                      # get all hosts that were scanned


for host in nm.all_hosts():
         print('----------------------------------------------------')
         print('Host : %s (%s)' % (host, nm[host].hostname()))
         print('State : %s' % nm[host].state())

for proto in nm[host].all_protocols():
    print('----------')
print('Protocol : %s' % proto)

lport = nm[host][proto].keys()
lport.sort()
for port in lport:
    print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

print('----------------------------------------------------')


#Explanation in detail:

nm['127.0.0.1'].hostname()          # get hostname for host 127.0.0.1
nm['127.0.0.1'].state()             # get state of host 127.0.0.1 (up|down|unknown|skipped)
nm['127.0.0.1'].all_protocols()     # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
nm['127.0.0.1']['tcp'].keys()       # get all ports for tcp protocol
nm['127.0.0.1'].all_tcp()           # get all ports for tcp protocol (sorted version)
nm['127.0.0.1'].all_udp()           # get all ports for udp protocol (sorted version)
nm['127.0.0.1'].all_ip()            # get all ports for ip protocol (sorted version)
nm['127.0.0.1'].all_sctp()          # get all ports for sctp protocol (sorted version)
nm['127.0.0.1'].has_tcp(22)         # is there any information for port 22/tcp on host 127.0.0.1
nm['127.0.0.1']['tcp'][22]          # get infos about port 22 in tcp on host 127.0.0.1
nm['127.0.0.1'].tcp(22)             # get infos about port 22 in tcp on host 127.0.0.1
nm['127.0.0.1']['tcp'][22]['state'] # get state of port 22/tcp on host 127.0.0.1 (open

#print result as CSV
print(nm.csv())


#Another scan example

# If you want to do a pingsweep on network 10.5.200.0/24
nm.scan(hosts='10.5.200.1/24', arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
for host, status in hosts_list:
    print('{0}:{1}'.format(host, status))

