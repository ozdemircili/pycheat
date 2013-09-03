# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:30:21 2013

@author: ozdemircili
"""
import platform
import os 
profile = [
platform.architecture(),
platform.dist(),
platform.libc_ver(),
platform.mac_ver(),
platform.machine(),
platform.node(),
platform.platform(),
platform.processor(),
platform.python_build(),
platform.python_compiler(),
platform.python_version(),
platform.system(),
platform.uname(),
platform.version(),
platform.linux_distribution(),

]
for item in profile:
    print item

def is_fedora():
    if platform.dist().startswith('fedora'):
        print "That Fedora"
    else:
        print "No it is not"


def is_os_64bit():
    return platform.machine().endswith('64')
    
bits = is_os_64bit

if bits == True:
    print "That`s a 64 bit system"
else:
    print "That`s a 32 bit system"


processor = platform.processor()
if processor.find("64") == -1:
    print "We got a 32 bit fighter here"
else:
    print "We got a 64 bit boy here."
