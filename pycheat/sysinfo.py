# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:21:57 2013

@author: ozdemircili
"""


import psutil
psutil.phymem_usage()
psutil.virtmem_usage()
psutil.cached_phymem()
psutil.phymem_buffers()
psutil.avail_phymem()
psutil.used_phymem()
psutil.total_virtmem()
psutil.avail_virtmem()
psutil.used_virtmem()

psutil.cpu_percent()

#CPU

from __future__ import print_function

with open('/proc/cpuinfo') as f:
    for line in f:
       
        #Formatting the output!!
        if line.strip():
            if line.rstrip('\n').startswith('model name'):
                model_name = line.rstrip('\n').split(':')[1]
                print(model_name)
        if line.strip():
            if line.rstrip('\n').startswith('cpu cores'):
                cores = line.strip('\n').split(':')[1]
                print (cores)
                
        if line.strip():
           if line.strip():
            if line.rstrip('\n').startswith('flags') \
                    or line.rstrip('\n').startswith('Features'):
                if 'lm' in line.rstrip('\n').split():
                    print('64-bit')
                else:
                    print('32-bit')
                    
#Memory
                    
from __future__ import print_function
from collections import OrderedDict

def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
    return meminfo

if __name__=='__main__':
    #print(meminfo())
    
    meminfo = meminfo()
    print('Total memory: {0}'.format(meminfo['MemTotal']))
    print('Free memory: {0}'.format(meminfo['MemFree']))
    
    
#NEtwork statistics
    
    #!/usr/bin/env python
from __future__ import print_function
from collections import namedtuple

def netdevs():
    ''' RX and TX bytes for each of the network devices '''

    with open('/proc/net/dev') as f:
        net_dump = f.readlines()
    
    device_data={}
    data = namedtuple('data',['rx','tx'])
    for line in net_dump[2:]:
        line = line.split(':')
        if line[0].strip() != 'lo':
            device_data[line[0].strip()] = data(float(line[1].split()[0])/(1024.0*1024.0), 
                                                float(line[1].split()[8])/(1024.0*1024.0))
    
    return device_data

if __name__=='__main__':
    
    netdevs = netdevs()
    for dev in netdevs.keys():
        print('{0}: {1} MiB {2} MiB'.format(dev, netdevs[dev].rx, netdevs[dev].tx))
        
#Processes
        
        
from __future__ import print_function
import os
def process_list():

    pids = []
    for subdir in os.listdir('/proc'):
        if subdir.isdigit():
            pids.append(subdir)

    return pids


if __name__=='__main__':

    pids = process_list()
    print('Total number of running processes:: {0}'.format(len(pids)))
    
    
    
#Black devices
    

from __future__ import print_function
import glob
import re
import os

# Add any other device pattern to read from
dev_pattern = ['sd.*','mmcblk*']

def size(device):
    nr_sectors = open(device+'/size').read().rstrip('\n')
    sect_size = open(device+'/queue/hw_sector_size').read().rstrip('\n')

    # The sect_size is in bytes, so we convert it to GiB and then send it back
    return (float(nr_sectors)*float(sect_size))/(1024.0*1024.0*1024.0)

def detect_devs():
    for device in glob.glob('/sys/block/*'):
        for pattern in dev_pattern:
            if re.compile(pattern).match(os.path.basename(device)):
                print('Device:: {0}, Size:: {1} GiB'.format(device, size(device)))

if __name__=='__main__':
    detect_devs()



#Print all the users and their login shells


from __future__ import print_function
import pwd


# Get the users from /etc/passwd
def getusers():
    users = pwd.getpwall()
    for user in users:
        print('{0}:{1}'.format(user.pw_name, user.pw_shell))

if __name__=='__main__':
    getusers()
    