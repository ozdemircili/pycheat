# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:37:40 2013

@author: ozdemircili
"""
"""

Install:

pip install pyspehre

"""

from pysphere import VIServer
server = VIServer()

server.connect("serverip","adminuser","pass")

#Get server characteristics
print server.get_server_type()

print server.get_api_version()

print server.get_clusters()

print server._get_resource_pools

#Get all the hosts
print server.get_hosts()

#Get VM`s in Prod resource pool which are in poweredon state

vmachines = server.get_registered_vms()
vmachines = server.get_registered_vms(resource_pool='Prod', status='poweredOn')

#Get virtual machine status
vm1 = server.get_vm_by_name('rhel5.3_prod')
print vm1.get_status()

#Also you can ask the following:
print vm1.is_powering_off()
print vm1.is_powered_off()
print vm1.is_powering_on()
print vm1.is_powered_on()
print vm1.is_suspending()
print vm1.is_suspended()
print vm1.is_resetting()
print vm1.is_blocked_on_msg()
print vm1.is_reverting()

#For power options:

vm1.power_on()
vm1.reset()
vm1.suspend()
vm1.power_off()

#Also power on another host
vm1.power_on(host="esx3.example.com")

#Snaphot operations
vm1.revert_to_snapshot() #reverts to the current snapshot
vm1.revert_to_named_snapshot("base") #reverts to the "base" snapshot
vm1.revert_to_path("/base/updated") #reverts to the "updated" snapshot which is a child of snapshot "base"

vm1.delete_current_snapshot()
vm1.delete_named_snapshot("base")
vm1.delete_snapshot_by_path("/base2/foo")

#Create snapshots
vm1.create_snapshot("mysnapshot")

#List snapshots
snapshot_list = vm1.get_snapshots()

#We can also do operations inside the server

vm1.login_in_guest("os_username", "os_password")

vm1.send_file("/home/seba/netcat.exe", r"c:\netcat.exe")
vm1.make_directory(r"c:\my\binary\tools")
vm1.move_file(r"c:\netcat.exe", r"c:\my\binary\tools\nc.exe")

#Guest OS processes
vm1.list_processes()
vm1.terminate_process(1680)