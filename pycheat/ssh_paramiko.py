import paramiko
import os
import sys

comm = raw_input("command?")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('server', username='user', password='pass')
stdin, stdout, stderr = ssh.exec_command(comm)
print stdout.readlines()
ssh.close()
