
# First we import the Fabric api
from fabric.api import *

#And needed parts
from fabric.colors import red, green
from fabric.context_managers import settings
from fabric.api import sudo
from fabric.api import puts as fabric_puts
from fabric import colors
from fabric.operations import local, run
from fabric.state import env
from fabric.utils import error

# We can then specify host(s) and run the same commands across those systems
env.user = 'user'
env.password = 'pass'
env.hosts = [
    'xxx.xxx.xxx.xxx',
    'xxx.xxx..xxx.xxx',
    ]

#Roles you can execute by fab  -R tomcat_servers , which will ONLY apply to those servers
env.roledefs = {
    'tomcat_servers' : ['server01','server02']
}

#Restrict the role to tomcat_servers
@roles('tomcat_servers')


#Add some color
def puts(msg, m_type='info'):
    messages_by_type = {
        'info': colors.blue(msg),
        'success': colors.green(msg),
        'warn': colors.yellow(msg),
        'error': colors.red(msg)
    }

    fabric_puts(messages_by_type[m_type])


def uptime():
    run("uptime")
    
def hostnameip():
    run("hostname")
    put('ip.sh', '/tmp/')
    run('/bin/bash /tmp/ip.sh')
    sudo('whoami')
    
def anonymous():
    run("uname -a")

def hello():
	print("Hello World")
 

def tcp_ports():
      puts('updating server')	 #Add some color!
      print run("lsof -i tcp")


#Running a command and capturing the output:

import functools
import logging
import sys

from fabric.api import run, hide

def do_stuff():
    for cmd in ['ls', 'w', 'who']:
        run(cmd)

# configure logging
logger = logging.getLogger("logged")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler('logfile.txt'))

def logged(func):
    """Logging decorator."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with hide('output'):
            output = func(*args, **kwargs)
        logger.info(output)
        return output
    return wrapper
run = logged(run)

