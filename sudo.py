#!/usr/bin/env python
import subprocess,getpass

#Get user pass and  restart something
import os
os.popen("sudo -S /etc/init.d/sshd restart", 'w').write("mypassword")
os.chdir('/')
os.system("ls -la")


