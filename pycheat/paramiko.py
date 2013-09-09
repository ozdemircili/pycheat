# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:11:59 2013

@author: ozdemircili
"""

import paramiko

hostname = 'server'
port     = 22
username = 'user'
password = 'pass'

#To avoid host not found exception

    
if __name__ == "__main__":
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print stdout.read()
    s.close()

